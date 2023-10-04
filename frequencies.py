"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
	frequencies = {}
	tempItems = []
    
	for i in range (0, len(tempItems)):
		tempItems.append(str(items[i]))

	for i in range (0,len(tempItems)):
		if tempItems[i] not in frequencies.keys():
			noOfAppearances = tempItems.count(tempItems[i])
			frequencies[tempItems[i]] = noOfAppearances
	
	return frequencies
