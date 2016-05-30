#!/usr/bin/env 

from util import get_yn

def yn(msg):
	val = raw_input('{msg} [yes/no]'.format(msg=msg))
	val = val.lower().strip()
	return get_yn(val)