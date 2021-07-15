import requests

headers = {
	'api-secret-key': 'YOUR API KEY GOES HERE',
	'api-version': 'v1', 'Content-Type': 'application/json', 'charset':'UTF-8'
	}

payload = {"ruleIDs": [21,22,23,......................,LIST OF RULE IDs]}
#payload = open("rules_id.json")

f = open('policy_id.txt', 'r')
for line in f.readlines():
	id = line.strip('\n')
	# TM DSM API URL {policy_id}
	url = "https://app.deepsecurity.trendmicro.com/api/policies/{0}/intrusionprevention/assignments".format(id)

	r  = requests.post(url,data= None, json = payload, headers=headers)

	print ("Machine ID "+line +" "+ r.text)

