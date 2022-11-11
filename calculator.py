import re
import sys
from PyQt5.QtWidgets import QWidget,QPushButton,QLineEdit,QGridLayout,QMessageBox,QApplication
from PyQt5.QtCore import Qt,QSize
from PyQt5.QtGui import QFont
 
class Example(QWidget):
    def __init__(self):
        super().__init__()
 
        self.initUI()
 
        self.move(300,150)
        self.setWindowTitle("Calculator")
        self.show()
 
    def initUI(self):
 
        self.string = ''
        self.number = '0'
        self.out='0'
 
        grid = QGridLayout()
        self.display = QLineEdit('0')
 
        self.display.setFont(QFont("Times", 20)) # set font
        self.display.setReadOnly(True) # Set editable
        self.display.setAlignment(Qt.AlignRight) # Set the text position, set to the right here
        self.display.setMaxLength(50) # set the maximum length
        grid.addWidget(self.display, 0, 0, 1, 4)
 
        names = ['Clear', 'Del', '(', ')',
                '7', '8', '9', '/',
                '4', '5', '6', '*',
                '1', '2', '3', '-',
                '0', '.', '=', '+']
        pos = [(0, 0), (0, 1), (0, 2), (0, 3),
                (1, 0), (1, 1), (1, 2), (1, 3),
                (2, 0), (2, 1), (2, 2), (2, 3),
                (3, 0), (3, 1), (3, 2), (3, 3 ),
                (4, 0), (4, 1), (4, 2), (4, 3)]
 
        c = 0
        for name in names:
            button = QPushButton(name)
                         #Key size setting
            button.setFixedSize(QSize(60,30))
                         # Set signal/slot for each button
            button.clicked.connect(self.Calculator)
                         # Determine the position of the graphic button by calling the pos row
            grid.addWidget(button, pos[c][0]+1, pos[c][1])
            c=c+1
        self.setLayout(grid)
 
    def Calculator(self):
        text=self.sender().text()
        #print(text)
 
        if text=="Del":#Slice, press down one bit at a time
            self.string=self.number
            self.number=self.number[:-1]
 
        elif text=="Clear":#set 0
            self.number='0'
 
        elif text=="=":#If you enter the equal sign calculation
            print("Number string to be calculated", self.number)
            self.out=calculate(self.number)
            self.out=self.out[:12]
            self.number='0'
            print(self.out)
 
        else:#In other cases, accumulate characters
            if (self.number=='0'):
                self.number=''
            self.number=self.number+text
            print(self.number)
 
                 #Different displays under different conditions
        while self.number == '0' and self.out!='0':
            self.display.setText(self.out)
            break
        while self.number != '0' or text=='Clear':
            self.display.setText(self.number)
            break
 
    def closeEvent(self,event):
        reply=QMessageBox.question(self,"Message","Are you sure to quit?", QMessageBox.Yes,QMessageBox.No)
        if reply==QMessageBox.Yes:
            event.accept()
        else:
            event.ignore() 
 
def refresh_formula(formula):
    formula = formula.replace(" ","")
    formula = formula.replace("+-","-")
    formula = formula.replace("-+","-")
    formula = formula.replace("--","+")
    return formula 
 
def total_calc(formula):
 
    def devide(formula):
        """"""
        devidestr = re.search('\d+\.?\d*(\/-?\d+\.?\d*)+', formula)
        if devidestr is None:
            return formula
        devidenum = re.findall('-?\d+\.?\d*', devidestr.group())
        devidelist = []
        for i in devidenum:
            devidelist.append(float(i))
        res = devidelist[0]
        for i in range(1, len(devidelist)):
            res = res / devidelist[i]
        formula = re.sub('\d+\.?\d*(\/-?\d+\.?\d*)+', str(res), formula, 1)
        return formula
 
    def multiply(formula):
        """"""
        multiplystr = re.search('\d+\.?\d*(\*-?\d+\.?\d*)+', formula)
        if multiplystr is None:
            return formula
        multiplynum = re.findall(r'-?\d+\.?\d*', multiplystr.group())
        multiplylist = []
        res = 1
        for i in multiplynum:
            multiplylist.append(float(i))
        for i in range(len(multiplylist)):
            res = res * multiplylist[i]
        formula = re.sub(r'\d+\.?\d*(\*-?\d+\.?\d*)+', str(res), formula, 1)
        return formula
 
    formula = refresh_formula(formula)
    res = 0
    while True:
 
        if '*' in formula:
            mul = formula.split("*")
            #print("mul",mul)
            if '/' in mul[0]:
                formula = devide(formula)
                #print("devide",formula)
            else:
                formula = multiply(formula)
                #print("multiply",formula)
 
        elif '/' in formula:
            formula = devide(formula)
  
        elif'+' or'-' in formula:#addition and subtraction
            addminus = re.findall('-?\d+\.?\d*',formula)
            #print("addminus",addminus)
            res = 0
            for digit in addminus:
                res = res + float(digit)
            return str(res)
 
        else:
            return res
 
def bracket_calc(bracketstr):
    bracketstr = bracketstr.replace("\(","")
    bracketstr = bracketstr.replace("\)","")
    return total_calc(bracketstr)
 
def calculate(formula):
    while True:
                 #Operation priority search
        bracket = re.search("\(([^()]+)\)",formula)
        # print("formula",formula)
        # print("bracket",bracket)
        if bracket:
            bracket = bracket.group()
            #print("BRACK",bracket)
            res = bracket_calc(bracket)
            #print("（）result is：%s" % res)
            formula = formula.replace(bracket,res)
        else:
            res = total_calc(formula)
            print("result is %s" % res)
            return res
 
if __name__=="__main__":
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())