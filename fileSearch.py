import maya.cmds as mc

basicFiles = "All Files(*.*);;PNG(*.png);;Tiff(*.tif)"

def search(projPath=''):
    searchPath = "{}/sourceimages".format(projPath)
    selectFiles = mc.fileDialog2(ff=basicFiles,fm=1,ds=1,dir=searchPath,caption="selectFiles")
    selectFiles = r"{}".format(selectFiles[0])
    localPath = selectFiles.replace("{}/".format(projPath)," ")
    print localPath
    return localPath
