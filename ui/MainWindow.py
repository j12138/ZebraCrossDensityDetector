# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1123, 751)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 470, 641, 201))
        self.groupBox_3.setObjectName("groupBox_3")
        self.statusBrowser = QtWidgets.QTextBrowser(self.groupBox_3)
        self.statusBrowser.setGeometry(QtCore.QRect(-5, 21, 651, 181))
        self.statusBrowser.setObjectName("statusBrowser")
        self.startSetting = QtWidgets.QGroupBox(self.centralwidget)
        self.startSetting.setGeometry(QtCore.QRect(640, 0, 481, 371))
        self.startSetting.setObjectName("startSetting")
        self.detectButton = QtWidgets.QPushButton(self.startSetting)
        self.detectButton.setGeometry(QtCore.QRect(260, 340, 93, 28))
        self.detectButton.setObjectName("detectButton")
        self.resetButton = QtWidgets.QPushButton(self.startSetting)
        self.resetButton.setGeometry(QtCore.QRect(370, 340, 93, 28))
        self.resetButton.setObjectName("resetButton")
        self.label = QtWidgets.QLabel(self.startSetting)
        self.label.setGeometry(QtCore.QRect(30, 60, 72, 15))
        self.label.setObjectName("label")
        self.chooseModelCombo = QtWidgets.QComboBox(self.startSetting)
        self.chooseModelCombo.setGeometry(QtCore.QRect(250, 60, 141, 22))
        self.chooseModelCombo.setObjectName("chooseModelCombo")
        self.label_2 = QtWidgets.QLabel(self.startSetting)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 111, 16))
        self.label_2.setObjectName("label_2")
        self.chooseZebraCombo = QtWidgets.QComboBox(self.startSetting)
        self.chooseZebraCombo.setGeometry(QtCore.QRect(250, 100, 141, 22))
        self.chooseZebraCombo.setObjectName("chooseZebraCombo")
        self.videoOptions = QtWidgets.QGroupBox(self.startSetting)
        self.videoOptions.setGeometry(QtCore.QRect(20, 140, 441, 61))
        self.videoOptions.setObjectName("videoOptions")
        self.label_3 = QtWidgets.QLabel(self.videoOptions)
        self.label_3.setGeometry(QtCore.QRect(70, 30, 111, 16))
        self.label_3.setObjectName("label_3")
        self.chooseVideoType = QtWidgets.QComboBox(self.videoOptions)
        self.chooseVideoType.setGeometry(QtCore.QRect(230, 30, 141, 22))
        self.chooseVideoType.setObjectName("chooseVideoType")
        self.imageOptions = QtWidgets.QGroupBox(self.startSetting)
        self.imageOptions.setGeometry(QtCore.QRect(20, 210, 441, 131))
        self.imageOptions.setObjectName("imageOptions")
        self.singleImageCheckbox = QtWidgets.QCheckBox(self.imageOptions)
        self.singleImageCheckbox.setGeometry(QtCore.QRect(50, 20, 91, 19))
        self.singleImageCheckbox.setObjectName("singleImageCheckbox")
        self.imageDirCheckbox = QtWidgets.QCheckBox(self.imageOptions)
        self.imageDirCheckbox.setGeometry(QtCore.QRect(50, 60, 141, 19))
        self.imageDirCheckbox.setObjectName("imageDirCheckbox")
        self.chooseImageBtn = QtWidgets.QPushButton(self.imageOptions)
        self.chooseImageBtn.setGeometry(QtCore.QRect(270, 10, 93, 28))
        self.chooseImageBtn.setObjectName("chooseImageBtn")
        self.imagePathLineEdit = QtWidgets.QLineEdit(self.imageOptions)
        self.imagePathLineEdit.setGeometry(QtCore.QRect(200, 100, 231, 21))
        self.imagePathLineEdit.setObjectName("imagePathLineEdit")
        self.label_4 = QtWidgets.QLabel(self.imageOptions)
        self.label_4.setGeometry(QtCore.QRect(50, 100, 101, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.startSetting)
        self.label_5.setGeometry(QtCore.QRect(30, 30, 72, 15))
        self.label_5.setObjectName("label_5")
        self.timeLabel = QtWidgets.QLabel(self.startSetting)
        self.timeLabel.setGeometry(QtCore.QRect(240, 30, 171, 16))
        self.timeLabel.setObjectName("timeLabel")
        self.resultArea = QtWidgets.QGroupBox(self.centralwidget)
        self.resultArea.setGeometry(QtCore.QRect(640, 370, 481, 301))
        self.resultArea.setObjectName("resultArea")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(0, 0, 641, 461))
        self.groupBox_4.setObjectName("groupBox_4")
        self.graphicsView = QtWidgets.QGraphicsView(self.groupBox_4)
        self.graphicsView.setGeometry(QtCore.QRect(0, 20, 641, 441))
        self.graphicsView.setObjectName("graphicsView")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(0, 670, 1121, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1123, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_choose_mode = QtWidgets.QMenu(self.menu)
        self.menu_choose_mode.setObjectName("menu_choose_mode")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actiondensity_setting = QtWidgets.QAction(MainWindow)
        self.actiondensity_setting.setObjectName("actiondensity_setting")
        self.actionglobal_setting = QtWidgets.QAction(MainWindow)
        self.actionglobal_setting.setObjectName("actionglobal_setting")
        self.actionweight_setting = QtWidgets.QAction(MainWindow)
        self.actionweight_setting.setObjectName("actionweight_setting")
        self.actionabout = QtWidgets.QAction(MainWindow)
        self.actionabout.setObjectName("actionabout")
        self.action_image_mode = QtWidgets.QAction(MainWindow)
        self.action_image_mode.setCheckable(True)
        self.action_image_mode.setChecked(True)
        self.action_image_mode.setObjectName("action_image_mode")
        self.action_video_mode = QtWidgets.QAction(MainWindow)
        self.action_video_mode.setCheckable(True)
        self.action_video_mode.setObjectName("action_video_mode")
        self.actioncommon_setting = QtWidgets.QAction(MainWindow)
        self.actioncommon_setting.setObjectName("actioncommon_setting")
        self.actionuse_camera_as_input = QtWidgets.QAction(MainWindow)
        self.actionuse_camera_as_input.setObjectName("actionuse_camera_as_input")
        self.actionuse_video_file_as_input = QtWidgets.QAction(MainWindow)
        self.actionuse_video_file_as_input.setObjectName("actionuse_video_file_as_input")
        self.actionauto_prepare = QtWidgets.QAction(MainWindow)
        self.actionauto_prepare.setObjectName("actionauto_prepare")
        self.menu_choose_mode.addAction(self.action_image_mode)
        self.menu_choose_mode.addAction(self.action_video_mode)
        self.menu.addAction(self.menu_choose_mode.menuAction())
        self.menu_2.addAction(self.actioncommon_setting)
        self.menu_3.addAction(self.actionabout)
        self.menu_4.addAction(self.actionauto_prepare)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_3.setTitle(_translate("MainWindow", "状态显示区域"))
        self.startSetting.setTitle(_translate("MainWindow", "启动设置"))
        self.detectButton.setText(_translate("MainWindow", "开始检测"))
        self.resetButton.setText(_translate("MainWindow", "重置"))
        self.label.setText(_translate("MainWindow", "选择模型"))
        self.label_2.setText(_translate("MainWindow", "选择斑马线种类"))
        self.videoOptions.setTitle(_translate("MainWindow", "视频选项"))
        self.label_3.setText(_translate("MainWindow", "选择视频类型"))
        self.imageOptions.setTitle(_translate("MainWindow", "图片选项"))
        self.singleImageCheckbox.setText(_translate("MainWindow", "单张图片"))
        self.imageDirCheckbox.setText(_translate("MainWindow", "多张图片的目录"))
        self.chooseImageBtn.setText(_translate("MainWindow", "选择图片"))
        self.label_4.setText(_translate("MainWindow", "文件或者目录"))
        self.label_5.setText(_translate("MainWindow", "当前时间"))
        self.timeLabel.setText(_translate("MainWindow", "TextLabel"))
        self.resultArea.setTitle(_translate("MainWindow", "结果显示区域"))
        self.groupBox_4.setTitle(_translate("MainWindow", "图片视频显示区域"))
        self.menu.setTitle(_translate("MainWindow", "模式选择"))
        self.menu_choose_mode.setTitle(_translate("MainWindow", "choose_mode"))
        self.menu_2.setTitle(_translate("MainWindow", "参数设置"))
        self.menu_3.setTitle(_translate("MainWindow", "关于"))
        self.menu_4.setTitle(_translate("MainWindow", "快速部署"))
        self.actiondensity_setting.setText(_translate("MainWindow", "density setting"))
        self.actionglobal_setting.setText(_translate("MainWindow", "global setting"))
        self.actionweight_setting.setText(_translate("MainWindow", "weight setting"))
        self.actionabout.setText(_translate("MainWindow", "about"))
        self.action_image_mode.setText(_translate("MainWindow", "image_mode"))
        self.action_video_mode.setText(_translate("MainWindow", "video_mode"))
        self.actioncommon_setting.setText(_translate("MainWindow", "common setting"))
        self.actionuse_camera_as_input.setText(_translate("MainWindow", "use camera as input"))
        self.actionuse_video_file_as_input.setText(_translate("MainWindow", "use video file as input"))
        self.actionauto_prepare.setText(_translate("MainWindow", "auto prepare"))


