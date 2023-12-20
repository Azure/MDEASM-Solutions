# MDEASM: Rapid7 InsightVM Vulnerability Management Integration

## Overview
Playbook demonstrates automation to integrate MDEASM Inventory Assets with Rapid7 InsightVM Vulnerability Management tool.  The solution is customizable by querying MDEASM for certain vulnerabilities or set criteria from your MDEASM Inventory and selected Host IP Addresses are transmitted to Rapid7 InsightVM and tracked via labels in MDEASM.

1. The playbook queries MDEASM Inventory using the 'filter' parameter for "Host" Asset type and transmits these Assets to Rapid7 InsightVM.
2. The playbook has inbuilt trigger condition to run only when Assets are returned by the EASM Query, this allows the playbook to run near-realtime frequency and not add any additional Azure cost. the 'RunFrequency' parameter (In Seconds) can be used to change the schedule to run the playbook as needed. By default it is run very 3600 seconds (hourly)
3. The playbook also adds/updates User-defined label to the MDEASM Asset detail field 'label' for reference and tracking. this also avoids creating duplicate transactions for the same asset/s.
4. The playbook solution uses "Create Assets" Rapid7 InsightVM API to integrate with it and below Prerequisities cover the requirements

## Prerequisites
1. MDEASM API in this playbook supports Azure AD Authentication which requires you to have an App registration or Service Principal setup and used for authorization
2. MDEASM filter parameter needs to be set to an appropriate value to query inventory assets. Refer MDEASM API documentation
	For Example: here's an example of a MDEASM query
					        state="confirmed" and kind = "HOST" and ipAddress !empty and ipv4 = true and cvssScore >= 7
    Reference for filtering, https://github.com/Azure/MDEASM-Solutions/blob/main/API%20Postman%20Collection/EASM%20Filter%20Mappings.xlsx
3. Rapid7 InsightVM "Create Assets" API is being utilized for this Integration which requires Rapid7 InsightVM API Keys (Username & Password) generated with write permissions to Add Assets within Rapid7.
            For Rapid7 InsightVM API Documentation, https://help.rapid7.com/insightvm/en-us/api/index.html#operation/createAsset
4. The solution also requires users to enter the correct server name or hostname with port number used for hosting the InsightVM instance. these values are available as parameters in this Azure Template as "Rapid7-Hostname" and "Rapid7-HostPort"
    

## Deployment

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2FMDEASM-Solutions%2Fmain%2FAutomation%2FRapid7-VulnManagement-Integration%2FRapid7-VulnIntegration.json" target="_blank">
    <img src="https://aka.ms/deploytoazurebutton"/>
</a>
<a href="https://portal.azure.us/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2FMDEASM-Solutions%2Fmain%2FAutomation%2FRapid7-VulnManagement-Integration%2FRapid7-VulnIntegration.json" target="_blank">
    <img src="https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/1-CONTRIBUTION-GUIDE/images/deploytoazuregov.png"/>
</a>

### Post-Deployment Instructions


The playbook can be edited if any custom changes needed.
