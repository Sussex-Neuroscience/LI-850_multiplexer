import serial
import Belay
import class_li7000



"""Licor serial comm is done with 9600 baud, 8 data bits, no parity, 1 stop bit (9600 N 8 1) configured as a DTE device
- XOFF (0x13) indicates full input buffer
- XON (0x11) when input buffer is free again
commands ARE case sensitive
commands start with "(" and must end with ")"
line feed character (decimal 10 <lf>) must follow commmands send to the analyzer
"""

"""
One experimental pipeline for testing the software:  

Cell A which is sample  
Cell B is control  
  
1- Calibration (so that A is zero) water  
2- Make A and B equal water  
3- Calibration (so that A is zero) co2  
4- Make A and B equal co2  
5- Start recording (two samples per second – give users an option)  
6- Open chamber, put animal in, close chamber  
7- If movement is being tracked, start timer with to synch recording to chamber measurements  
8- Recordings last 30 min  
  
Each sample should contain  
Licor temperature, co2, water for both chambers (check getting the difference from both chambers as well, or calculated via software afterwards)  

"""



li7=class_li7000.li7000(port = "COM1", baudrate=115200,time=1)
print(li7.li7000_header())



### calibration of H2O and CO2

#zero water cell A
li7.li7000_zeroh2o(span_interval=0.1)#span interval in minutes
#match  cell b equal to cell A
li7.li7000_matchH2O()
#get result of calibration
h20Cal=li7.li7000_h20calresult()


#zero c02 water cell A
li7.li7000_zeroco2(span_interval = 0.1)
#match cell B to cell A
li7.li7000_matchCO2()
#get result of calibration
CO2Cal=li7.li7000_co2calresult()

