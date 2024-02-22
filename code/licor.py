import serial
import time
import supportM as support


class Licor:
    def __init__(self, licor_port="COM1"):
        # connect to licor
        self.licor = serial.Serial(
            port=licor_port,
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
        )

        # set the output rate to zero so that data only comes out when the
        # computer pings the device
        self.write_data(msg="<li850><cfg><outrate>0</outrate></cfg></li850>")

        # clean buffer from Licor
        """
        print("before flush")
        print(self.licor.in_waiting)
        self.licor.reset_input_buffer()    
        print("after flush")
        print(self.licor.in_waiting)
        timer1 = support.getMillis()
        timer2 = support.getMillis()
        self.licor.write(b"<li850><cfg>?</cfg></li850>")
        while self.licor.in_waiting:
            self.licor.readline()
        
        return licor
        """

    def read_data(self):

        self.licor.reset_input_buffer()
        self.licor.reset_output_buffer()
        self.licor.write(b"<li850><data>?</data></li850>")

        ack = False

        while self.licor.in_waiting == 0:
            time.sleep(0.01)
            # self.licor.write(b"<li850><data>?</data></li850>")
        temp = self.licor.read_until()
        print(temp)
        # if temp.decode().find("ack>true")>-1:
        # data=self.licor.read_until()
        # print(data)
        # ack=True
        return temp  # ,data

    def write_data(self, msg):
        msg = bytes(msg.encode("utf-8"))
        ack = False

        self.licor.reset_input_buffer()
        self.licor.reset_output_buffer()
        while not ack:
            self.licor.write(msg)
            temp = self.licor.read_until()
            if temp.decode().find("ack>true") > -1:
                ack = True

    def close(self):
        self.licor.close()


"""
    def write():
        b'<LI850><CFG><OUTRATE>0.5</OUTRATE></CFG></LI850>'
        return
    
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
                </LI850>')

    licor.write(b'<LI850><RS232>?</RS232></LI850>')
    
            


ser = serial.Serial(licor_port)  # open serial port
print(ser.name)         # check which port was really used
ser.write(b"?")     # write a string
while ser.in_waiting:
    print (ser.readlines())
ser.close()             # close port
    
<LI850>
    <CFG>
        <OUTRATE>1</OUTRATE>
    </CFG>
</LI850>
"""
