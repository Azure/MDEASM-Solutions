# MDEASM: MDTI Domain Check

## Overview
Playbook demonstrates automation to check all Approved domains in MDEASM and check them against MDTI articles, intel profiles and reputation scores. An email is sent if there is a match on any of these checks.

1. The playbook queries MDEASM Inventory using the 'filter' parameter to get all confirmed domains, sends them to MDTI and creates and email alert to review the results
2. The playbook has a 'RunFrequency' parameter (In Days) can be used to change the schedule to run the playbook as needed. By default it is run every 7 days
3. The playbook checks if the approved domains are associated to any articles, intel profiles or reputation scores
4. The playbook uses Azure Logic Apps Office365 Connector as an example for sending Emails. Any other available Email connector can be used in place of this as needed by users. 

## Prerequisites
1. MDEASM API in this playbook supports Azure AD Authentication which requires you to have an App registration or Service Principal setup and used for authorization
2. MDTI API in this playbook supports Azure AD Authentication which requires you to have an App registration or Service Principal setup and used for authorization
3. Office365 connection requires authorization via login and destination email addresses where Alerts need to be sent

## Deployment

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2FMDEASM-Solutions%2Fmain%2FAutomation%2FMDTI-MDEASM-Integration%2FMDTI-MDEASM-Integration.json" target="_blank">
    <img src="https://aka.ms/deploytoazurebutton"/>
</a>
<a href="https://portal.azure.us/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2FMDEASM-Solutions%2Fmain%2FAutomation%2FMDTI-MDEASM-Integration%2FMDTI-MDEASM-Integration.json" target="_blank">
    <img src="https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/1-CONTRIBUTION-GUIDE/images/deploytoazuregov.png"/>
</a>

### Post-Deployment Instructions
After deploying the playbook, you must authorize the connections leveraged.

1. Visit the playbook resource.
2. Under "Development Tools" (located on the left), click "API Connections".
3. Ensure each connection has been authorized.

The playbook can be edited if any custom changes needed.
