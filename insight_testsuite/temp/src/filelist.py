import glob, os
def get_filelist():
    os.chdir("../input")
    filelist = []
    for file in glob.glob("*.txt"):
        filelist = filelist + [file]
    return filelist