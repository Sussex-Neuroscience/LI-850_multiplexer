from belay import Device

# import serial
from multiplexer import multiplexer
import supportM as support
import licor
from datetime import datetime
import serial
from pathlib import Path

# ---------------------------------------
#### PARAMETERS ####
# ---------------------------------------
# This section is the only one that should require changes to tweak stuff.
# Number of chambers (including control)
#n_chambers = 6

# Params for chamber stabilization (when it is first started)
stab_time_min = 1  # Total time (minutes) needed for stabilization
stab_cycle_time_s = 5  # How much time (s) each chamber should be open

# Params for experiments
exp_time_min = 1  # Total time (minutes) needed for experiment
exp_cycle_time_s = 5  # How much time (s) each chamber should be open


# ---------------------------------------
#### SETUP ####
# ---------------------------------------

# Convert times into ms
stab_time_ms = int(
    stab_time_min * 60 * 1000
)  # Convert the total stabilization time from minutes to milliseconds
exp_time_ms = int(
    exp_time_min * 60 * 1000
)  # Convert the total experiment time from minutes to milliseconds
stab_cycle_time_ms = int(stab_cycle_time_s * 1000)  # Convert to ms
exp_cycle_time_ms = int(exp_cycle_time_s * 1000)  # Convert to ms

# File naming
directory = Path(".")
now = datetime.now()
date = now.strftime("%d-%m-%Y_%H-%M-%S")
file_loc = "C:\\Users\\labadmin\\OneDrive - University of Sussex\\Desktop\\"
file_name = "BIGtest_" + date
file_name_stabilization = file_loc + file_name + "_stabilization.csv"
file_name_experiment = file_loc + file_name + "_experiment.csv"

# Initialize Licor
licor = licor.Licor()

# Setup multiplexer
multiplexer_port = "COM4"
multi = multiplexer(multiplexer_port)  # SerialBeeHive is now bh
multi.setup()  # call the set up function
print("done setup")

# Set which chambers are going to be used
#chambers = [1,2,3,4,5,6]
chambers = [3,4,5]

    
# n_chan = int(n_chambers * 2)
# if n_chan > 12:
#     n_chan = 12
# elif n_chan < 1:
#     n_chan = 1

# ---------------------------------------
#### Stabilisation ####
# ---------------------------------------
print("Stabilizing chamber...")
stab_data = support.cycleThrough(chambers=chambers,
                                 total_time_ms=stab_time_ms,
                                 cycle_time_ms=stab_cycle_time_ms,
                                 multiplexer=multi, licor=licor)
stab_data.to_csv(file_name_stabilization)
print("Stabilization done!")

# ---------------------------------------
#### Experiment ####
# ---------------------------------------
print("Starting data collection...")
exp_data = support.cycleThrough(chambers=chambers,
                                total_time_ms=exp_time_ms,
                                cycle_time_ms=exp_cycle_time_ms,
                                multiplexer=multi, licor=licor)
exp_data.to_csv(file_name_experiment)
print("Data collection done!")
licor.close()
