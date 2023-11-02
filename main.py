from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys

class MainUI(QWidget):
    def __init__(self):
        super(MainUI, self).__init__()
        self.ui = uic.loadUi('MyGUI.ui')
        self.text = None
        self.length = 0
        self.k = None

        self.ui.pushButton.clicked.connect(self.get_content)

    def get_content(self):
        self.text = self.ui.lineEdit.text().split()
        self.length = len(self.text)
        self.k = self.ui.lineEdit_2.text()
        self.handle()

    def handle(self):
        table = self.ui.tableWidget

        table.setRowCount(int(self.k) + 1)
        table.setColumnCount(self.length)

        time, vis = {}, {}
        phyblock = []
        cnt = 0
        for col in range(self.length):
            x = self.text[col]
            if x in vis and vis[x] == '1':
                pass
            else:
                cnt += 1
                vis[x] = '1'

                if len(phyblock) == int(self.k):
                    mi = self.length + 5
                    ind = 0
                    for row in range(len(phyblock)):
                        if int(time[phyblock[row]]) < mi:
                            mi = int(time[phyblock[row]])
                            ind = row
                    vis[phyblock[ind]] = '0'
                    phyblock[ind] = x
                else:
                    phyblock.append(x)
                    
                condition = QTableWidgetItem("X")
                table.setItem(int(self.k), col, condition)

            for row in range(len(phyblock)):
                item = QTableWidgetItem(phyblock[row])
                table.setItem(row, col, item)
            time[x] = col # 更新时间

        table.setHorizontalHeaderLabels(self.text) 
        table.resizeColumnsToContents()
        table.resizeRowsToContents()

        self.ui.lineEdit_3.setText(str(cnt))

app = QApplication(sys.argv)

mainUI = MainUI()
mainUI.ui.show()

sys.exit(app.exec_())