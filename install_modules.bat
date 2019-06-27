@ECHO OFF
REM Prepared by:
REM   Kelvin D. Meeks
REM   kmeeks@intltechventures.com
REM   International Technology Ventures, Inc.
REM   https://www.intltechventures.com
REM
REM References:
REM   https://packaging.python.org/tutorials/installing-packages/#upgrading-packages
REM
REM   https://github.com/intltechventures/Lab.Python
REM
REM This file:
REM   https://github.com/intltechventures/Lab.Python/blob/master/install_modules.bat


REM 
REM install_modules.bat
REM A simple batch command file to autoamte the install process for library dependencies (in the Example programs) - or which are frequently/commonly/often used...
REM


REM
REM Update pip
REM
ECHO About to check pip for updates
pause 
python -m pip install --upgrade pip


REM
REM Here's what's installed curently
REM
pip list
REM
REM Review current package versions
REM
ECHO Pausing to review current installed package versions
ECHO
pause
cls

REM
REM General sytax for installing/Upgrading a library
REM
REM pip install --upgrade SomeProject


REM
REM comtypes
REM
REM NOTE:
REM   A dependency for pyttsx3
REM
REM a lightweight Python COM package, based on the ctypes FFI library, in less than 10000 lines of code (not counting the tests).
REM allows to a Python program define, call, and implement custom and dispatch-based COM interfaces in pure Python. It works on Windows, 64-bit Windows, and Windows CE.
REM
ECHO Install/Upgrade comtypes
pause
cls
pip install --upgrade comtypes


REM 
REM for Text-to-Speech demos
REM
ECHO Install/Upgrade pyttsx3
pause
cls
pip install --upgrade pyttsx3


REM 
REM numpy 
REM
ECHO Install/Upgrade numpy
pause
cls
pip install --upgrade numpy



REM 
REM TensorFlow 2.0 Alpha
REM
ECHO Install/Upgrade tensorflow 2.0.0-alpha0
pause
cls
pip install --upgrade tensorflow==2.0.0-alpha0


REM 
REM jsonschema
REM
REM https://pypi.org/project/jsonschema/
REM
ECHO Install/Upgrade jsonschema
ECHO
pause
cls
pip install --upgrade jsonschema


REM
REM Review package update results
REM
cls
ECHO Review Package Update Results
ECHO
python -m pip install --upgrade pip


