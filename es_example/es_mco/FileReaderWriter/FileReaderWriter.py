import re

class FileReaderWriter():

    file = None

    def __init__(self, file=""):
        self.file = file
        pass

    def getData(self):
        file = open(self.file, "r")
        ret = dict()
        lines = file.readlines()
        for line in lines:
            ret.update(self.parseLine(line))
        file.close()
        return ret


    def parseLine(self, line):
        regex = r"(.*)=(.*)"
        matches = re.finditer(regex, line, re.MULTILINE)
        ret = dict()
        for matchNum, match in enumerate(matches, start=1):
            value = match.groups()[1]
            if self.isfloat(value):
                value = float(value)
            ret[match.groups()[0]] = value
        return ret

    def dictToString(self, dict):
        ret = ""
        first = True
        for item in dict:
            if not first:
                ret = ret + "\n"
            ret = ret + item + "=" + str(dict[item])
            first = False
        return ret

    def writeData(self, dict):
        file = open(self.file, "w")
        content = self.dictToString(dict)
        file.write(content)
        file.close()

    def isfloat(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False