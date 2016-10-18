# arcgis_strips_profit
This project combines spatial results of a slope analysis done by David James (NLAE) with ACPF and the subfield profit analalysis.

StripsProfit01.py:

This script includes the following processing steps as a test on the HUC 12 watershed 071000040103:

- import and reproject watershed layer
- import profit table of the respective county
- clip to watershed boundary
- join profit data to watershed layer


StripsProfit02.py:

This script includes the following processing steps as a test on the HUC 12 watershed 071000040103:

- rasterize the profit layer from script 1
- build an attribute table 
- reclassify
