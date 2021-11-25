# fusee-interfacee-cli
Command line python injection tool based on falquinho/fusee-interfacee-tk 

# how to use
## Clone repository
```
https://github.com/estgold/fusee-interfacee-cli.git
```
## Install requared dependencies
```
sudo pip3 install pyusb
```
# Steps
1. Find acceptable payload.bin
2. Connect your switch in RCM mode via usb.
3. Run script 
```sh

sudo python3 ./bashInjector.py --path <your-payload.bin-file>
```
