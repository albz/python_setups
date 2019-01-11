# HOW TO SET IT UP!
# ln -s ~/scripts/pythonstartup.py ~/.pythonstartup
#
# Also in your /home/dynasty/.bash_profile add this..
# PYTHONSTARTUP=$HOME/.pythonstartup
# export PYTHONSTARTUP
#


# --- #
import re
import os
import os.path
import glob
import sys
import shutil
import time
import datetime
import scipy as sci
import numpy as np
import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
import pylab as pyl
import string

import readline
import atexit
import rlcompleter

#import pandas as pd

# --- #

#--- *** Interactive graphs *** ---!
##########pyl.ion()
#--- *** ---#

#--- import: plotting style ---#
home_path = os.path.expanduser('~')
sys.path.append( os.path.join('/mnt','c','Users','a.marocchino','Documents','codes','python_setups','plot')                                   )
plt.style.use(   os.path.join('/mnt','c','Users','a.marocchino','Documents','codes','python_setups','plot','plot_style_reference.mplstyle')   )
# --- #

###---*** import: plasma parameter library ***---#
# home_path = os.path.expanduser('~')
# sys.path.append(os.path.join(home_path,'Codes/Plasma_PyCalculator/formulary'))
# from plasma_basic_parameters import *
# --- #

###---*** import: Plasma Wakefield Utilities ***---###
# sys.path.append(os.path.join(home_path,'Codes/PlasmaWakeField_utilities'))
# from PWFA_calculator import *
# --- #

#---*** import Architect graphical utilitites ***---#
# sys.path.append(os.path.join(os.path.expanduser('~'),'Codes/Code_Architect/Architect/utils/python_utils/architect_graphycal_unit'))
# from read_architect_bin import *


# --- # tab:complete
# readline.parse_and_bind('tab: complete')	#standard command does not work on Mac
############### readline.parse_and_bind ("bind ^I rl_complete")	#Mac command for tab:complete

# --- # save hystory
histpath = os.path.join(os.path.expanduser("~"), ".local", "share","python")
histfile = os.path.join(histpath, "pyhistory")
if not os.path.exists(histpath):
	os.mkdir(histpath)
atexit.register(readline.write_history_file, histfile)
try:
	readline.read_history_file(histfile)
except IOError:
     pass

# --- # History Search
# readline.parse_and_bind("bind ^[[5~ history_search_backwardy")
# readline.parse_and_bind("bind ^[[6~ : history-search-forward")
# --- #

