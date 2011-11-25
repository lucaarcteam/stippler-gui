#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys, subprocess
from PyQt4 import QtGui
from PyQt4 import QtCore

#################################################################### 


class STIPPLERGUI(QtGui.QWidget):
  
    
    def __init__(self):
        super(STIPPLERGUI, self).__init__()

        self.initUI()
        
    def initUI(self):

        self.label1 = QtGui.QLabel('RUN STIPPLER_PS', self)
        self.label1.move(20, 20)

# input image
        self.button1 = QtGui.QPushButton('Select Input Image', self)
        self.button1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button1.move(20, 50)
        self.connect(self.button1, QtCore.SIGNAL('clicked()'), self.showDialog1)
        self.setFocus()

        self.label2 = QtGui.QLabel('input image:', self)
        self.label2.move(180, 54)

        self.text4 = QtGui.QLineEdit(self)
        self.text4.move(280, 50)
        self.text4.resize(540, 27)

# help button select image
	self.help_button1 = QtGui.QPushButton("", self)
	self.help_button1.setIcon(QtGui.QIcon('icons/info_icon.png'))
        self.help_button1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.help_button1.move(830, 45)
        self.connect(self.help_button1, QtCore.SIGNAL('clicked()'), self.on_help1_clicked)
        self.setFocus()

# output file
        self.button2 = QtGui.QPushButton('Save Output as File', self)
        self.button2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button2.move(20, 90)
        self.connect(self.button2, QtCore.SIGNAL('clicked()'), self.showDialog2)
        self.setFocus()

        self.label3 = QtGui.QLabel('output file:', self)
        self.label3.move(180, 94)

        self.text5 = QtGui.QLineEdit(self)
        self.text5.move(280, 90)
        self.text5.resize(540, 27)

# help button select output
	self.help_button2 = QtGui.QPushButton("", self)
	self.help_button2.setIcon(QtGui.QIcon('icons/info_icon.png'))
        self.help_button2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.help_button2.move(830, 85)
        self.connect(self.help_button2, QtCore.SIGNAL('clicked()'), self.on_help2_clicked)
        self.setFocus()

# number dots
        self.label11 = QtGui.QLabel('Select Dots Number:', self)
        self.label11.move(20, 144)

        self.text6 = QtGui.QLineEdit('5000', self)
        self.text6.move(180, 140)
        self.text6.resize(70, 27)

# help button select output
	self.help_button3 = QtGui.QPushButton("", self)
	self.help_button3.setIcon(QtGui.QIcon('icons/info_icon.png'))
        self.help_button3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.help_button3.move(260, 135)
        self.connect(self.help_button3, QtCore.SIGNAL('clicked()'), self.on_help3_clicked)
        self.setFocus()

#B/W
        self.cb1 = QtGui.QCheckBox('Black dots and White BackGround', self)
        self.cb1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cb1.move(330, 132)
        self.cb1.toggle()
        self.connect(self.cb1, QtCore.SIGNAL('stateChanged(int)'), self.changeenv1)

        self.cb2 = QtGui.QCheckBox('White dots and Black BackGround', self)
        self.cb2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cb2.move(330, 162)
        self.cb2.toggle()
	self.cb2.setChecked(False)
        self.connect(self.cb2, QtCore.SIGNAL('stateChanged(int)'), self.changeenv2)

# start button
        self.button4 = QtGui.QPushButton('Run', self)
	self.button4.setIcon(QtGui.QIcon('icons/python_icon.png'))
        self.button4.move(20, 200)
	self.button4.setEnabled(True)

        self.text2 = QtGui.QLineEdit(self)
	self.text2.move(120, 204)
	self.text2.setReadOnly(False)
        self.text2.resize(700, 27)

	self.connect(self.text4, QtCore.SIGNAL('textChanged(QString)'), self.onChangedinput)     
	self.connect(self.text5, QtCore.SIGNAL('textChanged(QString)'), self.onChangedoutput)      
	self.connect(self.text6, QtCore.SIGNAL('textChanged(QString)'), self.onChangedot)            

	self.processLog1 = QtCore.QProcess() 
        QtCore.QObject.connect(self.button4, QtCore.SIGNAL("clicked()"), self.startstippler) 

# help button select output
	self.help_button4 = QtGui.QPushButton("", self)
	self.help_button4.setIcon(QtGui.QIcon('icons/info_icon.png'))
        self.help_button4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.help_button4.move(830, 200)
        self.connect(self.help_button4, QtCore.SIGNAL('clicked()'), self.on_help4_clicked)
        self.setFocus()


####################################################################    
        self.setWindowTitle('Stippler GUI v 0.1')
        self.setGeometry(300, 300, 890, 260)
	self.setWindowIcon(QtGui.QIcon('icons/stippler-gui_icon48.png'))
####################################################################  
   
    def showDialog1(self):
	directoryname = QtGui.QFileDialog.getOpenFileName(self, 'Select input image', '/home')
        self.text4.setText(directoryname)

    def showDialog2(self):
	directoryname = QtGui.QFileDialog.getSaveFileName(self, 'Save output file', '/home')
        self.text5.setText(directoryname)

    def onChangedinput(self, text):
        if self.cb1.isChecked(): self.text2.setText("env REVERSE_VIDEO=x stippler_ps " + self.text4.displayText() + " " + self.text6.displayText() + " > " +  self.text5.displayText())
        if self.cb2.isChecked(): self.text2.setText("stippler_ps " + self.text4.displayText() + " " + self.text6.displayText() + " > " +  self.text5.displayText())

    def onChangedoutput(self, text):
        if self.cb1.isChecked(): self.text2.setText("env REVERSE_VIDEO=x stippler_ps " + self.text4.displayText() + " " + self.text6.displayText() + " > " +  self.text5.displayText())
        if self.cb2.isChecked(): self.text2.setText("stippler_ps " + self.text4.displayText() + " " + self.text6.displayText() + " > " +  self.text5.displayText())

    def onChangedot(self, text):
        if self.cb1.isChecked(): self.text2.setText("env REVERSE_VIDEO=x stippler_ps " + self.text4.displayText() + " " + self.text6.displayText() + " > " +  self.text5.displayText())
        if self.cb2.isChecked(): self.text2.setText("stippler_ps " + self.text4.displayText() + " " + self.text6.displayText() + " > " +  self.text5.displayText())

    def changeenv1(self, value):      
        if self.cb1.isChecked():
            self.cb2.setChecked(False)
            self.text2.setText("env REVERSE_VIDEO=x stippler_ps " + self.text4.displayText() + " " + self.text6.displayText() + " > " +  self.text5.displayText())

    def changeenv2(self, text):      
        if self.cb2.isChecked():
            self.cb1.setChecked(False)
            self.text2.setText("stippler_ps " + self.text4.displayText() + " " + self.text6.displayText() + " > " +  self.text5.displayText())

    def startstippler(self):
	command = self.text2.displayText()
	self.proc = subprocess.Popen((str(command)), shell=True, stdout=subprocess.PIPE)

# help button 1 - select image
    def on_help1_clicked(self):
		QtGui.QMessageBox.information(self, "Help!", "Select the image file: a greyscale picture in .PGM format. \n\nIt generally must be smaller than the screen resolution.", QtGui.QMessageBox.Ok)

# help button 2 - select output
    def on_help2_clicked(self):
		QtGui.QMessageBox.information(self, "Help!", "Select the output file in .PS format.", QtGui.QMessageBox.Ok)

# help button 3 - select dot
    def on_help3_clicked(self):
		QtGui.QMessageBox.information(self, "Help!", "Select the number of dots to be used.\n\nDefault is 5000 dots", QtGui.QMessageBox.Ok)

# help button 4 - select dot
    def on_help4_clicked(self):
		QtGui.QMessageBox.information(self, "Help!", "Run stippler_ps. \n\nTo stop the process hit Control+c on the console.", QtGui.QMessageBox.Ok)

####################################################################                

if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    stip = STIPPLERGUI()
    stip.show()
    app.exec_()
