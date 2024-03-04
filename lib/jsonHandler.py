import os
import json
from PIL import Image

startup = {"config": {}, "playset": [], "actionset" : {}, "pictures": {}}
functions = ["keyPress", "compareRessources((1,1,1))",  "clickIfPicture(img, img)", "locateRessources(img)", "wait()", "conditionalAction(n, 2)"] # dragMouse 

class JsonHandler():

    def __init__(self, name) -> None:
        self.name = name
        self.jsonData = {}
        self.loadData()

    # from lib.JsonHandler import JsonHandler 
    # than JsonHandler.create_...
    # no object need to be created
    def create_ressourceData(name, value, x, y):
            return {name : {'value' : value, 'position' : {'x' : x,'y' : y}}}

    def create_playsetData(name, arg1, arg2, argN):
        return {'name': name, 'arg1': arg1, 'arg2' : arg2, 'argN' : argN}

    # TODO reag img path
    def saveNewPicture(self, name, img : Image, path, windowSize, screenSize):
        w, h = img.size
        window_width, window_height = windowSize
        screen_width, screen_height = screenSize
        data = {
            name: {
                "width": w,
                "height": h,
                "path": path,
                "windowSize": {
                    "width": window_width,
                    "height": window_height
                },
                "screenSize": {
                    "width": screen_width,
                    "height": screen_height
                }
            }
        }
        self.add(data, "pictures",)
        self.saveData()



  

    def __str__(self):
        return self.jsonData

    def loadData(self):
        config_file = f'{self.name}/config.json'
        if os.path.exists(config_file):
            with open(config_file, 'r') as f:
                self.jsonData = json.load(f)
        else:
            with open(config_file, "w") as f:
                json.dump(startup, f, indent=4)
                self.jsonData = startup

    def saveData(self): 
        with open(f'{self.name}/config.json', 'w') as f:
            json.dump(self.jsonData, f, indent=4)



    # data is Tuple (name, directory)
    def add(self, option, data : tuple):
        if option not in self.jsonData:
            raise ValueError(f'No {option} in jsonData')
        self.jsonData[option][data[0]] = data[1]

    def add(self,  data : dict, option = None):
        if option == None:
            self.jsonData.update(data)
            return

        if option not in self.jsonData:
            raise ValueError(f'No {option} in jsonData')
        self.jsonData[option].update(data)

    def update(self, option, data : tuple):

        ## TODO Makes no sens 
        # if option not in self.jsonData:
        #     print(0)
        #     if data[0] in self.jsonData[option]:
        #         raise ValueError(f'No {option} in jsonData')
            
        key, value = data
        
        if key not in self.jsonData[option]:
            raise ValueError(f'No {key} in {option}')
        
        self.jsonData[option][key]["value"] = value
        # [ ]
        # self.jsonData[option][key].update(data)
        
        self.saveData()

    
    # TODO playset update if needed
    # def update(self, option, data : list):
    #     self.jsonData[option] = data
    #     self.saveData()

    def remove(self):
        None
  

    def getData(self, option : str, key=None):
        # return the complete playset
        if key == None:
            if option in self.jsonData:
                return self.jsonData[option]

        # if option == 'playset':
        #     return self.jsonData[option]
        
        # if option == 'actionset':
        #     return self.jsonData[option]
        
        # if option == 'pictures' and key == 0:
        #     return self.jsonData[option]

        # Checks if a key is valid
        if key not in self.jsonData[option]:
            raise ValueError(f'No {key} in jsonData[{option}]')
        
        data = self.jsonData[option][key]

        return data

    def getPictureData(self, key):
        data = self.getData('pictures', key=key)
        w = data['width']
        h = data['height']
        p = data['path']

        img = Image.open(p)

        return (w, h, img)
    
    def getRessourceData(self, key):
        data = self.getData('ressource', key=key)
        v = data['value']
        sx = data['position']['x']
        sy = data['position']['y']
        return (v, sx, sy) 







# def start():

#     all = list(filter(os.path.isdir, os.listdir()))

#     rm = ['.', 'lib']

#     directorys = [x for x in all if not any(substring in x for substring in rm)]


#     for directory in directorys:


#         ressource_section = {
#             "money" : {
#                 "value" : 0, 
#                 "position" : {
#                     "x" : 0,
#                     "y" : 0
#                 }
#             },
            
#         }
#         config = {}
#         playset = [{'name' : "",
#                     'arg1' : "",
#                     'arg2' : "",
#                     'argN' : "",
#                     }]

#         pictures_section = {}

#         for imge in os.listdir(directory):
#             if any(el in imge for el in ["png", "PNG"]):

#                 img = Image.open(f"{directory}/{imge}")
#                 img_dat = JsonHandler.create_imageData(os.path.splitext(imge)[0], img, f"{directory}/{imge}")
#                 # pictures_section[os.path.splitext(imge)[0]] = {'width' : w, 'height' : h, 'path': f'{directory}/{imge}'}
#                 pictures_section[img_dat[0]] = img_dat[1]

#         full_data = {'config': config, 'ressource' : ressource_section, 'playset' : playset, 'pictures' : pictures_section}

#         file_path = os.path.join(directory, "config.json")


#         with open(file_path, 'w') as f:
#             json.dump(full_data, f, indent=2)