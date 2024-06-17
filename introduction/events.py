@onevent # Write this before events
def buttons(): # The block of code below will be executed each time a button is pressed
    global motor_left_target, motor_right_target 	#Write this to modify global variables
    if button_forward:								# Check if we press the forward button
        motor_left_target = 150 					# If so, go forward...
        motor_right_target = 150 					#... with both wheels!
        
        


@onevent # Write this before events
def prox(): # The block of block below will be executed each time Thymio senses an obstacle
    global motor_left_target, motor_right_target # Write this to modity global variables
    if prox_horizontal[2] > 2000: 				  # If the front sensor's value is higher than 2000
        motor_left_target = 0     				  # Stop both wheels...
        motor_right_target = 0					  # ... before Thymio crashes into the wall!

