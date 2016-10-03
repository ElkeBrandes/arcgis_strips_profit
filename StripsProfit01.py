
import csv # for export into csv file
import sys # for export into csv file
import arcpy
import re # regular expression, to extract the cutoff values out of the scenario names

# set the environment so that output data are being overwritten
arcpy.env.overwriteOutput=True
# specify the workspace to avoid having to write the path for each feature class
arcpy.env.workspace = "C:\\Users\\ebrandes\\Documents\\DNDC\\switchgrass_integration.gdb"


# import data:

# subfieldIA_single (already in the geodatabase)

# watershed feature class
in_feature = "C:\\Users\\ebrandes\\Documents\\shapefiles\\wbdhu12_a_07100004.shp"
out_path = "C:\\Users\\ebrandes\\Documents\\DNDC\\switchgrass_integration.gdb"
out_name = "HUC_07100004"
arcpy.FeatureClassToFeatureClass_conversion(in_feature, out_path, out_name)

# reproject "HUC_07100004"
in_dataset = "HUC_07100004"
out_dataset = str(in_dataset) + "_Projected"
out_coor_system = arcpy.SpatialReference('NAD 1983 UTM Zone 15N')
arcpy.Project_management(in_dataset, out_dataset, out_coor_system)

# check the spatial reference of the new feature class
desc = arcpy.Describe(out_dataset)
spatialRef = desc.SpatialReference
print("Just checking ... Reference System is " + str(spatialRef.Name) + ".")

# profit data (table)
in_rows =
out_path = "C:\\Users\\ebrandes\\Documents\\DNDC\\switchgrass_integration.gdb"
out_name = "subfield_profit_2012_2014"
TableToTable_conversion (in_rows, out_path, out_name)

# clip subfieldIA_single to HUC 12 071000040103 watershed (select in HUC_07100004 layer first)

# join profit data to subfieldIA_single




