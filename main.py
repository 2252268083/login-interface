import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from auth import login1
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



    loginUi.pushButton_3.clicked.connect(lambda:login1.login_check(loginUi,win,lambda w: print("执行操作")))
    loginUi.pushButton_4.clicked.connect(lambda:login1.register_users(loginUi,win))

    
    win.show()
    sys.exit(app.exec_())