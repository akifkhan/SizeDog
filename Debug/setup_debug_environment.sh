
#For First time run the below command too.

qemu-img create -f raw /home/akif/test/image.img 4G 

losetup -f /home/akif/test/image.img

echo " loop created "

pvcreate /dev/loop0
echo " PV created"
vgcreate test /dev/loop0
echo " VG created"
lvcreate -L1000 -ntestlv test
echo " lv created testlv"
mke2fs /dev/test/testlv
echo " File system created"
lvcreate -L1000 -ntestlv2 test
echo " 2nd lv created testlv2"
mke2fs /dev/test/testlv2
echo " File system created"

