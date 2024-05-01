from PyQt5 import QtCore, QtGui, QtWidgets
import sys,res1
import subprocess
import menu

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1800, 1082)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 1920, 1080))  # Match the size of the window
        self.label.setStyleSheet("border-image: url(:/images/360_F_195508679_tMnsBg8hznqrvJNFPyZD7qFUyyzdc56M.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(800, 370, 280, 320))
        self.label_5.setStyleSheet("background-color:rgba(0, 0, 0, 100);\n"
"\n"
"border-radius:10px;\n"
"border: 0.5px solid white;")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(840, 590, 201, 51))
        self.pushButton.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border-radius:15px;")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/login_img-removebg-preview (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(400, 200))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(840, 510, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(255,255,255,255);\n"
"color:rgba(255,255,255,255);\n"
"padding-bottom:7px;\n"
"\n"
"")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(870, 300, 140, 140))
        self.label_4.setStyleSheet("image: url(:/images/NDUzeDUwMC5wbmc-removebg-preview.png);\n"
"")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(480, 0, 901, 341))
        self.label_2.setStyleSheet("image: url(:/images/loho-removebg-preview.png);\n"
"border-image:15px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.toolButton = QtWidgets.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(1000, 510, 41, 31))
        self.toolButton.setStyleSheet("background-color: transparent; border: none;")
        self.toolButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/Icons/download-removebg-preview.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.toolButton.setIcon(icon1)
        self.toolButton.setIconSize(QtCore.QSize(76, 15))
        self.toolButton.setObjectName("toolButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.toolButton.clicked.connect(self.toggle_password_visibility)
        self.pushButton.clicked.connect(self.login)

    def toggle_password_visibility(self):
        current_mode = self.lineEdit_2.echoMode()
        new_mode = (
            QtWidgets.QLineEdit.Normal
            if current_mode == QtWidgets.QLineEdit.Password
            else QtWidgets.QLineEdit.Password
        )
        self.lineEdit_2.setEchoMode(new_mode)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "  Password"))

    def login(self):
        # Get the entered password
        entered_password = self.lineEdit_2.text()

        try:
            # Execute menu.py using subprocess
            subprocess.run(['python', 'menu.py'], input=entered_password+'\n', check=True, text=True)
            print('Login successful!')
            Form.close()
        except subprocess.CalledProcessError as e:
            print(f'Error: {e}')
            print('Login failed!')


if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = Ui_Form()
        ui.setupUi(Form)
        Form.show()
        sys.exit(app.exec_())
