from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog, QPushButton, QListWidgetItem
from PyQt5.QtCore import Qt, QMimeData, QObject
from PyQt5.QtGui import QDrag, QDragEnterEvent, QDropEvent, QPixmap, QIcon
import pyautogui
from app.hello import Ui_MainWindow  # Import Ui_MainWindow from the generated module
import sys, os
from lib.commander import Commander
from lib.gamer import Gamer
from lib.jsonHandler import JsonHandler, functions
from PIL import Image
import threading

# class DragHandler(QObject):
#     def __init__(self, widget):
#         super().__init__(widget)
#         self.widget = widget

#     def setupDraggableButton(self, button):
#         button.installEventFilter(self)

#     def eventFilter(self, obj, event):
#         if obj == self.widget.ddButton:
#             if event.type() == event.MouseButtonPress:
#                 self.drag_start_position = event.pos()
#             elif event.type() == event.MouseMove:
#                 if hasattr(self, 'drag_start_position') and (event.buttons() & Qt.LeftButton):
#                     drag = QDrag(self.widget.ddButton)
#                     mime_data = QMimeData()
#                     drag.setMimeData(mime_data)

#                     drag.setHotSpot(event.pos() - self.drag_start_position)

#                     drag.exec_(Qt.MoveAction)

#         return super().eventFilter(obj, event)
class App(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        self.setupUi(self)
        self.jHandler = None
        self.com = Commander()


        self.create_folder_name = None
        self.create_img = None
        self.windowSize = None
        self.screenSize = pyautogui.size()
        self.comboBoxselected_item = None
        self.thread_var = None
        self.newSaveTextBox.hide()

        # self.setAcceptDrops(True)

        # self.ddButton = QPushButton('Drag me', self)
        # self.ddButton.setGeometry(50, 50, 100, 50)

        # # Initialize DragHandler and set up drag for ddButton
        # self.dragHandler = DragHandler(self)
        # self.dragHandler.setupDraggableButton(self.ddButton)
    
    # def openConfig(self):
    #     if self.jHandler:
    #         item = sum(self.jHandler.getData('playset'), [])
    #         print(item)
    #         current_text = ""
    #         for i in item:
    #             current_text += i + "\n"
    #         self.textlist.setText(current_text)
    #         self.openConfigButton.setText("Config Loaded")
    #     else:
    #         self.openConfigButton.setText("No Config Found")


    def openDir(self):
        # Clear bevor new Folder
        self.comboBox.clear()
        self.functionWidget.clear()
        self.pictureWidget.clear()

        options = QFileDialog.Options()
        current_dir = QFileDialog.getExistingDirectory(self,"QFileDialog.getExistingDirectory()", "", options=options)
        if os.path.exists(current_dir + "/config.json") == True:
            folder_name = os.path.basename(current_dir)
            self.jHandler = JsonHandler(folder_name)

            self.openDirButton.setText(folder_name)

            # Drag and drop boxes
            pic = self.jHandler.getData('pictures').keys()
            self.pictureWidget.addItems(pic)
            # self.functionWidget.addItems(functions)


            for function, description in functions.items():
                item = QListWidgetItem(function)
                item.setToolTip(f"{function}: {description}")  # Set tooltip for each item
                self.functionWidget.addItem(item)
            

            actionset_keys = self.jHandler.getData('actionset').keys()
            self.functionWidget.addItems(["actionset : " + key for key in actionset_keys])

            # Init ComboBox

            dropDown = ["playset"]
            dropDown.extend(["actionset : " + key for key in actionset_keys])
            dropDown.append("Add new Actionset")

            self.comboBox.addItems(dropDown)

            self.saveButton.setEnabled(True)


    def save(self):
        arr = []
        temp = []

        for i in range(self.textlist.count()):
            item_text = self.textlist.item(i).text()
            if item_text in functions :
                if temp:
                    arr.append(temp)
                    temp = []
            if item_text.split(" : ")[0] == "actionset":
                item_text = item_text.split(" : ")[1]
            temp.append(item_text)
        
        if temp:
            arr.append(temp)

        for sublist in arr:
            # Check if the sublist has more than one element
            if len(sublist) > 1:
                # Add double quotes around each element except the first one
                for i in range(1, len(sublist)):
                    sublist[i] = f"\"{sublist[i]}\""


        if self.comboBoxselected_item == "playset":
            data = {'playset': arr}
            self.jHandler.add(data)
            self.jHandler.saveData()
            self.saveButton.setText("Saved")
            return


        if self.comboBoxselected_item == "Add new Actionset":
            key = self.newSaveTextBox.text()

            if key == "":
                self.saveButton.setText("Add Savename")
                return

            current_items = [self.comboBox.itemText(i) for i in range(self.comboBox.count())]
            current_items.insert(-1, "actionset : " + key)
            self.comboBox.clear()
            self.comboBox.addItems(current_items)

            self.newSaveTextBox.clear()
        else:
            aset, key = self.comboBoxselected_item.split(" : ")

        
        
        result = {key : arr}
        print(result)
        self.jHandler.add(result, "actionset",)
        self.jHandler.saveData()

        # Renew the functionWidget
        self.functionWidget.clear()
        self.functionWidget.addItems(functions)
        actionset_keys = self.jHandler.getData('actionset').keys()
        self.functionWidget.addItems(["actionset : " + key for key in actionset_keys])

        

    def handleComboBoxSelection(self, index):
        self.comboBoxselected_item = self.comboBox.itemText(index)
        self.newSaveTextBox.hide()

        self.textlist.clear()

        actionset_keys = self.jHandler.getData('actionset').keys()
        actionset_text = ["actionset : " + key for key in actionset_keys]
        if self.comboBoxselected_item == "playset":
            item = sum(self.jHandler.getData('playset'), [])
            for i in range(len(item)):
                if isinstance(item[i], str):
                    item[i] = item[i].replace('"', '')
            self.textlist.addItems(item)


        if self.comboBoxselected_item in actionset_text:
            key = self.comboBoxselected_item.split(" : ")[1]
            item = sum(self.jHandler.getData('actionset', key ), [])
            for i in range(len(item)):
                if isinstance(item[i], str):
                    item[i] = item[i].replace('"', '')
            self.textlist.addItems(item)

        if self.comboBoxselected_item == "Add new Actionset":
            self.newSaveTextBox.show()

    def keyPressEvent(self, event):
            if event.key() == Qt.Key_Delete:
                selected_items = self.textlist.selectedItems()
                if selected_items:
                    for item in selected_items:
                        self.textlist.takeItem(self.textlist.row(item))
                self.textlist.clearSelection()
            else:
                super().keyPressEvent(event)

    def mouseMoveEvent(self, event):
        item = self.functionWidget.itemAt(event.pos())
        if item:
            tooltip = f"Item: {item.text()}"
            self.functionWidget.setToolTip(tooltip)
        else:
            self.functionWidget.setToolTip("")

    # def dragEnterEvent(self, event):
    #     event.accept()
    
    # def dropEvent(self, event):
    #     position = event.pos()
    #     self.ddButton.move(position)
    #     event.accept()
    
    def add(self):
        selected_item = self.pictureWidget.currentItem()
        if selected_item is not None:
            current_text = self.textlist.text()
            self.textlist.setText(current_text + f"\"{selected_item.text()}\"\n")
        self.pictureWidget.clearSelection()
        self.pictureWidget.setCurrentItem(None)

    def deleteLast(self):
        current_text = self.textlist.text()
        lines = current_text.splitlines()
        resultText = '\n'.join(lines[:-1])
        self.textlist.setText(resultText + "\n")


    # All Gamer Button Functions 

    # def simpleClick(self):
    #     current_text = self.textlist.text()
    #     if self.xLabel.text() != "" and self.yLabel.text() != "":
    #         self.textlist.setText(current_text + f"simpleClick\n {self.xLabel.text()}\n {self.yLabel.text()}\n")
    #         self.xLabel.setText("")
    #         self.yLabel.setText("")

    # def clickOnPicture(self):
    #     current_text = self.textlist.text()
    #     self.textlist.setText(current_text + "clickOnPicture\n")

    # # Listen on Keypress and add 
    def keyPress(self):
        current_text = self.valueTextBox.text()
        if current_text != "":
            self.textlist.addItems([current_text])
            self.valueTextBox.setText("")

    # def clickIfPicture(self):
    #     current_text = self.textlist.text()
    #     self.textlist.setText(current_text + "clickIfPicture\n")

    # def locateRessource(self):
    #     current_text = self.textlist.text()
    #     self.textlist.setText(current_text + "locateRessource\n")
  

    # Play 

    def loadGame(self):
        options = QFileDialog.Options()
        current_dir = QFileDialog.getExistingDirectory(self,"QFileDialog.getExistingDirectory()", "", options=options)
        if os.path.exists(current_dir + "/config.json") == True:
            folder_name = os.path.basename(current_dir)

            self.loadGameButton.setText(folder_name)

            self.thread_var = threading.Thread(target=self.com.addGame, args=(folder_name,))
            self.thread_var.start()
            self.start_stopButton.setEnabled(True)
            self.killButton.setEnabled(True)
        

    def kill(self):
        pass

    def start_stop(self):
        if self.start_stopButton.isChecked():
            self.start_stopButton.setText("STOP") 
            self.start_stopButton.setStyleSheet("background-color : red")
            # Check if a previous thread is running and join it to ensure it's finished
            if self.game_loop_thread and self.game_loop_thread.is_alive():
                self.game_loop_thread.join()
            # Start a new thread for the game loop
            self.game_loop_thread = threading.Thread(target=self.start_game_loop, args=(self.com,))
            self.game_loop_thread.start()
        else:
            self.start_stopButton.setText("Start")
            self.start_stopButton.setStyleSheet("background-color : lightgrey")
            # Check if a previous thread is running and join it to ensure it's finished
            if self.game_loop_thread and self.game_loop_thread.is_alive():
                self.stop_game_loop(self.com)  # Stop the game loop
                self.game_loop_thread.join()

    # Create 
            
    def selectGame(self):
        options = QFileDialog.Options()
        current_dir = QFileDialog.getExistingDirectory(self,"QFileDialog.getExistingDirectory()", "", options=options)
        if os.path.exists(current_dir) == True:
            self.create_folder_name = os.path.basename(current_dir)
            self.selectGameButton.setText(self.create_folder_name)
            self.jHandler = JsonHandler(self.create_folder_name)

    def selectFrameSize(self):
        pos = Gamer.getCommandArea()
        self.windowSize = (pos["width"], pos["height"])

        self.selectFrameSizeButton.setText(f"{self.windowSize[0]} x {self.windowSize[1]}")
        self.takePictureButton.setEnabled(True)

    def takePicture(self):

        self.createSaveButton.setText("Save")

        pos = Gamer.getCommandArea()
        region = (pos["x"], pos["y"], pos["width"], pos["height"])
        self.create_img = pyautogui.screenshot(region=region)

        self.takePictureButton.setText("Take New Picture")

        # Needs to be save, QPixmap cant handel raw picture
        self.create_img.save("temp.png")

        self.pictureWidget_2.setPixmap(QPixmap("temp.png").scaled(580,580,True))
        os.remove("temp.png")

        self.createSaveButton.setEnabled(True)

    def createSave(self):
        try:
            if self.create_img != None :
                text = self.fileNameTextBox.text()
                if text.strip() != "":
                    # Save
                    path = f"{self.create_folder_name}/{text}"
                    self.create_img.save(f"{path}.png")
                    self.jHandler.saveNewPicture(text, self.create_img, path, self.windowSize, self.screenSize)

                    # Cleanup
                    self.create_img = None
                    self.pictureWidget_2.setPixmap(QPixmap())
                    self.fileNameTextBox.setText("")

                    # Responds
                    self.createSaveButton.setText("Successfully Saved")
                    self.createSaveButton.setEnabled(False)
                else:
                    self.createSaveButton.setText("Name!?!!!")
        except Exception as e:
            self.createSaveButton.setText("Error While Saving")
            print(e)
        

        




def main():
    app = QApplication(sys.argv)
    form = App()
    form.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
