"""Exercise 14.3. In a large collection of MP3 files, there may be more than one copy of the same song, stored in different directories or with different file names. The goal of this exercise is to search for duplicates.
1. Writeaprogramthatsearchesadirectoryandallofitssubdirectories,recursively,andreturns a list of complete paths for all files with a given suffix (like .mp3). Hint: os.path provides several useful functions for manipulating file and path names.
2. To recognize duplicates, you can use md5sum to compute a “checksum” for each files. If two files have the same checksum, they probably have the same contents.
3. To double-check, you can use the Unix command diff.
Solution: http: // thinkpython2. com/ code/ find_ duplicates. py ."""

import os

def mapFiles(extension, root):
    res = {} 
    for item in os.listdir(root):
        path = os.path.join(root, item)
        if os.path.isdir(path):
            res.update(mapFiles(extension, path))
        elif extension in item:
            res.setdefault(item, path)
        else:
            continue
    return res 

def mapDuplicates(path_map):
    res = {} 
    for key, value in path_map.items():
        cmd = 'md5 ' + value.replace(" ", "\ ")
        md5 = os.popen(cmd).read().split(" = ")
        res.setdefault(md5[1], []).append(key) 
    return res.values()

print(mapDuplicates(mapFiles(".pdf", "/Users/gabrielbarberini/Desktop/MIT OCW/1.A-gentle-introduction-to-programming-using-python-january")))
