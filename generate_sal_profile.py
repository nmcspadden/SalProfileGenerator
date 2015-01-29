#!/usr/bin/python

import argparse
import os
from mcxToProfile import *

parser = argparse.ArgumentParser()
parser.add_argument("key", help="Machine Group key")
parser.add_argument("-u", "--url", help="Server URL to Sal. Defaults to http://sal.")
parser.add_argument("-o", "--output", help="Path to output .mobileconfig. Defaults to 'com.salsoftware.sal.mobileconfig' in current working directory.")
args = parser.parse_args()

plistDict = dict()

if args.url:
	plistDict['ServerURL'] = args.url
else:
	plistDict['ServerURL'] = "http://sal"

plistDict['key'] = args.key

newPayload = PayloadDict("com.salsoftware.sal", makeNewUUID(), False, "Sal", "Sal")

newPayload.addPayloadFromPlistContents(plistDict, 'com.salsoftware.sal', 'Always')

filename = "com.salsoftware.sal"

filename+="." + plistDict['key'][0:5]

if args.output:
	if os.path.isdir(args.output):
		output_path = os.path.join(args.output, filename + '.mobileconfig')
	elif os.path.isfile(args.output):
		output_path = args.output
	else:
		print "Invalid path. Must be a valid directory or an output file."
else:
	output_path = os.path.join(os.getcwd(), filename + '.mobileconfig')

newPayload.finalizeAndSave(output_path)