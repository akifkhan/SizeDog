import subprocess
import shlex




comm= "df '/dev/sda5' | awk 'NR ==1 {next} {print $6; exit}'"
com= shlex.split(comm)

p1=subprocess.Popen(com,stdout=subprocess.PIPE)
output, error = p1.communicate()
if output:
	print output
if error:
	print error