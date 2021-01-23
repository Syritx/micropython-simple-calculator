import machine
import time
import ssd1306


# D1, D2, D3 and D5 Pins
BUTTON_PINS = [5, 4, 0, 14]

# D6 and D7 Pins
SCREEN_PINS = [12, 13]

class Button:
	
    button = None
    id = 0
    is_up = False

    def __init__(self, pin, id):
	self.button = machine.Pin(pin, machine.Pin.IN, machine.Pin.PULL_UP) 
	self.id = id

def display_numbers(nums_array, display):
    display.fill(0)
    display.text('NUMS: {a}, {b}'.format(a=nums_array[0], b=nums_array[1]), 0,0)
    display.show()

def display_numbers_and_operation(nums_array, operator, display):
    result = 0
    if str(operator) == '-':
	result = nums_array[0] - nums_array[1]
    elif str(operator) == '+':
	result = nums_array[0] + nums_array[1]

    display.fill(0)
    display.text('NUMS: {a}, {b}'.format(a=nums_array[0], b=nums_array[1]), 0, 0)
    display.text('RESULT: {a}'.format(a=result), 0, 16)
    display.show()

def start():
    
    i2c = machine.I2C(scl=machine.Pin(SCREEN_PINS[1]), sda=machine.Pin(SCREEN_PINS[0]))
    display = ssd1306.SSD1306_I2C(128, 64, i2c)	
    nums = [0, 0]

    buttons = [Button(BUTTON_PINS[0], 0),
	       Button(BUTTON_PINS[1], 1),
	       Button(BUTTON_PINS[2], 2),
	       Button(BUTTON_PINS[3], 3)]

    while True:
	for button in buttons:
	    if button.button.value() == 0 and button.is_up == False:		
		button.is_up = True		

		if button.id == 3:
		    nums[0] += 1
		    display_numbers(nums, display)
		    print('[NB 1]: {i} -> {j}'.format(i=str(nums[0]-1), j=str(nums[0])))	    
	
		elif button.id == 2:
		    nums[1] += 1
		    display_numbers(nums, display)
		    print('[NB 2]: {i} -> {j}'.format(i=str(nums[1]-1), j=str(nums[1])))

		elif button.id == 1:
		    display_numbers_and_operation(nums, '+', display)
		    print(str(nums[0]+nums[1]))

		elif button.id == 0:
		    display_numbers_and_operation(nums, '-', display)
		    print(str(nums[0]-nums[1]))

	#	display.fill(0)
	#	display.text('nums: {a}, {b}'.format(a=nums[0], b=nums[1]), 0, 0)
	#	display.show()
		
	    if button.button.value() == 1 and button.is_up == True:
		button.is_up = False

	time.sleep(0.1)

