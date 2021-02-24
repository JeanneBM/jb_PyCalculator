# install the State Tool
# Windows: 
IEX(New-Object Net.WebClient).downloadString('https://platform.activestate.com/dl/cli/install.ps1')
state activate --default ActiveState/ActivePython-3.8

Linux, Mac : 
sh <(curl -q https://platform.activestate.com/dl/cli/install.sh)
state activate --default ActiveState/ActivePython-3.8 

