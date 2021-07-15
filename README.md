# Trend-Micro-DSM--Automation

<b>Use-case 1:</b> Computer/ Computers Intrusion Prevention Rules Assignment 
<b>Objective:</b> Add Intrusion Prevention Rule IDs to specific computer or computers for virtual patching or applying rules based on applications running on hosts.
1.	Trend Micro API used: 
a.	HTTP Method: Post
b.	URL: https://dsm.example.com:4119/api/computers/{computerID}/intrusionprevention/assignments
2.	HTTP Header Parameter used: computerID, api-version, api-secret-key, content-type.
3.	Request body schema: ruleIDs
4.	Python modules used: requests
<b>Sample output:</b> 
Machine ID 5 {"assignedRuleIDs":[1,2,3,6,8,10,11,12,124,125,6664],"assignedApplicationTypeIDs":[81,84,143,157,212,297],"recommendationScanStatus":"none","recommendedToAssignRuleIDs":[],"recommendedToUnassignRuleIDs":[]}
Machine ID 22 {"assignedRuleIDs":[1,2,3,6,8,12,6664],"assignedApplicationTypeIDs":[81,143,212,297],"recommendationScanStatus":"none","recommendedToAssignRuleIDs":[],"recommendedToUnassignRuleIDs":[]}
<br>
<b>Use-case 2:</b> Policy Intrusion Prevention Rules Assignment 
<b>Objective:</b> Assigning Intrusion Prevention Rule IDs to a policy
1.	Trend Micro API used: 
a.	HTTP Method: Post
b.	URL: https://dsm.example.com:4119/api/policies/{policyID}/intrusionprevention/assignments
2.	HTTP Header Parameter used: policyID, api-version, api-secret-key, content-type.
3.	Request body schema: ruleIDs
4.	Python modules used: requests
<b>Sample output: </b>
Machine ID 529 {"assignedRuleIDs":[5,6,8,9,10,11,124,125,4292,6534,7229],"assignedApplicationTypeIDs":[44,86,103,213,290,299,302,337],"recommendationScanStatus":"none","recommendedToAssignRuleIDs":[],"recommendedToUnassignRuleIDs":[]}
