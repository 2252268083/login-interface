import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import login

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QMainWindow()
    loginUi = login.Ui_MainWindow()
    loginUi.setupUi(win)
    loginUi.widget_3.hide()#hide是隐藏的意思  3是注册
    def change_widege3():
        loginUi.widget_2.hide()
        loginUi.widget_3.show()#展示
    def change_widege2():
        loginUi.widget_3.hide()
        loginUi.widget_2.show() 
    loginUi.pushButton.clicked.connect(change_widege2)
    loginUi.pushButton_2.clicked.connect(change_widege3)
    win.show()
    sys.exit(app.exec_())