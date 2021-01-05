import pandas as pd 
import os 
import netCDF4 as nc
from datetime import datetime
import shutil

def change_name(root, old, new):
    with os.scandir(root) as entries:
        for f in entries:
            if f.name.endswith('.csv'):
                f_new = f.name.replace(old, new)
                os.rename(os.path.join(root, f.name), os.path.join(root, f_new))

def sort_in_folder(root_orig: str):
    with os.scandir(root_orig) as entries:
        for folder in entries:
            root_yr = os.path.join(root_orig, folder.name)
            with os.scandir(root_yr) as entries2:
                for folder2 in entries2:
                    root_month = os.path.join(root_yr, folder2.name)
                    with os.scandir(root_month) as entries3:
                        for f in entries3:
                            if f.name.endswith('.nc'):
                                root_new = os.path.join(root_orig.replace('archive', 'wind'), f.name)
                                shutil.move(os.path.join(root_month, fn), root_new)





