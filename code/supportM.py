import time
import pandas as pd
import licor as li
from datetime import datetime as dt

def getMillis() -> float:
    """
    Returns the current time in milliseconds
    """
    current_time_ms = time.monotonic_ns() / (1000_000)
    return current_time_ms


def cycleThrough(multiplexer, licor,
                 chambers=[1,2,3,4,5,6],
                 total_time_ms=500,
                 cycle_time_ms=10,             ):
    """Cycles through the different chambers

    Returns:
        Pandas data frame with all the data
    """
    chamberMap = {"1":[0,1],"2":[2,3],"3":[4,5],
               "4":[6,7],"5":[8,9],"6":[10,11]}
    # Set timers
    timer1 = getMillis()
    timer2 = getMillis()

    # Initialize data object (writes the first line)
    temp = licor.read_data()  # temp is short for temporary (not temperature)
    temp = temp[0 : temp.decode().find("</data>") + 7].decode() + "</li850>"
    data = pd.read_xml(temp)
    data["chamber_open"] = "na"
    data["time_ms"] = timer2 - timer1
    data["absolute_time"] = dt.now()
    # Stopping after the total duration
    while (timer2 - timer1) < total_time_ms:
        # Loop through the number of chambers
           # Loop through the number of chambers
        for item in chambers:
            valve1 = chamberMap[str(item)][0]
            valve2 = chamberMap[str(item)][1]
            
            print("Chamber: "+str(item))

            # Open the two valves for the chamber
            multiplexer.chanOn(valve1)
            multiplexer.chanOn(valve2)

            # Turn LED ON and OFF
            timer4 = getMillis()
            timer3 = getMillis()
            multiplexer.ledOn(1)
            
            # Record data for the duration of the cycle
            while (timer3 - timer4) < cycle_time_ms:
                timerLed = getMillis()
                if (timerLed-timer4) >= 0.15:
                    multiplexer.ledOff(1)
                    
                
                temp = licor.read_data()
                temp = temp[0 : temp.decode().find("</data>") + 7].decode() + "</li850>"
                temp = pd.read_xml(temp)
                temp["chamber_open"] = item
                temp["time_ms"] = timer3 - timer1
                temp["absolute_time"] = dt.now()
                data = pd.concat([data, temp])
                timer3 = getMillis()
            # Close the two valves for the chamber
            multiplexer.chanOff(valve1)
            multiplexer.chanOff(valve2)

        timer2 = getMillis()

    return data
