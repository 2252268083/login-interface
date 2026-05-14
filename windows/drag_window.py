from PyQt5.QtCore import Qt,QPoint

class DragaMixin:
    def __init__(self):
        # super().__init__()#初始化父类
        self._drag_pos=None#用来记录拖拽的起始坐标

    def mousePressEvent(self,event):#鼠标在屏幕全局坐标
        if event.button() == Qt.LeftButton:#event是窗口的位置
            #记录鼠标相对于窗口左上角的位置
            self._drag_pos = event.globalPos() - self.frameGeometry().topLeft()#frameGeometry().topLeft()当前窗口左上角在「整个电脑屏幕」上的坐标点
            event.accept()
        # super().mousePressEvent(event)#调用父类的鼠标按下事件处理方法，保留默认行为 + 保证事件正常传递。
    
    def mouseMoveEvent(self,event):
        if event.buttons() == Qt.LeftButton and self._drag_pos:#仅左键按下时才执行拖拽（移动事件中用 buttons() 检测持续按键状态）。
            #移动窗口,左键按住 + 已记录偏移量 → 执行拖拽
            self.move(event.globalPos() - self._drag_pos)
            event.accept()
        # super().mouseMoveEvent(envent)

    def mouseReleaseEvent(self, event):
        self._drag_pos = None
        # super().mouseReleaseEven(event)
