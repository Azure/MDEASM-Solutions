# MDEASM: Inventory Email Alerts

## Overview
Playbook demonstrates automation to Monitor Inventory Assets and alert via Email notifications by querying for certain vulnerabilities or set criteria from your MDEASM Inventory.

1. The playbook queries MDEASM Inventory using the 'filter' parameter and creates email alerts for the inventory Asset results
2. The playbook has inbuilt trigger condition to run only when Assets are returned by the EASM Query, this allows the playbook to run near-realtime frequency and not add any additional Azure cost. the 'RunFrequency' parameter (In Seconds) can be used to change the schedule to run the playbook as needed. By default it is run very 60 seconds
3. The playbook also adds/updates User-defined label to the MDEASM Asset detail field 'label' for reference and tracking. this also avoids creating duplicate alerts for the same assets.
4. The playbook uses Azure Logic Apps Office365 Connector as an example for sending Emails. any other available Email connector can be used in place of this as needed by users. 

## Prerequisites
1. MDEASM API in this playbook supports Azure AD Authentication which requires you to have an App registration or Service Principal setup and used for authorization
2. Office365 connection requires authorization via login and destination email addresses where Alerts need to be sent
3. MDEASM filter parameter needs to be set to an appropriate value to query inventory assets. Refer MDEASM API documentation
	For Example: here's a query to monitor and alert for all assets with CVSS Score >= 8
					state="confirmed" and kind = "page" and rooturl = true and cvssScore >= 8

## Deployment

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2FMDEASM-Solutions%2Fmain%2FAutomation%2FInventory-Alerts-Email%2FInventory-Alerts-Email.json" target="_blank">
    <img src="https://aka.ms/deploytoazurebutton"/>
</a>
<a href="https://portal.azure.us/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2FMDEASM-Solutions%2Fmain%2FAutomation%2FInventory-Alerts-Email%2FInventory-Alerts-Email.json" target="_blank">
    <img src="https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/1-CONTRIBUTION-GUIDE/images/deploytoazuregov.png"/>
</a>

### Post-Deployment Instructions
After deploying the playbook, you must authorize the connections leveraged.

1. Visit the playbook resource.
2. Under "Development Tools" (located on the left), click "API Connections".
3. Ensure each connection has been authorized.

The playbook can be edited if any custom changes needed.
