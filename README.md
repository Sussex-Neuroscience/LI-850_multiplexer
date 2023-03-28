# LI-850_multiplexer
A multiplexing system for a LICOR CO2 and H20 analyser







### meeting logs:

#### 25/02/2022

I am writing to summarise what we discussed and to ask a couple of follow up questions:
 
Right now you have a system where you need to open up the chambers when new metabolism from different animals needs to be measured. This adds a long delay to measurements, as it takes time for the internal chamber environment to stabilise. Moreover, needs constant “supervision” as user interaction is needed. 
 
So to solve this issue, you would like a system that allows for chambers to be cycled automatically. To do that we would add one manifold on the input side and one on the output side of the chambers. The path of the gas going through a specific channel in the manifolds is to be controlled by with software so that measurements can be done in individual chambers at custom cycles
 
Another issue is your measurement device. It works fine and is quite accurate, but interfacing options are rubbish. So it would be good to find a way to have better interface, including the possibility to do faster sampling and to synchronise the behavioural side of things with metabolic measurements. 
 
Timewise you would like to have a first working system this summer. Than a final working system for March 2023. 
 
Does this sound correct?
 
@Jeremy, please send me the tubing specifications.
 
A couple of follow up questions:
A.	I tend to use Python and/or Bonsai-rx for a lot of projects, as there are quite nice libraries for hardware communication/interfaces. In this case because you want to record video data, I think Bonsai-rx would make sense as we could grab camera data, do motion tracking and some other things there, together with synching with the metabolic data. Would that be ok? Bonsai-rx can then output video files that can be read anywhere, and csv data with trigger times, metabolic data, etc. 
B.	The device has two cells (A and B), from what I read normally one of them is used as control and one as sample reading. Is this how your device is configured?
C.	What variables do you normally use from the device (Jeremy mentioned using ~8 out of 40?)
D.	Are you settled in 6 chambers at a time?
E.	I normally develop things “out in the open” in GitHub (examples can be seen here: https://github.com/sussex-neuroscience) with everything being publicly available from the start. This allow me to keep changes tracked and also to have all documentation for the project in one place. Would you be ok with that?
 
Reading a bit on the manual, I found two potential pathways for user interfacing:
1 -  it is possible to get raw voltage traces from the device that can be converted back to meaningful values using a formular they provide. 
2 – Using the RS232 port should be possible to communicate using custom software to grab specific variables at specific time intervals. (the manual has a “language reference” section describing how to send commands to query the device).
 
I am tending to think for integration purposes, using method 2 would be the most straightforward.

---


In terms of measurements, the tubing is 4 mm (inner diameter) x 6 mm (outer diameter). It should fit standard aquarium valves etc. 

A. We do already use Bonsai in the lab for some projects, so I'd be happy to go with that option.
B. We always use one chamber as the control (as you've said), which allows us to take both absolute and differential measurements. 
C. We usually need - CO2 A, CO2 B, CO2 D (the differential measure), H2O A, H2O B, H2O D, temperature (7 measures) - we usually don't use the others in our analysis.
D. Not at all, we can be flexible about the exact number.
E. Very happy with everything being open source. 