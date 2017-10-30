import glob, os
def get_filelist():
    os.chdir("../Input")
    filelist = []
    for file in glob.glob("*.txt"):
        filelist = filelist + [file]
    return filelist