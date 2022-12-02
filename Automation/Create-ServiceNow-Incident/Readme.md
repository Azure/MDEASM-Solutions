# MDEASM: Create ServiceNow Incidents

## Overview
Playbook demonstrates automation to create incidents in ServiceNow for select Inventory Assets by querying for certain vulnerabilities or set criteria from your MDEASM Inventory.

## Prerequisites
MDEASM API in this playbook supports Azure AD Authentication which requires you to have an App registration or Service Principal setup and used for authorization
Service Now API connection requires authorization using serviceNow instance URL, username and password
MDEASM filter parameter needs to be set to an appropriate query to query inventory assets. Refer MDEASM API documentation

## Deployment

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2FMDEASM-Solutions%2Fmaster%2FAutomation%2FCreate-ServiceNow-Incident.json" target="_blank">
    <img src="https://aka.ms/deploytoazurebutton"/>
</a>
<a href="https://portal.azure.us/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2FMDEASM-Solutions%2Fmaster%2FAutomation%2FCreate-ServiceNow-Incident.json" target="_blank">
    <img src="https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/1-CONTRIBUTION-GUIDE/images/deploytoazuregov.png"/>
</a>

### Post-Deployment Instructions
After deploying the playbook, you must authorize the connections leveraged.

1. Visit the playbook resource.
2. Under "Development Tools" (located on the left), click "API Connections".
3. Ensure each connection has been authorized.

**Note: any notes FYI **
