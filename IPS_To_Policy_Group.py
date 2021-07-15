import requests

headers = {
	'api-secret-key': '7AF31EED-D12F-FE15-2FAF-F49552B093F3:70C71471-9AEE-ED71-3C5C-6133C627D9C8:hJfFVu0fc3NYuFiYdNfOUo8j2eCrG7pJtb6qK3miOa0=',
	'api-version': 'v1', 'Content-Type': 'application/json', 'charset':'UTF-8'
	}

payload = {"ruleIDs": [21,22,23]}
#payload = open("rules_id.json")

f = open('policy_id.txt', 'r')
for line in f.readlines():
	id = line.strip('\n')
	# TM DSM API URL {policy_id}
	url = "https://app.deepsecurity.trendmicro.com/api/policies/{0}/intrusionprevention/assignments".format(id)

	r  = requests.post(url,data= None, json = payload, headers=headers)

	print ("Machine ID "+line +" "+ r.text)

