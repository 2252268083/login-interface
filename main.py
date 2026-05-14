
import os
import subprocess
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
    def login_ok(self,window=None):
        print("成功")
        self.hide()
        scrip_path = r"F:\编程文件\Python代码\ai的调用\前后端通信.py"
        python_exe = r"F:\Python3.10\python.exe"
        if os.path.exists(scrip_path):
            subprocess.Popen([python_exe,scrip_path],cwd=os.path.dirname(scrip_path))
        else:
            print("没找到文件")





if __name__ == '__main__':
    app = QApplication([])
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())