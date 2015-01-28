#!/usr/bin/python

import argparse
import os
from mcxToProfile import *

if not os.getenv("PROFILE_PATH"):
	profile_path="/home/docker/profiles"

parser = argparse.ArgumentParser()
parser.add_argument("key", help="Machine Group key")
parser.add_argument("-u", "--url", help="Server URL to Sal", default="http://sal")
args = parser.parse_args()

plistDict = dict()

plistDict['ServerURL'] = args.url
plistDict['key'] = args.key

newPayload = PayloadDict("com.salsoftware.sal", makeNewUUID(), False, "Sal", "Sal")

newPayload.addPayloadFromPlistContents(plistDict, 'com.salsoftware.sal', 'Always')

filename = "com.salsoftware.sal"

filename+="." + plistDict['key'][0:5]

newPayload.finalizeAndSave(os.path.join(profile_path, filename + '.mobileconfig'))