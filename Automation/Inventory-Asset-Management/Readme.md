# MDEASM: Inventory Rules/Query based Asset Management 

## Overview
Playbook demonstrates automation that can be scheduled to run at regular intervals to update Inventory Assets by querying for certain vulnerabilities or set criteria using the "filter" parameter from your MDEASM Inventory.

### Asset update options for this playbooks are,
    1. Apply labels
    2. Change Asset Status
    3. Do both Change Asset Status and Apply label

1. The playbook queries MDEASM Inventory using the 'filter' parameter and updates inventory Asset results
2. The 'RunFrequency' parameter (In Hours) can be used to change the schedule to run the playbook as needed. By default it is run very 24 Hours.
3. The 'LabelName' parameter is used to apply the label by the playbook on the resultant Inventory Assets. The playbook will create a new label, if the label provided doesn't already exist in the EASM Workspace.
4. The 'StateValue' parameter is used to mention the New Changed State needed for Inventory Assets. allowed Asset state values: archived, candidate, associatedThirdparty, associated, dismissed, candidateInvestigate, confirmed, associatedPartner.
5. The Playbook also checks the status of the EASM Update till it completes successfully within the EASM Workspace. 
6. The Playbook will remain in running state or get failed if the update takes more than 2 hours to complete. Upon which it that playbook instance can be Re-Run.

## Prerequisites
1. MDEASM API in this playbook supports Azure AD Authentication which requires you to have an App registration or Service Principal setup and used for authorization
2. Atleast one of the parameters 'LabelName' and/or 'StateValue' is needed to be set fo rthe playbook to run
3. MDEASM filter parameter needs to be set to an appropriate value to query inventory assets. Refer MDEASM API documentation
	For Example: here's a query to monitor and alert for all assets with CVSS Score >= 8
					state="confirmed" and kind = "page" and rooturl = true and cvssScore >= 8

## Deployment

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2FMDEASM-Solutions%2Fmain%2FAutomation%2FInventory-Asset-Management%2FInventory-Asset-Management.json" target="_blank">
    <img src="https://aka.ms/deploytoazurebutton"/>
</a>
<a href="https://portal.azure.us/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2FMDEASM-Solutions%2Fmain%2FAutomation%2FInventory-Asset-Management%2FInventory-Asset-Management.json" target="_blank">
    <img src="https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/1-CONTRIBUTION-GUIDE/images/deploytoazuregov.png"/>
</a>

### Post-Deployment Instructions
After deploying the playbook, you must authorize the connections leveraged.

1. Visit the playbook resource.
2. Under "Development Tools" (located on the left), click "API Connections".
3. Ensure each connection has been authorized.

The playbook can be edited if any custom changes needed.
