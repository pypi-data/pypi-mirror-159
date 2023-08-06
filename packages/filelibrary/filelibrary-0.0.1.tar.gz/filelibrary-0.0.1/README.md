# How to use filelibrary

1. Install filelibrary package
```bash
pip install filelibrary
```

2. You're done! Now all there is to do is read the documentation.

# Documentation

1. Load Package
```python
from filelibrary import filelibrary

fileLibrary = filelibrary("path")
```

2. Get files in path
```python
files = fileLibrary.getFileList()
print(files) # prints every files in the specified path
```

3. Get directories in path
```python
dirs = fileLibrary.getDirList()
print(dirs) # prints every directories in the specified path
```

4. Print all (prints files and directories)
```python
fileLibrary.printAll()
```

5. Read file
```python
fileLibrary.openFile("fileName.extension")
# fileLibrary.openFile("test.txt")
```

6. Write file
```python
fileLibrary.writeFile("fileName.extension", "just a text here")
# fileLibrary.writeFile("test.txt", "just a text here")
```

7. Read file as JSON
```python
fileLibrary.openFileAsJson("fileName.extension")
# fileLibrary.openFileAsJson("test.json")
```

8. Write file as JSON
```python
fileLibrary.writeFileAsJson("fileName.extension", {"data": "here"})
# fileLibrary.writeFileAsJson("test.json", {"name": "John", "age": "30"})
```

# Congratulations! You've finished the documentation. Explore the package and create awesome projects!