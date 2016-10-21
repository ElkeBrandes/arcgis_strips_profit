
import csv # for export into csv file
import sys # for export into csv file
import arcpy
import re # regular expression, to extract the cutoff values out of the scenario names

# set the environment so that output data are being overwritten
arcpy.env.overwriteOutput=True
# specify the workspace to avoid having to write the path for each feature class
arcpy.env.workspace = "C:\\Users\\ebrandes\\Documents\\DNDC\\switchgrass_integration.gdb"


# import data:

# SubfieldIA_single (already in the geodatabase)

# profit data (table)
in_rows ="C:\\Users\\ebrandes\\Documents\\STRIPS_profit\\tables\\cgsb_profit_surface_2012_2014.txt"
out_path = "C:\\Users\\ebrandes\\Documents\\DNDC\\switchgrass_integration.gdb"
out_name = "subfield_profit_surface_2012_2014"
#arcpy.TableToTable_conversion(in_rows, out_path, out_name)

print("Joining data...")
# join profit data to SubfieldIA_single
in_feature_class = "SubfieldIA_single"
in_field = "cluid_mukey" 
join_table = "subfield_profit_surface_2012_2014"
join_field = "cluid_mukey"
field_list = ["profit_cg_2012", "profit_sb_2012", "profit_cg_2014", "profit_sb_2014"]
arcpy.JoinField_management(in_feature_class, in_field, join_table, join_field, field_list)

print("Done joining.")



