import arcpy, os, sys

def ChangeSymbology(sym, symType, breaks):
    """
    I’m a function that changes the symbology    
    """
    sym.updateRenderer(symType)
    sym.renderer.breakCount = breaks

projectFilePath = r"C:\GIS5578\fall2017"
arcpy.env.workspace = projectFilePath

aprxFiles = [f for root, dirs, files in os.walk(projectFilePath) for f in files if 'aprx' in f]
shpFilePaths = ["%s/%s" % (root,f) for root, dirs, files in os.walk(projectFilePath) for f in files if 'shp' in f]

aprxFilePath = r"%s\%s" % (projectFilePath, aprxFiles[0])
arcProj = arcpy.mp.ArcGISProject(aprxFilePath)
maps = arcProj.listMaps()
featureClasses = arcpy.ListFeatureClasses()
layer = maps[0].addDataFromPath(r"%s\%s" % (projectFilePath, featureClasses[0]))

for lyr in maps[0].listLayers():
  if lyr.isFeatureLayer:
    sym = lyr.symbology
    if hasattr(sym, 'renderer'): ChangeSymbology(sym, 'GraduatedColors', 6)

