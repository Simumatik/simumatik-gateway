# Contributing

Welcome to the Simumatik Gateway repository! Our goal making this project open-source is to allow everyone playing around with the platform. Feel free to take a look to the different drivers implementation and the whole architecture. Keep in mind that we have a code of conduct mandatory to follow.

## Issues / Features

If you have an issue or feature request, don't hesiate to open an issue for us. Prior to that, check to see if there's an existing related issue/pull request opened. In order to ease the communication, the following data must be supplied:

- Issue/Feature description
- Expected behavior
- How to reproduce it
- Gateway, Server and App versions
- Python version if running the Gateway from source.

## Pull requests

Before contributing code that changes the current files, please open an issue first so we can discuss the changes you wish to make. Please note that this is not neccessary if you want to contribute new drivers to improve the 3rd party integration support. 

The PR must fulfill some requirements:
-  Works across all supported versions of Python3.
-  The code is properly formatted.
-  Has comments included as needed.
-  A test case is provided
-  Must be appropriately licensed (GNU).

## New drivers

Simumatik components are modelled following the Simumatik Datamodel. Therefore, the drivers found in the communication_driver item must be specified in the datamodel beforehand. 

In order to allow everyone trying their creations, a new driver option was added to the datamodel: *development*. When creating your own driver, please use the development class found in `src/drivers/development/development.py` as a base. The corresponding test can be found in `src/tests/test_development.py`.

Once the PR is reviewed and approved, a specific name must be decided for the driver and it will be added to the datamodel as well, making it available for all the users in the platform. 
