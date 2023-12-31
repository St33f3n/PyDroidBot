import queue
import random
from threading import local
import pyautogui, json, os, keyboard, time, cv2
import win32api, win32con
from .timers import Timers
from .ocr import Ocr
from .jsonHandler import JsonHandler 
from .playset import Playset


class Gamer():
    def __init__(self, name):
        self.name = name
        self.pos = self.getCommandArea()
        if self.pos != None  :
            self.uL = (self.pos.get("x"), self.pos.get("y"))
            self.uR = (self.pos.get("x") + self.pos.get("width"), self.pos.get("y"))
            self.dL = (self.pos.get("x"), self.pos.get("y") + self.pos.get("height")) 
            self.dR = (self.pos.get("x") + self.pos.get("width"), self.pos.get("y") + self.pos.get("height")) 
        self.timer = {}
        self.json_handler = JsonHandler(name)
        self.playset = Playset(self.json_handler, name)

    def __str__(self):
        string = f'Game: {self.name}\nThe controlled Area is:\nupperLeft({self.uL}) | upperRight({self.uR})\nlowerLeft({self.uL}) | lowerRight({self.uR})\n'
        string = f'{string}It has the timers:\n'
        for e in self.timer.keys():
            string = f'{string}{e} with {self.timer.get(e)}\n'
        string = f'{string}{self.playset}'
        return string
        
    def addTimer(self, key ,timer : Timers):
        self.timer.update({key:timer})

    def getName(self):
        return self.name

    def getCommandArea(self):
        print("Select the upper left edge on wich you want to start the bot.\nPress c to capture the edge.")
        while True:
            if keyboard.read_key() == 'c':
                upperEdge = pyautogui.position()
                break
            
            print(".", " ")

        print("Select the lower right edge on wich you want to start the bot.\nPress e to capture the edge.")
        time.sleep(1)
        while True:
            if keyboard.read_key() == 'e':
                lowerEdge = pyautogui.position()
                break
            
            print(".", " ")
        winPos = {"x" : upperEdge[0], "y" : upperEdge[1], "width" : lowerEdge[0]-upperEdge[0], "height": lowerEdge[1]-upperEdge[1]}
        print(f"Window at: {winPos} captured!")
        if lowerEdge != None and upperEdge != None:
            return winPos
        else:
            return None


    def getActions(self):
        if self.playset.actions.empty():
            self.playset.queuePlayset()
            return self.playset.getQueue()
        else:
            return self.playset.getQueue()
        

    def simpleClick(self, x, y):
        if x in range(self.uL[0],self.uR[0]) and y in range(self.uL[1],self.dR[1]):
            win32api.SetCursorPos((x,y))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
            self.timer.get("click").hPause()
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        else:
            print("out of window")

    def keyPress(self, key):
        pyautogui.keyDown(key)
        self.timer.get("key").hPause()
        pyautogui.keyUp(key)

    def clickIfPicture(self, key1, key2):
        """key1 = Ziel das erkannt werden soll\n
        key2 = Ziel auf das gedrückt wird"""

        _, _, img = self.json_handler.getPictureData(key1)
        if pyautogui.locateOnScreen(img, grayscale=True, confidence=0.8) != None:
            self.clickOnPicture(key2)
        else:
            print("Picture not found!\nMaybe the sequenze is messed up?")
    
    def clickOnPicture(self, key):
        target = self.picToCoordinates(key)
        if target != None:
            self.simpleClick(target[0],target[1])
            return True 
        else:
            return False
        
    def picToCoordinates(self, key):
        width , height, img = self.json_handler.getPictureData(key)
        location = pyautogui.locateOnScreen(img, grayscale=True, confidence=0.8)
        rndPoint = (random.randint(location[0],location[0]+width), random.randint(location[1], location[1]+height))
        return rndPoint
    
    # TODO use it 
    def locateRessources(self, key):
        width , height, img = self.json_handler.getPictureData(key)
        v, sizeX, sizeY = self.json_handler.getRessourceData(key)
        location = pyautogui.locateOnScreen(img, grayscale=True, confidence=0.75)
        print("Loc: ", location)
        region = (int(location[0] + location[2]), int(location[1] + sizeY), int(sizeX), int(location[3] - 2 * sizeY))
        print( type(region), region)
        value = Ocr(region)
        print("Value", value)
        newInp = JsonHandler.create_ressourceData(key, value, sizeX, sizeY)
        print(newInp)
        self.json_handler.update("ressource" , newInp)

    def wait(self):
        self.timer.get('stop').hPause()
    

