# Constants
NORMAL = 0
WALLS = 1
LINE = 2
STOP = 3
GOBACK = 4

# Start
mode = NORMAL

@onevent
def prox():
    global mode, motor_left_target, motor_right_target

    if mode == NORMAL:
        nf_leds_top(0, 32, 0)  # Green
        
        if prox_horizontal[2] < 2500:
            mode = WALLS
            motor_left_target = 251 
            motor_right_target = 251
            
    
    elif mode == WALLS:
        nf_leds_top(32, 0, 0)  # Red
        if prox_horizontal[2] > 4300:
            motor_left_target = -51
            motor_left_target = -51
            mode = GOBACK

    elif mode == GOBACK:
        print("JE PASSE EN GOBACK")
        if prox_ground_delta[0] < 200 or prox_ground_delta[1] < 200:
            mode = LINE
            timer_period[0] = 1950 #turn during 1950ms            
            motor_left_target = -251
            motor_right_target = 251
        else:
            print("ICI")
            motor_left_target = -51
            motor_right_target = -51


@onevent
def timer0():
    global mode, motor_left_target, motor_right_target
    # Check if the current mode is LINE to switch back to NORMAL
    if mode == LINE:
        motor_left_target = 251 
        motor_right_target = 251
        nf_leds_top(32, 32, 0) # Orange
        mode = NORMAL
        
@onevent
def buttons():
    global motor_left_target, motor_right_target, mode
    if button_center:
        motor_left_target = 0
        motor_right_target = 0
        mode = STOP
        nf_leds_top(0, 0, 0)  # Turn off all LEDs
        
        
        
        
# ------------------------------------------------------------- #
# ------------------------------------------------------------- #
# ------------------------------------------------------------- #
# ------------------------------------------------------------- #
# ------------------------------------------------------------- #
# ---------------- DONT TOUCH - USED FOR LOGS ----------------- #



print(" --- Start of the program Bug_TheTransporter.py --- ")
        
# To avoid flood, can print once every second if manipulated
can_print_acc = True
can_print_mot = True

@onevent
def timer1():
    global can_print_acc, can_print_mot
    can_print_acc = True
    can_print_mot = True
    timer_period[1] = 0
        
left_last = 0
right_last = 0

@onevent
def acc():
    global left_last, right_last, can_print_acc, can_print_mot, timer_period
    
    # If the motors' speed changes
    if left_last != motor_left_target or right_last != motor_right_target:
        
        # Update and print the new target
        left_last = motor_left_target
        right_last = motor_right_target
        print("LOGS: Wheels ,", left_last, ",", right_last)
        can_print_mot = False
        can_print_acc = False
        timer_period[1] = 400
        
    # Check the acc to see if Thymio is manipulated
    elif (acc[0]*acc[0] > 9 or acc[1]*acc[1] > 36) and (left_last !=0 or right_last !=0) and can_print_acc:
        print("LOGS: Acc ,", acc[0], ",", acc[1], ",", acc[2])
        can_print_acc = False
        timer_period[1] = 1000
        
    # Be less indulgent for the thresholds if Thymio is not supposed to move    
    if (acc[2]-20)*(acc[2]-20) > 9  and (left_last == 0 or right_last == 0) and can_print_acc:
        print("LOGS: Acc ,", acc[0], ",", acc[1], ",", acc[2])
        can_print_acc = False
        timer_period[1] = 1000
        
# Button prints
@onevent
def button_center():
    if button_center: print("LOGS: center , pressed")
    else:            print ("LOGS: center , released")
@onevent
def button_left():
    if button_left: print("LOGS: left , pressed")
    else:            print ("LOGS: left , released")
@onevent
def button_right():
    if button_right: print("LOGS: right , pressed")
    else:            print ("LOGS: right , released")
@onevent
def button_forward():
    if button_forward: print("LOGS: forward , pressed")
    else:            print ("LOGS: forward , released")
@onevent
def button_backward():
    if button_backward: print("LOGS: backward , pressed")
    else:            print ("LOGS: backward , released")