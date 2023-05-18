from belay import Device
#import serial
from multiplexer import multiplexer
import support
import licor
from datetime import datetime
import serial
from pathlib import Path


directory = Path(".")

now = datetime.now()
date = now.strftime("%d-%m-%Y_%H-%M-%S")

file_loc = "data\\"

file_name = "test_"+date
file_name_stabilization = file_loc+file_name+"_stabilization_phase.csv"
file_name_experiment = file_loc+file_name+"_experiment_phase.csv"

licor = licor.Licor()


multiplexer_port="COM4"
multi = multiplexer(multiplexer_port) #SerialBeeHive is now bh
multi.setup() # call the set up function
print("done setup")

n_chan = 12

if n_chan>12:
    n_chan=12 

if n_chan<1:
    n_chan=1


#parameters for chamber stabilization (when it is first started)
#total time needed for stabilization
stab_time = 1 #in min
#just convert the total stabilization time from minutes to milliseconds
stab_time_ms = int(stab_time*60*1000)
#how much time each chamber should be open
cycle_time_ms = 5000


#parameters for experiments
#total time needed for experiment
exp_time = 1 #in min
#just convert the total experiment time from minutes to milliseconds
exp_time_ms = int(exp_time*60*1000)
#how much time each chamber should be open
cycle_time_ms = 1000

print("stabilizing chamber")
data = support.cycleThrough(n_chan,stab_time_ms,cycle_time_ms,multi,licor)
data.to_csv(file_name_stabilization)
print("stabilization done")




print("start data collection")
data = support.cycleThrough(n_chan,stab_time_ms,cycle_time_ms,multi,licor)
data.to_csv(file_name_experiment)
print("data_collection_ended")




















