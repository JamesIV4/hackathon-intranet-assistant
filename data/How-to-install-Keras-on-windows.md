The purpose of this guide is to provide information on how to install Keras (<https://keras.io/>), a deep learning library in python.

## Step-by-step guide

  1. Make sure you have installed Visual Studio 2010
  2. Install CUDA toolkit <https://developer.nvidia.com/cuda-downloads>
  3. Install Python 2.7. (<https://sourceforge.net/projects/winpython/files/WinPython_2.7/2.7.10.3/>)
  4. Download numpy <http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy> - choose "numpy-1.11.1+mkl-cp27-cp27m-win_amd64.whl"
  5. Download scipy <http://www.lfd.uci.edu/~gohlke/pythonlibs/#scipy> - choose "scipy-0.18.0-cp27-cp27m-win_amd64.whl"
  6. Open the command prompt from python installation (something like: D:\WinPython-64bit-2.7.10.3\WinPython Command Prompt.exe)
  7. Install numpy using: pip install "numpy-1.11.1+mkl-cp27-cp27m-win_amd64.whl"
  8. Install scipy using: pip install "scipy-0.18.0-cp27-cp27m-win_amd64.whl"
  9. Install Keras using: pip install keras  
  




Now you should have Keras installed.

To start using GPU, in your main training/testing script add this to the beginning - before all imports:

py
