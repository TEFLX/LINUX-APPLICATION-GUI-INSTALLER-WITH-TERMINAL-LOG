from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess,os,shutil
from PyQt5.QtGui import QPixmap,QIcon
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QPushButton, QLabel,QMessageBox, QFileDialog
from PyQt5.QtCore import QProcess, QTextCodec

class SecondWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None, label_text="" , label_disc="", label_image="",soft_weight=""):
        super(SecondWindow, self).__init__(parent)
        self.setupUi(self)
        self.label_2.setText(label_text )
        self.label_3.setText(label_disc )
        self.label_3.setWordWrap(True)


        original_pixmap = QPixmap(label_image)
        desired_width = 100
        desired_height = 100
        scaled_pixmap = original_pixmap.scaled(desired_width, desired_height, QtCore.Qt.KeepAspectRatio)
        self.label_4.setPixmap(scaled_pixmap)
        self.softweight = soft_weight

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1115, 701)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(0, 0, 1150, 671))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.frame_5.setStyleSheet("border: none;")

        self.frame_2 = QtWidgets.QFrame(self.frame_5)
        self.frame_2.setGeometry(QtCore.QRect(50, 80, 1150, 600))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setGeometry(QtCore.QRect(50, 50, 900, 201))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")

        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setGeometry(QtCore.QRect(50, 10, 141, 141))
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setGeometry(QtCore.QRect(200, 30, 250, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setGeometry(QtCore.QRect(200, 80, 500, 31))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.frame_4)
        self.pushButton.setGeometry(QtCore.QRect(200, 140, 101, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("""QPushButton {background-color: #ffffff;border: 1px solid #999999;}QPushButton:hover {background-color: #eeeeee;}QPushButton:pressed {background-color: #dddddd;}""")

        self.pushButton_2 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 140, 101, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("""QPushButton {background-color: #ffffff;border: 1px solid #999999;}QPushButton:hover {background-color: #eeeeee;}QPushButton:pressed {background-color: #dddddd;}""")

        self.radioButton = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton.setGeometry(QtCore.QRect(775, 30, 95, 20))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_2.setGeometry(QtCore.QRect(775, 55, 95, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.frame51 = QtWidgets.QFrame(self.frame_2)
        self.frame51.setGeometry(QtCore.QRect(235, 250, 530, 40))
        self.frame51.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame51.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame51.setObjectName("frame_3")
        self.frame51.setStyleSheet("border:none;")
        self.label_on_frame51 = QtWidgets.QLabel(self.frame51)
        self.label_on_frame51.setGeometry(QtCore.QRect(0, 0, 530, 40))  # Adjust geometry as needed
        self.label_on_frame51.setObjectName("label_on_frame51")
        self.label_on_frame51.setText("Wait after click it may take time to load  . . . . . . . . .")

        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(235, 285, 530, 281))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_3.setStyleSheet("border: 1px solid #999999;")
        self.terminal_log = QtWidgets.QTextEdit(self.frame_3)
        self.terminal_log.setGeometry(QtCore.QRect(0, 0, 530, 281))
        self.terminal_log.setObjectName("terminal_log")
        self.terminal_log.setReadOnly(True)

        self.frame = QtWidgets.QFrame(self.frame_5)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1150, 81))
        self.frame.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(848, -20, 261, 141))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        image_path = '/home/TEFLX/PycharmProjects/pythonProject/projectmain/sliderpage/loho-removebg-preview.png'
        pixmap = QPixmap(image_path)
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 0, 61, 81))
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        image_path = "/home/TEFLX/PycharmProjects/pythonProject/projectmain/sliderpage/WhatsApp_Image_2024-02-16_at_17.42.16_5552f279-removebg-preview.png"
        pixmap = QPixmap(image_path)
        pixmap_resized = pixmap.scaled(QSize(60, 60))
        self.pushButton_3.setIcon(QIcon(pixmap_resized))
        self.pushButton_3.setIconSize(pixmap_resized.size())
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1103, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Launch"))
        self.pushButton_2.setText(_translate("MainWindow", "Remove"))
        self.radioButton.setText(_translate("MainWindow", "florida"))
        self.radioButton_2.setText(_translate("MainWindow", "debian"))
        self.pushButton.clicked.connect(self.install_software)
        self.pushButton_2.clicked.connect(self.remove_software)

    def append_output_to_log(self, output):
        self.terminal_log.append(output.decode())
    def install_software(self, package_manager):
        soft_weight = self.softweight
        if soft_weight == 1:
            if self.radioButton.isChecked():
                try:

                    apt_key_process = subprocess.run(["sudo", "apt-key", "adv", "--fetch-keys","https://brave-browser-apt-release.s3.brave.com/brave-core.asc"],check=True, capture_output=True)
                    self.append_output_to_log(apt_key_process.stdout)
                    self.append_output_to_log(apt_key_process.stderr)

                    apt_process = subprocess.run(["sudo", "apt", "install", "brave-keyring", "fonts-liberation"], check=True, capture_output=True)
                    self.append_output_to_log(apt_process.stdout)
                    self.append_output_to_log(apt_process.stderr)

                    deb_file = "/home/TEFLX/PycharmProjects/pythonProject/projectmain/files/brave-browser_1.57.47_amd64.deb"
                    dpkg_process = subprocess.run(["sudo", "dpkg", "-i", deb_file], check=True, capture_output=True)
                    self.append_output_to_log(dpkg_process.stdout)
                    self.append_output_to_log(dpkg_process.stderr)

                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            elif self.radioButton_2.isChecked():
                try:
                    gpg_key_url = "https://brave-browser-rpm-release.s3.brave.com/brave-core.asc"
                    import_gpg_key_command = f"rpm --import  {gpg_key_url}"
                    rpm_key_process = subprocess.run(import_gpg_key_command, shell=True, check=True,capture_output=True)
                    self.append_output_to_log(rpm_key_process.stdout)
                    self.append_output_to_log(rpm_key_process.stderr)

                    rpm_file = "/home/TEFLX/PycharmProjects/pythonProject/projectmain/files/brave-browser-1.63.169-1.x86_64.rpm"
                    rpm_process = subprocess.run(["sudo", "dnf", "install", rpm_file, "-y"], check=True,capture_output=True)
                    self.append_output_to_log(rpm_process.stdout)
                    self.append_output_to_log(rpm_process.stderr)

                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            else:
                self.terminal_log.append("No package manager selected")

        elif soft_weight == 2:
            if self.radioButton.isChecked():
                try:
                    deb_file = "/home/TEFLX/PycharmProjects/pythonProject/projectmain/files/google-chrome-stable_current_amd64.deb"
                    dpkg_process = subprocess.run(["sudo", "dpkg", "-i", deb_file], check=True, capture_output=True)
                    self.append_output_to_log(dpkg_process.stdout)
                    self.append_output_to_log(dpkg_process.stderr)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            elif self.radioButton_2.isChecked():
                try:
                    rpm_file = "/home/TEFLX/PycharmProjects/pythonProject/projectmain/files/google-chrome-stable_current_x86_64.rpm"
                    rpm_process = subprocess.run(["sudo", "dnf", "install", rpm_file, "-y"], check=True,
                                                 capture_output=True)
                    self.append_output_to_log(rpm_process.stdout)
                    self.append_output_to_log(rpm_process.stderr)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            else:
                self.terminal_log.append("No package manager selected")


        elif soft_weight == 3:
            if self.radioButton.isChecked():
                try:
                    deb_file = "/home/TEFLX/PycharmProjects/pythonProject/projectmain/files/opera-stable_108.0.5067.20_amd64.deb"
                    dpkg_process = subprocess.run(["sudo", "dpkg", "-i", deb_file], check=True, capture_output=True)
                    self.append_output_to_log(dpkg_process.stdout)
                    self.append_output_to_log(dpkg_process.stderr)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            elif self.radioButton_2.isChecked():
                try:
                    rpm_file = "/home/TEFLX/PycharmProjects/pythonProject/projectmain/files/opera-stable_108.0.5067.20_amd64.rpm"
                    rpm_process = subprocess.run(["sudo", "dnf", "install", rpm_file, "-y"], check=True,
                                                 capture_output=True)
                    self.append_output_to_log(rpm_process.stdout)
                    self.append_output_to_log(rpm_process.stderr)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            else:
                self.terminal_log.append("No package manager selected")


        elif soft_weight == 4:
            if self.radioButton.isChecked():
                try:
                    deb_file = "/home/TEFLX/PycharmProjects/pythonProject/projectmain/files/firefox.deb"
                    dpkg_process = subprocess.run(["sudo", "dpkg", "-i", deb_file], check=True, capture_output=True)
                    self.append_output_to_log(dpkg_process.stdout)
                    self.append_output_to_log(dpkg_process.stderr)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            elif self.radioButton_2.isChecked():
                try:
                    rpm_file = "/home/TEFLX/PycharmProjects/pythonProject/projectmain/files/firefox.deb"
                    rpm_process = subprocess.run(["sudo", "dnf", "install", rpm_file, "-y"], check=True,
                                                 capture_output=True)
                    self.append_output_to_log(rpm_process.stdout)
                    self.append_output_to_log(rpm_process.stderr)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            else:
                self.terminal_log.append("No package manager selected")

        elif soft_weight == 5:
            if self.radioButton.isChecked():
                try:
                    tar_file = "/home/TEFLX/PycharmProjects/pythonProject/projectmain/files/tor-browser-linux-x86_64-13.0.11.tar.xz"
                    extraction_dir = "/home/TEFLX/PycharmProjects/pythonProject/projectmain/files/tor_browser"
                    subprocess.run(["tar", "-xf", tar_file, "-C", extraction_dir], check=True)

                    tor_path = os.path.join(extraction_dir, "tor-browser-linux-x86_64", "start-tor-browser.desktop")
                    subprocess.run([tor_path], check=True)

                    self.terminal_log.append("Tor Browser installed and started successfully.")
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            elif self.radioButton_2.isChecked():
                self.terminal_log.append("Tor Browser installation not supported for this package manager.")
            else:
                self.terminal_log.append("No package manager selected")

        elif soft_weight == 6:
            if self.radioButton.isChecked():
                try:
                    apt_process = subprocess.run(["sudo", "apt", "install", "gparted", "-y"], check=True,capture_output=True)
                    self.append_output_to_log(apt_process.stdout)
                    self.append_output_to_log(apt_process.stderr)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            elif self.radioButton_2.isChecked():
                try:
                    dnf_process = subprocess.run(["sudo", "dnf", "install", "gparted", "-y"], check=True, capture_output=True)
                    self.append_output_to_log(dnf_process.stdout)
                    self.append_output_to_log(dnf_process.stderr)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            else:
                self.terminal_log.append("No package manager selected")

        elif soft_weight == 7:
            if self.radioButton.isChecked():
                try:
                    apt_process = subprocess.run(["sudo", "apt", "install", "p7zip", "-y"], check=True, capture_output=True)
                    self.append_output_to_log(apt_process.stdout)
                    self.append_output_to_log(apt_process.stderr)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            elif self.radioButton_2.isChecked():
                try:
                    dnf_process = subprocess.run(["sudo", "dnf", "install", "p7zip", "-y"], check=True, capture_output=True)
                    self.append_output_to_log(dnf_process.stdout)
                    self.append_output_to_log(dnf_process.stderr)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            else:
                self.terminal_log.append("No package manager selected")

        elif soft_weight == 8:
            if self.radioButton.isChecked():
                try:
                    apt_process = subprocess.run(["sudo", "apt", "install", "gnome-calculator", "-y"], check=True,capture_output=True)
                    self.append_output_to_log(apt_process.stdout)
                    self.append_output_to_log(apt_process.stderr)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            elif self.radioButton_2.isChecked():
                try:
                    dnf_process = subprocess.run(["sudo", "dnf", "install", "gnome-calculator", "-y"], check=True, capture_output=True)
                    self.append_output_to_log(dnf_process.stdout)
                    self.append_output_to_log(dnf_process.stderr)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            else:
                self.terminal_log.append("No package manager selected")
        elif soft_weight == 9:
            if self.radioButton.isChecked():
                try:
                    apt_process = subprocess.run(["sudo", "apt", "install", "vim-gtk3", "-y"], check=True,capture_output=True)
                    self.append_output_to_log(apt_process.stdout)
                    self.append_output_to_log(apt_process.stderr)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            elif self.radioButton_2.isChecked():
                try:
                    dnf_process = subprocess.run(["sudo", "dnf", "install", "vim-X11", "-y"], check=True,capture_output=True)
                    self.append_output_to_log(dnf_process.stdout)
                    self.append_output_to_log(dnf_process.stderr)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            else:
                self.terminal_log.append("No package manager selected")

        elif soft_weight == 10:

            if self.radioButton.isChecked():
                try:
                    snap_process = subprocess.run(["sudo", "snap", "install", "vlc"], check=True, capture_output=True)
                    self.append_output_to_log(snap_process.stdout)
                    self.append_output_to_log(snap_process.stderr)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")

            elif self.radioButton_2.isChecked():
                try:
                    # rpm_file2 = "/home/TEFLX/PycharmProjects/pythonProject/projectmain/files/epel-release-latest-8.noarch.rpm"
                    # rpm_file = "/home/TEFLX/PycharmProjects/pythonProject/projectmain/files/rpmfusion-free-release-8.noarch.rpm"
                    # rpm_process = subprocess.run(["sudo", "dnf", "install", rpm_file2, "-y"], check=True,capture_output=True)
                    # rpm_process2 = subprocess.run(["sudo", "dnf", "install", rpm_file, "-y"], check=True,capture_output=True)
                    rpm_process3 = subprocess.run(["sudo", "dnf", "install", "vlc", "-y"], check=True,capture_output=True)
                    # self.append_output_to_log(rpm_process.stdout)
                    # self.append_output_to_log(rpm_process.stderr)
                    # self.append_output_to_log(rpm_process2.stdout)
                    # self.append_output_to_log(rpm_process2.stderr)
                    self.append_output_to_log(rpm_process3.stdout)
                    self.append_output_to_log(rpm_process3.stderr)

                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            else:
                self.terminal_log.append("No package manager selected")

        elif soft_weight == 11:
            if self.radioButton.isChecked():
                try:
                    apt_process = subprocess.run(["sudo", "apt", "install", "gimp", "-y"], check=True,capture_output=True)
                    self.append_output_to_log(apt_process.stdout)
                    self.append_output_to_log(apt_process.stderr)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            elif self.radioButton_2.isChecked():
                try:
                    dnf_process = subprocess.run(["sudo", "dnf", "install", "gimp", "-y"], check=True,capture_output=True)
                    self.append_output_to_log(dnf_process.stdout)
                    self.append_output_to_log(dnf_process.stderr)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            else:
                self.terminal_log.append("No package manager selected")

        elif soft_weight == 12:
            if self.radioButton.isChecked():
                try:
                    apt_process = subprocess.run(["sudo", "apt", "install", "cheese", "-y"], check=True,capture_output=True)
                    self.append_output_to_log(apt_process.stdout)
                    self.append_output_to_log(apt_process.stderr)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            elif self.radioButton_2.isChecked():
                try:
                    dnf_process = subprocess.run(["sudo", "dnf", "install", "cheese", "-y"], check=True, capture_output=True)
                    self.append_output_to_log(dnf_process.stdout)
                    self.append_output_to_log(dnf_process.stderr)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            else:
                self.terminal_log.append("No package manager selected")

        elif soft_weight == 13:
            if self.radioButton.isChecked():
                try:
                    self.terminal_log.append(" coming soon: UM-player")
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            elif self.radioButton_2.isChecked():
                try:
                    self.terminal_log.append(" coming soon: UM-player")
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            else:
                self.terminal_log.append("No package manager selected")
        elif soft_weight == 14:
            if self.radioButton.isChecked():
                try:
                    wget_process = subprocess.run(["wget","https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb"],check=True, capture_output=True)
                    self.append_output_to_log(wget_process.stdout)
                    self.append_output_to_log(wget_process.stderr)

                    chmod_process = subprocess.run(["chmod", "+x", "msfinstall"], check=True, capture_output=True)
                    self.append_output_to_log(chmod_process.stdout)
                    self.append_output_to_log(chmod_process.stderr)

                    msf_install_process = subprocess.run(["./msfinstall"], check=True, capture_output=True)
                    self.append_output_to_log(msf_install_process.stdout)
                    self.append_output_to_log(msf_install_process.stderr)

                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            elif self.radioButton_2.isChecked():
                try:
                    dnf_process = subprocess.run(["sudo", "dnf", "install", "wget", "-y"], check=True,capture_output=True)
                    self.append_output_to_log(dnf_process.stdout)
                    self.append_output_to_log(dnf_process.stderr)

                    wget_process = subprocess.run(["wget", "https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb"], check=True, capture_output=True)
                    self.append_output_to_log(wget_process.stdout)
                    self.append_output_to_log(wget_process.stderr)

                    chmod_process = subprocess.run(["chmod", "+x", "msfinstall"], check=True, capture_output=True)
                    self.append_output_to_log(chmod_process.stdout)
                    self.append_output_to_log(chmod_process.stderr)

                    msf_install_process = subprocess.run(["./msfinstall"], check=True, capture_output=True)
                    self.append_output_to_log(msf_install_process.stdout)
                    self.append_output_to_log(msf_install_process.stderr)

                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            else:
                self.terminal_log.append("No package manager selected")

        elif soft_weight == 15:
            if self.radioButton.isChecked():
                try:
                    apt_process = subprocess.run(["sudo", "apt", "install", "mysql-server", "-y"], check=True,capture_output=True)
                    self.append_output_to_log(apt_process.stdout)
                    self.append_output_to_log(apt_process.stderr)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            elif self.radioButton_2.isChecked():
                try:
                    dnf_process = subprocess.run(["sudo", "dnf", "install", "mysql-server", "-y"], check=True,capture_output=True)
                    self.append_output_to_log(dnf_process.stdout)
                    self.append_output_to_log(dnf_process.stderr)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            else:
                self.terminal_log.append("No package manager selected")

        elif soft_weight == 16:
            if self.radioButton.isChecked():
                try:
                    apt_process = subprocess.run(["sudo", "apt", "install", "wireshark", "-y"], check=True,capture_output=True)
                    self.append_output_to_log(apt_process.stdout)
                    self.append_output_to_log(apt_process.stderr)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            elif self.radioButton_2.isChecked():
                try:
                    dnf_process = subprocess.run(["sudo", "dnf", "install", "wireshark", "-y"], check=True, capture_output=True)
                    self.append_output_to_log(dnf_process.stdout)
                    self.append_output_to_log(dnf_process.stderr)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            else:
                self.terminal_log.append("No package manager selected")
        elif soft_weight == 17:
            if self.radioButton.isChecked():
                try:
                    apt_process = subprocess.run(["sudo", "apt", "install", "python3-pip", "-y"], check=True,capture_output=True)
                    self.append_output_to_log(apt_process.stdout)
                    self.append_output_to_log(apt_process.stderr)
                    pip_process = subprocess.run(["sudo", "pip3", "install", "notebook"], check=True, capture_output=True)
                    self.append_output_to_log(pip_process.stdout)
                    self.append_output_to_log(pip_process.stderr)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            elif self.radioButton_2.isChecked():
                try:
                    dnf_process = subprocess.run(["sudo", "dnf", "install", "python3-pip", "-y"], check=True,capture_output=True)
                    self.append_output_to_log(dnf_process.stdout)
                    self.append_output_to_log(dnf_process.stderr)
                    pip_process = subprocess.run(["sudo", "pip3", "install", "notebook"], check=True,capture_output=True)
                    self.append_output_to_log(pip_process.stdout)
                    self.append_output_to_log(pip_process.stderr)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            else:
                self.terminal_log.append("No package manager selected")
        elif soft_weight == 18:
            if self.radioButton.isChecked():
                try:
                    self.terminal_log.append(" coming soon: MS Office removal using apt-get")
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            elif self.radioButton_2.isChecked():
                try:
                    self.terminal_log.append(" coming soon: MS Office removal using yum")
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            else:
                self.terminal_log.append("No package manager selected")
        elif soft_weight == 19:
            if self.radioButton.isChecked():
                try:
                    apt_process = subprocess.run(["sudo", "apt", "install", "libreoffice", "-y"], check=True,
                                                 capture_output=True)
                    self.append_output_to_log(apt_process.stdout)
                    self.append_output_to_log(apt_process.stderr)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            elif self.radioButton_2.isChecked():
                try:
                    dnf_process = subprocess.run(["sudo", "dnf", "install", "libreoffice", "-y"], check=True,
                                                 capture_output=True)
                    self.append_output_to_log(dnf_process.stdout)
                    self.append_output_to_log(dnf_process.stderr)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            else:
                self.terminal_log.append("No package manager selected")

        elif soft_weight == 20:
            if self.radioButton.isChecked():
                try:
                    apt_process = subprocess.run(["sudo", "apt", "install", "wine", "-y"], check=True,
                                                 capture_output=True)
                    self.append_output_to_log(apt_process.stdout)
                    self.append_output_to_log(apt_process.stderr)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            elif self.radioButton_2.isChecked():
                try:
                    dnf_process = subprocess.run(["sudo", "dnf", "install", "wine", "-y"], check=True,
                                                 capture_output=True)
                    self.append_output_to_log(dnf_process.stdout)
                    self.append_output_to_log(dnf_process.stderr)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            else:
                self.terminal_log.append("No package manager selected")

        elif soft_weight == 21:
            if self.radioButton.isChecked():
                try:
                    apt_process = subprocess.run(["sudo", "apt", "install", "qttools5-dev-tools", "-y"], check=True,
                                                 capture_output=True)
                    self.append_output_to_log(apt_process.stdout)
                    self.append_output_to_log(apt_process.stderr)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            elif self.radioButton_2.isChecked():
                try:
                    dnf_process = subprocess.run(["sudo", "dnf", "install", "qt5-designer", "-y"], check=True,
                                                 capture_output=True)
                    self.append_output_to_log(dnf_process.stdout)
                    self.append_output_to_log(dnf_process.stderr)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            else:
                self.terminal_log.append("No package manager selected")

        elif soft_weight == 22:
            python_tar_file = "/home/TEFLX/PycharmProjects/pythonProject/projectmain/files/Python-3.12.1.tgz"

            if self.radioButton.isChecked():
                try:
                    apt_process = subprocess.run(["sudo", "apt", "install", "build-essential", "-y"], check=True, capture_output=True)
                    self.append_output_to_log(apt_process.stdout)
                    self.append_output_to_log(apt_process.stderr)

                    # Extract and install Python
                    os.chdir("/tmp")
                    subprocess.run(["tar", "-xzvf", python_tar_file], check=True)
                    os.chdir("Python-3.12.1")
                    subprocess.run(["./configure"], check=True)
                    subprocess.run(["make"], check=True)
                    subprocess.run(["sudo", "make", "install"], check=True)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            elif self.radioButton_2.isChecked():
                try:
                    dnf_process = subprocess.run(["sudo", "dnf", "install", "gcc", "-y"], check=True, capture_output=True)
                    self.append_output_to_log(dnf_process.stdout)
                    self.append_output_to_log(dnf_process.stderr)

                    # Extract and install Python
                    os.chdir("/tmp")
                    subprocess.run(["tar", "-xzvf", python_tar_file], check=True)
                    os.chdir("Python-3.12.1")
                    subprocess.run(["./configure"], check=True)
                    subprocess.run(["make"], check=True)
                    subprocess.run(["sudo", "make", "install"], check=True)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            else:
                self.terminal_log.append("No package manager selected")

        elif soft_weight == 23:
            pycharm_tar_file = "/home/TEFLX/PycharmProjects/pythonProject/projectmain/files/pycharm-community-2023.3.5.tar.gz"
            install_path = "/home/TEFLX/PycharmProjects/pythonProject/projectmain/files"
            if self.radioButton.isChecked():
                try:
                    os.makedirs(install_path, exist_ok=True)
                    shutil.unpack_archive(pycharm_tar_file, install_path)
                    os.chdir(os.path.join(install_path, "pycharm-community-2023.3.5"))
                    subprocess.run(["./bin/pycharm.sh"], check=True)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            elif self.radioButton_2.isChecked():
                try:
                    os.makedirs(install_path, exist_ok=True)
                    shutil.unpack_archive(pycharm_tar_file, install_path)
                    os.chdir(os.path.join(install_path, "pycharm-community-2023.3.5"))
                    subprocess.run(["./bin/pycharm.sh"], check=True)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            else:
                self.terminal_log.append("No package manager selected")

        elif soft_weight == 24:
            if self.radioButton.isChecked():
                try:
                    deb_file = "/home/TEFLX/PycharmProjects/pythonProject/projectmain/files/visualstudio.deb"
                    dpkg_process = subprocess.run(["sudo", "dpkg", "-i", deb_file], check=True, capture_output=True)
                    self.append_output_to_log(dpkg_process.stdout)
                    self.append_output_to_log(dpkg_process.stderr)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            elif self.radioButton_2.isChecked():
                try:
                    rpm_file = "/home/TEFLX/PycharmProjects/pythonProject/projectmain/files/visual studio.rpm"
                    rpm_process = subprocess.run(["sudo", "dnf", "install", rpm_file, "-y"], check=True,
                                                 capture_output=True)
                    self.append_output_to_log(rpm_process.stdout)
                    self.append_output_to_log(rpm_process.stderr)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            else:
                self.terminal_log.append("No package manager selected")

        elif soft_weight == 25:
            if self.radioButton.isChecked():
                try:
                    deb_file = "/home/TEFLX/PycharmProjects/pythonProject/projectmain/files/java.deb"
                    dpkg_process = subprocess.run(["sudo", "dpkg", "-i", deb_file], check=True, capture_output=True)
                    self.append_output_to_log(dpkg_process.stdout)
                    self.append_output_to_log(dpkg_process.stderr)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            elif self.radioButton_2.isChecked():
                try:
                    rpm_file = "/home/TEFLX/PycharmProjects/pythonProject/projectmain/files/java.rpm"
                    rpm_process = subprocess.run(["sudo", "dnf", "install", rpm_file, "-y"], check=True,
                                                 capture_output=True)
                    self.append_output_to_log(rpm_process.stdout)
                    self.append_output_to_log(rpm_process.stderr)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            else:
                self.terminal_log.append("No package manager selected")

        elif soft_weight == 26:
            if self.radioButton.isChecked():
                try:
                    apt_process = subprocess.run(["sudo", "apt", "install", "g++", "-y"], check=True,
                                                 capture_output=True)
                    self.append_output_to_log(apt_process.stdout)
                    self.append_output_to_log(apt_process.stderr)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            elif self.radioButton_2.isChecked():
                try:
                    dnf_process = subprocess.run(["sudo", "dnf", "install", "gcc-c++", "-y"], check=True,
                                                 capture_output=True)
                    self.append_output_to_log(dnf_process.stdout)
                    self.append_output_to_log(dnf_process.stderr)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            else:
                self.terminal_log.append("No package manager selected")

        else:
            QMessageBox.warning(self, "Warning", "Invalid soft weight value.")


    def remove_software(self, package_manager):
        soft_weight = self.softweight
        if soft_weight == 1:
            if self.radioButton.isChecked():
                try:
                    result = subprocess.run(["sudo", "apt-get", "remove", "brave-browser", "-y"], capture_output=True ,text=True, check=True)
                    self.terminal_log.append(result.stdout)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            elif self.radioButton_2.isChecked():
                try:
                    result = subprocess.run(["sudo", "yum", "remove", "brave-browser", "-y"], capture_output=True, text=True, check=True)
                    self.terminal_log.append(result.stdout)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            else:
                self.terminal_log.append("No package manager selected")

        elif soft_weight == 2:
            if self.radioButton.isChecked():
                try:
                    result = subprocess.run(["sudo", "apt-get", "remove", "google-chrome-stable", "-y"], capture_output=True,text=True, check=True)
                    self.terminal_log.append(result.stdout)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            elif self.radioButton_2.isChecked():
                try:
                    result = subprocess.run(["sudo", "yum", "remove", "google-chrome-stable", "-y"], capture_output=True,text=True, check=True)
                    self.terminal_log.append(result.stdout)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            else:
                self.terminal_log.append("No package manager selected")

        elif soft_weight == 3:
            if self.radioButton.isChecked():
                try:
                    result = subprocess.run(["sudo", "apt-get", "remove", "opera-stable", "-y"], capture_output=True, text=True, check=True)
                    self.terminal_log.append(result.stdout)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            elif self.radioButton_2.isChecked():
                try:
                    result = subprocess.run(["sudo", "yum", "remove", "opera-stable","-y"], capture_output=True, text=True, check=True)
                    self.terminal_log.append(result.stdout)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            else:
                self.terminal_log.append("No package manager selected")

        elif soft_weight == 4:
            if self.radioButton.isChecked():
                try:
                    result = subprocess.run(["sudo", "apt-get", "remove", "firefox", "-y"], capture_output=True,text=True, check=True)
                    self.terminal_log.append(result.stdout)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            elif self.radioButton_2.isChecked():
                try:
                    result = subprocess.run(["sudo", "yum", "remove", "firefox","-y"], capture_output=True, text=True, check=True)
                    self.terminal_log.append(result.stdout)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            else:
                self.terminal_log.append("No package manager selected")

        elif soft_weight == 5:
            if self.radioButton.isChecked():
                try:
                    result = subprocess.run(["sudo", "apt-get", "remove", "torbrowser-launcher", "-y"],capture_output=True,text=True, check=True)
                    self.terminal_log.append(result.stdout)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            elif self.radioButton_2.isChecked():
                try:
                    result = subprocess.run(["sudo", "yum", "remove", "torbrowser-launcher","-y"], capture_output=True, text=True, check=True)
                    self.terminal_log.append(result.stdout)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            else:
                self.terminal_log.append("No package manager selected")

        elif soft_weight == 6:
            if self.radioButton.isChecked():
                try:
                    result = subprocess.run(["sudo", "apt-get", "remove", "gparted", "-y"], capture_output=True,text=True, check=True)
                    self.terminal_log.append(result.stdout)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            elif self.radioButton_2.isChecked():
                try:
                    result = subprocess.run(["sudo", "yum", "remove", "gparted", "-y"], capture_output=True,text=True, check=True)
                    self.terminal_log.append(result.stdout)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            else:
                self.terminal_log.append("No package manager selected")

        elif soft_weight == 7:
            if self.radioButton.isChecked():
                try:
                    result = subprocess.run(["sudo", "apt-get", "remove", "7zip", "-y"],capture_output=True, text=True, check=True)
                    self.terminal_log.append(result.stdout)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            elif self.radioButton_2.isChecked():
                try:
                    result = subprocess.run(["sudo", "yum", "remove", "p7zip", "-y"], capture_output=True, text=True, check=True)
                    self.terminal_log.append(result.stdout)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            else:
                self.terminal_log.append("No package manager selected")

        elif soft_weight == 8:
            if self.radioButton.isChecked():
                try:
                    result = subprocess.run(["sudo", "apt-get", "remove", "gnome-calculator", "-y"],capture_output=True, text=True, check=True)
                    self.terminal_log.append(result.stdout)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            elif self.radioButton_2.isChecked():
                try:
                    result = subprocess.run(["sudo", "yum", "remove", "gnome-calculator", "-y"], capture_output=True,text=True, check=True)
                    self.terminal_log.append(result.stdout)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            else:
                self.terminal_log.append("No package manager selected")

        elif soft_weight == 9:
            if self.radioButton.isChecked():
                try:
                    result = subprocess.run(["sudo", "apt-get", "remove", "gvim", "-y"],capture_output=True,text=True, check=True)
                    self.terminal_log.append(result.stdout)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            elif self.radioButton_2.isChecked():
                try:
                    result = subprocess.run(["sudo", "yum", "remove", "gvim", "-y"], capture_output=True,text=True, check=True)
                    self.terminal_log.append(result.stdout)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            else:
                self.terminal_log.append("No package manager selected")

        elif soft_weight == 10:
            if self.radioButton.isChecked():
                try:
                    result = subprocess.run(["sudo", "apt-get", "remove", "vlc", "-y"],capture_output=True, text=True, check=True)
                    self.terminal_log.append(result.stdout)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            elif self.radioButton_2.isChecked():
                try:
                    result = subprocess.run(["sudo", "yum", "remove", "vlc", "-y"], capture_output=True,text=True, check=True)
                    self.terminal_log.append(result.stdout)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            else:
                self.terminal_log.append("No package manager selected")

        elif soft_weight == 11:
            if self.radioButton.isChecked():
                try:
                    result = subprocess.run(["sudo", "apt-get", "remove", "gimp", "-y"],capture_output=True,text=True, check=True)
                    self.terminal_log.append(result.stdout)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            elif self.radioButton_2.isChecked():
                try:
                    result = subprocess.run(["sudo", "yum", "remove", "gimp", "-y"], capture_output=True,text=True, check=True)
                    self.terminal_log.append(result.stdout)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            else:
                self.terminal_log.append("No package manager selected")

        elif soft_weight == 12:
            if self.radioButton.isChecked():
                try:
                    result = subprocess.run(["sudo", "apt-get", "remove", "cheese", "-y"], capture_output=True,text=True, check=True)
                    self.terminal_log.append(result.stdout)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            elif self.radioButton_2.isChecked():
                try:
                    result = subprocess.run(["sudo", "yum", "remove", "cheese", "-y"], capture_output=True, text=True, check=True)
                    self.terminal_log.append(result.stdout)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            else:
                self.terminal_log.append("No package manager selected")

        elif soft_weight == 13:
            if self.radioButton.isChecked():
                try:
                    result = subprocess.run(["sudo", "apt-get", "remove", "umplayer", "-y"], capture_output=True, text=True, check=True)
                    self.terminal_log.append(result.stdout)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            elif self.radioButton_2.isChecked():
                try:
                    result = subprocess.run(["sudo", "yum", "remove", "umplayer", "-y"], capture_output=True, text=True, check=True)
                    self.terminal_log.append(result.stdout)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            else:
                self.terminal_log.append("No package manager selected")
        elif soft_weight == 14:
            if self.radioButton.isChecked():
                try:
                    result = subprocess.run(["sudo", "apt-get", "remove", "metasploit-framework", "-y"],capture_output=True, text=True, check=True)
                    self.terminal_log.append(result.stdout)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            elif self.radioButton_2.isChecked():
                try:
                    result = subprocess.run(["sudo", "yum", "remove", "metasploit-framework", "-y"], capture_output=True, text=True, check=True)
                    self.terminal_log.append(result.stdout)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            else:
                self.terminal_log.append("No package manager selected")
        elif soft_weight == 15:
            if self.radioButton.isChecked():
                try:
                    result = subprocess.run(["sudo", "apt-get", "remove", "mysql-server", "-y"], capture_output=True, text=True, check=True)
                    self.terminal_log.append(result.stdout)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            elif self.radioButton_2.isChecked():
                try:
                    result = subprocess.run(["sudo", "yum", "remove", "mysql-server", "-y"],capture_output=True,text=True, check=True)
                    self.terminal_log.append(result.stdout)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            else:
                self.terminal_log.append("No package manager selected")
        elif soft_weight == 16:
            if self.radioButton.isChecked():
                try:
                    result = subprocess.run(["sudo", "apt-get", "remove", "wireshark", "-y"],capture_output=True,text=True, check=True)
                    self.terminal_log.append(result.stdout)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            elif self.radioButton_2.isChecked():
                try:
                    result = subprocess.run(["sudo", "yum", "remove", "wireshark", "-y"],  capture_output=True, text=True, check=True)
                    self.terminal_log.append(result.stdout)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            else:
                self.terminal_log.append("No package manager selected")
        elif soft_weight == 17:
            if self.radioButton.isChecked():
                try:
                    result = subprocess.run(["sudo", "apt-get", "remove", "jupyter-notebook", "-y"],capture_output=True, text=True, check=True)
                    self.terminal_log.append(result.stdout)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            elif self.radioButton_2.isChecked():
                try:
                    result = subprocess.run(["sudo", "yum", "remove", "jupyter-notebook", "-y"],capture_output=True,text=True, check=True)
                    self.terminal_log.append(result.stdout)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            else:
                self.terminal_log.append("No package manager selected")

        elif soft_weight == 18:
            if self.radioButton.isChecked():
                try:
                    self.terminal_log.append(" coming soon: MS Office removal using apt-get")
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            elif self.radioButton_2.isChecked():
                try:
                    self.terminal_log.append(" coming soon: MS Office removal using yum")
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            else:
                self.terminal_log.append("No package manager selected")
        elif soft_weight == 19:
            if self.radioButton.isChecked():
                try:
                    result = subprocess.run(["sudo", "apt-get", "remove", "libreoffice", "-y"],capture_output=True, text=True, check=True)
                    self.terminal_log.append(result.stdout)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            elif self.radioButton_2.isChecked():
                try:
                    result = subprocess.run(["sudo", "yum", "remove", "libreoffice", "-y"], capture_output=True,text=True, check=True)
                    self.terminal_log.append(result.stdout)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            else:
                self.terminal_log.append("No package manager selected")
        elif soft_weight == 20:
            if self.radioButton.isChecked():
                try:
                    result = subprocess.run(["sudo", "apt-get", "remove", "wine", "-y"], capture_output=True,text=True, check=True)
                    self.terminal_log.append(result.stdout)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            elif self.radioButton_2.isChecked():
                try:
                    result = subprocess.run(["sudo", "yum", "remove", "wine","-y"], capture_output=True,text=True, check=True)
                    self.terminal_log.append(result.stdout)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            else:
                self.terminal_log.append("No package manager selected")
        elif soft_weight == 21:
            if self.radioButton.isChecked():
                try:
                    result = subprocess.run(["sudo", "apt-get", "remove", "qtdisigner", "-y"],capture_output=True,text=True, check=True)
                    self.terminal_log.append(result.stdout)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            elif self.radioButton_2.isChecked():
                try:
                    result = subprocess.run(["sudo", "yum", "remove", "qtdisigner", "-y"], capture_output=True, text=True, check=True)
                    self.terminal_log.append(result.stdout)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            else:
                self.terminal_log.append("No package manager selected")
        elif soft_weight == 22:
            if self.radioButton.isChecked():
                try:
                    self.terminal_log.append("Uninstalling Python from a Linux distribution can be a bit risky\n wait checking dependencies and uninstalling")
                    result = subprocess.run(["sudo", "apt-get", "remove", "python3.12.1", "-y"], capture_output=True,text=True, check=True)
                    self.terminal_log.append(result.stdout)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            elif self.radioButton_2.isChecked():
                try:
                    self.terminal_log.append("Uninstalling Python from a Linux distribution can be a bit risky\n wait checking dependencies and uninstalling")
                    result = subprocess.run(["sudo", "yum", "remove", "python3.12.1", "-y"], capture_output=True,text=True, check=True)
                    self.terminal_log.append(result.stdout)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            else:
                self.terminal_log.append("No package manager selected")
        elif soft_weight == 23:
            directory_path = QFileDialog.getExistingDirectory(self, "Select Directory")
            if directory_path:
                try:
                    result = subprocess.run(["sudo", "rm", "-rf", directory_path],capture_output=True, text=True, check=True)
                    self.terminal_log.append(result.stdout)
                    QMessageBox.information(self, "Success", "Directory removed successfully.")
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
                    QMessageBox.warning(self, "Error", f"An error occurred: {e}")
            else:
                self.terminal_log.append("No directory selected")

        elif soft_weight == 24:
            if self.radioButton.isChecked():
                try:
                    result = subprocess.run(["sudo", "apt-get", "remove", "visual-studio", "-y"], capture_output=True,text=True, check=True)
                    self.terminal_log.append(result.stdout)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            elif self.radioButton_2.isChecked():
                try:
                    result = subprocess.run(["sudo", "yum", "remove", "visual-studio", "-y"], capture_output=True,text=True, check=True)
                    self.terminal_log.append(result.stdout)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            else:
                self.terminal_log.append("No package manager selected")
        elif soft_weight == 25:
            if self.radioButton.isChecked():
                try:
                    result = subprocess.run(["sudo", "apt-get", "remove", "openjdk-*", "-y"], capture_output=True, text=True, check=True)
                    self.terminal_log.append(result.stdout)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            elif self.radioButton_2.isChecked():
                try:
                    result = subprocess.run(["sudo", "yum", "remove", "java-*-openjdk", "-y"], capture_output=True,  text=True, check=True)
                    self.terminal_log.append(result.stdout)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            else:
                self.terminal_log.append("No package manager selected")

        elif soft_weight == 26:
            if self.radioButton.isChecked():
                try:
                    result = subprocess.run(["sudo", "apt-get", "remove", "g++", "-y"],capture_output=True,text=True, check=True)
                    self.terminal_log.append(result.stdout)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            elif self.radioButton_2.isChecked():
                try:
                    result = subprocess.run(["sudo", "yum", "remove", "gcc-c++", "-y"], capture_output=True,text=True, check=True)
                    self.terminal_log.append(result.stdout)
                except subprocess.CalledProcessError as e:
                    self.terminal_log.append(f"Error: {e}")
            else:
                self.terminal_log.append("No package manager selected")


        else:
            QMessageBox.warning(self, "Warning", "Invalid soft weight value.")

    def execute_process(self, command):
        try:
            process = QProcess()
            process.start(*command)
            process.waitForFinished()

            codec = QTextCodec.codecForLocale()
            stdout = process.readAllStandardOutput()
            stderr = process.readAllStandardError()
            output = codec.toUnicode(stdout) + codec.toUnicode(stderr)
            self.terminal_log.append(output)

        except Exception as e:
            self.terminal_log.append(f"Error: {e}")
