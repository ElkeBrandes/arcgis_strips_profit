
import csv # for export into csv file
import sys # for export into csv file
import arcpy
import re # regular expression, to extract the cutoff values out of the scenario names
from arcpy.sa import *  #spatial analyst extension - needed for reclassify?

# set the environment so that output data are being overwritten
arcpy.env.overwriteOutput=True
# specify the workspace to avoid having to write the path for each feature class
arcpy.env.workspace = "C:\\Users\\ebrandes\\Documents\\DNDC\\switchgrass_integration.gdb"

# environment setting: snap raster
# raster = # the raster that the output rasters should be snapped to (existing raster)
# arcpy.env.snapRaster = raster


# rasterize the subfield layer, keeping profit data for 2014
in_features = "SubfieldHUC071000040103"
value_field = "profit14"
out_rasterdataset = "profit14_raster"
arcpy.PolygonToRaster_conversion(in_features, value_field, out_rasterdataset,\
                                 "MAXIMUM_COMBINED_AREA", "", 30)

# attribute tables can only be built for rasters with integer values. Because the transformation from
# float to integer would simply truncate the decimal digits, it is better to round the profit in the
# SQL db to the dollar and then use that dataset to join to the feature class.

# Build an attribute table
in_raster = out_rasterdataset
arcpy.BuildRasterAttributeTable_management(in_raster, "OVERWRITE")


# reclassify to differentiate only between pixels of a profit category and all others

in_raster = out_rasterdataset
reclass_field = value_field
remap = RemapRange([[-1000,-250,"<-250"],[-250,-100,"-250--100"]])
arcpy.Reclassify(in_raster, reclass_field, remap)
