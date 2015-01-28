#!/usr/bin/python

import argparse
import os
from mcxToProfile import *

parser = argparse.ArgumentParser()
parser.add_argument("key", help="Machine Group key")
parser.add_argument("-u", "--url", help="Server URL to Sal", default="http://sal")
args = parser.parse_args()

plistDict = dict()

plistDict['ServerURL'] = args.url
plistDict['key'] = args.key

newPayload = PayloadDict("com.salsoftware.sal", makeNewUUID(), False, "Sal", "Sal")

newPayload.addPayloadFromPlistContents(plistDict, 'com.salsoftware.sal', 'Always')

newPayload.finalizeAndSave(os.path.join(os.getcwd(), 'com.salsoftware.sal.mobileconfig'))