from cyberbot import *


# pin 0 Green LED
# pin 1 Red LED
# pin 2 Yellow LED

# pin 22 Buzzer
# Sensor connected to ad1 (pin1)

# Initial State

while True:
    
#defined case a for case 3
        
    def a():
        bot(0).write_digital(0)#Green LED off
        bot(2).write_digital(0)#Yellow LED off
        bot(1).write_digital(1)#Red LED on
        bot(22).tone(1000, 500) #Buzzer on
        print("Dangerously High Water Level")
        sleep(500)
        bot(1).write_digital(0) #Red LED off
        sleep(500)
        bot(1).write_digital(1)#Red LED on
        bot(22).write_digital(0) #Buzzer off
        sleep(500)
        bot(1).write_digital(0) #Red LED off
        sleep(500)
        bot(1).write_digital(1)#Red LED on
        sleep(500)
        bot(1).write_digital(0) #Red LED off
        sleep(500)
        
        

    bot(22).write_digital(0)  # Buzzer off
    moisture = pin1.read_analog()

# Case 1 (Normal Water Levels)

    if moisture <= 400:
        bot(0).write_digital(1)  #Green LED on
        bot(1).write_digital(0)  #Red LED off
        bot(2).write_digital(0)  #Yellow LED off
        
# Case 2 (Low 2" Water Levels)

    elif moisture > 400 and moisture <= 800:
    
        bot(0).write_digital(0) #Green LED off
        bot(2).write_digital(1) #Yellow LED on
        bot(1).write_digital(0) #Red LED off
        bot(22).tone(1000, 2000) #Buzzer on
        display.scroll("High Water Level", 50) #buzzer to screen "High Water Level"
        print("High Water Level")
        sleep(1000)              #delay 1 sec
        bot(22).write_digital(0) #Buzzer off
        sleep(4000)              #delay 4 sec
        
# Case 3 (High 4" Water Levels)
    
    elif moisture > 800:
        
        a()
