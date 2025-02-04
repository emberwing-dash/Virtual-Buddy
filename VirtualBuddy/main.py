import time
from pyautogui import *

#Classes Imported
from Classes.autoType import AutoType


#Objects of classes
def main():
    auto = AutoType()

    #check mouse position
    #auto.display_mouse_position()
    #auto.cursorMaham()

    #type and paint
    #auto.typeWrite("Hiii")
    auto.paintEmoji("happy")
    

main()