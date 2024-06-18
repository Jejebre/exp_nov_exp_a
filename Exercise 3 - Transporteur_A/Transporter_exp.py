speed = 251
motor_left_target = speed
motor_right_target = speed
front = 2  # Index for the front sensor
ground_sensor_left = 0  # Index for the left ground sensor

# State to track whether the robot has recently seen a wall
has_seen_wall = False

@onevent
def prox():
    global prox_horizontal, prox_ground_delta, motor_left_target, motor_right_target, has_seen_wall
        
    nf_leds_top(32, 16, 0)  # Orange initially

    # Detect wall at the front
    if prox_horizontal[front] > 2500:
        nf_leds_top(0, 32, 0)  # Green for backing off
        motor_left_target = -speed
        motor_right_target = -speed
        has_seen_wall = True  # Set the flag that the wall has been detected

    # Check if the robot has seen a wall and then a black line
    elif has_seen_wall and prox_ground_delta[ground_sensor_left] < 100:
        nf_leds_top(32, 0, 0)  # Red for turning
        motor_left_target = -speed
        motor_right_target = speed
        has_seen_wall = False  # Reset the wall detection flag

    # Default movement: move forward if no wall is detected initially or after turning
    else:
        nf_leds_top(32, 16, 0)  # Orange for moving forward
        motor_left_target = speed
        motor_right_target = speed
