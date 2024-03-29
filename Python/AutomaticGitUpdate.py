# Generate an SSH-Key for the server
# Upload the SSH-Key .Pub file to Github (for the repository that the script should automatically auto commit to)
# Create a script "gitpush.ps1" in the same directory as this file that just contains "git push"

import subprocess
import os
import os.path
import sys
from datetime import datetime

dateformat="%Y-%m-%d"
today=datetime.today().strftime(dateformat)

os.environ["HOME"]=os.path.expanduser('~')
shell=r"powershell.exe"
gitexe=r"C:\Program Files\Git\cmd\git.exe"
gitmsg="automated git updates for " + today
gitadd="add ."
gitcommit="commit -m \""+gitmsg+"\""
gitpush="gitpush.ps1"
cwd=os.path.dirname(os.path.realpath(__file__))

subprocess.call(gitexe+" "+gitadd, cwd=cwd)
subprocess.call(gitexe+" "+gitcommit, cwd=cwd)
process=subprocess.call('powershell.exe -ExecutionPolicy RemoteSigned -file "' + gitpush +'"', cwd=cwd)
