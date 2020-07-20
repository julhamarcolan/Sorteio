
from PyQt5 import QtCore, QtGui, QtWidgets
import random 

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.imagemFundo = QtWidgets.QLabel(self.centralwidget)
        self.imagemFundo.setGeometry(QtCore.QRect(20, 0, 611, 391))
        self.imagemFundo.setText("")
        self.imagemFundo.setPixmap(QtGui.QPixmap("../../../Downloads/Vermelho Nacional Hambúrguer Dia Mídia Social Post.png"))
        self.imagemFundo.setObjectName("imagemFundo")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 410, 121, 31))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.sortear)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SORTEIO DE LANCHE "))
        self.pushButton.setText(_translate("MainWindow", "SORTEAR"))

    def sortear(self): 
        #O sorteio será feito entre uma das @ 
        lista = ['@Srta_Wayne', '@tuitesdadebs', '@isyxxxx', '@sassalouca1', '@itispedro_', '@napaulac0', 
        '@sofia_fonsecao', '@wallyness007', '@astroaline', '@rafaelmgr94', '@memedomudkip', '@Caio_bob ', '@victormmonte',
        '@JFagner_', '@yolandamrcll', '@lactobahiro', '@nataliawho_', '@assimleo', '@tisranje', '@sergiowebx', '@IbraNoVasco',
        '@jaimealves', '@Ruteferro ', '@zikafrom802', '@YaponiraVox', '@ivegetal', '@fafabbiiiLove', '@lariblackfox', 
        '@mp_eduard', '@ea_sato', '@zerenatosa', '@flaizamor ', '@fisicozao', '@leandro842', '@almeidonis', '@encasquetada',
        '@Ehamans', '@CrisSpoltiL', '@vncstxr ', '@rafraella ', '@w3513y_f3rr31r4', '@bochagas']
        n = random.randint(0, 45)
        sorteado = lista[n]
        self.pushButton.setText(sorteado)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
