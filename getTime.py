'''
	Author: Robin Gautam
	Email: RGautam@cvent.com

'''
import re

reportFile = open("Test_Results.txt", "a")

try:
	file = open("sub.log", "r")
except Exception as e:
	print("Rename the Log file to be processed as: 'sub.log'")
	exit()


writer = open("Diagnosis.log", "w")
lines = file.readlines()

totalSET = 0
totalGET = 0

totalSETTime = 0.0
totalGETTime = 0.0

isSET = False
isGET = False

for line in lines:
	match = re.search("\"Time\": (.*)", line)
	if match:
		writer.writelines(match.group(1) + "\n")
		if isSET:
			totalSETTime = totalSETTime + float(match.group(1))
			totalSET = totalSET + 1
			isSET = False
		elif isGET:
			totalGETTime = totalGETTime + float(match.group(1))
			totalGET = totalGET + 1
			isGET = False
	else:
		successor = re.search("\"Type\": \"(.*)ET (.*)\",", line)
		if successor:
			if(successor.group(1) is 'G'):
				isGET = True
			elif (successor.group(1) is 'S'):
				isSET = True
			writer.writelines(successor.group(1) + "ET:")
		pass

print("\nTotal Time(ms)\nSET: " + str(totalSETTime) + "\nGET: " + str(totalGETTime))
print("\n\nTotal # of Requests\nSET: " + str(totalSET) + "\nGET: " + str(totalGET))
print("\nReport: Test_Results.txt\nDetailed log: Diagnosis.log")

writer.writelines("\nTotal Time(ms)\nSET: " + str(totalSETTime) + "\nGET: " + str(totalGETTime))
writer.writelines("\n\nTotal # of Requests\nSET: " + str(totalSET) + "\nGET: " + str(totalGET))

reportFile.writelines("\n\n--------LOG------------")
reportFile.writelines("\nTotal Time(ms)\nSET: " + str(totalSETTime) + "\nGET: " + str(totalGETTime))
reportFile.writelines("\n\nTotal # of Requests\nSET: " + str(totalSET) + "\nGET: " + str(totalGET))
reportFile.writelines("\n-----------------------")