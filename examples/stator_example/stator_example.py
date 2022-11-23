from prodsim import Environment

# This code is used to plot the data
# To run this code matplotlib and pandas must be installed

import matplotlib.pyplot as plt
import pandas as pd

#######################################################
# define folder name                                  #
#######################################################
output_path = 'output_test_3'

if __name__ == '__main__':

    # Create simulation environment
    env = Environment()

    # Start application to define a process
    # env.define_process()

    # Read in the process files
    env.read_files('./data/stator_example_process.json', './data/stator_example_function.py')

    # Inspect and visualize (optional)
    env.inspect()
    # env.visualize()

    # Start the simulation (start sim_time = 4320)
    env.simulate(sim_time=4320, track_components=['stator', 'welding', 'quality_check'], progress_bar=True)

    # Export the simulation data
    env.data_to_csv(path_to_wd='./' + output_path + '/', keep_original=False)

    stator_data = pd.read_csv('./' + output_path + '/stator.csv')
    welding_data = pd.read_csv('./' + output_path + '/welding.csv')
    quality_data = pd.read_csv('./' + output_path + '/quality_check.csv')

    print(welding_data)
