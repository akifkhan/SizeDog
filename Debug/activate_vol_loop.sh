#script to create loop device and activate LVM Volumes for debugging purpose only.




# Commands
losetup -f /home/akif/test/image.img ]

  echo " loop created "


# Activating the VG
vgchange -a y test
#activated VG

#mount /dev/test/testlv /mnt
#echo " Mounted and Finished succesfully "
