

import time
import pandas as pd

def read_data(licor):
    pass


def getMillis():
    output = time.monotonic_ns()/(1000_000)
    return output

def cycleThrough(n_chan,stab_time_ms,cycle_time_ms,multiplexer,licor):
    
    licor.reset_input_buffer()
    
    time.sleep(0.2)
    temp = licor.readline()
    #while temp.decode()[0:7]!=""
    #print(temp)
    data = pd.read_xml(temp)
    data["chamber_open"] = "na"
    data["time_in_millis"] = getMillis()
    
    timer1 = getMillis()
    timer2 = getMillis()
    
    
    
    while timer2-timer1<stab_time_ms:  
        for i in range(0,n_chan,2): 
            chamber = int(i/2+1)
            print("chamber "+str(chamber))
            multiplexer.chanOn(i)
            multiplexer.chanOn(i+1)
            licor.reset_input_buffer()
            time.sleep(0.1)
            timer4 = getMillis()
            timer3 = getMillis()
            while timer3-timer4 < float(cycle_time_ms):
                temp = licor.readline()
                
                #print(temp)
                timer3 = getMillis()
                print(timer3-timer4)
                temp = pd.read_xml(temp)
                temp["chamber_open"] = chamber
                temp["time_in_millis"] = timer3
                data = pd.concat([data,temp])
                
            
            timer4=getMillis()
            
            multiplexer.chanOff(i)
            multiplexer.chanOff(i+1)
            
        timer2 = getMillis()
        
    
    return data



