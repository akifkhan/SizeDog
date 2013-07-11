#script to Create Loop devices and create LVM Volumes onto them for debugging purpose only.


#For First time run the below command too.
#qemu-img create -f raw /home/akif/test/image.img 2G 

# Commands
losetup -f /home/akif/test/image.img
echo " loop created "
#pvcreate /dev/loop0
#echo " PV created"
#vgcreate test /dev/loop0
#echo " VG created"
#lvcreate -L1000 -ntestlv test
#echo " lv created testlv"
#lvcreate -L1000 -ntestlv2 test
#echo " 2nd lv created testlv2"
#mke2fs /dev/test/testlv
#echo " File system created"
# Activating the VG
vgchange -a y test
#activated VG

mount /dev/test/testlv /mnt
echo " Mounted and Finished succesfully "