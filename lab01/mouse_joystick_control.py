import time
import mouse
import pygame
import sys
pygame.init()

joystick_count = pygame.joystick.get_count()
print("Number of joysticks: {}".format(joystick_count) )

if joystick_count == 0:
	print("No joysticks found")
	sys.exit(0)

joystick = pygame.joystick.Joystick(0)

is_pressed = mouse.is_pressed()
is_pressed_right = mouse.is_pressed(button='right')

while True:
	pygame.event.pump()
	time.sleep(1.0 / 30.0)
	mult = 3
	mouse.move((mult * joystick.get_axis(0)) ** 3, (mult * joystick.get_axis(1)) ** 3, absolute=False)
	
	if joystick.get_button(0) and not is_pressed:
		is_pressed = True
		mouse.press()
		
	if not joystick.get_button(0) and is_pressed:
		is_pressed = False
		mouse.release()
	
	if joystick.get_button(2) and not is_pressed_right:
		is_pressed_right = True
		mouse.press(button='right')
		
	if not joystick.get_button(0) and is_pressed_right:
		is_pressed_right = False
		mouse.release(button='right')
	