# -*- coding: utf-8 -*-
"""
Spyder Editor

This script provides automated data loading
"""

import arcpy, os, sys



projectFilePath = r"C:\work\fall2017"
arcpy.env.workspace = projectFilePath

aprxFiles = [f for root, dirs, files in os.walk(projectFilePath) for f in files if 'aprx' in f]
aprxFilePath = os.path.join(projectFilePath, aprxFiles[0])

#Set the arcpy Project file to the file path
arcProj = arcpy.mp.ArcGISProject(aprxFilePath)

#Use the list maps and feature classes to get all files.
theMaps = arcProj.listMaps()
featureClasses = arcpy.ListFeatureClasses()

#Create the layer object
layer = theMaps[0].addDataFromPath(os.path.join(projectFilePath, featureClasses[0]) )
layer.visible = True
layer.visible = False
