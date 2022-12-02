# MDEASM: Create ServiceNow Incidents

## Overview
Playbook demonstrates automation to create incidents in ServiceNow for select Inventory Assets by querying for certain vulnerabilities or set criteria from your MDEASM Inventory.

1. The playbook queries MDEASM Inventory using the 'filter' parameter and creates incidents in ServiceNow Instance for each Asset result from the MDEASM query
2. The playbook has inbuilt trigger condition to run only when Assets are returned by the EASM Query, this allows the playbook to run near-realtime frequency and not add any additional Azure cost. the 'RunFrequency' parameter (In Seconds) can be used to change the schedule to run the playbook as needed. By default it is run very 60 seconds
3. The playbook also adds/updates the ServiceNow Incident Number to the MDEASM Asset detail field 'ExternalId' for reference
4. The playbook uses Azure Logic Apps Service Now Connector

## Prerequisites
1. MDEASM API in this playbook supports Azure AD Authentication which requires you to have an App registration or Service Principal setup and used for authorization
2. ServiceNow API connection requires authorization using serviceNow instance URL, username and password
3. MDEASM filter parameter needs to be set to an appropriate value to query inventory assets. Refer MDEASM API documentation

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

The playbook can be edited if any custom changes needed.
