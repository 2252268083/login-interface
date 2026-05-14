
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from auth import login1
import login
from windows.drag_window import DragaMixin

#添加一个自定义窗口
class MainWindow(QMainWindow,DragaMixin):
    def __init__(self):
        super().__init__()
        DragaMixin.__init__(self)
        self.loginUi = login.Ui_MainWindow()
        self.loginUi.setupUi(self)
        self.loginUi.widget_3.hide()#hide是隐藏的意思  3是注册

    #登录按钮的转换



        self.loginUi.pushButton.clicked.connect(self.change_widege2)
        self.loginUi.pushButton_2.clicked.connect(self.change_widege3)


    #登录成功后运行或者注册
        self.loginUi.pushButton_3.clicked.connect(
            lambda:login1.login_check(self.loginUi,self,self.login_ok)
            )
        self.loginUi.pushButton_4.clicked.connect(
            lambda:login1.register_users(self.loginUi,self)
            )

    def change_widege3(self):
         
        self.loginUi.widget_2.hide()
        self.loginUi.widget_3.show()#展示n
    def change_widege2(self):
        self.loginUi.widget_3.hide()
        self.loginUi.widget_2.show() 
    def login_ok(self):
        print("成功")





if __name__ == '__main__':
    app = QApplication([])
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())