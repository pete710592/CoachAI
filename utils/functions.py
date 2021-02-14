import os
import shutil

def checkDirExist(path):
    if not os.path.isdir(path):
        os.makedirs(path)
        
def deleteDir(path):
    try:
        shutil.rmtree(path)
    except OSError as e:
        pass
    else:
        print("The directory is deleted successfully")
