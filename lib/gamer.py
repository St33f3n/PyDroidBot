from operator import and_
import queue
import random
from threading import local
import numpy
import pyautogui, json, os, keyboard, time
import win32api, win32con
from .timers import Timers
from .ocr import Ocr
from .jsonHandler import JsonHandler 
from .playset import Playset
import math
class Gamer():
    """🎮 Represents a gamer entity.

    Args:
        name (str): The name of the gamer.

    Attributes:
        name (str): The name of the gamer.
        pos (dict): The position of the command area.
        area (tuple): The coordinates of the command area.
        uL (tuple): Upper-left coordinates of the command area.
        uR (tuple): Upper-right coordinates of the command area.
        dL (tuple): Lower-left coordinates of the command area.
        dR (tuple): Lower-right coordinates of the command area.
        timer (dict): A dictionary containing timers.
        json_handler (JsonHandler): The JSON handler for the gamer.
        playset (Playset): The playset associated with the gamer.
    """

    def __init__(self, name):
        self.name = name
        self.pos = self.getCommandArea()
        self.area = (self.pos.get("x"), self.pos.get("y"), self.pos.get("width"), self.pos.get("height"))
        if self.pos != None  :
            self.uL = (self.pos.get("x"), self.pos.get("y"))
            self.uR = (self.pos.get("x") + self.pos.get("width"), self.pos.get("y"))
            self.dL = (self.pos.get("x"), self.pos.get("y") + self.pos.get("height")) 
            self.dR = (self.pos.get("x") + self.pos.get("width"), self.pos.get("y") + self.pos.get("height")) 
        self.timer = {}
        self.json_handler = JsonHandler(name)
        self.playset = Playset(self.json_handler, name, self)

    def __str__(self):
        """📜 Returns a string representation of the gamer."""
        string = f'Game: {self.name}\nThe controlled Area is:\nupperLeft({self.uL}) | upperRight({self.uR})\nlowerLeft({self.uL}) | lowerRight({self.uR})\n'
        string = f'{string}It has the timers:\n'
        for e in self.timer.keys():
            string = f'{string}{e} with {self.timer.get(e)}\n'
        string = f'{string}{self.playset}'
        return string
        
    def addTimer(self, key ,timer : Timers):
        """⏱️ Add a timer to the gamer."""
        self.timer.update({key:timer})

    def getName(self):
        """🆔 Get the name of the gamer."""
        return self.name

    @staticmethod
    def getCommandArea():
        try:
            """🖱️ Get the command area coordinates."""
            print("Select the upper left edge on wich you want to start the bot.\nPress w to capture the edge.")
            while True:
                if keyboard.read_key() == 'w':
                    upperEdge = pyautogui.position()
                    break
                if keyboard.read_key() == 'q':
                    return
                
                print(".", " ")

            print("Select the lower right edge on wich you want to start the bot.\nPress w to capture the edge.")
            time.sleep(1)
            while True:
                if keyboard.read_key() == 'w':
                    lowerEdge = pyautogui.position()
                    break
                if keyboard.read_key() == 'q':
                    return
                
                print(".", " ")

                
            winPos = {"x" : upperEdge[0], "y" : upperEdge[1], "width" : lowerEdge[0]-upperEdge[0], "height": lowerEdge[1]-upperEdge[1]}
            print(f"Window at: {winPos} captured!")
            if lowerEdge != None and upperEdge != None:
                return winPos
            else:
                return None
        except:
            return None


    def getActions(self):
        """🎮 Get the actions of the gamer."""
        if self.playset.actions.empty():
            self.playset.queuePlayset()
            return self.playset.getQueue()
        else:
            return self.playset.getQueue()
        

    def simpleClick(self, x, y):
        """🖱️ Perform a simple click action."""
        if x in range(self.uL[0],self.uR[0]) and y in range(self.uL[1],self.dR[1]):
            win32api.SetCursorPos((x,y))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
            self.timer.get("click").hPause()
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        else:
            print("out of window")

    def dragMouse(self, start, end):
        """🖱️ Drag the mouse from start to end."""
        win32api.SetCursorPos(start)
        pyautogui.dragTo(end[0], end[1], 1, pyautogui.easeOutQuad, button='left')

    def dragPictureToPicture(self, key1, key2):
        """🖱️ Drag from the location of key1 picture to the location of key2 picture."""
        start = self.picToCoordinates(key1)
        end = self.picToCoordinates(key2)
        self.dragMouse(start, end)

    def dragFromPicture(self, key, distance, direction):
        """🖱️ Drag the mouse from the location of a picture."""
        distance = float(distance)
        direction = float(direction)-90
        target = self.picToCoordinates(key)
        targetx, targety = target
        angle = math.radians(direction)
        goal = (targetx + round(distance*math.cos(angle)), targety + round(distance*math.sin(angle)))
        self.dragMouse(target, goal)

    def keyPress(self, key):
        """⌨️ Simulate a key press."""
        pyautogui.keyDown(key)
        self.timer.get("key").hPause()
        pyautogui.keyUp(key)

    def clickIfPicture(self, key1, key2):
        """🖱️ Click on key2 if key1 picture is found."""
 
        _, _, img = self.json_handler.getPictureData(key1)
        if pyautogui.locateOnScreen(img, region=self.area, grayscale=True, confidence=0.8) != None:
            target = self.picToCoordinates(key2)
            if target != None:
                self.simpleClick(target[0],target[1])
                return True 
            else:
                return False
        else:
            print("Picture not found!\nMaybe the sequenze is messed up?")
    
        
    def picToCoordinates(self, key):
        """📸 Convert picture key to coordinates."""
        width , height, img = self.json_handler.getPictureData(key)
        location = pyautogui.locateOnScreen(img, region=self.area, grayscale=True, confidence=0.8)
        if location == None:
            print(f"Picture {key} not found")
            return None
        rndPoint = (random.randint(location[0],location[0]+width), random.randint(location[1], location[1]+height))
        return rndPoint
    
    # TODO regular automatic Checkup 
    def locateRessources(self, key):
        """🔍 Locate resources using OCR."""
        width , height, img = self.json_handler.getPictureData(key)
        v, sizeX, sizeY = self.json_handler.getRessourceData(key)        
        
        location = pyautogui.locateOnScreen(img, region=self.area, grayscale=True, confidence=0.75)
        print("Loc: ", location)
        if location == None:
            print("No location found")
        else:
            region = (int(location[0] + location[2]), int(location[1] + sizeY), int(sizeX), int(location[3] - 2 * sizeY))
            print( type(region), region)
            value = Ocr(region)
            print("Value", value)
            self.json_handler.valueUpdate("ressource" , (key, value))

    def wait(self, key):
        """⏸️ Pause execution based on stop timer."""
        self.timer.get(key).hPause()

    def conditionalAction(self, condition, action, confidence):
        """🛑 Perform an action based on condition.
               Args:
                condition (list): A list of conditions to evaluate.
                action (str): The name of the action to perform if the conditions are met.
                confidence (float): The confidence level required to trigger the action.
        """
        confidence = float(confidence)
        checklist = [None]*len(condition)   

        for idx, e in enumerate(condition):
            if type(e) is tuple:
                checklist[idx] = self.compareRessources(e)
            else:
                currentPic = self.json_handler.getPictureData(e)[2]
                print(currentPic)
                checklist[idx] = pyautogui.locateOnScreen(currentPic, region=self.area, grayscale=True, confidence=0.8) != None
        print(checklist)
        average = numpy.mean([1 if item else 0 for item in checklist])
        print(average)
        if average >= confidence and self.playset.actionSets.get(action) != None:
            self.playset.actionSets.get(action).runActionset()
        elif average > confidence and self.playset.actionSets.get(action) == None:
            print(f"No actionset found with name: {action}")

        else:    
            print("To few hits in the condition")

    def compareRessources(self, e : tuple):
        """🔁 Compare resources."""
        ressource, comperator, value = e
        currentRessources,  currentValue = self.json_handler.getRessourceData(ressource)
        
        match comperator:

            case 0:
                return currentValue>value
            
            case 1:
                return currentRessources<value
            
            case 2:
                return currentValue==value
            
            case _:
                print("Unknown Comperator")
                return None
        
        