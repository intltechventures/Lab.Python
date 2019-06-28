@ECHO OFF
cls
REM Prepared by:
REM   Kelvin D. Meeks
REM   kmeeks@intltechventures.com
REM   International Technology Ventures, Inc.
REM   https://www.intltechventures.com
REM
REM References:
REM   https://packaging.python.org/tutorials/installing-packages/#upgrading-packages
REM     General sytax for installing/Upgrading a library
REM      ```pip install --upgrade SomeProject```
REM
REM
REM This file:
REM   https://github.com/intltechventures/Lab.Python/blob/master/install_modules.bat
REM
REM 
REM Description: 
REM   A simple batch command file to autoamte the install process for library dependencies (in the Example programs) - or which are frequently/commonly/often used...



REM ************************************************************************************************************
REM Update pip
REM
ECHO Checking pip for updates
python -m pip install --upgrade pip



REM ************************************************************************************************************
REM Here's what's installed curently...
REM
pip list

REM Verify installed packages have compatible dependencies...
REM
pip check

ECHO Pausing to review current installed package versions & pip check results
pause



REM ************************************************************************************************************
REM Instal/Upgrade Package: comtypes
REM
REM NOTE:
REM   A dependency for pyttsx3
REM
REM Usage:
REM   A lightweight Python COM package, based on the ctypes FFI library, in less than 10000 lines of code (not counting the tests).
REM   allows to a Python program define, call, and implement custom and dispatch-based COM interfaces in pure Python. 
REM   Works on Windows, 64-bit Windows, and Windows CE.

cls
ECHO Install/Upgrade comtypes
pip install --upgrade comtypes
pause



REM ************************************************************************************************************
REM Install/Updgrade Package: pyttsx3
REM
REM Usage:  
REM   Text-to-Speech demos

cls
ECHO Install/Upgrade pyttsx3
pip install --upgrade pyttsx3
pause



REM ************************************************************************************************************
REM Install/Upgrade Package:  numpy 
REM

cls
ECHO Install/Upgrade numpy
pip install --upgrade numpy
pause



REM ************************************************************************************************************
REM Install/Upgrade Package: TensorFlow 2.0 Alpha
REM

cls
ECHO Install/Upgrade tensorflow 2.0.0-alpha0
pip install --upgrade tensorflow==2.0.0-alpha0
pause


REM ************************************************************************************************************
REM Install/Upgrade Package: jsonschema
REM
REM Referneces:
REM   https://pypi.org/project/jsonschema/

cls
ECHO Install/Upgrade jsonschema
pip install --upgrade jsonschema
pause



REM ************************************************************************************************************
REM Verify installed packages have compatible dependencies...

cls
pip check

ECHO Pausing to review ```pip check``` results
pause 



REM ************************************************************************************************************
REM Review package update results

cls
ECHO Review Package Update Results
pip list


