#!/usr/bin/python
def formatdef(definition, idx = 1):

	stillFound = True
	newDef = definition
	pos = definition.find(str(idx))

	if pos != -1 and definition[pos + 1] == ".":
		newDef = definition[:pos] + "\n" + definition[pos:]
		idx += 1
		return formatdef(newDef, idx)

	return newDef