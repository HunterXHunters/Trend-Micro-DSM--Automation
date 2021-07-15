import requests

#Authentication Header
headers = {
	'api-secret-key': 'DA26C635-BB1B-C97F-1421-465725518170:RWbN/9p+RONKEv3Kx6JTp77Do2/90cxTM8filwsuH3o=',
	'api-version': 'v1', 'Content-Type': 'application/json', 'charset':'UTF-8'
	}

#DSM IPS Rule IDs
rule_ids = {"ruleIDs": [3,12,25,45]}
#payload = open("rules_id.json")

#Looping List of Computer IDs to which above Rule IDs will get applied
f = open('computer_id.txt', 'r')
for line in f.readlines():
	id = line.strip('\n')
	# TM DSM API URL {computer_id}
	url = "https://10.255.252.67:4119/api/computers/{0}/intrusionprevention/assignments".format(id)

	r  = requests.post(url,data= none,json=rule_ids, headers=headers, verify=False)

	print ("Machine ID "+line +" "+ r.text)

