#!/usr/bin/python

import argparse
import os
from mcxToProfile import *

parser = argparse.ArgumentParser()
parser.add_argument("key", help="Machine Group key")
parser.add_argument("-u", "--url", help="Server URL to Sal, defaults to http://sal")
parser.add_argument("-o", "--output", help="Path to output .mobileconfig, defaults to current directory")
args = parser.parse_args()

plistDict = dict()

if args.url:
	plistDict['ServerURL'] = args.url
else:
	plistDict['ServerURL'] = "http://sal"

plistDict['key'] = args.key

output_path = args.output or os.getcwd()

newPayload = PayloadDict("com.salsoftware.sal", makeNewUUID(), False, "Sal", "Sal")

newPayload.addPayloadFromPlistContents(plistDict, 'com.salsoftware.sal', 'Always')

filename = "com.salsoftware.sal"

filename+="." + plistDict['key'][0:5]

newPayload.finalizeAndSave(os.path.join(output_path, filename + '.mobileconfig'))