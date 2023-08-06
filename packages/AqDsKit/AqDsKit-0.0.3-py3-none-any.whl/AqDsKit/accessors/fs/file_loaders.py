import json
import logging
import os
from collections import OrderedDict



''' ---- 			file loader 			---- '''

def loadJSON(file):
    if isinstance(file, (list, dict)):
        return file
    elif isinstance(file, str):
        with open(file, "rb") as obj:
            return json.load(obj, object_pairs_hook = OrderedDict)
    else:
        raise ValueError("Please parse a file path or JS object")


def toJSON(js, file):
    with open(file, "w") as obj:
        json.dump(js, obj, indent = 4)



class File:
    def __init__(self, fileModule):
        self.__fileModule = fileModule

    def getDirPath(self):
        return os.path.abspath(os.path.dirname(self.__fileModule))

    def concatPath(self, relativefileName):
        paths = relativefileName.split("/")
        return os.path.join(self.getDirPath(), *paths)

    def loadJson(self, fileName):
        filepath = self.concatPath(fileName)

        file = loadJSON(filepath)
        return file

    def toJson(self, df, fileName):
        filepath = self.concatPath(fileName)
        toJSON(df, filepath)

    def loadCsv(self, fileName):
        filepath = self.concatPath(fileName)
        file = pd.read_csv(filepath, encoding="utf8", engine="python")
        return file

    def loadYML(self, fileName):
        filepath = self.concatPath(fileName)
        with open(filepath, "rb") as obj:
            cfg = yaml.load(obj)
        return cfg