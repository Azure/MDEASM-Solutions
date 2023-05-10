<img src="logic_app_logo.png" alt="LogicApps Logo" width="300" height="200">

## About
This repo contains the filters which can be used to label the attack surface for specific use cases.

## Instructions for adding the filter
The filters can be used in the API or in the logic apps.
MDEASM API documentation can be found here, https://learn.microsoft.com/en-us/rest/api/defenderforeasm/
These filters can also be added to Logic Apps such as Inventory-Alerts-Email, https://github.com/Azure/MDEASM-Solutions/tree/main/Automation/Inventory-Alerts-Email


After selecting a playbook from https://github.com/Azure/MDEASM-Solutions:
1. Click "Deploy to Azure"
2. Wait for Microsoft Azure to load
3. Edit all the relevant fields such as the Label Name, Run Frequency and Filter (located in each txt file within this directory) 
4. Click **Review+Create**

Once deployment is complete, you will need to authorize each connection.
1. For Example, Click the Email connection resource
2. Select a Email Connection or create a new Email Connection
3. Click Authorize
4. Sign in
5. Click Save
6. Repeat steps for other connections

You can now edit the playbook in Azure Logic apps.

## Suggestions and feedback
We value your feedback. Let us know if you run into any problems or share your suggestions and feedback to MDEASM Go-To-Production (GTP) Customer Experience Engineering (CxE) Team. Email: mdeasm_cxe@microsoft.com