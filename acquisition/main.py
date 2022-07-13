# Main will be used to collect all indivisual functions to run a simple code that has all the functions in it.

#----------------------------------------------------
# Modelling
# Main.py
# Implement all the components to here.
# Components folder contains all the necessary parts.
# Here are some useful links:
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
# https://datatofish.com/import-csv-file-python-using-pandas/
#----------------------------------------------------

# Package imports.
import sys

# Adding path to the function calls. 1 here lets the python to idetntify the path.
sys.path.insert(1, 'Components/Functions/')
sys.path.insert(1, 'Components/Functions/Chem_Building')
# Native function imports/calls.
# Campus
import EUI as eui


# Weather
import UBC_Weather as UBC_wth
import Van_Weather as Van_wth

# Building
import ChemCentre_UT as cc_ut   
import ChemEast_UT as ce_ut
import ChemNorth_UT as cn_ut    
import ChemPhys_UT as cp_ut     
import ChemSouth_UT as cs_ut
import ChemHebb_UT as hb_ut
import ChemHenn_UT as hn_ut
import WaterVol as w_v         
                             

#------------------------------------------------
# Main function call
def Main():

  cc_ut.centre_hw_energy_day()
 


#------------------------------------------------
# Run Main
Main()
  
