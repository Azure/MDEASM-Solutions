# MDEASM: Inventory Assets Download

## Overview
Playbook demonstrates automation to download MDEASM Inventory assets and their details to Onedrive Storage providing a template to Query EASM at regular intervals to get Asset data and integrate into your desired storage solution.

1. The playbook queries MDEASM Inventory using the 'filter' parameter and saves the API response in a specified folder in OneDrive Storage as JSON Files with datetimestamp in the file name.
2. The default 'filter' parameter is set to query all Inventory Assets in the "Approved Inventory" Status. the parameter is made available to set your inventory query to match your requirements. Refer MDEASM API documentation for more details on this.
3. The playbook uses OneDrive Logic Apps Connector
4. This same process can be used to download newly added and updated assets in Inventory on a daily basis or at a set run frequency by including the field 'updatedAt' in the filter parameter.

## Prerequisites
1. MDEASM API in this playbook supports Azure AD Authentication which requires you to have an App registration or Service Principal setup and used for authorization
2. OneDrive connection requires authorization using your login and access to the folder path where the files need to be saved.
3. MDEASM filter parameter needs to be set to an appropriate value to query inventory assets. Refer MDEASM API documentation

## Deployment

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2FMDEASM-Solutions%2Fmain%2FAutomation%2FInventory-Assets-Download%2FInventory-Assets-Download.json" target="_blank">
    <img src="https://aka.ms/deploytoazurebutton"/>
</a>
<a href="https://portal.azure.us/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2FMDEASM-Solutions%2Fmain%2FAutomation%2FInventory-Assets-Download%2FInventory-Assets-Download.json" target="_blank">
    <img src="https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/1-CONTRIBUTION-GUIDE/images/deploytoazuregov.png"/>
</a>

### Post-Deployment Instructions
After deploying the playbook, you must authorize the connections leveraged.

1. Visit the playbook resource.
2. Under "Development Tools" (located on the left), click "API Connections".
3. Ensure each connection has been authorized.

The playbook can be edited if any custom or parameter changes needed.
