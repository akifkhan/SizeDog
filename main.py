#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
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
 

import os
import sys
import argparse
import resize

#volume = "/dev/test/testlv2"

def main():
   	


   	parser = argparse.ArgumentParser()
	#Parsing the command line arguments
	# The options are specified here

	resize_group = parser.add_argument_group('resize_group','Resizing Fuctions')

	resize_group.add_argument('-r','--resize', action="store_true", default=False, help="Input the volume and size by which you want to increase the volume")

	resize_group.add_argument('volume',action ="store" ,help= " Name of the volume along with its path to be increased")

	resize_group.add_argument('size',action ="store",type=int ,help= "Size by which a volume is to be incresed only in Mega Byte [M], Giga Byte [G], Tera Byte[T] ")		
	
	resize_group.add_argument('unit', action ="store" ,help ='Units of size use as main.py -r /dev/testlv/lv1 1G' ,choices=('M','G','T','m','g','t'))

	args = parser.parse_args()

	print args.volume
	print args.size
	print args.unit
	#resize.increase(volume,size,'G')

	return 0
    

if __name__ == '__main__':
	main()

