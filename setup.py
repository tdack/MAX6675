from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages

setup(name              = 'MAX6675',
      version           = '1.0.0',
      author            = 'Troy Dack',
      author_email      = 'troy@dack.com.au',
      description       = 'Library for accessing the MAX6675 thermocouple temperature sensor on a Raspberry Pi or Beaglebone Black.',
      license           = 'MIT',
      url               = 'https://github.com/tdack/MAX6675/',
      dependency_links  = ['https://github.com/adafruit/Adafruit_Python_GPIO/tarball/master#egg=Adafruit-GPIO-0.6.5'],
      install_requires  = ['Adafruit-GPIO>=0.6.5'],
      packages          = find_packages())
