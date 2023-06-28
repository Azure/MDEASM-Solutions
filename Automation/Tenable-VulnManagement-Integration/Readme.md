# MDEASM: Tenable Vulnerability Management Integration

## Overview
Playbook demonstrates automation to integrate MDEASM Inventory Assets with Tenable Vulnerability Management tool.  The solution is customizable by querying MDEASM for certain vulnerabilities or set criteria from your MDEASM Inventory and selected Host IP Addresses are transmitted to Tenable and tracked via labels in MDEASM.

1. The playbook queries MDEASM Inventory using the 'filter' parameter for "Host" Asset type and transmits these Assets to tenable.
2. The playbook has inbuilt trigger condition to run only when Assets are returned by the EASM Query, this allows the playbook to run near-realtime frequency and not add any additional Azure cost. the 'RunFrequency' parameter (In Seconds) can be used to change the schedule to run the playbook as needed. By default it is run very 3600 seconds (hourly)
3. The playbook also adds/updates User-defined label to the MDEASM Asset detail field 'label' for reference and tracking. this also avoids creating duplicate transactions for the same asset/s.
4. The playbook solution uses "Import Assets" Tenable API to integrate with it and below Prerequisities cover the requirements

## Prerequisites
1. MDEASM API in this playbook supports Azure AD Authentication which requires you to have an App registration or Service Principal setup and used for authorization
2. Office365 connection requires authorization via login and destination email addresses where Alerts need to be sent
3. MDEASM filter parameter needs to be set to an appropriate value to query inventory assets. Refer MDEASM API documentation
	For Example: here's an example of a MDEASM query
					        state="confirmed" and kind = "HOST" and ipAddress !empty and ipv4 = true and cvssScore >= 7
    Reference for filtering, https://github.com/Azure/MDEASM-Solutions/blob/main/API%20Postman%20Collection/EASM%20Filter%20Mappings.xlsx
4. Tenable "Import Assets" API is being utilized for this Integration which requires Tenable API Keys generated with "ADMINISTRATOR [64] user permissions and CAN EDIT [64] scan permissions"
    Tenable API reference,  https://developer.tenable.com/reference/assets-import/
                            https://developer.tenable.com/docs/authorization/
                            https://developer.tenable.com/docs/add-asset-data-to-tenableio/

## Deployment

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2FMDEASM-Solutions%2Fmain%2FAutomation%2FTenable-VulnManagement-Integration%2FTenable-VulnIntegration.json" target="_blank">
    <img src="https://aka.ms/deploytoazurebutton"/>
</a>
<a href="https://portal.azure.us/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2FMDEASM-Solutions%2Fmain%2FAutomation%2FTenable-VulnManagement-Integration%2FTenable-VulnIntegration.json" target="_blank">
    <img src="https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/1-CONTRIBUTION-GUIDE/images/deploytoazuregov.png"/>
</a>

### Post-Deployment Instructions


The playbook can be edited if any custom changes needed.
