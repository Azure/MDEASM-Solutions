#imports
from azure.defender.easm import EasmClient
from azure.mgmt.defendereasm import EasmMgmtClient
from azure.identity import ClientSecretCredential
import xlsxwriter
import sys

# Script parameters
client_id = ''
# App Client secret
client_secret = ''
# Tenant ID
tenant_id = ''
# Subscription ID
subcription_id = ''
# Resource Group Name Where EASM resides
resource_group = ''
# EASM Region
region = ''
# Name of EASM resource
workspace_name = ''

# Get credentials and create client
completeCredential = ClientSecretCredential(tenant_id, client_id, client_secret)
dataEndpoint = f'{region}.easm.defender.microsoft.com'
dataClient = EasmClient(dataEndpoint, resource_group, subcription_id, workspace_name, completeCredential)
controlClient = EasmMgmtClient(completeCredential, subcription_id)
workbook = xlsxwriter.Workbook('AssetBreakdown.xlsx', {'strings_to_urls': False})
worksheet = workbook.add_worksheet('Assets')
assetType_list = ["billable_ip_addresses", "billable_domains", "billable_hosts"]


def get_billable_list(assetType, count):
    page = 0
    last_page = False
    while last_page is False:
        billable = dataClient.reports.snapshot(body={"metric": assetType, "page": page, "size": 100})
        last_page = billable['assets']['last']
        page += 1
        for each_biilable_asset in billable['assets']['content']:
            print(each_biilable_asset['name'])
            worksheet.write(count, 0, assetType)
            worksheet.write(count, 1, each_biilable_asset['name'])
            count += 1
    return count

def create_headers():
    # Headers
    worksheet.write(0, 0, "Asset Type")
    worksheet.write(0, 1, "Asset Name")


def main():
    create_headers()
    AssetPageCount = 1
    for each_assetType in assetType_list:
        AssetPageCount = get_billable_list(each_assetType, AssetPageCount)
    workbook.close()


if __name__ == '__main__':
    sys.exit(main())
