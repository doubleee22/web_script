# Script which allows to search for tenders on:

## Fabrikant.ru, Rostender.info, Rosatom.rts-tender.ru, online.Sbis.ru

It's now only **optimized for mac os** (ARC64 and x64 CPUs).

For running a script on x64 CPUs (M1 Macs 2020 and older) conviniently - via executable file - you will need to install Swift. 

Instructions: 
--

TENDERS TO SEARCH:
To change keywords from default proceed to TO_CHANGE folder, input_list.py
You can freely change values of all the variables, but adding more is not supported yet.

LOGINS AND PASSWORDS:
In order to access online.Sbis.ru you have to create account on the following platform and add your login and password into a passes.py file.




ARC64 CPUs executable file creation:
--
**Run following commands in Terminal:**

pip3 install pyinstaller

pip3 install selenium

cd (path to the WEB_SCRIPT folder)

pyinstaller --onefile main.py

--

After running the commands there will be a folder DIST created right in the script folder. In DIST folder you will find an executable file, which can be moved to any directory on your machine.


x64 (x86_64) CPUs executable file creation:
--
**install Xcode:** https://apps.apple.com/app/xcode/id497799835

--
**Run following commands in Terminal:**

pip3 install selenium

cd (path to the TO_CHANGE folder)

swiftc main.swift -o (name of the exe file - you can choose any)

--

After running the commands there will be an executable file created right in the TO_CHANGE folder. It can be moved to any directory on your machine.
