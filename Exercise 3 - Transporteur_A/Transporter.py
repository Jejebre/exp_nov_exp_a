speed = 251
motor_left_target = speed
motor_right_target = speed
front = 2
back = 6

@onevent
def prox():
    global prox_horizontal, motor_left_target, motor_right_target
        
    nf_leds_top(32,16,0) # Orange

    if prox_horizontal[front] < 2500:
        nf_leds_top(0,32,0) # Green
        motor_left_target = -speed 
        motor_right_target = -251
        
    elif prox_horizontal[7] < 2500: 
        nf_leds_top(32,0,0) # Red
        motor_left_target = 251
        motor_right_target = speed
        

