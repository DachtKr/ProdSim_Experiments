from prodsim import Environment

# This code is used to plot the data
# To run this code matplotlib and pandas must be installed

import matplotlib.pyplot as plt
import pandas as pd

#######################################################
# define folder name                                  #
#######################################################
output_path = 'output3'


def plot_surface():

     surface_data = pd.read_csv('./' + output_path + '/shaft.csv')

     labels = ['drill', 'lathe', 'polisher']

     plt.figure(figsize=(25,7))
     for index, label in enumerate(labels):
         plt.plot(surface_data[surface_data['station_id'] == index]['time'],
                  surface_data[surface_data['station_id'] == index]['surface'], label=label)

     plt.xlabel('Sim. time')
     plt.ylabel('Surface roughness')
     plt.title('Surface over simulated time')
     plt.legend(loc='upper right')

     plt.savefig('./' + output_path + '/shaft_surface.png')


if __name__ == '__main__':

    # Create simulation environment
    env = Environment()

    # Start application to define a process
    env.define_process()

    # Read in the process files
    env.read_files('./data/process.json', './data/function.py')

    # Inspect and visualize (optional)
    env.inspect()
    env.visualize()

    # Start the simulation (start sim_time = 4320)
    env.simulate(sim_time=5760, track_components=['shaft'], progress_bar=True)

    # Export the simulation data
    env.data_to_csv(path_to_wd='./' + output_path + '/', keep_original=False)

    surface_data = pd.read_csv('./' + output_path + '/shaft.csv')

    # surface_data.pivot_table(index="time", columns="station_id", values="surface", aggfunc="np.mean")
    # print(surface_data)

    # create file with table for analyzation in excel
    surface_data.to_csv('./' + output_path + '/shaft_test.csv', sep=';')

    # Plot 'surface' over simulation time (optional)
    plot_surface()