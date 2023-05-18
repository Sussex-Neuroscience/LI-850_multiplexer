

import time
import pandas as pd
import licor as li

def getMillis():
    output = time.monotonic_ns()/(1000_000)
    return output

def cycleThrough(n_chan,total_time_ms,cycle_time_ms,multiplexer,licor):
    

    temp = licor.read_data()
    temp = temp[0:temp.decode().find("</data>")+7].decode()+"</li850>"
    data = pd.read_xml(temp)
    data["chamber_open"] = "na"
    data["time_in_millis"] = getMillis()
    
    timer1 = getMillis()
    timer2 = getMillis()
    
    
    
    while timer2-timer1<total_time_ms:  
        for i in range(0,n_chan,2): 
            chamber = int(i/2+1)
            
            print("chamber "+str(chamber))
            
            
            multiplexer.chanOn(i)
            multiplexer.chanOn(i+1)
            #time.sleep(0.1)
            timer4 = getMillis()
            multiplexer.ledOn(1)
            time.sleep(0.15)
            multiplexer.ledOff(1)
            timer3 = getMillis()
            while timer3-timer4 < int(cycle_time_ms):
                temp = licor.read_data()
                temp = temp[0:temp.decode().find("</data>")+7].decode()+"</li850>"
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



