## MDEASM API sample Jupyter Notebooks
This repo contains sample notebooks for using the Microsoft Defender External Attack Surface Management (MDEASM) API.

These Jupyter Notebooks demonstrate the usage of the MDEASM API endpoints that allow users to access their attack surface data easily using PowerShell or Python in an interactive environment.

Available endpoints/actions:
Assets - List
Assets - Get
Assets - Update
Tasks - Get
Tasks - List
Tasks - Cancel
Bonus Function - Get Common Assets
Labels - Create And Update
Labels -  List
Labels - Get
Labels - Delete
Labels - Update


## Instructions to use the notebooks
Recommended - Use VS Code and Extensions
Python notebook, follow these steps:
1. Install [VS Code](https://code.visualstudio.com/)
2. Add the [Python Extension for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python) once configured, `pip install requests`
3. Add the [Jupyter Extension for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)   

PowerShell notebook, follow these steps:
1. Install [VS Code](https://code.visualstudio.com/)
2. Add the [PowerShell Extension for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-vscode.PowerShell)
3. Add the [.NET Extension Pack](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.vscode-dotnet-pack) which includes Jupyter support  

Non-VS Code setups vary by language preference and operating systems...

4. Enter in the required MDEASM information (tenantId, subscriptionId, resourceGroupName, workspaceName, region, service principal clientId, & clientSecret)
5. See the helper file [**EASM Filter Mappings.xlsx**](https://github.com/Azure/MDEASM-Solutions/blob/main/API%20Postman%20Collection/EASM%20Filter%20Mappings.xlsx) for finding queryable field names for Asset Search parameter "filter"

MDEASM API documentation can be found here, https://learn.microsoft.com/en-us/rest/api/defenderforeasm/

Azure AD Authentication details can be found here, https://docs.microsoft.com/en-us/rest/api/azure/#how-to-call-azure-rest-apis-with-postman



## Suggestions and feedback
We value your feedback. Let us know if you run into any problems or share your suggestions and feedback to MDEASM Go-To-Production (GTP) Customer Experience Engineering (CxE) Team. Email: mdeasm_cxe@microsoft.com
