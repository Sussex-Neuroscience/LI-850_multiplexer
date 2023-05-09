

import serial
import time
import support
import pandas



def setup(licor_port="COM1"):
    #connect to licor
    licor = serial.Serial(licor_port,9600)
    #clean buffer from Licor
    print("before flush")
    print(licor.in_waiting)
    licor.reset_input_buffer()    
    print("after flush")
    print(licor.in_waiting)
    timer1 = support.getMillis()
    timer2 = support.getMillis()
    licor.write(b"<li850><cfg>?</cfg></li850>")
    while licor.in_waiting:
        licor.readline()

    return licor

'''
licor.write("""<LI850>
                 <CFG>
                    <OUTRATE>1</OUTRATE>
                </CFG>
                <RS232>
                    <CO2>TRUE</CO2>
                    <FLOWRATE>TRUE</FLOWRATE>
                    <H2O>TRUE</H2O>
                    <CELLTEMP>TRUE</CELLTEMP>
                    <CELLPRES>TRUE</CELLPRES>
                    <IVOLT>FALSE</IVOLT>
                    <CO2ABS>TRUE</CO2ABS>
                    <H2OABS>TRUE</H2OABS>
                    <H2ODEWPOINT>TRUE</H2ODEWPOINT>
                    <RAW>FALSE</RAW>
                    <ECHO>FALSE</ECHO>
                    <STRIP>FALSE</STRIP>
                </RS232>
            </LI850>""".unicode("utf-8"))

licor.write("""<LI850><RS232>?</RS232></LI850>""".unicode("utf-8"))
'''
            
"""



ser = serial.Serial(licor_port)  # open serial port
print(ser.name)         # check which port was really used
ser.write(b"?")     # write a string
while ser.in_waiting:
    print (ser.readlines())
ser.close()             # close port
    
"""

"""
<LI850>
    <CFG>
        <OUTRATE>1</OUTRATE>
    </CFG>
</LI850>
"""