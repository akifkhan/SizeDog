import subprocess

volume = "/dev/test/testlv2"


def increase(volume,size,unit):
	
	# Fetching the Filesystem of Volume
	
	p = subprocess.Popen(['blkid','-s','TYPE',volume],stdout=subprocess.PIPE)						
						
	# SHELL command to get filesystem of a disk is " blkid -s TYPE /dev/test/testlv 
	
	FILESYSTEM, err = p.communicate()
	
	
	if 'ext2' in FILESYSTEM:
		
		p1 = subprocess.Popen(['lvextend','-L+1G',volume],stdout=subprocess.PIPE)
		
		output, error = p1.communicate()
	
		if output:
			print output
			
		if error:
			print error	
			
	# Resizing Filesystem
	
	p1=subprocess.Popen(['umount',volume],stdout=subprocess.PIPE)
	
	output, error = p1.communicate()
	
			
	p1=subprocess.Popen(['resize2fs',volume],stdout=subprocess.PIPE)
	
	output, error = p1.communicate()
	
	
	p1=subprocess.Popen(['mount',volume,'/mnt'],stdout=subprocess.PIPE)
	
	output, error = p1.communicate()
	
	if output:
		print output
			
	if error:
		print error
	
	
increase(volume,1,'G')
#fsadm to grow the file system online.  ext4
