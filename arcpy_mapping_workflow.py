# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import arcpy
import os

def LoadDataFromDirectory(theDirectory, theMap ):
    """
    
    """
    arcpy.env.workspace = theDirectory
    
    mapLayers = []    
    for shp in arcpy.ListFeatureClasses():
        shpFilePath = r"%s\%s" % (theDirectory, shp)
        mapLayers.append(theMap.addDataFromFile(shpFilePath))
        
    return mapLayers
        
    
def ChangeLayerSymbology(theLayer, symbologyName, breakValue = 5):
    """
    
    """
    sym = theLayer.symbology
    
    if symbologyName in ['GraduatedColorsRenderer', 'GraduatedSymbolsRenderer']:        
        sym.updateRenderer('GraduatedColorsRenderer')
        sym.renderer.breakCount = breakValue
        theLayer.symbology = sym   
        
    elif symbologyName == 'SimpleRenderer':
        sym.updateRenderer('GraduatedColorsRenderer')
        theLayer.symbology = sym
        
    elif symbologyName == 'UniqueValueRenderer':
        pass
        theLayer.symbology = sym
    
    

def ChangeLayerAttribute(theLayer, theFieldName):
    """
    
    """
    myFields = {f.name: f.type for f in arcpy.ListFields(theLayer.name) }    

    sym = theLayer.symbology
    if theFieldName in list(myFields.keys()):
       sym.renderer.classificationField = theFieldName
    else:
        print("Not a Valid field Name for layer %s" % (theLayer.name))
        print(list(myFields.keys()))

arcPRJFilePath = r"C:\work\week9"

arpxFilePaths = []
for root, dirs, files in os.walk(arcPRJFilePath):
    for f in files:
        #if 'aprx' in f: arpxFilePath = r"%s\%s" % (root, f):
        if 'aprx' in f: arpxFilePath.append(r"%s\%s" % (root, f) )

arpxFilePaths = [r"%s\%s" % (root,f) for root, dirs, files in os.walk(arcPRJFilePath) for f in files if 'aprx' in f ]

#for arcPRJPath in arpxFilePaths:
    
arcPRJ = arcpy.mp.ArcGISProject(arpxFilePaths[0])
maps = arcPRJ.listMaps()
myMap = maps[0]

myDatasetPath = r"%s\%s" % (arcPRJFilePath, features[0])


myLayer.visible = True
sym = myLayer.symbology


sym.updateRenderer('GraduatedColorsRenderer')
sym.renderer.breakCount = 6
myLayer.symbology = sym
sym.renderer.classificationField
'OBJECTID_1'

myFields {f.name: f.type for f in arcpy.ListFields(myLayer.name) }



#this return a single ramp object
ramp = arcPRJ.listColorRamps('Red-Yellow-Blue (6 Classes)')[0]
sym.renderer.colorRamp = ramp
myLayer.symbology = sym