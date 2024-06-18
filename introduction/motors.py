# In this window is the program you want to send.

# For example, we want Thymio's wheel to turn at 150 speed forward
motor_right_target = 150
motor_left_target = 150
if button_forward == True:
    motor_right_target = 0
    motor_left_target = 0