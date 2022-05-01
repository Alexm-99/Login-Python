import sys

from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QTableWidgetItem, QFileDialog, QMainWindow
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
from views.login_ui import Ui_Form
from data.db_sesion import Sesion
import hashlib
class Login(QDialog):
    
    def __init__(self):
        super().__init__()
        self.usuario = ''
        self.passwd = ''
        
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.sesion = Sesion()
        self.ui.pushButton.clicked.connect(self.ingreso)
        self.ui.lineEdit.setFocus()
        #self.ui.lineEdit.setCursor()
        self.ui.label.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.ui.label_2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    def cifradoPasswd(self, passwd):
        clave_cifrada = hashlib.sha512(passwd.encode())
        return clave_cifrada.hexdigest()

    def verificarDatos(self, usuario, passwd):
        clavecifrada = self.cifradoPasswd(passwd)
        #print(clavecifrada)
        self.valor = self.sesion.consulta(usuario, clavecifrada)
        print(self.valor)
        if self.valor is not None:
            return True
        else:
            return self.valor
    
    def ingreso(self):
        self.usuario = self.ui.lineEdit.text()
        self.passwd = self.ui.lineEdit_2.text()

        entrar= self.verificarDatos(self.usuario, self.passwd)
        if entrar == True:
            print('Bienvenido...')
        else:
            print('Datos Erroneos')



if __name__== '__main__':
    app = QApplication(sys.argv)
    ventana = Login()
    ventana.show()
    sys.exit(app.exec_())

