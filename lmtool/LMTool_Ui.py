# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LMTool_Ui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1062, 767)
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabs = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(39)
        sizePolicy.setHeightForWidth(self.tabs.sizePolicy().hasHeightForWidth())
        self.tabs.setSizePolicy(sizePolicy)
        self.tabs.setAutoFillBackground(False)
        self.tabs.setObjectName("tabs")
        self.imageTab = GraphicsLayoutWidget()
        self.imageTab.setObjectName("imageTab")
        self.tabs.addTab(self.imageTab, "")
        self.profilePlot = PlotWidget()
        self.profilePlot.setObjectName("profilePlot")
        self.tabs.addTab(self.profilePlot, "")
        self.fitTab = GraphicsLayoutWidget()
        self.fitTab.setObjectName("fitTab")
        self.tabs.addTab(self.fitTab, "")
        self.verticalLayout.addWidget(self.tabs)
        self.parameterFrame = QtWidgets.QFrame(self.centralwidget)
        self.parameterFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.parameterFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.parameterFrame.setObjectName("parameterFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.parameterFrame)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName("gridLayout")
        self.a_p = QParameterWidget(self.parameterFrame)
        self.a_p.setFrameShape(QtWidgets.QFrame.Panel)
        self.a_p.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.a_p.setObjectName("a_p")
        self.gridLayout.addWidget(self.a_p, 1, 0, 1, 1)
        self.k_p = QParameterWidget(self.parameterFrame)
        self.k_p.setFrameShape(QtWidgets.QFrame.Panel)
        self.k_p.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.k_p.setObjectName("k_p")
        self.gridLayout.addWidget(self.k_p, 1, 2, 1, 1)
        self.magnification = QParameterWidget(self.parameterFrame)
        self.magnification.setFrameShape(QtWidgets.QFrame.Panel)
        self.magnification.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.magnification.setObjectName("magnification")
        self.gridLayout.addWidget(self.magnification, 0, 1, 1, 1)
        self.n_m = QParameterWidget(self.parameterFrame)
        self.n_m.setFrameShape(QtWidgets.QFrame.Panel)
        self.n_m.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.n_m.setObjectName("n_m")
        self.gridLayout.addWidget(self.n_m, 0, 2, 1, 1)
        self.n_p = QParameterWidget(self.parameterFrame)
        self.n_p.setFrameShape(QtWidgets.QFrame.Panel)
        self.n_p.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.n_p.setObjectName("n_p")
        self.gridLayout.addWidget(self.n_p, 1, 1, 1, 1)
        self.z_p = QParameterWidget(self.parameterFrame)
        self.z_p.setFrameShape(QtWidgets.QFrame.Panel)
        self.z_p.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.z_p.setObjectName("z_p")
        self.gridLayout.addWidget(self.z_p, 2, 2, 1, 1)
        self.y_p = QParameterWidget(self.parameterFrame)
        self.y_p.setFrameShape(QtWidgets.QFrame.Panel)
        self.y_p.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.y_p.setObjectName("y_p")
        self.gridLayout.addWidget(self.y_p, 2, 1, 1, 1)
        self.x_p = QParameterWidget(self.parameterFrame)
        self.x_p.setFrameShape(QtWidgets.QFrame.Panel)
        self.x_p.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.x_p.setObjectName("x_p")
        self.gridLayout.addWidget(self.x_p, 2, 0, 1, 1)
        self.wavelength = QParameterWidget(self.parameterFrame)
        self.wavelength.setFrameShape(QtWidgets.QFrame.Panel)
        self.wavelength.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.wavelength.setObjectName("wavelength")
        self.gridLayout.addWidget(self.wavelength, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.parameterFrame)
        self.optimizerFrame = QtWidgets.QFrame(self.centralwidget)
        self.optimizerFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.optimizerFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.optimizerFrame.setObjectName("optimizerFrame")
        self.optimizerLayout = QtWidgets.QHBoxLayout(self.optimizerFrame)
        self.optimizerLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.optimizerLayout.setContentsMargins(0, 0, 0, 0)
        self.optimizerLayout.setSpacing(5)
        self.optimizerLayout.setObjectName("optimizerLayout")
        self.bbox = QParameterWidget(self.optimizerFrame)
        self.bbox.setFrameShape(QtWidgets.QFrame.Panel)
        self.bbox.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.bbox.setObjectName("bbox")
        self.optimizerLayout.addWidget(self.bbox)
        self.optimizeButton = QtWidgets.QPushButton(self.optimizerFrame)
        self.optimizeButton.setMinimumSize(QtCore.QSize(0, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.optimizeButton.setFont(font)
        self.optimizeButton.setWhatsThis("")
        self.optimizeButton.setObjectName("optimizeButton")
        self.optimizerLayout.addWidget(self.optimizeButton)
        self.methodLayout = QtWidgets.QVBoxLayout()
        self.methodLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.methodLayout.setObjectName("methodLayout")
        self.LMButton = QtWidgets.QRadioButton(self.optimizerFrame)
        self.LMButton.setObjectName("LMButton")
        self.methodLayout.addWidget(self.LMButton)
        self.NMButton = QtWidgets.QRadioButton(self.optimizerFrame)
        self.NMButton.setObjectName("NMButton")
        self.methodLayout.addWidget(self.NMButton)
        self.optimizerLayout.addLayout(self.methodLayout)
        self.verticalLayout.addWidget(self.optimizerFrame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1062, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave_Parameters = QtWidgets.QAction(MainWindow)
        self.actionSave_Parameters.setObjectName("actionSave_Parameters")
        self.actionSave_Parameters_As = QtWidgets.QAction(MainWindow)
        self.actionSave_Parameters_As.setObjectName("actionSave_Parameters_As")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave_Parameters)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabs.setCurrentIndex(0)
        self.actionQuit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LMTool"))
        self.tabs.setTabText(self.tabs.indexOf(self.imageTab), _translate("MainWindow", "image"))
        self.tabs.setTabText(self.tabs.indexOf(self.profilePlot), _translate("MainWindow", "profile"))
        self.tabs.setTabText(self.tabs.indexOf(self.fitTab), _translate("MainWindow", "fit"))
        self.a_p.setStatusTip(_translate("MainWindow", "Radius of particle [micrometers]"))
        self.k_p.setStatusTip(_translate("MainWindow", "Absorption coefficient of particle"))
        self.magnification.setStatusTip(_translate("MainWindow", "Magnification [micrometers/pixel]"))
        self.n_m.setStatusTip(_translate("MainWindow", "Refractive index of medium"))
        self.n_p.setStatusTip(_translate("MainWindow", "Refractive index of particle"))
        self.z_p.setStatusTip(_translate("MainWindow", "Axial position of particle [pixel]"))
        self.y_p.setStatusTip(_translate("MainWindow", "y coordinate [pixel]"))
        self.x_p.setStatusTip(_translate("MainWindow", "x coordinate [pixel]"))
        self.wavelength.setStatusTip(_translate("MainWindow", "Wavelength of illumination [micrometers]"))
        self.bbox.setStatusTip(_translate("MainWindow", "Bounding box height"))
        self.optimizeButton.setStatusTip(_translate("MainWindow", "Optimize parameters"))
        self.optimizeButton.setText(_translate("MainWindow", "Optimize"))
        self.LMButton.setStatusTip(_translate("MainWindow", "Use Levenberg-Marquardt optimization"))
        self.LMButton.setText(_translate("MainWindow", "Levenberg-Marquardt"))
        self.NMButton.setStatusTip(_translate("MainWindow", "Use Nelder-Mead --> Levenberg-Marquardt hybrid optimization"))
        self.NMButton.setText(_translate("MainWindow", "Amoeba -> Levenberg-Marquardt"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionOpen.setText(_translate("MainWindow", "Open ..."))
        self.actionSave_Parameters.setText(_translate("MainWindow", "Save Parameters ..."))
        self.actionSave_Parameters_As.setText(_translate("MainWindow", "Save Parameters As ..."))

from QParameterWidget import QParameterWidget
from pyqtgraph import GraphicsLayoutWidget, PlotWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

