import maya.cmds as mc
import fileSearch
import connectNode

projPath = r"//172.29.44.4/cg/ct13a_rask/kmr/ML_Shintaiso"

# Reload =============================
reload(fileSearch)
reload(connectNode)

# import File Path #
def importNormal(*args):
    fPath = fileSearch.search(projPath)
    print fPath
    mc.textField('nmPath', e=True, text=fPath)

def importColor(*args):
    fPath = fileSearch.search(projPath)
    print fPath
    mc.textField('cPath', e=True, text=fPath)

def importLoud(*args):
    fPath = fileSearch.search(projPath)
    print fPath
    mc.textField('lnPath', e=True, text=fPath)

def importEmission(*args):
    fPath = fileSearch.search(projPath)
    print fPath
    mc.textField('emPath', e=True, text=fPath)

def importBump(*args):
    fPath = fileSearch.search(projPath)
    print fPath
    mc.textField('bpPath', e=True, text=fPath)

def importMetal(*args):
    fPath = fileSearch.search(projPath)
    print fPath
    mc.textField('mnPath', e=True, text=fPath)

# connect File => Node #
def connectFiles(*args):
    cN = mc.textField('nmPath', q=True)
    cC = mc.textField('cPath', q=True)
    cL = mc.textField('lnPath', q=True)
    cE = mc.textField('emPath', q=True)
    cM = mc.textField('mnPath', q=True)
    connectNode.connectNor(cN)
    connectNode.connectCol(cC)
    connectNode.connectLou(cL)
    connectNode.connectEmi(cE)
    connectNode.connectMet(cM)
    pass

def ui():
    if mc.window("subTexConnecter", exists=True):
        mc.deleteUI("subTexConnecter")

    win = mc.window("subTexConnecter",t="subTexConnecter",w=250)

    mc.frameLayout(label='normalMap')
    mc.button("selectFiles", command=importNormal)
    mc.textField('nmPath')
    mc.frameLayout(label='colorMap')
    mc.button("selectFiles", command=importColor)
    mc.textField('cPath')
    mc.frameLayout(label='loudness')
    mc.button("selectFiles", command=importLoud)
    mc.textField('lnPath')
    mc.frameLayout(label='emission')
    mc.button("selectFiles", command=importEmission)
    mc.textField('emPath')
    mc.frameLayout(label='metalness')
    mc.button("selectFiles", command=importMetal)
    mc.textField('mnPath')

    mc.columnLayout(adj=True)
    mc.button("Submit", command=connectFiles)

    mc.showWindow(win)
