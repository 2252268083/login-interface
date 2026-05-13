import json
import os
from PyQt5.QtWidgets import QMessageBox,QMainWindow

file_json = "./data/users.json"

def load_users():#登录读取用户
    if not os.path.exists(file_json):
        with open (file_json,"w",encoding="utf-8") as f:
            json.dump({"users":{}},f)#如果没有 就写入
    
    with open (file_json,"r",encoding="utf-8") as f:
        data = json.load(f)#读取json的文件内容 自动转换成Python的格式
    return data["users"]


#保存账号密码
def save_user (users):
    with open (file_json,"w",encoding="utf-8") as f:
        json.dump({"users":users},f,indent=4,ensure_ascii=False)


#登录验证密码
def login_check (ui , parent_window ,success_callback):
    username = ui.lineEdit_3.text()
    password = ui.lineEdit_2.text()

    users = load_users()

    if username in users and users[username] == password:
        QMessageBox.information(parent_window,"提示","登录成功")
        success_callback(parent_window)
    else:
        QMessageBox.warning(parent_window,"提示","密码错误")

#注册新账号

def register_users(ui,parent_window):
    username = ui.lineEdit.text()
    password = ui.lineEdit_6.text()
    password_1 = ui.lineEdit_5.text()
    if password !=password_1:
        QMessageBox.warning(parent_window,"提示","两个密码都不对")
        return 
    
    users = load_users()

    if username in users:
        QMessageBox.warning(parent_window,"提示","已经有了的账号，你注册干嘛")
        return 
    users[username] = password
    save_user(users)
    QMessageBox.information(parent_window,"提示","恭喜你注册成功了")

    ui.widget_3.hide()#消失
    ui.widget_2.show()#展示
    





