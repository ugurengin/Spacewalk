# Spacewalk scheduled task cleaner

__author__ = 'ugurengin'
 
import xmlrpclib as connect
 
SATELLITE_URL = "https://spacewalk_url/rpc/api"
SATELLITE_LOGIN = "<user>"
SATELLITE_PASSWORD = "<pass>"
 
client = connect.Server(SATELLITE_URL, verbose=0)
key = client.auth.login(SATELLITE_LOGIN, SATELLITE_PASSWORD)
 
 
def total(list):
    print("Total jobs:", len(action_ids))
    return
 
a="Archiving failed actions."
print (a)
failed_list = client.schedule.listFailedActions(key)
action_ids=[]
for action in failed_list:
    action_ids.append(action['id'])
 
total(list)
archive_result=client.schedule.archiveActions(key,action_ids)
 
b="Archiving completed actions."
print (b)
completed_list = client.schedule.listCompletedActions(key)
action_ids=[]
for action in completed_list:
    action_ids.append(action['id'])
 
total(list)
archive_result=client.schedule.archiveActions(key,action_ids)
 
c="Finally deleting archived actions."
print (c)
archived_list = client.schedule.listArchivedActions(key)
action_ids=[]
for action in archived_list:
    action_ids.append(action['id'])
 
total(list)
del_result=client.schedule.deleteActions(key,action_ids)
 
client.auth.logout(key)