#!/usr/bin/python

import sys
new_dict={}
for line in sys.stdin:
	line=line.split('\t')
	key=str(line[0])
	new_dict[key]=line[-1]
for i in set(new_dict.keys()):
	print i,new_dict[i]