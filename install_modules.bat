
REM install_modules.bat
REM A simple batch command file to autoamte the install process for library dependencies (in the Example programs) - or which are frequently/commonly/often used...

REM comtypes
REM a lightweight Python COM package, based on the ctypes FFI library, in less than 10000 lines of code (not counting the tests).
REM allows to a Python program define, call, and implement custom and dispatch-based COM interfaces in pure Python. It works on Windows, 64-bit Windows, and Windows CE.
pip install comtypes
REM - comtypes is a dependency for pyttsx3



REM for Text-to-Speech demos
pip install pyttsx3


REM numpy 
pip install numpy



REM TensorFlow 2.0 Alpha
pip install tensorflow==2.0.0-alpha0


REM https://pypi.org/project/jsonschema/
pip install jsonschema

