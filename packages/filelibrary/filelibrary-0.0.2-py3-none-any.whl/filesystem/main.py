import os

class filesystem:
    def __init__(self, path):
        self.path = path
        self.files = []
        self.dirs = []
        self.getFilesInPath()
        self.getDirsInPath()

    def getFilesInPath(self):
        for file in os.listdir(self.path):
            if os.path.isfile(os.path.join(self.path, file)):
                self.files.append(file)

    def getDirsInPath(self):
        for dir in os.listdir(self.path):
            if os.path.isdir(os.path.join(self.path, dir)):
                self.dirs.append(dir)

    def getFileList(self):
        return self.files

    def getDirList(self):
        return self.dirs

    def printFiles(self):
        for file in self.files:
            print(file)

    def printDirs(self):
        for dir in self.dirs:
            print(dir)

    def printAll(self):
        self.printFiles()
        self.printDirs()

    def openFile(self, path):
        with open(path, 'r') as f:
            return f.read()

    def writeFile(self, path, text):
        with open(path, 'w') as f:
            f.write(text)
        with open(path, 'r') as f:
            return f.read() 

    def openFileAsJson(self, path):
        with open(path, 'r') as f:
            return json.load(f)

    def writeFileAsJson(self, path, data):
        with open(path, 'w') as f:
            return json.dump(data, f, indent=4)

    def test(self):
        print("haha testing go brrrrr")