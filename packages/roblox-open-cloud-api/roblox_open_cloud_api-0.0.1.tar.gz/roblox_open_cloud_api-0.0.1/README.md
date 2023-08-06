# Roblox Open Cloud API
## Coded in python

Contains a module which allows you to utilise open cloud on Roblox.

Install this module using pip!
Choose whichever fits your environment.
```batch
python3 pip install roblox_open_cloud

pip install roblox_open_cloud
```

Start with the following;
```py
from roblox_open_cloud import Client as OpenCloudAPI, BaseEnum, Enum

# Key is necessary
OpenCloudClient = OpenCloudAPI(api_key="YOUR_API_KEY", cookies=None, headers=None)

# set the cookie for any request, optional info
OpenCloudClient.setCookie("cookie_name", "cookie_value", "domain" or None)

# set the headers in any request, optional info
OpenCloudClient.setHeader("header_name", "header_value")

# universe_id = integer, topic = string, data = string
resultEnum = OpenCloudClient.PostOnMessagingService(universe_id=0, topic=None, data=None)
if resultEnum == Enum.Success:
	print("Success")
else:
	print("Unsuccessful - Reason; ", resultEnum)

[UNAVAILABLE ITEMS - FUTURE REFERENCE]
# DATASTORE API
# OpenCloudClient.GetAllDataInDataStore(universe_id=0)
# OpenCloudClient.GetDataFromKeyInDataStore(universe_id=0, key="key_to_search")
# OpenCloudClient.GetDataFromKeysInDataStore(universe_id=0, key=["key_1", "key_2"])

# OpenCloudClient.SetDataForKeyInDataStore(universe_id=0, key="key_to_search", json_data="")
# OpenCloudClient.SetDataFromTuplesInDataStore(universe_id=0, data_tuples=[ ("key", "json_value") ])
# OpenCloudClient.SetDataFromDictInDataStore(universe_id=0, data_dict={"key":"json_value"})
# OpenCloudClient.SetDataFromArraysInDataStore(universe_id=0, key_array=["key_1", "key_2"], data_array=["data_1", "data_2"]) # USE for key, data in ZIP(arrayA, arrayB)

# OpenCloudClient.ClearDataStore(universe_id=0, backupDataLocally=True)

# PUBLISH PLACE API
# OpenCloudClient.PublishPlace(universe_id=0, filepath="")
```

Simple to use ;-)
