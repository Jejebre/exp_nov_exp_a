timer_period[0] = 500 # set the timer's period to 500 ms
nf_leds_top (32,0,0)  # and we set the color of the leds to red (R=32, G=0, B=0)
color_is_red = True   # we will use this variable to track the state of the LEDS

@onevent
def timer0():
# each time the timer triggers
# the following block of code is executed
    global leds_top, color_is_red # make sure the variables we want to modify are global
    
    if color_is_red:         # then if the led is already red ...
        nf_leds_top(0,0,32)  # ... we set it to blue
    else:                    # else if it's not red ...
        nf_leds_top (32,0,0) # ... we set it to red
    color_is_red = not color_is_red # Finally we update the state of the variable