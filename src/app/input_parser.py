import sys
from utils import makeNameString

class InputParser:
    def __init__(self, path, delimiter="", excludeHeader=True):
        self.path = path
        self.delimiter = delimiter
        self.excludeHeader = excludeHeader

    def parseFile(self):
        lines=[]
        with open(self.path) as data:
            if self.excludeHeader:
                data.readline() # Reads and removes the header

            for line in data.readlines():
                line.replace("\n", "")
                elems = line.split(self.delimiter)
                if len(elems) == 3:
                    name = makeNameString(elems[0], elems[1])
                    try:
                        lines.append([name, int(elems[2])])
                    except:
                        sys.stdout.write("Could not extract socre for %s. Please ensure the score is a number." % str(elems))
                else:
                    sys.stdout.write("Could not extract info for %s. Please ensure you set all the values." % str(elems))

        return lines