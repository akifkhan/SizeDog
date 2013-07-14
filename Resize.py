import subprocess

volume = "/dev/test/testlv2"


def increase(volume,size,unit):
	
	p = subprocess.Popen(['blkid','-s','TYPE',volume]
						,stdout=subprocess.PIPE)						
						
	# SHELL command to get filesystem of a disk is " blkid -s TYPE /dev/test/testlv 
	
	FILESYSTEM, err = p.communicate()
	
	print FILESYSTEM
	
	if 'ext2' in FILESYSTEM:
		print "lolo"
		p1 = subprocess.Popen(['lvextend','-L','+',size,unit,volume]
							,stdout=subprocess.PIPE)
					
		output, err = p1.communicate()
	
		print output
		print err
	

increase(volume,10,'M')
