import os
import numpy as np
import pandas as pd
from pathlib import Path
from datetime import datetime
from pyteomics import mgf

def params_pars(mgf_filename, filepath=rootpath):
  # get pepmass and mz array for the following data pipeline
  pepmass = []
  mz_array = []
  mgf_file = mgf.read(str(filepath/mgf_filename))
  for spectrum in mgf_file:
    pepmass.append(spectrum.get('params').get('pepmass')[0])
    mz_array.append(spectrum.get('m/z array'))
  mgf_file.close()
  return mgf_file
