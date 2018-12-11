### About this repository

This repository is about Junos monitoring with healthbot.  
It has healthbot automation examples and healthbot configuration examples.  
It describes some of the heathbot components.    

### About healthbot

You can use Healthbot to:
 - collect data from the network
 - store the data collected
 - process the data collected

Here's the Healthbot documentation https://techlibrary.juniper.net/documentation/product/en_US/contrail-healthbot  

This repository has been tested with healthbot version 1.0  
```
$ healthbot version
Healthbot vhealthbot-1.0.0
```

### Instructions to use this repository 

- Install Docker (Docker is required before to install Healthbot)
- Download Healthbot from https://support.juniper.net/support/downloads/  
- Install Healthbot 
  - example with ```healthbot-1.0.0.tar.gz``` file
   ```
   $ tar xvf healthbot-1.0.0.tar.gz
   $ cd healthbot-1.0.0
   $ sudo ./install
   ```

- Start Healthbot
  - ```$ healthbot start```  
- clone this repository
   ```
   $ cd 
   $ git clone https://github.com/ksator/junos_monitoring_with_healthbot.git
   $ cd junos_monitoring_with_healthbot
   ```
- Visit the repository wiki to get the instructions https://github.com/ksator/junos_monitoring_with_healthbot/wiki
