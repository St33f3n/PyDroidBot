# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(847, 874)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(-1, -1, 850, 841))
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.play_tab = QtWidgets.QWidget()
        self.play_tab.setObjectName("play_tab")
        self.loadGameButton = QtWidgets.QPushButton(self.play_tab)
        self.loadGameButton.setGeometry(QtCore.QRect(30, 40, 141, 41))
        self.loadGameButton.setObjectName("loadGameButton")
        self.killButton = QtWidgets.QPushButton(self.play_tab)
        self.killButton.setEnabled(False)
        self.killButton.setGeometry(QtCore.QRect(180, 190, 141, 41))
        self.killButton.setObjectName("killButton")
        self.start_stopButton = QtWidgets.QPushButton(self.play_tab)
        self.start_stopButton.setEnabled(False)
        self.start_stopButton.setGeometry(QtCore.QRect(30, 190, 141, 41))
        self.start_stopButton.setAcceptDrops(False)
        self.start_stopButton.setCheckable(True)
        self.start_stopButton.setObjectName("start_stopButton")
        self.tabWidget.addTab(self.play_tab, "")
        self.create_tab = QtWidgets.QWidget()
        self.create_tab.setObjectName("create_tab")
        self.takePictureButton = QtWidgets.QPushButton(self.create_tab)
        self.takePictureButton.setEnabled(False)
        self.takePictureButton.setGeometry(QtCore.QRect(30, 90, 141, 41))
        self.takePictureButton.setObjectName("takePictureButton")
        self.selectGameButton = QtWidgets.QPushButton(self.create_tab)
        self.selectGameButton.setGeometry(QtCore.QRect(30, 20, 141, 41))
        self.selectGameButton.setObjectName("selectGameButton")
        self.createSaveButton = QtWidgets.QPushButton(self.create_tab)
        self.createSaveButton.setEnabled(False)
        self.createSaveButton.setGeometry(QtCore.QRect(540, 90, 141, 41))
        self.createSaveButton.setObjectName("createSaveButton")
        self.pictureWidget_2 = QtWidgets.QLabel(self.create_tab)
        self.pictureWidget_2.setEnabled(True)
        self.pictureWidget_2.setGeometry(QtCore.QRect(40, 180, 582, 582))
        self.pictureWidget_2.setText("")
        self.pictureWidget_2.setObjectName("pictureWidget_2")
        self.fileNameTextBox = QtWidgets.QLineEdit(self.create_tab)
        self.fileNameTextBox.setGeometry(QtCore.QRect(190, 90, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.fileNameTextBox.setFont(font)
        self.fileNameTextBox.setAutoFillBackground(False)
        self.fileNameTextBox.setObjectName("fileNameTextBox")
        self.selectFrameSizeButton = QtWidgets.QPushButton(self.create_tab)
        self.selectFrameSizeButton.setGeometry(QtCore.QRect(300, 20, 141, 41))
        self.selectFrameSizeButton.setObjectName("selectFrameSizeButton")
        self.tabWidget.addTab(self.create_tab, "")
        self.gameplay_tab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gameplay_tab.sizePolicy().hasHeightForWidth())
        self.gameplay_tab.setSizePolicy(sizePolicy)
        self.gameplay_tab.setObjectName("gameplay_tab")
        self.openDirButton = QtWidgets.QPushButton(self.gameplay_tab)
        self.openDirButton.setGeometry(QtCore.QRect(600, 618, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.openDirButton.setFont(font)
        self.openDirButton.setObjectName("openDirButton")
        self.pictureWidget = QtWidgets.QListWidget(self.gameplay_tab)
        self.pictureWidget.setGeometry(QtCore.QRect(590, 20, 231, 501))
        self.pictureWidget.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.pictureWidget.setObjectName("pictureWidget")
        self.saveButton = QtWidgets.QPushButton(self.gameplay_tab)
        self.saveButton.setEnabled(False)
        self.saveButton.setGeometry(QtCore.QRect(370, 618, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.saveButton.setFont(font)
        self.saveButton.setObjectName("saveButton")
        self.textlist = QtWidgets.QListWidget(self.gameplay_tab)
        self.textlist.setGeometry(QtCore.QRect(10, 70, 271, 711))
        self.textlist.setDragEnabled(False)
        self.textlist.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.textlist.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.textlist.setObjectName("textlist")
        self.functionWidget = QtWidgets.QListWidget(self.gameplay_tab)
        self.functionWidget.setGeometry(QtCore.QRect(350, 20, 231, 501))
        self.functionWidget.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.functionWidget.setObjectName("functionWidget")
        self.keyValueButton = QtWidgets.QPushButton(self.gameplay_tab)
        self.keyValueButton.setGeometry(QtCore.QRect(370, 540, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.keyValueButton.setFont(font)
        self.keyValueButton.setObjectName("keyValueButton")
        self.valueTextBox = QtWidgets.QLineEdit(self.gameplay_tab)
        self.valueTextBox.setGeometry(QtCore.QRect(600, 540, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.valueTextBox.setFont(font)
        self.valueTextBox.setAutoFillBackground(False)
        self.valueTextBox.setObjectName("valueTextBox")
        self.comboBox = QtWidgets.QComboBox(self.gameplay_tab)
        self.comboBox.setGeometry(QtCore.QRect(10, 20, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.newSaveTextBox = QtWidgets.QLineEdit(self.gameplay_tab)
        self.newSaveTextBox.setEnabled(True)
        self.newSaveTextBox.setGeometry(QtCore.QRect(370, 690, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.newSaveTextBox.setFont(font)
        self.newSaveTextBox.setAutoFillBackground(False)
        self.newSaveTextBox.setText("")
        self.newSaveTextBox.setClearButtonEnabled(False)
        self.newSaveTextBox.setObjectName("newSaveTextBox")
        self.trash = QtWidgets.QListWidget(self.gameplay_tab)
        self.trash.setGeometry(QtCore.QRect(300, 70, 31, 711))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.trash.setFont(font)
        self.trash.setAutoScroll(False)
        self.trash.setAutoScrollMargin(0)
        self.trash.setDragDropMode(QtWidgets.QAbstractItemView.DropOnly)
        self.trash.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.trash.setObjectName("trash")
        self.trash.raise_()
        self.openDirButton.raise_()
        self.pictureWidget.raise_()
        self.saveButton.raise_()
        self.textlist.raise_()
        self.functionWidget.raise_()
        self.keyValueButton.raise_()
        self.valueTextBox.raise_()
        self.comboBox.raise_()
        self.newSaveTextBox.raise_()
        self.tabWidget.addTab(self.gameplay_tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 847, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setTearOffEnabled(False)
        self.menuSettings.setSeparatorsCollapsible(False)
        self.menuSettings.setToolTipsVisible(False)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.menuFile.addAction(self.actionOpen)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.actionOpen.triggered.connect(MainWindow.openDir) # type: ignore
        self.createSaveButton.clicked.connect(MainWindow.createSave) # type: ignore
        self.openDirButton.clicked.connect(MainWindow.openDir) # type: ignore
        self.saveButton.clicked.connect(MainWindow.save) # type: ignore
        self.start_stopButton.clicked.connect(MainWindow.start_stop) # type: ignore
        self.takePictureButton.clicked.connect(MainWindow.takePicture) # type: ignore
        self.selectGameButton.clicked.connect(MainWindow.selectGame) # type: ignore
        self.loadGameButton.clicked.connect(MainWindow.loadGame) # type: ignore
        self.killButton.clicked.connect(MainWindow.kill) # type: ignore
        self.selectFrameSizeButton.clicked.connect(MainWindow.selectFrameSize) # type: ignore
        self.comboBox.currentIndexChanged['int'].connect(MainWindow.handleComboBoxSelection) # type: ignore
        self.keyValueButton.clicked.connect(MainWindow.keyPress) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Visual Automation Bot"))
        self.loadGameButton.setText(_translate("MainWindow", "Load Game"))
        self.killButton.setText(_translate("MainWindow", "KILL"))
        self.start_stopButton.setText(_translate("MainWindow", "Start"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.play_tab), _translate("MainWindow", "Play"))
        self.takePictureButton.setText(_translate("MainWindow", "Take Picture"))
        self.selectGameButton.setText(_translate("MainWindow", "Select Game"))
        self.createSaveButton.setText(_translate("MainWindow", "Save"))
        self.fileNameTextBox.setPlaceholderText(_translate("MainWindow", "Picture Name"))
        self.selectFrameSizeButton.setText(_translate("MainWindow", "Select Window"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.create_tab), _translate("MainWindow", "Create"))
        self.openDirButton.setText(_translate("MainWindow", "Open Folder"))
        self.saveButton.setText(_translate("MainWindow", "Save"))
        self.keyValueButton.setText(_translate("MainWindow", "Add Value"))
        self.valueTextBox.setPlaceholderText(_translate("MainWindow", "Value or Name"))
        self.newSaveTextBox.setPlaceholderText(_translate("MainWindow", "Savename"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.gameplay_tab), _translate("MainWindow", "Gameplay"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
