import serial
import Belay
import class_li7000



"""Licor serial comm is done with 9600 baud, 8 data bits, no parity, 1 stop bit (9600 N 8 1) configured as a DTE device

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

class li850:
    pass