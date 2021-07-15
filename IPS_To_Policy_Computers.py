import requests

#Authentication Header
headers = {
	'api-secret-key': 'YOUR API KEY GOES HERE',
	'api-version': 'v1', 'Content-Type': 'application/json', 'charset':'UTF-8'
	}

#DSM IPS Rule IDs
rule_ids = {"ruleIDs": [3,12,25,45,......................,LIST OF RULE IDs]}
#payload = open("rules_id.json")

#Looping List of Computer IDs to which above Rule IDs will get applied
f = open('computer_id.txt', 'r')
for line in f.readlines():
	id = line.strip('\n')
	# TM DSM API URL {computer_id}
	url = "https://10.255.252.67:4119/api/computers/{0}/intrusionprevention/assignments".format(id)

	r  = requests.post(url,data= none,json=rule_ids, headers=headers, verify=False)

	print ("Machine ID "+line +" "+ r.text)

