# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/grossmj/PycharmProjects/gns3-gui/gns3/modules/docker/ui/docker_vm_configuration_page.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dockerVMConfigPageWidget(object):
    def setupUi(self, dockerVMConfigPageWidget):
        dockerVMConfigPageWidget.setObjectName("dockerVMConfigPageWidget")
        dockerVMConfigPageWidget.resize(938, 872)
        self.verticalLayout = QtWidgets.QVBoxLayout(dockerVMConfigPageWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.uiTabWidget = QtWidgets.QTabWidget(dockerVMConfigPageWidget)
        self.uiTabWidget.setObjectName("uiTabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.uiNameLabel = QtWidgets.QLabel(self.tab)
        self.uiNameLabel.setObjectName("uiNameLabel")
        self.gridLayout.addWidget(self.uiNameLabel, 0, 0, 1, 1)
        self.uiNameLineEdit = QtWidgets.QLineEdit(self.tab)
        self.uiNameLineEdit.setObjectName("uiNameLineEdit")
        self.gridLayout.addWidget(self.uiNameLineEdit, 0, 1, 1, 1)
        self.uiDefaultNameFormatLabel = QtWidgets.QLabel(self.tab)
        self.uiDefaultNameFormatLabel.setObjectName("uiDefaultNameFormatLabel")
        self.gridLayout.addWidget(self.uiDefaultNameFormatLabel, 1, 0, 1, 1)
        self.uiDefaultNameFormatLineEdit = QtWidgets.QLineEdit(self.tab)
        self.uiDefaultNameFormatLineEdit.setObjectName("uiDefaultNameFormatLineEdit")
        self.gridLayout.addWidget(self.uiDefaultNameFormatLineEdit, 1, 1, 1, 1)
        self.uiCategoryLabel = QtWidgets.QLabel(self.tab)
        self.uiCategoryLabel.setObjectName("uiCategoryLabel")
        self.gridLayout.addWidget(self.uiCategoryLabel, 2, 0, 1, 1)
        self.uiCategoryComboBox = QtWidgets.QComboBox(self.tab)
        self.uiCategoryComboBox.setObjectName("uiCategoryComboBox")
        self.gridLayout.addWidget(self.uiCategoryComboBox, 2, 1, 1, 1)
        self.uiSymbolLabel = QtWidgets.QLabel(self.tab)
        self.uiSymbolLabel.setObjectName("uiSymbolLabel")
        self.gridLayout.addWidget(self.uiSymbolLabel, 3, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.uiSymbolLineEdit = QtWidgets.QLineEdit(self.tab)
        self.uiSymbolLineEdit.setObjectName("uiSymbolLineEdit")
        self.horizontalLayout_7.addWidget(self.uiSymbolLineEdit)
        self.uiSymbolToolButton = QtWidgets.QToolButton(self.tab)
        self.uiSymbolToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiSymbolToolButton.setObjectName("uiSymbolToolButton")
        self.horizontalLayout_7.addWidget(self.uiSymbolToolButton)
        self.gridLayout.addLayout(self.horizontalLayout_7, 3, 1, 1, 1)
        self.uiCMDLabel = QtWidgets.QLabel(self.tab)
        self.uiCMDLabel.setObjectName("uiCMDLabel")
        self.gridLayout.addWidget(self.uiCMDLabel, 4, 0, 1, 1)
        self.uiCMDLineEdit = QtWidgets.QLineEdit(self.tab)
        self.uiCMDLineEdit.setObjectName("uiCMDLineEdit")
        self.gridLayout.addWidget(self.uiCMDLineEdit, 4, 1, 1, 1)
        self.uiAdapterLabel = QtWidgets.QLabel(self.tab)
        self.uiAdapterLabel.setObjectName("uiAdapterLabel")
        self.gridLayout.addWidget(self.uiAdapterLabel, 5, 0, 1, 1)
        self.uiAdapterSpinBox = QtWidgets.QSpinBox(self.tab)
        self.uiAdapterSpinBox.setMinimum(1)
        self.uiAdapterSpinBox.setObjectName("uiAdapterSpinBox")
        self.gridLayout.addWidget(self.uiAdapterSpinBox, 5, 1, 1, 1)
        self.uiCustomAdaptersLabel = QtWidgets.QLabel(self.tab)
        self.uiCustomAdaptersLabel.setObjectName("uiCustomAdaptersLabel")
        self.gridLayout.addWidget(self.uiCustomAdaptersLabel, 6, 0, 1, 1)
        self.uiCustomAdaptersConfigurationPushButton = QtWidgets.QPushButton(self.tab)
        self.uiCustomAdaptersConfigurationPushButton.setObjectName("uiCustomAdaptersConfigurationPushButton")
        self.gridLayout.addWidget(self.uiCustomAdaptersConfigurationPushButton, 6, 1, 1, 1)
        self.uiConsoleTypeLabel = QtWidgets.QLabel(self.tab)
        self.uiConsoleTypeLabel.setObjectName("uiConsoleTypeLabel")
        self.gridLayout.addWidget(self.uiConsoleTypeLabel, 7, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.uiConsoleTypeComboBox = QtWidgets.QComboBox(self.tab)
        self.uiConsoleTypeComboBox.setObjectName("uiConsoleTypeComboBox")
        self.uiConsoleTypeComboBox.addItem("")
        self.uiConsoleTypeComboBox.addItem("")
        self.uiConsoleTypeComboBox.addItem("")
        self.uiConsoleTypeComboBox.addItem("")
        self.uiConsoleTypeComboBox.addItem("")
        self.horizontalLayout.addWidget(self.uiConsoleTypeComboBox)
        self.uiConsoleAutoStartCheckBox = QtWidgets.QCheckBox(self.tab)
        self.uiConsoleAutoStartCheckBox.setObjectName("uiConsoleAutoStartCheckBox")
        self.horizontalLayout.addWidget(self.uiConsoleAutoStartCheckBox)
        self.gridLayout.addLayout(self.horizontalLayout, 7, 1, 1, 1)
        self.uiConsoleResolutionLabel = QtWidgets.QLabel(self.tab)
        self.uiConsoleResolutionLabel.setObjectName("uiConsoleResolutionLabel")
        self.gridLayout.addWidget(self.uiConsoleResolutionLabel, 8, 0, 1, 1)
        self.uiConsoleResolutionComboBox = QtWidgets.QComboBox(self.tab)
        self.uiConsoleResolutionComboBox.setObjectName("uiConsoleResolutionComboBox")
        self.uiConsoleResolutionComboBox.addItem("")
        self.uiConsoleResolutionComboBox.addItem("")
        self.uiConsoleResolutionComboBox.addItem("")
        self.uiConsoleResolutionComboBox.addItem("")
        self.uiConsoleResolutionComboBox.addItem("")
        self.uiConsoleResolutionComboBox.addItem("")
        self.uiConsoleResolutionComboBox.addItem("")
        self.gridLayout.addWidget(self.uiConsoleResolutionComboBox, 8, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 9, 0, 1, 1)
        self.uiConsoleHttpPortSpinBox = QtWidgets.QSpinBox(self.tab)
        self.uiConsoleHttpPortSpinBox.setMinimum(1)
        self.uiConsoleHttpPortSpinBox.setMaximum(65535)
        self.uiConsoleHttpPortSpinBox.setObjectName("uiConsoleHttpPortSpinBox")
        self.gridLayout.addWidget(self.uiConsoleHttpPortSpinBox, 9, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 10, 0, 1, 1)
        self.uiHttpConsolePathLineEdit = QtWidgets.QLineEdit(self.tab)
        self.uiHttpConsolePathLineEdit.setObjectName("uiHttpConsolePathLineEdit")
        self.gridLayout.addWidget(self.uiHttpConsolePathLineEdit, 10, 1, 1, 1)
        self.uiEnvironmentLabel = QtWidgets.QLabel(self.tab)
        self.uiEnvironmentLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.uiEnvironmentLabel.setWordWrap(False)
        self.uiEnvironmentLabel.setObjectName("uiEnvironmentLabel")
        self.gridLayout.addWidget(self.uiEnvironmentLabel, 11, 0, 1, 1)
        self.uiEnvironmentTextEdit = QtWidgets.QTextEdit(self.tab)
        self.uiEnvironmentTextEdit.setObjectName("uiEnvironmentTextEdit")
        self.gridLayout.addWidget(self.uiEnvironmentTextEdit, 11, 1, 1, 1)
        self.uiNetworkConfigLabel = QtWidgets.QLabel(self.tab)
        self.uiNetworkConfigLabel.setObjectName("uiNetworkConfigLabel")
        self.gridLayout.addWidget(self.uiNetworkConfigLabel, 12, 0, 1, 1)
        self.uiNetworkConfigEditButton = QtWidgets.QPushButton(self.tab)
        self.uiNetworkConfigEditButton.setObjectName("uiNetworkConfigEditButton")
        self.gridLayout.addWidget(self.uiNetworkConfigEditButton, 12, 1, 1, 1)
        self.uiTabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.uiExtraHostsLabel = QtWidgets.QLabel(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiExtraHostsLabel.sizePolicy().hasHeightForWidth())
        self.uiExtraHostsLabel.setSizePolicy(sizePolicy)
        self.uiExtraHostsLabel.setWordWrap(True)
        self.uiExtraHostsLabel.setObjectName("uiExtraHostsLabel")
        self.gridLayout_2.addWidget(self.uiExtraHostsLabel, 0, 0, 1, 1)
        self.uiExtraHostsTextEdit = QtWidgets.QPlainTextEdit(self.tab_2)
        self.uiExtraHostsTextEdit.setObjectName("uiExtraHostsTextEdit")
        self.gridLayout_2.addWidget(self.uiExtraHostsTextEdit, 0, 1, 1, 1)
        self.uiExtraVolumeLabel = QtWidgets.QLabel(self.tab_2)
        self.uiExtraVolumeLabel.setObjectName("uiExtraVolumeLabel")
        self.gridLayout_2.addWidget(self.uiExtraVolumeLabel, 1, 0, 1, 1)
        self.uiExtraVolumeTextEdit = QtWidgets.QPlainTextEdit(self.tab_2)
        self.uiExtraVolumeTextEdit.setPlainText("")
        self.uiExtraVolumeTextEdit.setObjectName("uiExtraVolumeTextEdit")
        self.gridLayout_2.addWidget(self.uiExtraVolumeTextEdit, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 388, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 2, 1, 1, 1)
        self.uiTabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.uiUsageTextEdit = QtWidgets.QPlainTextEdit(self.tab_3)
        self.uiUsageTextEdit.setObjectName("uiUsageTextEdit")
        self.verticalLayout_2.addWidget(self.uiUsageTextEdit)
        self.uiTabWidget.addTab(self.tab_3, "")
        self.verticalLayout.addWidget(self.uiTabWidget)

        self.retranslateUi(dockerVMConfigPageWidget)
        self.uiTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(dockerVMConfigPageWidget)

    def retranslateUi(self, dockerVMConfigPageWidget):
        _translate = QtCore.QCoreApplication.translate
        dockerVMConfigPageWidget.setWindowTitle(_translate("dockerVMConfigPageWidget", "Docker container template configuration"))
        self.uiNameLabel.setText(_translate("dockerVMConfigPageWidget", "Name:"))
        self.uiDefaultNameFormatLabel.setText(_translate("dockerVMConfigPageWidget", "Default name format"))
        self.uiCategoryLabel.setText(_translate("dockerVMConfigPageWidget", "Category"))
        self.uiSymbolLabel.setText(_translate("dockerVMConfigPageWidget", "Symbol:"))
        self.uiSymbolToolButton.setText(_translate("dockerVMConfigPageWidget", "&Browse..."))
        self.uiCMDLabel.setText(_translate("dockerVMConfigPageWidget", "Start command:"))
        self.uiAdapterLabel.setText(_translate("dockerVMConfigPageWidget", "Adapters:"))
        self.uiCustomAdaptersLabel.setText(_translate("dockerVMConfigPageWidget", "Custom adapters:"))
        self.uiCustomAdaptersConfigurationPushButton.setText(_translate("dockerVMConfigPageWidget", "&Configure custom adapters"))
        self.uiConsoleTypeLabel.setText(_translate("dockerVMConfigPageWidget", "Console type:"))
        self.uiConsoleTypeComboBox.setItemText(0, _translate("dockerVMConfigPageWidget", "telnet"))
        self.uiConsoleTypeComboBox.setItemText(1, _translate("dockerVMConfigPageWidget", "vnc"))
        self.uiConsoleTypeComboBox.setItemText(2, _translate("dockerVMConfigPageWidget", "http"))
        self.uiConsoleTypeComboBox.setItemText(3, _translate("dockerVMConfigPageWidget", "https"))
        self.uiConsoleTypeComboBox.setItemText(4, _translate("dockerVMConfigPageWidget", "none"))
        self.uiConsoleAutoStartCheckBox.setText(_translate("dockerVMConfigPageWidget", "Auto start console"))
        self.uiConsoleResolutionLabel.setText(_translate("dockerVMConfigPageWidget", "VNC console resolution:"))
        self.uiConsoleResolutionComboBox.setItemText(0, _translate("dockerVMConfigPageWidget", "1920x1080"))
        self.uiConsoleResolutionComboBox.setItemText(1, _translate("dockerVMConfigPageWidget", "1366x768"))
        self.uiConsoleResolutionComboBox.setItemText(2, _translate("dockerVMConfigPageWidget", "1280x1024"))
        self.uiConsoleResolutionComboBox.setItemText(3, _translate("dockerVMConfigPageWidget", "1280x800"))
        self.uiConsoleResolutionComboBox.setItemText(4, _translate("dockerVMConfigPageWidget", "1024x768"))
        self.uiConsoleResolutionComboBox.setItemText(5, _translate("dockerVMConfigPageWidget", "800x600"))
        self.uiConsoleResolutionComboBox.setItemText(6, _translate("dockerVMConfigPageWidget", "640x480"))
        self.label.setText(_translate("dockerVMConfigPageWidget", "HTTP port in the container:"))
        self.label_2.setText(_translate("dockerVMConfigPageWidget", "HTTP path:"))
        self.uiEnvironmentLabel.setText(_translate("dockerVMConfigPageWidget", "Environment variables:\n"
"(KEY=VALUE, one per line)"))
        self.uiNetworkConfigLabel.setText(_translate("dockerVMConfigPageWidget", "Network configuration"))
        self.uiNetworkConfigEditButton.setText(_translate("dockerVMConfigPageWidget", "Edit"))
        self.uiTabWidget.setTabText(self.uiTabWidget.indexOf(self.tab), _translate("dockerVMConfigPageWidget", "General settings"))
        self.uiExtraHostsLabel.setText(_translate("dockerVMConfigPageWidget", "Extra hosts added\n"
"to the /etc/hosts file.\n"
"(hostname:IP\n"
"one per line)"))
        self.uiExtraHostsTextEdit.setPlaceholderText(_translate("dockerVMConfigPageWidget", "e.g. router:192.168.0.1"))
        self.uiExtraVolumeLabel.setText(_translate("dockerVMConfigPageWidget", "Additional directories to\n"
"make persistent that are\n"
"not included in the image\n"
"VOLUMES config. One\n"
"directory per line."))
        self.uiExtraVolumeTextEdit.setPlaceholderText(_translate("dockerVMConfigPageWidget", "e.g. /etc/sysctl.d"))
        self.uiTabWidget.setTabText(self.uiTabWidget.indexOf(self.tab_2), _translate("dockerVMConfigPageWidget", "Advanced"))
        self.uiTabWidget.setTabText(self.uiTabWidget.indexOf(self.tab_3), _translate("dockerVMConfigPageWidget", "Usage"))

