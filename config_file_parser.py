import ConfigParser


    
if ConfigParser:
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
        
        if auto_re in ['y','Y']:
            config.set('resize_options', 'auto_resize', 'True')

        else:
            print" Auto Resize Disabled"
            config_add()



        auto_vol_re = raw_input("Volume Resize Enable (y/n)")
        
        if auto_vol_re in ['y','Y']:
           config.set('resize_options', 'volume_resize', 'True')

        else:
            print" Volume Resize Disabled"
            config_add()
            
        
        # Writing our configuration file to 'sizedog.cfg'

        with open('/etc/sizedog.cfg', 'wb') as configfile:
            config.write(configfile)


    def add_volume(volume,free_size):

        config = ConfigParser.RawConfigParser()
        
        config.add_section('auto_resize_options')


        config.set('auto_resize_options',volume,free_size)

        

        with open('/etc/sizedog.cfg', 'wb') as configfile:
            config.write(configfile)



