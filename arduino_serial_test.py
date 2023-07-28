


# Receives a string from Arduino using readline()
# Requires PySerial

# (c) www.xanthium.in 2021
# Rahul.S
import keyboard
import serial
import time

SerialObj = serial.Serial('/dev/ttyACM0',9600) # COMxx   format on Windows
                                        # /dev/ttyUSBx format on Linux
                                        #
                                        # Eg /dev/ttyUSB0
                                        # SerialObj = serial.Serial('/dev/ttyUSB0')

time.sleep(3)   # Only needed for Arduino,For AVR/PIC/MSP430 & other Micros not needed
                # opening the serial port from Python will reset the Arduino.
                # Both Arduino and Python code are sharing Com11 here.
                # 3 second delay allows the Arduino to settle down.


SerialObj.timeout = 3 # set the Read Timeout
while True:
    
    received_string = SerialObj.readline().decode().strip()

    # Perform actions based on the received string
    if received_string == "Play":
        print("Play action")
        keyboard.press_and_release('ctrl+w')
        # Add your code here for the play action

    elif received_string == "Pause":
        print("Pause action")
        keyboard.press_and_release('ctrl+w')
        # Add your code here for the pause action

    elif received_string == "Next":
        print("Next action")
        keyboard.press_and_release('ctrl+f10')
        # Add your code here for the next action

    elif received_string == "Prev":
        print("Previous action")
        keyboard.press_and_release('ctrl+f8')
        # Add your code here for the previous action

    elif received_string == "Up":
        print("Up action")
        keyboard.press_and_release('ctrl+8')
        # Add your code here for the up action
    elif received_string == "Down":
        keyboard.press_and_release('ctrl+0')
        print("Down action")
    # Add additional conditions for more commands if needed

    else:
        print("Unknown command:", received_string)

SerialObj.close()          # Close the port