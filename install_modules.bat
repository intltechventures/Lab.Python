@ECHO OFF
cls
REM ************************************************************************************************************
REM Prepared by:
REM   Kelvin D. Meeks
REM   kmeeks@intltechventures.com
REM   International Technology Ventures, Inc.
REM   https://www.intltechventures.com
REM
REM References:
REM   https://packaging.python.org/tutorials/installing-packages/#upgrading-packages
REM     General sytax for installing/Upgrading a library
REM     	pip install --upgrade SomeProject
REM
REM
REM This file:
REM   https://github.com/intltechventures/Lab.Python/blob/master/install_modules.bat
REM
REM 
REM Description: 
REM   A simple batch command file to autoamte the install process for library dependencies (in the Example programs) - or which are frequently/commonly/often used...
REM ************************************************************************************************************


REM ************************************************************************************************************
REM Update pip
REM
ECHO Checking pip for updates
python -m pip install --upgrade pip



REM ************************************************************************************************************
REM Here's what's installed currently...
REM
pip3 list

REM Verify installed packages have compatible dependencies...
REM
pip3 check

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
pip3 install --upgrade comtypes
pause



REM ************************************************************************************************************
REM Install/Updgrade Package: pyttsx3
REM
REM Usage:  
REM   Text-to-Speech demos

cls
ECHO Install/Upgrade pyttsx3
pip3 install --upgrade pyttsx3
pause



REM ************************************************************************************************************
REM Install/Upgrade Package:  numpy 
REM
REM References: 
REM		http://www.numpy.org/
REM

cls
ECHO Install/Upgrade numpy
pip3 install --upgrade numpy
pause




REM ************************************************************************************************************
REM Install/Upgrade Package:  SciPy
REM
REM	References:
REM 	https://www.scipy.org/scipylib/
REM

cls
ECHO Install/Upgrade scipy
pip3 install --upgrade scipy
pause



REM ************************************************************************************************************
REM Install/Upgrade Package:  Pandas
REM
REM	References:
REM 	http://pandas.pydata.org/
REM

cls
ECHO Install/Upgrade pandas
pip3 install --upgrade pandas
pause



REM ************************************************************************************************************
REM Install/Upgrade Package: torch
REM
REM
REM References:
REM   https://pytorch.org/
REM   https://pytorch.org/docs/stable/index.html
REM
REM   See this:
REM   	https://pytorch.org/get-started/locally/
REM
cls
ECHO 2019-12-22 - I've run into some issue getting torch to install - will have to come back and research this
pause
REM   pip install --upgrade torch
REM cls
REM ECHO Install/Upgrade torch
REM pip3 install --upgrade torch==1.3.1+cpu torchvision==0.4.2+cpu -f https://download.pytorch.org/whl/torch_stable.html
REM pip install --pre torch torchvision -f https://download.pytorch.org/whl/nightly/cu101/torch_nightly.html
REM pause


cls
ECHO Install/Upgrade torchvision
pip3 install --upgrade pip3 install torchvision
pause

REM ************************************************************************************************************
REM Install/Upgrade Package:  matplotlib
REM
REM	References:
REM 	https://matplotlib.org/
REM

cls
ECHO Install/Upgrade matplotlib
pip3 install --upgrade matplotlib
pause



REM ************************************************************************************************************
REM Install/Upgrade Package:  seaborn
REM
REM	References:
REM 	https://seaborn.pydata.org/
REM

cls
ECHO Install/Upgrade seaborn
pip3 install --upgrade seaborn
pause




REM ************************************************************************************************************
REM Install/Upgrade Package:  SciKitLearn
REM
REM	References:
REM 	https://scikit-learn.org/stable/
REM

cls
ECHO Install/Upgrade scikit-learn
pip3 install --upgrade scikit-learn
pause




REM ************************************************************************************************************
REM Install/Upgrade Package: TensorFlow
REM
REM References:
REM   https://www.tensorflow.org/install/pip
REM
cls
ECHO Install/Upgrade tensorflow
REM pip install --upgrade tensorflow
pip3 install --upgrade tensorflow
pause



REM ************************************************************************************************************
REM
REM References:
REM   https://github.com/google/tf-quant-finance
REM   https://www.openquants.com/
REM

cls
ECHO install/upgrade tf-quant-finance
pip3 install --upgrade tf-quant-finance
pause




REM ************************************************************************************************************
REM Install/Upgrade Package: TensorFlow 
REM
REM	Reference:
REM		https://github.com/microsoft/tensorwatch 
REM 

cls
ECHO Install/Upgrade tensowwatch
pip3 install --upgrade tensorwatch
pause 



REM ************************************************************************************************************
REM Install/Upgrade Package: jsonschema
REM
REM Referneces:
REM   https://pypi.org/project/jsonschema/

cls
ECHO Install/Upgrade jsonschema
pip3 install --upgrade jsonschema
pause



REM ************************************************************************************************************
REM Verify installed packages have compatible dependencies...

cls
pip3 check

ECHO Pausing to review ```pip check``` results
pause 



REM ************************************************************************************************************
REM Review package update results

cls
ECHO Review Package Update Results
pip3 list


