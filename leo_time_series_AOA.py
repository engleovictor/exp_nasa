#!/usr/bin/env python

import os
from netCDF4 import Dataset
import numpy as np
import glob
import sys
import time

def serial_time_series_processing():
    variable_name = 'aoa'
    beginning_year = 1990
    #end_year = 2009
    end_year = 1991

    first_file = 0
    reference_latitude = -86.0

    num_days = 0

    coefficient = 365.5

    reference_directory = './Data/'

    # Loop over the years
    for year in range(beginning_year, end_year+1):
        #print('Processing year: %d' % (year))
        directory_name = 'Y'+str(year)
        directory_Y = os.path.join(reference_directory, directory_name)

        list_files = glob.glob(directory_Y+"/runAOA.TR."+str(year)+"*_1200z.nc4")

        num_days += len(list_files)

        # Loop over the daily files
        for file in list_files:
            # Open file
            opened_file = Dataset(file, mode='r')

            # Extract information if it is the first file
            if first_file == 0:
                longitudes = opened_file.variables['lon'][:]
                latitudes = opened_file.variables['lat'][:]
                #levels = opened_file.variables['lev'][::-1]
                num_longitudes = np.size(longitudes)
                num_latitudes = np.size(latitudes)
                #num_levels = np.size(levels)

                #levels = pressLevels.calcPressureLevels(num_levels)
                latitude_index = (np.abs(latitudes - reference_latitude)).argmin()
                #print("Latitude index: ", latitude_index)

            # Read the daily average age of air
            age_air = opened_file.variables[variable_name][0, ::-1, latitude_index, :] / coefficient

            # Determine the zonal mean
            zonal_mean = np.mean(age_air, axis=1)

            # Stack the daily values into an existing array
            if first_file == 0:
                first_file = 1
                data_value = zonal_mean
            else:
                data_value = np.column_stack((data_value, zonal_mean))

            # Close file
            opened_file.close()


def main():
    t0 = time.perf_counter()
    serial_time_series_processing()
    print(time.perf_counter()-t0)

if __name__ == "__main__":
    main()
