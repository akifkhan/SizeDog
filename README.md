SizeDog
=======

Google Summer of Code Project with openSUSE (Still in Development )

To build a standalone Application/tool called Size Dog that can perform Automatic resizing of File system and Logical Volumes. This Application/Tool can be called by the package manager if the size of the package to be installed exceeds the size available on the logical volume and increase the size of the logical volume if there is unallocated space in the logical volume group.

HOW TO USE THE TOOL:

sizedog -h	will give the help options and will have all details regarding using it.

usage: sizedog.py [-h] [-r] [--volume VOLUME] [--size SIZE]
                  [--unit {M,G,T,m,g,t}] [-c] [-v] [-a]

optional arguments:
  -h, --help            show this help message and exit
  
  -r, --resize          Input the volume and size by which you want to
                        increase the volume

  --volume VOLUME       Name of the volume along with its path to be increased

  --size SIZE           Size by which a volume is to be incresed only in Mega
                        Byte [M], Giga Byte [G], Tera Byte[T]

  --unit {M,G,T,m,g,t}  Units of size use as main.py -r /dev/testlv/lv1 1 G

  -c, --config          Build Config File Manually

  -v                    Add volumes to Config File Manually

  -a                    Automatic increase size of volumes
