#!/usr/bin/env 

YES_MATCH_SCORE_THRESHOLD = 2
NO_MATCH_SCORE_THRESHOLD = 1.25

yMatch = {
	'5': 0.25,
	'6': 0.25,
	'7': 0.25,
	't': 0.75,
	'y': 1,
	'u': 0.75,
	'g': 0.25,
	'h': 0.25,
	'k': 0.25,
}

eMatch = {
	'2': 0.25,
	'3': 0.25,
	'4': 0.25,
	'w': 0.75,
	'e': 1,
	'r': 0.75,
	's': 0.25,
	'd': 0.25,
	'f': 0.25,
};

sMatch = {
	'q': 0.25,
	'w': 0.25,
	'e': 0.25,
	'a': 0.75,
	's': 1,
	'd': 0.75,
	'z': 0.25,
	'x': 0.25,
	'c': 0.25,
};

nMatch = {
	'h': 0.25,
	'j': 0.25,
	'k': 0.25,
	'b': 0.75,
	'n': 1,
	'm': 0.75,
};

oMatch = {
	'9': 0.25,
	'0': 0.25,
	'i': 0.75,
	'o': 1,
	'p': 0.75,
	'k': 0.25,
	'l': 0.25,
};

def get_yes_match_score(val):
	score = 0
	y = val[0]
	e = val[1]
	s = val[2]

	if yMatch.has_key(y):
		score += yMatch[y]

	if eMatch.has_key(e):
		score += eMatch[e]

	if sMatch.has_key(s):
		score += sMatch[s]

	return score;

def get_no_match_score(val):
	score = 0
	n = val[0]
	o = val[1]

	if nMatch.has_key(n):
		score += nMatch[n]

	if oMatch.has_key(o):
		score += oMatch[o]

	return score

def get_yn(val):
	if get_yes_match_score >= YES_MATCH_SCORE_THRESHOLD:
		return True

	if get_no_match_score >= NO_MATCH_SCORE_THRESHOLD:
		return False