import subprocess
import re

#capture the output obtain from the command line input 
command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode()

#List all the wifi user profiles that is saved in the local machine 
profile_names = (re.findall("All User Profile     : (.*)\r", command_output))

wifi_list = []

if len(profile_names) != 0:
    for name in profile_names:
      if re.search("Security key           : Absent", profile_info):
            continue
        else:
           wifi_profile["ssid"] = name
            #    "key=clear" is a linux comment to obtain the password.
            profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output = True).stdout.decode()
            password = re.search("Key Content            : (.*)\r", profile_info_pass)
            if password == None:
                wifi_profile["password"] = None
            else:
                wifi_profile["password"] = password[1]
            #    The information is stored in wifi_list
            wifi_list.append(wifi_profile)

#Display all the wifi name and passwords
for x in range(len(wifi_list)):
    print(wifi_list[x])
