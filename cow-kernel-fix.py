#!/usr/bin/python env

"""
     ''' Dirty COW (CVE-2016-5195) is a privilege escalation vulnerability in the Linux Kernel.
     ''' This script is trying to schedule errata to patch this bug.
     ''' Referance: https://access.redhat.com/security/cve/cve-2016-5195
     ''' Author: Ugur Engin
"""

import xmlrpclib as connect
import sys

SATELLITE_URL = "<sw-rpc-api-uri>"
SATELLITE_LOGIN = "<user>"
SATELLITE_PASSWORD = "<pass>"

client = connect.Server(SATELLITE_URL, verbose=0)
key = client.auth.login(SATELLITE_LOGIN, SATELLITE_PASSWORD)

def get_sys_id():
    sys_id = client.system.getId(key, "<sys-name>")
    rhn_id = sys_id[0]['id']
    if isinstance(rhn_id, int):
        return rhn_id
    else:
      raise ValueError("failure during to get rhn_id in spacewalk.")
      raise SystemExit, 3

def cow_fix():
  rhn_id = get_sys_id()
  adv_id = "CESA-2016:2098"
  for errata in client.system.getRelevantErrata(key, rhn_id):
         if errata["advisory_type"] == "Security Advisory":
            if adv_id in errata["advisory_name"]:
              errata_id = client.errata.getDetails(key, adv_id)
              client.system.scheduleApplyErrata(key, rhn_id, errata_id.get('id'))
              print "Kernel COW errata" + ' ' +'(' + (adv_id) + ')' + ' ' + "is scheduled to update."
              break
if __name__ == '__main__':
    cow_fix()
