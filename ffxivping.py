import os
import sys
ffxivserver = "204.2.229.9"
pingresponse = os.system("ping " + ffxivserver)
tracerouteresponse = os.system("tracert " +ffxivserver)
print ("Press 'x' then the enter key to exit the program")
ff_input = input()

if ff_input == "x":
	sys.exit(0)
	