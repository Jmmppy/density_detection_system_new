# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'u1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1288, 803)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setStyleSheet("QMainWindow{\n"
"}\n"
"QGroupBox{\n"
"background-color:#EDF1F4;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 0, 1391, 831))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setStyleSheet("")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 90, 601, 703))
        self.groupBox_3.setStyleSheet("QGroupBox{\n"
"background-color:white;\n"
"}")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.CamLabel = QtWidgets.QLabel(self.groupBox_3)
        self.CamLabel.setGeometry(QtCore.QRect(20, 70, 561, 581))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CamLabel.sizePolicy().hasHeightForWidth())
        self.CamLabel.setSizePolicy(sizePolicy)
        self.CamLabel.setObjectName("CamLabel")
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_7.setGeometry(QtCore.QRect(620, 90, 421, 401))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy)
        self.groupBox_7.setStyleSheet("QGroupBox{\n"
"background-color:white;\n"
"}")
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.pic_0 = QtWidgets.QLabel(self.groupBox_7)
        self.pic_0.setGeometry(QtCore.QRect(20, 10, 381, 381))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pic_0.sizePolicy().hasHeightForWidth())
        self.pic_0.setSizePolicy(sizePolicy)
        self.pic_0.setObjectName("pic_0")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_4.setGeometry(QtCore.QRect(620, 500, 421, 291))
        font = QtGui.QFont()
        font.setFamily("Clarendon BT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setAutoFillBackground(False)
        self.groupBox_4.setStyleSheet("QTableWidget{\n"
"font-weight:500;\n"
"color:#19232D;\n"
"border:none;\n"
"}")
        self.groupBox_4.setObjectName("groupBox_4")
        self.table = QtWidgets.QTableWidget(self.groupBox_4)
        self.table.setGeometry(QtCore.QRect(0, 30, 421, 271))
        self.table.setLineWidth(4)
        self.table.setAutoScrollMargin(20)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table.setRowCount(4)
        self.table.setColumnCount(1)
        self.table.setObjectName("table")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        item.setBackground(QtGui.QColor(208, 213, 232))
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        item.setFont(font)
        item.setBackground(QtGui.QColor(233, 236, 245))
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        item.setFont(font)
        item.setBackground(QtGui.QColor(208, 213, 232))
        self.table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        item.setFont(font)
        item.setBackground(QtGui.QColor(233, 236, 245))
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.table.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        item.setFont(font)
        item.setBackground(QtGui.QColor(68, 113, 198))
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(208, 213, 232))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(8, 13, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(233, 236, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(8, 13, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.table.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(208, 213, 232))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(8, 13, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.table.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(233, 236, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(8, 13, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.table.setItem(3, 0, item)
        self.table.horizontalHeader().setCascadingSectionResizes(True)
        self.table.horizontalHeader().setDefaultSectionSize(327)
        self.table.verticalHeader().setDefaultSectionSize(59)
        self.table.verticalHeader().setMinimumSectionSize(26)
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_6.setGeometry(QtCore.QRect(1050, 0, 241, 821))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setStyleSheet("QGroupBox{\n"
"    background:#2D3D4D;\n"
"    color:white;\n"
"}\n"
"QLabel{\n"
"    color:white\n"
"}\n"
"QPushButton{\n"
"    background:#4471C6;\n"
"    color:white;\n"
"}\n"
"QRadioButton{\n"
"    color:white;\n"
"}")
        self.groupBox_6.setObjectName("groupBox_6")
        self.btn_open = QtWidgets.QPushButton(self.groupBox_6)
        self.btn_open.setGeometry(QtCore.QRect(20, 90, 201, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_open.sizePolicy().hasHeightForWidth())
        self.btn_open.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_open.setFont(font)
        self.btn_open.setAutoFillBackground(False)
        self.btn_open.setStyleSheet("QPushButton{\n"
"}")
        self.btn_open.setObjectName("btn_open")
        self.btn_light = QtWidgets.QPushButton(self.groupBox_6)
        self.btn_light.setGeometry(QtCore.QRect(20, 330, 201, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_light.sizePolicy().hasHeightForWidth())
        self.btn_light.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_light.setFont(font)
        self.btn_light.setStyleSheet("")
        self.btn_light.setObjectName("btn_light")
        self.btn_close = QtWidgets.QPushButton(self.groupBox_6)
        self.btn_close.setGeometry(QtCore.QRect(20, 150, 200, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_close.setFont(font)
        self.btn_close.setStyleSheet("")
        self.btn_close.setObjectName("btn_close")
        self.btn_open_2 = QtWidgets.QPushButton(self.groupBox_6)
        self.btn_open_2.setGeometry(QtCore.QRect(20, 420, 200, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_open_2.sizePolicy().hasHeightForWidth())
        self.btn_open_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_open_2.setFont(font)
        self.btn_open_2.setStyleSheet("")
        self.btn_open_2.setObjectName("btn_open_2")
        self.btn_open_3 = QtWidgets.QPushButton(self.groupBox_6)
        self.btn_open_3.setGeometry(QtCore.QRect(20, 470, 200, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_open_3.sizePolicy().hasHeightForWidth())
        self.btn_open_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_open_3.setFont(font)
        self.btn_open_3.setStyleSheet("")
        self.btn_open_3.setObjectName("btn_open_3")
        self.btn_open_4 = QtWidgets.QPushButton(self.groupBox_6)
        self.btn_open_4.setGeometry(QtCore.QRect(20, 560, 200, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_open_4.sizePolicy().hasHeightForWidth())
        self.btn_open_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_open_4.setFont(font)
        self.btn_open_4.setStyleSheet("")
        self.btn_open_4.setObjectName("btn_open_4")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_6)
        self.comboBox.setGeometry(QtCore.QRect(20, 30, 200, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.btn_open_5 = QtWidgets.QPushButton(self.groupBox_6)
        self.btn_open_5.setGeometry(QtCore.QRect(20, 610, 200, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_open_5.sizePolicy().hasHeightForWidth())
        self.btn_open_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_open_5.setFont(font)
        self.btn_open_5.setStyleSheet("")
        self.btn_open_5.setObjectName("btn_open_5")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton.setGeometry(QtCore.QRect(20, 660, 200, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.groupBox_6)
        self.label.setGeometry(QtCore.QRect(20, 390, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_6)
        self.label_2.setGeometry(QtCore.QRect(20, 530, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
"    color???white;\n"
"}")
        self.label_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_2.setObjectName("label_2")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 210, 201, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton.setGeometry(QtCore.QRect(20, 30, 89, 16))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 60, 89, 16))
        self.radioButton_2.setObjectName("radioButton_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 740, 200, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(70, 10, 871, 71))
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "?????????"))
        self.CamLabel.setText(_translate("MainWindow", "???????????????"))
        self.pic_0.setText(_translate("MainWindow", "???????????????"))
        self.groupBox_4.setTitle(_translate("MainWindow", "????????????"))
        item = self.table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "????????????"))
        item = self.table.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "???????????????"))
        item = self.table.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "????????????"))
        item = self.table.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "????????????"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "??????"))
        __sortingEnabled = self.table.isSortingEnabled()
        self.table.setSortingEnabled(False)
        self.table.setSortingEnabled(__sortingEnabled)
        self.groupBox_6.setTitle(_translate("MainWindow", "????????????"))
        self.btn_open.setText(_translate("MainWindow", "????????????"))
        self.btn_light.setText(_translate("MainWindow", "????????????"))
        self.btn_close.setText(_translate("MainWindow", "????????????"))
        self.btn_open_2.setText(_translate("MainWindow", "????????????"))
        self.btn_open_3.setText(_translate("MainWindow", "????????????"))
        self.btn_open_4.setText(_translate("MainWindow", "????????????"))
        self.comboBox.setItemText(0, _translate("MainWindow", "????????????"))
        self.comboBox.setItemText(1, _translate("MainWindow", "?????????"))
        self.btn_open_5.setText(_translate("MainWindow", "????????????"))
        self.pushButton.setText(_translate("MainWindow", "???????????????"))
        self.label.setText(_translate("MainWindow", "???????????????"))
        self.label_2.setText(_translate("MainWindow", "????????????"))
        self.groupBox_5.setTitle(_translate("MainWindow", "????????????"))
        self.radioButton.setText(_translate("MainWindow", "???"))
        self.radioButton_2.setText(_translate("MainWindow", "???"))
        self.pushButton_2.setText(_translate("MainWindow", "??????"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:26pt; font-weight:600;\">?????????????????????????????????????????????</span></p></body></html>"))
