#script to create loop device and activate LVM Volumes for debugging purpose only.




# Commands
losetup -f /home/akif/test/image.img
losetup -f /home/akif/test/image2.img
echo " loop created "s

# Activating the VG
vgchange -a y test
#activated VG

#mount /dev/test/testlv /mnt
#echo " Mounted and Finished succesfully "
