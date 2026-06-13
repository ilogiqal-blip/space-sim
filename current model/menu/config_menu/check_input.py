def check_mouse_input():
    
    if active_field == "r" and pr.is_mouse_button_down(pr.MOUSE_BUTTON_LEFT):
        r += 2
        time.sleep(0.05)
    elif active_field == "r" and pr.is_mouse_button_down(pr.MOUSE_BUTTON_RIGHT):
        r -= 2
        time.sleep(0.05)
        if r < 0:
            r = 0

    if active_field == "d" and pr.is_mouse_button_down(pr.MOUSE_BUTTON_LEFT):
        d += 0.1
        time.sleep(0.05)
    elif active_field == "d" and pr.is_mouse_button_down(pr.MOUSE_BUTTON_RIGHT):
        d -= 0.1
        time.sleep(0.05)
        if d < 0:
            d = 0  

    if active_field == "x" and pr.is_mouse_button_down(pr.MOUSE_BUTTON_LEFT):
        x += 2
        time.sleep(0.05)
    elif active_field == "x" and pr.is_mouse_button_down(pr.MOUSE_BUTTON_RIGHT):
        x -= 2
        time.sleep(0.05)

    if active_field == "y" and pr.is_mouse_button_down(pr.MOUSE_BUTTON_LEFT):
        y += 2
        time.sleep(0.05)
    elif active_field == "y" and pr.is_mouse_button_down(pr.MOUSE_BUTTON_RIGHT):
        y -= 2
        time.sleep(0.05)

    if active_field == "z" and pr.is_mouse_button_down(pr.MOUSE_BUTTON_LEFT):
        z += 2
        time.sleep(0.05)
    elif active_field == "z" and pr.is_mouse_button_down(pr.MOUSE_BUTTON_RIGHT):
        z -= 2
        time.sleep(0.05)

    if active_field == "speed" and pr.is_mouse_button_down(pr.MOUSE_BUTTON_LEFT):
        speed += 2
        time.sleep(0.05)
    elif active_field == "speed" and pr.is_mouse_button_down(pr.MOUSE_BUTTON_RIGHT):
        speed -= 2
        time.sleep(0.05)
        if speed < 0:
            speed = 0

    if active_field == "direction_x" and pr.is_mouse_button_down(pr.MOUSE_BUTTON_LEFT):
        direction_degrees_x += 2
        time.sleep(0.05)
        if direction_degrees_x > 359:
            direction_degrees_x = 0

    elif active_field == "direction_x" and pr.is_mouse_button_down(pr.MOUSE_BUTTON_RIGHT):
        direction_degrees_x -= 2
        time.sleep(0.05)
        if direction_degrees_x < 0:
            direction_degrees_x = 359

    if active_field == "direction_y" and pr.is_mouse_button_down(pr.MOUSE_BUTTON_LEFT):
        direction_degrees_y += 2
        time.sleep(0.05)
        if direction_degrees_y > 359:
            direction_degrees_y = 0

    elif active_field == "direction_y" and pr.is_mouse_button_down(pr.MOUSE_BUTTON_RIGHT):
        direction_degrees_y -= 2
        time.sleep(0.05)
        if direction_degrees_y < 0:
            direction_degrees_y = 359


def check_button_input():
    
    if active_field == "r" and pr.is_key_pressed(pr.KEY_EQUAL):
        r += 1
        time.sleep(0.05)
    elif active_field == "r" and pr.is_key_pressed(pr.KEY_MINUS):
        r -= 1
        time.sleep(0.05)
        if r < 0:
            r = 0

    if active_field == "d" and pr.is_key_pressed(pr.KEY_EQUAL):
        d += 0.05
        time.sleep(0.05)
    elif active_field == "d" and pr.is_key_pressed(pr.KEY_MINUS):
        d -= 0.05
        time.sleep(0.05)
        if d < 0:
            d = 0  

    if active_field == "x" and pr.is_key_pressed(pr.KEY_EQUAL):
        x += 1
        time.sleep(0.05)
    elif active_field == "x" and pr.is_key_pressed(pr.KEY_MINUS):
        x -= 1
        time.sleep(0.05)

    if active_field == "y" and pr.is_key_pressed(pr.KEY_EQUAL):
        y += 1
        time.sleep(0.05)
    elif active_field == "y" and pr.is_key_pressed(pr.KEY_MINUS):
        y -= 1
        time.sleep(0.05)

    if active_field == "z" and pr.is_key_pressed(pr.KEY_EQUAL):
        z += 1
        time.sleep(0.05)
    elif active_field == "z" and pr.is_key_pressed(pr.KEY_MINUS):
        z -= 1
        time.sleep(0.05)

    if active_field == "speed" and pr.is_key_pressed(pr.KEY_EQUAL):
        speed += 1
        time.sleep(0.05)
    elif active_field == "speed" and pr.is_key_pressed(pr.KEY_MINUS):
        speed -= 1
        time.sleep(0.05)
        if speed < 0:
            speed = 0

    if active_field == "direction_x" and pr.is_key_pressed(pr.KEY_EQUAL):
        direction_degrees_x += 1
        time.sleep(0.05)
        if direction_degrees_x > 359:
            direction_degrees_x = 0
    elif active_field == "direction_x" and pr.is_key_pressed(pr.KEY_MINUS):
        direction_degrees_x -= 1
        time.sleep(0.05)
        if direction_degrees_x < 0:
            direction_degrees_x = 359

    if active_field == "direction_y" and pr.is_key_pressed(pr.KEY_EQUAL):
        direction_degrees_y += 1
        time.sleep(0.05)
        if direction_degrees_y > 359:
            direction_degrees_y = 0
    elif active_field == "direction_y" and pr.is_key_pressed(pr.KEY_MINUS):
        direction_degrees_y -= 1
        time.sleep(0.05)
        if direction_degrees_y < 0:
            direction_degrees_y = 359
