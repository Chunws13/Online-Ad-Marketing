# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AB_Test.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
from Data import Data_sorting
from Sub_view import sub_window

class Ui_MainWindow(object):

    def __init__(self):
        data = pd.read_excel("./2021_메리츠TM_데이터라벨링.xlsx", sheet_name='raw', skiprows=1)
        self.product_list = data.loc[:, "보종"].unique()
        self.device_list = data.loc[:, "기기"].unique()
        self.lptype_list = data.loc[:, "LP유형"].unique()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(730, 544)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # 이미지 영역
        self.bo_label = QtWidgets.QLabel(self.centralwidget)
        self.bo_label.setGeometry(QtCore.QRect(410, 11, 291, 41))
        self.pixmap = QtGui.QPixmap("./LP/logo.png")
        self.bo_label.setPixmap(self.pixmap)
        self.bo_label.setScaledContents(True)
        self.bo_label.setObjectName("bo_label")

        # 조회하기
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(320, 40, 75, 22))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText('조회')

        # 라벨 목록 - 사용하지 않음
        self.font_label = QtWidgets.QLabel(self.centralwidget)
        self.font_label.setGeometry(QtCore.QRect(30, 80, 80, 15))
        self.font_label.setText('# 폰트')
        self.font_label.setObjectName("font_label")

        self.font_color_label = QtWidgets.QLabel(self.centralwidget)
        self.font_color_label.setGeometry(QtCore.QRect(170, 80, 80, 15))
        self.font_color_label.setText('# 폰트 컬러')
        self.font_color_label.setObjectName("font_color_label")

        self.background_color_label = QtWidgets.QLabel(self.centralwidget)
        self.background_color_label.setGeometry(QtCore.QRect(310, 80, 80, 15))
        self.background_color_label.setText('# 배경 컬러')
        self.background_color_label.setObjectName("background_color_label")

        self.point_color_label = QtWidgets.QLabel(self.centralwidget)
        self.point_color_label.setGeometry(QtCore.QRect(450, 80, 80, 15))
        self.point_color_label.setText('# 포인트 컬러')
        self.point_color_label.setObjectName("point_color_label")

        self.image_label = QtWidgets.QLabel(self.centralwidget)
        self.image_label.setGeometry(QtCore.QRect(580, 80, 80, 15))
        self.image_label.setText('# 이미지')
        self.image_label.setObjectName("image_label")

        self.layout_label = QtWidgets.QLabel(self.centralwidget)
        self.layout_label.setGeometry(QtCore.QRect(30, 290, 80, 15))
        self.layout_label.setText('# 레이아웃')
        self.layout_label.setObjectName("layout_label")

        self.item_label = QtWidgets.QLabel(self.centralwidget)
        self.item_label.setGeometry(QtCore.QRect(170, 290, 80, 15))
        self.item_label.setText('# 아이템')
        self.item_label.setObjectName("item_label")

        self.expression_label = QtWidgets.QLabel(self.centralwidget)
        self.expression_label.setGeometry(QtCore.QRect(310, 290, 80, 15))
        self.expression_label.setText('# 화법')
        self.expression_label.setObjectName("expression_label")

        self.content_label = QtWidgets.QLabel(self.centralwidget)
        self.content_label.setGeometry(QtCore.QRect(450, 290, 80, 15))
        self.content_label.setText('# 담보')
        self.content_label.setObjectName("content_label")

        # 필터 목록
        self.product_select = QtWidgets.QComboBox(self.centralwidget)
        self.product_select.setGeometry(QtCore.QRect(20, 10, 90, 22))
        self.product_select.setObjectName("product_select")
        self.product_select.addItems(self.product_list)

        self.device_select = QtWidgets.QComboBox(self.centralwidget)
        self.device_select.setGeometry(QtCore.QRect(125, 10, 75, 22))
        self.device_select.setObjectName("device_select")
        self.device_select.addItems(self.device_list)

        self.lp_select = QtWidgets.QComboBox(self.centralwidget)
        self.lp_select.setGeometry(QtCore.QRect(215, 10, 75, 22))
        self.lp_select.setObjectName("lp_select")
        self.lp_select.addItems(self.lptype_list)

        # 서브 뷰 조회
        self.sub_view = QtWidgets.QPushButton(self.centralwidget)
        self.sub_view.setGeometry(QtCore.QRect(20, 40, 270, 22))
        self.sub_view.setObjectName("sub_view")
        self.sub_view.setText('Win 목록조회')

        # 테이블 목록
        self.font_table = QtWidgets.QTableWidget(self.centralwidget)
        self.font_table.setGeometry(QtCore.QRect(20, 100, 130, 180))
        self.font_table.setObjectName("font_table")

        self.font_color_table = QtWidgets.QTableWidget(self.centralwidget)
        self.font_color_table.setGeometry(QtCore.QRect(160, 100, 130, 180))
        self.font_color_table.setObjectName("font_color_table")

        self.background_color_table = QtWidgets.QTableWidget(self.centralwidget)
        self.background_color_table.setGeometry(QtCore.QRect(300, 100, 130, 180))
        self.background_color_table.setObjectName("background_color_table")

        self.point_color_table = QtWidgets.QTableWidget(self.centralwidget)
        self.point_color_table.setGeometry(QtCore.QRect(440, 100, 130, 180))
        self.point_color_table.setObjectName("point_color_table")

        self.image_table = QtWidgets.QTableWidget(self.centralwidget)
        self.image_table.setGeometry(QtCore.QRect(580, 100, 130, 180))
        self.image_table.setObjectName("image_table")

        self.layout_table = QtWidgets.QTableWidget(self.centralwidget)
        self.layout_table.setGeometry(QtCore.QRect(20, 310, 130, 180))
        self.layout_table.setObjectName("layout_table")

        self.item_table = QtWidgets.QTableWidget(self.centralwidget)
        self.item_table.setGeometry(QtCore.QRect(160, 310, 130, 180))
        self.item_table.setObjectName("item_table")

        self.expression_table = QtWidgets.QTableWidget(self.centralwidget)
        self.expression_table.setGeometry(QtCore.QRect(300, 310, 130, 180))
        self.expression_table.setObjectName("expression_table")

        self.content_table = QtWidgets.QTableWidget(self.centralwidget)
        self.content_table.setGeometry(QtCore.QRect(440, 310, 271, 180))
        self.content_table.setObjectName("content_table")

        # 메인윈도우 설정
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 730, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 클릭 이벤트
        self.pushButton.clicked.connect(self.font_event)
        self.pushButton.clicked.connect(self.font_color_event)
        self.pushButton.clicked.connect(self.background_color_event)
        self.pushButton.clicked.connect(self.point_color_event)
        self.pushButton.clicked.connect(self.image_event)
        self.pushButton.clicked.connect(self.layout_event)
        self.pushButton.clicked.connect(self.item_event)
        self.pushButton.clicked.connect(self.expression_event)
        self.pushButton.clicked.connect(self.content_event)
        self.sub_view.clicked.connect(self.show_sub_window)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    # 서브 뷰 구현
    def show_sub_window(self):
        self.sub_window = QtWidgets.QMainWindow()
        self.ui = sub_window(self.product_select.currentText(), self.device_select.currentText(), self.lp_select.currentText())
        self.ui.setupUi(self.sub_window)
        self.sub_window.show()

    # 클릭시 이벤트 모음
    def font_event(self):
        data = Data_sorting(self.product_select.currentText(), self.device_select.currentText(), self.lp_select.currentText()).font_list()
        self.font_table.setRowCount(len(data.index))
        self.font_table.setColumnCount(len(data.columns))
        self.font_table.setHorizontalHeaderLabels(list(data.columns))

        for i in range(len(data)):
            for j in enumerate(data.iloc[i]) :
                self.font_table.setItem(i, j[0], QtWidgets.QTableWidgetItem(str(j[1])))

        self.font_table.resizeColumnsToContents()
        self.font_table.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

    def font_color_event(self):
        data = Data_sorting(self.product_select.currentText(), self.device_select.currentText(), self.lp_select.currentText()).font_color_list()
        self.font_color_table.setRowCount(len(data.index))
        self.font_color_table.setColumnCount(len(data.columns))
        self.font_color_table.setHorizontalHeaderLabels(list(data.columns))

        for i in range(len(data)):
            for j in enumerate(data.iloc[i]):
                self.font_color_table.setItem(i, j[0], QtWidgets.QTableWidgetItem(str(j[1])))

        self.font_color_table.resizeColumnsToContents()
        self.font_color_table.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

    def background_color_event(self):
        data = Data_sorting(self.product_select.currentText(), self.device_select.currentText(), self.lp_select.currentText()).background_color_list()
        self.background_color_table.setRowCount(len(data.index))
        self.background_color_table.setColumnCount(len(data.columns))
        self.background_color_table.setHorizontalHeaderLabels(list(data.columns))

        for i in range(len(data)):
            for j in enumerate(data.iloc[i]):
                self.background_color_table.setItem(i, j[0], QtWidgets.QTableWidgetItem(str(j[1])))

        self.background_color_table.resizeColumnsToContents()
        self.background_color_table.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

    def point_color_event(self):
        data = Data_sorting(self.product_select.currentText(), self.device_select.currentText(), self.lp_select.currentText()).point_color_list()
        self.point_color_table.setRowCount(len(data.index))
        self.point_color_table.setColumnCount(len(data.columns))
        self.point_color_table.setHorizontalHeaderLabels(list(data.columns))

        for i in range(len(data)):
            for j in enumerate(data.iloc[i]):
                self.point_color_table.setItem(i, j[0], QtWidgets.QTableWidgetItem(str(j[1])))

        self.point_color_table.resizeColumnsToContents()
        self.point_color_table.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

    def image_event(self):
        data = Data_sorting(self.product_select.currentText(), self.device_select.currentText(), self.lp_select.currentText()).image_list()
        self.image_table.setRowCount(len(data.index))
        self.image_table.setColumnCount(len(data.columns))
        self.image_table.setHorizontalHeaderLabels(list(data.columns))

        for i in range(len(data)):
            for j in enumerate(data.iloc[i]):
                self.image_table.setItem(i, j[0], QtWidgets.QTableWidgetItem(str(j[1])))

        self.image_table.resizeColumnsToContents()
        self.image_table.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

    def layout_event(self):
        data = Data_sorting(self.product_select.currentText(), self.device_select.currentText(), self.lp_select.currentText()).layout_list()
        self.layout_table.setRowCount(len(data.index))
        self.layout_table.setColumnCount(len(data.columns))
        self.layout_table.setHorizontalHeaderLabels(list(data.columns))

        for i in range(len(data)):
            for j in enumerate(data.iloc[i]):
                self.layout_table.setItem(i, j[0], QtWidgets.QTableWidgetItem(str(j[1])))

        self.layout_table.resizeColumnsToContents()
        self.layout_table.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

    def item_event(self):
        data = Data_sorting(self.product_select.currentText(), self.device_select.currentText(), self.lp_select.currentText()).item_list()
        self.item_table.setRowCount(len(data.index))
        self.item_table.setColumnCount(len(data.columns))
        self.item_table.setHorizontalHeaderLabels(list(data.columns))

        for i in range(len(data)):
            for j in enumerate(data.iloc[i]):
                self.item_table.setItem(i, j[0], QtWidgets.QTableWidgetItem(str(j[1])))

        self.item_table.resizeColumnsToContents()
        self.item_table.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

    def expression_event(self):
        data = Data_sorting(self.product_select.currentText(), self.device_select.currentText(), self.lp_select.currentText()).expression_list()
        self.expression_table.setRowCount(len(data.index))
        self.expression_table.setColumnCount(len(data.columns))
        self.expression_table.setHorizontalHeaderLabels(list(data.columns))

        for i in range(len(data)):
            for j in enumerate(data.iloc[i]):
                self.expression_table.setItem(i, j[0], QtWidgets.QTableWidgetItem(str(j[1])))

        self.expression_table.resizeColumnsToContents()
        self.expression_table.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

    def content_event(self):
        data = Data_sorting(self.product_select.currentText(), self.device_select.currentText(), self.lp_select.currentText()).content_list()
        self.content_table.setRowCount(len(data.index))
        self.content_table.setColumnCount(len(data.columns))
        self.content_table.setHorizontalHeaderLabels(list(data.columns))

        for i in range(len(data)):
            for j in enumerate(data.iloc[i]):
                self.content_table.setItem(i, j[0], QtWidgets.QTableWidgetItem(str(j[1])))

        self.content_table.resizeColumnsToContents()
        self.content_table.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())