Python MAX66755
===============

Python library for accessing the MAX6675 thermocouple temperature sensor on a Raspberry Pi or Beaglebone Black.

To install, first make sure some dependencies are available by running the following commands (on a Raspbian
or Beaglebone Black Debian install):

````
sudo apt-get update
sudo apt-get install build-essential python-dev python-smbus
````

Then download the library by clicking the download zip link and unzip the archive somewhere on your Raspberry Pi or Beaglebone Black.  Then execute the following command in the directory of the library:

````
sudo python setup.py install
````

Make sure you have internet access on the device so it can download the required dependencies.

See examples of usage in the examples folder.

Written by Troy Dack.
MIT license, all text above must be included in any redistribution