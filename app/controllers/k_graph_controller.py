from PyQt5 import QtCore
from PyQt5.QtCore import QObject, QEvent


class KGraphEvents(QObject):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.parent = parent
        self.app = app

    def eventFilter(self, source: QObject, event: QEvent):
        if event.type() == QtCore.QEvent.FocusOut:
            self.save_scratch_pad()

        return super().eventFilter(source, event)

    def save_graph_state(self):
        # scratch = self.parent.txt_scratch_pad.toPlainText()
        # self.app.data.update_scratch_note(scratch)
        nodes = self.parent.nodes
        self.app.data.update_graph_store(nodes)


class KGraphController:
    def __init__(self, parent, app):
        self.parent = parent
        self.app = app
        self.events = KGraphEvents(self.parent, self.app)

        # self.parent.txt_scratch_pad.installEventFilter(self.events)

    def init(self):
        nodes = self.app.data.nodes()
        #self.parent.txt_scratch_pad.setPlainText(scratch_note)

    def save_graph_state(self):
        self.events.save_graph_state()