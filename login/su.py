# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(380, 173)
        self.layoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_2.setGeometry(QtCore.QRect(190, 130, 158, 25))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_8.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_8.addWidget(self.pushButton_4)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 30, 294, 82))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_5.setMinimumSize(QtCore.QSize(180, 0))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_6.addWidget(self.lineEdit_5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_6.setMinimumSize(QtCore.QSize(180, 0))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_7.addWidget(self.lineEdit_6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_9.addWidget(self.label_7)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem2)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_7.setMinimumSize(QtCore.QSize(180, 0))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_9.addWidget(self.lineEdit_7)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Crear cuenta"))
        self.pushButton_3.setText(_translate("Dialog", "Entrar"))
        self.pushButton_4.setText(_translate("Dialog", "Crear cuenta"))
        self.label_5.setText(_translate("Dialog", "Usuario"))
        self.label_6.setText(_translate("Dialog", "Contraseña"))
        self.label_7.setText(_translate("Dialog", "Repetir contraseña"))
