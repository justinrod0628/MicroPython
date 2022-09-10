from cyberbot import *


# pin 0 = red dir B
# pin 1 = yellow dir b
# pin 2 = green dir B

# pin 10 = red dir a straight
# pin 11 = yellow dir a straight
# pin 12 = green dir a straight

# pin 5 = red dir a left
# pin 6 = yellow dir a left
# pin 7 = green dir a left



#Traffic Light

#Initial State

while True:

    bot(10).write_digital(0)          #Red off          Dir A straight
    bot(11).write_digital(0)          #Yellow off       Dir A straight
    bot(12).write_digital(1)          #Green on         Dir A straight
    bot(5).write_digital(1)           #red on           Dir A left
    bot(6).write_digital(0)           #Yellow off       Dir A left
    bot(7).write_digital(0)           #Green off        Dir A left
    bot(0).write_digital(1)           #Red on           Dir B
    bot(1).write_digital(0)           #Yellow off       Dir B
    bot(2).write_digital(0)           #Green off        Dir B
    
    if bot(15).read_digital() == 0:
    
        bot(10).write_digital(0)      #Red off       Dir A straight
        bot(11).write_digital(0)      #Yellow on     Dir A straight
        bot(12).write_digital(1)      #Green on      Dir A straight
    
        bot(0).write_digital(1)      #Red on         Dir b
        bot(1).write_digital(0)      #Yellow off     Dir b
        bot(2).write_digital(0)      #Green off      Dir b
    
    
        sleep(3000)
    
        bot(10).write_digital(0)      #Red off       Dir A straight
        bot(11).write_digital(1)      #Yellow on     Dir A straight
        bot(12).write_digital(0)      #Green off     Dir A straight
    
        sleep (1000)
    
        bot(10).write_digital(1)      #Red on        Dir A straight
        bot(11).write_digital(0)      #Yellow off    Dir A straight
        bot(0).write_digital(0)       #Red off       Dir B
        bot(2).write_digital(1)       #Green on      Dir B
        
        sleep (3000)
    
        bot(1).write_digital(1)       #Yellow on     Dir B
        bot(2).write_digital(0)       #Green off     Dir B
    
        sleep (1000)
        
    elif bot(15).read_digital() == 1:
    
        bot(5).write_digital(0)       #Red off        Dir A left
        bot(6).write_digital(0)       #Yellow off     Dir A left
        bot(7).write_digital(1)       #Green on       Dir A left
        bot(10).write_digital(1)      #Red on         Dir A straight
        bot(11).write_digital(0)      #Yellow off     Dir A straight
        bot(12).write_digital(0)      #Green off      Dir A straight
        bot(0).write_digital(1)       #Red on         Dir B
        bot(1).write_digital(0)       #Yellow off     Dir B
        bot(2).write_digital(0)       #Green off      Dir B
        
        sleep(3000)
    
        bot(6).write_digital(1)       #Yellow on      Dir A left
        bot(7).write_digital(0)       #Green off      Dir A left
        
        sleep(1000)
        
        bot(5).write_digital(1)       #red on         Dir A left
        bot(6).write_digital(0)       #yellow off     Dir A left
        bot(10).write_digital(0)      #red off        Dir A straight
        bot(12).write_digital(1)      #green on       Dir A straight
        bot(0).write_digital(0)       #red off        Dir B
        bot(2).write_digital(1)       #green on       Dir B
        
        sleep(1000)
	
