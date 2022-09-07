import requests
import json


class MakeApiCall:

    def get_data(self, api):
        #response = requests.get(f"{api}", headers= headers)
        headers = {
            "Accept": "application/json",
            "keyid": "5e5951bf-ebde-443e-a40d-a4e24c4b9103"
        }
        response = requests.get(f"{api}", headers=headers)
        if response.status_code == 200:
            print("sucessfully fetched the data")
            self.formatted_print(response.json())
        else:
            print(
                f"Hello person, there's a {response.status_code} error with your request")
    def formatted_print(self, obj):
        text = json.dumps(obj, sort_keys=True, indent=4)
        print(text)
        #length = len(text)
        #for i in text:
            #j = json.dumps(i)
            #nodeId = (i["nodeID"])

            #print(type(i))
            #print("******************************************************")
       # print(length)


    def __init__(self, api):
        self.get_data(api)

if __name__ == "__main__":
    api_call = MakeApiCall("https://webapi.vermeer.com/integrations/external/vcom/v1/equipment/126348/specifications?cmsLanguageID=1&displayFilter=0")
    #api_call1 = MakeApiCall("https://webapi.vermeer.com/integrations/external/vcom/v1/products/8549?documentculture=en-us&regions=NorthAmerica")