import keyboard

def play_pause():
    keyboard.press_and_release('ctrl+w')

def next_track():
    keyboard.press_and_release('ctrl+f10')

def previous_track():
    keyboard.press_and_release('ctrl+f8')

while True:
    # Get user input
    action = input("Enter action (play, pause, next, previous, exit): ").lower()

    # Perform action
    if action == 'play':
        play_pause()
    elif action == 'pause':
        play_pause()
    elif action == 'next':
        next_track()
    elif action == 'prev':
        previous_track()
    elif action == 'exit':
        break
    else:
        print("Invalid action. Please try again.")
