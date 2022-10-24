#!/usr/bin/env python

import os
import sys
from netCDF4 import Dataset
import numpy as np
import glob
import multiprocessing
import time

from intpy.intpy import deterministic, initialize_intpy

@deterministic
def get_data_from_file(file_name):
    v_name = 'aoa'
    reference_latitude = -86.0

    coefficient = 365.5

    opened_file = Dataset(file_name, mode='r')

    latitudes = opened_file.variables['lat'][:]

    latitude_index = (np.abs(latitudes - reference_latitude)).argmin()

    # Read the daily average age of air
    age_air = opened_file.variables[v_name][0, ::-1, latitude_index, :] / coefficient

    # Determine the zonal mean to be returned
    data_value = np.mean(age_air, axis=1)

    # Close file
    opened_file.close()

    return data_value

def parallel_time_series_processing(num_threads):
    beginning_year = 1990
    end_year = 2009
    num_days = 0
    my_list = []

    reference_directory = './Data/'

    # Loop over the years
    for year in range(beginning_year, end_year+1):
        directory_name = 'Y'+str(year)
        directory_Y = os.path.join(reference_directory, directory_name)

        list_files = glob.glob(directory_Y + "/runAOA.TR." + str(year) + "*_1200z.nc4")

        num_days += len(list_files)

        my_pool = multiprocessing.Pool(num_threads)
        my_array = my_pool.map(get_data_from_file, list_files)

        my_pool.close()
        my_pool.terminate()

        my_list.extend(my_array)

@initialize_intpy(__file__)
def main():
    num_threads = int(sys.argv[1])
    t0 = time.perf_counter()
    parallel_time_series_processing(num_threads)
    print(time.perf_counter() - t0)

if __name__ == "__main__":
    main()