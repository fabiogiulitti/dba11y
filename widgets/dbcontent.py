from PyQt6.QtWidgets import QTextEdit, QSizePolicy
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtCore import Qt
from core.manager import getCntAction
from widgets.ContentData import ContentData
from core.ActonTypeEnum import ActonTypeEnum

class DbContent(QTextEdit):
    def __init__(self,parent):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.setAccessibleDescription("Content view")
        self.setAccessibleName("Content view box")
        self.setTabChangesFocus(True)
        #self.resize(400, 300)
        self.show()


    def refreshText(self, text):
        if self.isVisible == False:
            self.setVisible(True)
        #self.clear
        self.setText(text)

    def refreshData(self, data: ContentData):
        self.metaData = data.metaData
        self.refreshText(data.text)

    def keyPressEvent(self, event):
        if event.modifiers() == Qt.KeyboardModifier.ControlModifier and event.key() == Qt.Key.Key_PageDown:
            ctx = self.metaData
            ctx['action_type'] = ActonTypeEnum.PAGE_DOWN.value
            ctx['action_obj'] = 'edit'
            result: ContentData = getCntAction(ctx)
            if result is not None:
                self.refreshData(result)
        elif event.modifiers() == Qt.KeyboardModifier.ControlModifier and  event.key() == Qt.Key.Key_PageUp:
            ctx = self.metaData
            ctx['action_type'] = ActonTypeEnum.PAGE_UP.value
            ctx['action_obj'] = 'edit'
            result: ContentData = getCntAction(ctx)
            if result != None:
                self.refreshData(result)
        super().keyPressEvent(event)