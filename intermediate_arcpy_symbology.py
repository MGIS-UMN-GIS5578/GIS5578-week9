import arcpy, os, sys
projectFilePath = r"C:\GIS5578\fall2017"
arcpy.env.workspace = projectFilePath

aprxFiles = [f for root, dirs, files in os.walk(projectFilePath) for f in files if 'aprx' in f]
aprxFilePath = r"%s\%s" % (projectFilePath, aprxFiles[0])
arcProj = arcpy.mp.ArcGISProject(aprxFilePath)
maps = arcProj.listMaps()
featureClasses = arcpy.ListFeatureClasses()

layer = maps[0].addDataFromPath(r"%s\%s" % (projectFilePath, featureClasses[0]))

layer.visible = False

for lyr in maps[0].listLayers():
  if lyr.isFeatureLayer:
    sym = lyr.symbology
    if hasattr(sym, 'renderer'):
      if sym.renderer.type == 'SimpleRenderer':
        sym.updateRenderer('GraduatedColorsRenderer')
        sym.renderer.breakCount = 6
        
        lyr.symbology = sym

p.saveACopy(relpath + r"\\SavedOutput.aprx")
