@onevent
def buttons():
    global motor_left_target, motor_right_target
    
    if button_forward:
        nf_leds_top(0,32,0)
        motor_left_target == 255
        motor_right_target = 255
        
    if button_left:
        nf_leds_top(32,16,0)
        motor_left_target = -100
        motor_right_target = 100
        
    if button_right:
        nf_leds_top(32,16,0)
        motor_left_target = 100
        motor_right_target = -100
        
    if button_forward:
        nf_leds_top(32,0,0)
        motor_left_target = -255
        motor_right_target = -255
        
    if button_center:
        nf_leds_top(0,0,0)
        motor_left_target = 0
        motor_right_target = 0
