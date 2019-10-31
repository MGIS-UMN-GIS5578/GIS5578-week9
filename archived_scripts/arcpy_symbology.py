import arcpy, os, sys
relpath = os.path.dirname(sys.argv[0])
p = arcpy.mp.ArcGISProject(relpath + r'\\Symbol.aprx') 
m = p.listMaps('Map')[0] 
for lyr in m.listLayers(): 
    if lyr.isFeatureLayer: 
        sym = lyr.symbology 
        if hasattr(sym, 'renderer'): 
            if sym.renderer.type == 'SimpleRenderer':
                sym.updateRenderer('GraduatedColorsRenderer')
                sym.renderer.breakCount = 6 
        lyr.symbology = sym 
        p.saveACopy(relpath + r"\\SavedOutput.aprx")
