#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Resize.py
#  
#  Copyright 2013 akif khan <akif500@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

import subprocess

def increase(volume,size,unit):

	size_unit = '+' + size + unit

	# Fetching the Filesystem of Volume

	p = subprocess.Popen(['blkid','-s','TYPE',volume],stdout=subprocess.PIPE)

	# SHELL command to get filesystem of a disk is " blkid -s TYPE /dev/test/testlv

	FILESYSTEM, err = p.communicate()

	# Extending Logical volume
	
	p1 = subprocess.Popen(['lvextend','-L',size_unit,volume],stdout=subprocess.PIPE)

	output, error = p1.communicate()

	if output:
		print output

	if error:
		print error

	# Resizing Filesystem ext2 and ext3
	
	
	if ('ext2' or 'ext3' or 'ext4') in FILESYSTEM:
		
		p1=subprocess.Popen(['fsadm','-e','-y','resize',volume,size+unit],stdout=subprocess.PIPE)
		output, error = p1.communicate()

		if output:
			print output
		
		if error:
			print error


	# Resizing File system reiserfs
	
	if 'reiserfs' in FILESYSTEM:
		
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


#increase(volume,'1','G')
