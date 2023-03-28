from belay import Device


class multiplexer(Device): #This is the class that contains all the phases 
    #now we are going to setup the number of trials and data collection
    #ntrials = 10
    #data collection time in hours
    coll_time_h = 2
    coll_time_ms = 2*60*60*1000

    #time between data collection in min
    period = 7 #previoulsy discussed that each data collection should be 7min long
    period_ms = period*60*1000


    #time needed for chambers to stabilize in min
    #n_runs = 3
    stab_time = 25 #in min
    stab_time_ms = stab_time*60*1000

    #number of chambers to be used. Min 1, max 6
    n_chan = 6
    if n_chan>6:
        n_chan=6 
    if n_chan<1:
        n_chan=1
    @Device.setup # Device setup is where the yellow LEDs and sensor LEDs are defined, also imports.
    def setup():

        #import libraries directly in the micropython board
        import time 
        import random
        from machine import Pin 

        #assign each channel to a pair of pins
        ch1_in = Pin(15,Pin.OUT)
        ch1_out = Pin(2,Pin.OUT)
        ch2_in = Pin(16,Pin.OUT)
        ch2_out = Pin(17,Pin.OUT)
        ch3_in = Pin(19,Pin.OUT)
        ch3_out = Pin(21,Pin.OUT)

        ch4_in = Pin(5,Pin.OUT)
        ch4_out = Pin(18,Pin.OUT)
        ch5_in = Pin(22,Pin.OUT)
        ch5_out = Pin(23,Pin.OUT)
        ch6_in = Pin(14,Pin.OUT)
        ch6_out = Pin(27,Pin.OUT)
        
        #assign a pin to LED indicator
        led_ind = Pin(25,Pin.OUT)
        #assign a pin to bnc output for triggering the LI7000
        li_ind = Pin(26,Pin.OUT)

        all_chan = [ch1_in,ch1_out,
                    ch2_in,ch2_out,
                    ch3_in,ch3_out,
                    ch4_in,ch4_out,
                    ch5_in,ch5_out,
                    ch6_in,ch6_out,
                    ]


        #we start our protocol by turning everything off.

        for valve in allChan:
            valve.off()
        led_ind.off()
        li_ind.off()
        
        return

    @device.task
    def stabilize():#than we set the stabilization time for the chambers:

        timer1 = time.ticks_ms()
        timer2 = time.ticks_ms()
        #stabTimeMs
        while timer2-timer1<stabTimeMs:  
            for i in range(0,nChan,2):
                all_chan[nChan].on()
                all_chan[nChan+1].on()
                time.sleep_ms(10000)
                all_chan[nChan].off()
                all_chan[nChan+1].off()
        
            timer2 = time.ticks_ms()
    
    @device.task
    def protocol():
        temp_chan=1
        for i in range(0,n_chan,2):
            timer1 = time.ticks_ms()
            timer2 = time.ticks_ms()
            
            yield("channel: "+str(temp_chan))
            temp_chan=temp_chan+1
            if temp_chan>6:
                temp_chan=1
            all_chan[nChan].on()
            all_chan[nChan+1].on()
                
            while timer2-timer1<period_ms:
                timer2 =time.ticks_ms()
                
                
            
            
        

        
