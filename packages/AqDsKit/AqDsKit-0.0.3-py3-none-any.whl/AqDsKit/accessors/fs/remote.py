import contextlib
import fnmatch
import os
import glob
import paramiko
import logging
from stat import S_ISDIR, S_ISREG


class MyRemote:
    def __init__(self, host, port, username, password, private_key_file=None):
        """Remote server operations using paramiko

        :param host: ip address of the remote server
        :param port: port number of the remote server
        :param username: username to login
        :param password: password to login, could be None if private key file is provided
        :param private_key_file: the path to the private key file (id_rsa, should be in openSSH format)

        Ref:
        https://avleonov.com/2017/09/05/ssh-sftp-public-key-authentication-and-python/
        https://stackoverflow.com/questions/8382847/how-to-ssh-connect-through-python-paramiko-with-ppk-public-key

        """
        self.host = host
        self.port = port
        self.username = username
        self.__password = password

        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(host, port, username=username, password=password, key_filename=private_key_file)

    def bash(self, bash_cmd: str):
        stdin_, stdout_, stderr_ = self.ssh.exec_command(bash_cmd)
        return stdin_, stdout_, stderr_

    def getFilePath(self, file):
        return f"SFTP://{self.username}@{self.host}:{self.port}/{file}"

    def ls(self, remoteFolderPath: str, pattern: str = None):
        with self.getSFTP() as sftp:
            file_list = sftp.listdir(remoteFolderPath)
            if pattern:
                file_list = list(filter(lambda x: fnmatch.fnmatch(x, pattern), file_list))
        print(f"{len(file_list)} files found under {remoteFolderPath}:")
        for i, file in enumerate(file_list):
            print(i, file)

    def mkdir(self, path: str, mode: int = 511, ignore_existing: bool = False) -> int:
        """create a remote directory

        :param path: the remote directory path to create
        :param mode: mode of the file
        :param ignore_existing: if True, will not do anything when the remote folder already exists
        :return:
        """
        with self.getSFTP() as sftp:
            try:
                sftp.mkdir(path, mode)
            except IOError as e:
                if ignore_existing:
                    logging.info(f"Folder already exists, will not do anything")
                    return 1
                else:
                    logging.error(
                        f"Folder already exists: {path}, manually delete the folder or set ignore_existing to True")
                    return 0
            else:
                logging.info(f"Folder successfully created: {path}")
                return 1

    @contextlib.contextmanager
    def getSFTP(self):
        sftp = self.ssh.open_sftp()
        yield sftp
        sftp.close()

    @contextlib.contextmanager
    def getFileHandler(self, fullFilePath: str, mode: str = 'r'):
        with self.getSFTP() as sftp:
            fileObject = sftp.file(fullFilePath, mode)
            yield fileObject
            fileObject.close()

    def download(self, remoteFilePath, localFilePath):
        with self.getSFTP() as sftp:
            sftp.get(remoteFilePath, localFilePath)
            logging.info(f"Successfully download File from {self.getFilePath(remoteFilePath)} to {localFilePath}")

    def download_folder(self, remoteFolderPath: str, localFolderPath: str, pattern: str = None, verbose: bool = False):
        """download a remote folder to local

        :param remoteFolderPath:
        :param localFolderPath:
        :param pattern: the wildcard for file mask. e.g. *.csv to include only csv files
        :param verbose: if True, will print downloading details
        :return:

        Note: will create local folder if not exists
        """
        if not os.path.exists(localFolderPath):
            os.makedirs(localFolderPath)

        with self.getSFTP() as sftp:
            item_list = sftp.listdir_attr(remoteFolderPath)

            if not os.path.isdir(localFolderPath):
                os.makedirs(localFolderPath, exist_ok=True)

            for item in item_list:
                remoteSubFolder = os.path.join(remoteFolderPath, item.filename)
                localSubFolder = os.path.join(localFolderPath, item.filename)

                if S_ISDIR(item.st_mode):
                    self.download_folder(remoteSubFolder, localSubFolder, pattern=pattern, verbose=verbose)
                else:
                    logging.info(f"Start downloading folder {remoteFolderPath} to {localFolderPath}")
                    if pattern:
                        if not fnmatch.fnmatch(item.filename, pattern):
                            continue
                    sftp.get(remoteSubFolder, localSubFolder)

                    if verbose:
                        logging.info(f"Successfully download File {item.filename}")

    def upload(self, localFilePath, remoteFilePath):
        with self.getSFTP() as sftp:
            sftp.put(localFilePath, remoteFilePath)
            logging.info(f"Successfully upload File from {localFilePath} to {self.getFilePath(remoteFilePath)}")

    def upload_folder(self, localFolderPath, remoteFolderPath, pattern: str = None, verbose: bool = False):
        """download a remote folder to local

        :param localFolderPath:
        :param remoteFolderPath:
        :param pattern: the wildcard for file mask. e.g. *.csv to include only csv files
        :param verbose: if True, will print uploading details
        :return:

        Note: will create remote folder if not exists
        """
        self.mkdir(remoteFolderPath, ignore_existing=True)

        with self.getSFTP() as sftp:
            for item in os.listdir(localFolderPath):
                remoteSubFolder = os.path.join(remoteFolderPath, item)
                localSubFolder = os.path.join(localFolderPath, item)

                if os.path.isfile(localSubFolder):
                    if pattern:
                        if not fnmatch.fnmatch(item, pattern):
                            continue
                    sftp.put(localSubFolder, remoteSubFolder)

                    if verbose:
                        logging.info(f"Successfully uploaded File {item}")
                else:
                    self.mkdir(remoteSubFolder, mode=511, ignore_existing=False)
                    self.upload_folder(localSubFolder, remoteSubFolder, pattern=pattern, verbose=verbose)

    def delete_folder(self, remoteFolderPath: str):
        with self.getSFTP() as sftp:
            for item in sftp.listdir_attr(remoteFolderPath):
                rpath = os.path.join(remoteFolderPath, item.filename)

                if S_ISDIR(item.st_mode):
                    self.delete_folder(rpath)
                else:
                    sftp.remove(rpath)

            sftp.rmdir(remoteFolderPath)
            logging.info(f"Successfully delete folder: {remoteFolderPath}")