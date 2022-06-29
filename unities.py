import os
import numpy as np
import pandas as pd
from pathlib import Path
from datetime import datetime
from pyteomics import mgf

def params_pars(fname, fpath):
  # get pepmass and mz array for the following data pipeline
  mgf_file = mgf.read(str(fpath/fname))
  pepmass = []
  mz_array = []
  for spectrum in mgf_file:
    rtime = float(spectrum.get('params').get('title').split(' ')[3])
    # keep data between 6 to 110 mins
    if (rtime > 6) and (rtime < 110):
      pepmass.append(spectrum.get('params').get('pepmass')[0])
      mz_array.append(spectrum.get('m/z array'))
  mgf_file.close()
  
  return pepmass, mz_array
