import ConfigParser


def config_add():

    config = ConfigParser.RawConfigParser()
    config.add_section('resize_options')
    config.set('resize_options', 'auto_resize', 'False')
    config.set('resize_options', 'volume_resize', 'False')




    # Writing our configuration file to 'sizedog.cfg'

    with open('/etc/sizedog.cfg', 'wb') as configfile:
        config.write(configfile)



def config_edit():


 # Manual Input of values in config file by the user

    config = ConfigParser.RawConfigParser()
    config.add_section('resize_options')


    auto_re = raw_input("Auto Resize Enable (y/n)")
    
    if ['y','Y'] in auto_re:
        config.set('resize_options', 'auto_resize', 'False')

    else:
        print"Wrong Choice Auto Resize Disabled"




auto_vol_re = raw_input("Volume Resize Enable (y/n)")
    
    if ['y','Y'] in auto_vol_re:
       config.set('resize_options', 'volume_resize', 'False') 

    else:
        print"Wrong Choice Volume Resize Disabled"

    
    # Writing our configuration file to 'sizedog.cfg'

    with open('/etc/sizedog.cfg', 'wb') as configfile:
        config.write(configfile)


