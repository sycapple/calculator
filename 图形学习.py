
from PySide2.QtWidgets import QApplication, QWidget, QFileDialog, QVBoxLayout, QLineEdit, QTextEdit
from PySide2.QtUiTools import QUiLoader

expression = ''


class UI:

    def __init__(self):
        global expression
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('untitled.ui')
        self.ui.Button_1.clicked.connect(self.Add_Number(lambda: self.Add_Number(self.ui.Button_1.text())))
        self.ui.Button_2.clicked.connect(self.Add_Number(lambda: self.Add_Number(self.ui.Button_1.text())))
        self.ui.Button_3.clicked.connect(self.Add_Number(lambda: self.Add_Number(self.ui.Button_1.text())))
        self.ui.Button_4.clicked.connect(self.Add_Number(lambda: self.Add_Number(self.ui.Button_1.text())))
        self.ui.Button_5.clicked.connect(self.Add_Number(lambda: self.Add_Number(self.ui.Button_1.text())))
        self.ui.Button_6.clicked.connect(self.Add_Number(lambda: self.Add_Number(self.ui.Button_1.text())))
        self.ui.Button_7.clicked.connect(self.Add_Number(lambda: self.Add_Number(self.ui.Button_1.text())))
        self.ui.Button_8.clicked.connect(self.Add_Number(lambda: self.Add_Number(self.ui.Button_1.text())))
        self.ui.Button_9.clicked.connect(self.Add_Number(lambda: self.Add_Number(self.ui.Button_1.text())))
        self.ui.Button_0.clicked.connect(self.Add_Number(lambda: self.Add_Number(self.ui.Button_1.text())))
        self.ui.Button_point.clicked.connect(self.Add_Number(lambda: self.Add_Number(self.ui.Button_1.text())))
        self.ui.Button_left.clicked.connect(self.Add_Number(lambda: self.Add_Number(self.ui.Button_1.text())))
        self.ui.Button_right.clicked.connect(self.Add_Number(lambda: self.Add_Number(self.ui.Button_1.text())))
        self.ui.Button_up.clicked.connect(self.Add_Number(lambda: self.Add_Number(self.ui.Button_1.text())))
        self.ui.Button_divide.clicked.connect(self.Add_Number(lambda: self.Add_Number(self.ui.Button_1.text())))
        self.ui.Button_multiply.clicked.connect(self.Add_Number(lambda: self.Add_Number(self.ui.Button_1.text())))
        self.ui.Button_minus.clicked.connect(self.Add_Number(lambda: self.Add_Number(self.ui.Button_1.text())))
        self.ui.Button_and.clicked.connect(self.Add_Number(lambda: self.Add_Number(self.ui.Button_1.text())))

        self.ui.Button_OK.clicked.connect(self.calculate())
        self.ui.Button_del.clicked.connect(self.DEL())
        self.ui.Button_ce.clicked.connect(self.CE())

        self.textbox = self.ui.findChild(QLineEdit, "textBrowser")
        self.edit_text = self.ui.findChild(QTextEdit, "textBrowser")
        self.textbox.textChanged.connect(self.text_changed)

    def text_changed(self, text):
        global expression
        expression = text

    def renew(self):
        global expression
        self.edit_text.setText(expression)

    def calculate(self):
        pass

    def DEL(self):
        global expression
        expression = expression[:-1]
        self.renew()

    def CE(self):
        global expression
        expression = ''
        self.renew()

    def Add_Number(self, button_text):
        pass
        # global expression
        # expression = expression + button_text
        # self.renew()



app = QApplication([])
stats = UI()
stats.ui.show()
app.exec_()

