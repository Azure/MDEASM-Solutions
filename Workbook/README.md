# MDEASM
 MD External Attack Surface Management workbook for connecting to either a Log Analytics or Azure Data Explorer source

### Conolidated workbook with all visualizations in either a single scrollable page or clickable tabs

If your `EASM Workspace Name` dropdown fails to populate, then you have one (or more) of the following problems:
1. your Azure Data Explorer Cluster URI and/or Database name are wrong
2. your Log Analytics workspace name and/or Resource Group name were entered incorrectly when you deployed the workbook
3. your Azure Data Explorer and/or Log Analytics do(es) not have data (empty tables; best to confirm this directly within `Azure Data Explorer/Query` or `Log Analytics/Logs`)

If you only have a single snapshot of data, then the charts and visuals will populate with that information.  
As soon as there is more than one snapshot of data, the Asset and Risk data from the oldest snapshot will be ignored in order to minimize the large variance that can show between pre-built EASM workspaces and those same workspaces after discovery has run.

[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2FMDEASM-Solutions%2Fmain%2FWorkbook%2Fmdeasm_workbook_template.json)
![workbook_condolidated](https://raw.githubusercontent.com/Azure/MDEASM-Solutions/main/Workbook/.images/image_workbook_consolidated.png "workbook_condolidated")