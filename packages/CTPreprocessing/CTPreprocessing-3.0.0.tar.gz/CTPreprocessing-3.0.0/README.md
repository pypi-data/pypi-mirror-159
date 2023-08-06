**_installation_**
-----------------------------------------------
install the package:
~~~~
pip install CTPreprocessing
~~~~
**_HOW TO_**
----------------------------------------------
After the installation, do the following:
~~~~
from ctbrain_preprocessing import PreProcessor
from pathlib import Path

path = directory/to/ct series
preprocessor = PreProcessor()
preprocessed_series, headers = preprocessor.preprocess(path)
~~~~

**_Description_**
----------------------------------------------
This is the first preprocessing on the input dicoms.
the preprocessing consists of:

~~~~
1- removing artifacts
2- removing the neck slices
3- centering the image