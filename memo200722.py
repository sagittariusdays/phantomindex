# PINGTEST
# This program is aimed to monitoring the KANKYO_Visualizer, to check whether it is working.
# MODULE 1

# ping IPs
import os
# import subprocess as sp

hostname = 'www.google.com' # Testsite Google.com

# response_os = os.system("ping -c 1 " + hostname) #ping -c needs Administration
response_os = os.system("ping " + hostname)
# response_sp = sp.getstatusoutput("ping " + hostname) #same function

# print (response_os)
# print (response_sp)
if response_os == 0:
    print(hostname + " is available!")
else:
    print(hostname + " is unavailable!")
