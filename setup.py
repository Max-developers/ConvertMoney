#!/usr/bin/python3 

import requests 
import json
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import (QWidget, QLabel,
    QComboBox, QApplication,QLineEdit)
from PyQt5.QtWidgets import QMessageBox
import math
# import re 

Form, _ = uic.loadUiType("gui.ui")

class Ui(QtWidgets.QDialog, Form):
      def __init__(self):
         super(Ui,self).__init__()
         self.setupUi(self)
         self.pushButton.clicked.connect(self.exchange)

         self.textEdit.setPlainText('0') 
         self.label_2.setAlignment(Qt.AlignCenter) 
         self.label_3.setAlignment(Qt.AlignCenter) 
         self.comboBox.activated.connect(self.currency1)
         self.comboBox_2.activated.connect(self.currency2)

         self.comboBox.addItem('ДОЛЛАР') 
         self.comboBox.addItem('ЕВРО') 
         self.comboBox.addItem('РУБЛЬ')  
         self.comboBox.addItem('БЕЛ.РУБЛЬ') 
         self.comboBox.addItem('ГРИВНА') 
         self.comboBox.addItem('ТЕНГЕ')  
         self.comboBox.addItem('ЮАНЬ')
         self.comboBox.addItem('ЯП.ИЕНА')
         self.comboBox.addItem('ДИРХАМ')
         self.comboBox.addItem('АВСТ.ДОЛЛАР')
         self.comboBox.addItem('КАН.ДОЛЛАР')
         self.comboBox.addItem('ФУНТ СТЕРЛ.')
         self.comboBox.addItem('ШВЕЙ.ФРАНК')
         self.comboBox.addItem('BITCOIN') 
         self.comboBox.addItem('BITCOIN CASH')  
         self.comboBox.addItem('LITECOIN') 
         self.comboBox.addItem('ETHEREUM')  
         self.comboBox.addItem('ETHEREUM CL.')  
         self.comboBox.addItem('DASH') 
         self.comboBox.addItem('MONERO')  
         self.comboBox.addItem('Zcash')  
         self.comboBox.addItem('RIPPLE')  
         self.comboBox.addItem('DOGECOIN')  
         self.comboBox.addItem('TRON')  

         self.comboBox_2.addItem('РУБЛЬ')  
         self.comboBox_2.addItem('ДОЛЛАР')  
         self.comboBox_2.addItem('ЕВРО')        
         self.comboBox_2.addItem('БЕЛ.РУБЛЬ') 
         self.comboBox_2.addItem('ГРИВНА') 
         self.comboBox_2.addItem('ТЕНГЕ')  
         self.comboBox_2.addItem('ЮАНЬ')
         self.comboBox_2.addItem('ЯП.ИЕНА')
         self.comboBox_2.addItem('ДИРХАМ')
         self.comboBox_2.addItem('АВСТ.ДОЛЛАР')
         self.comboBox_2.addItem('КАН.ДОЛЛАР')
         self.comboBox_2.addItem('ФУНТ СТЕРЛ.')
         self.comboBox_2.addItem('ШВЕЙ.ФРАНК')
         self.comboBox_2.addItem('BITCOIN') 
         self.comboBox_2.addItem('BITCOIN CASH')  
         self.comboBox_2.addItem('LITECOIN')  
         self.comboBox_2.addItem('ETHEREUM')  
         self.comboBox_2.addItem('ETHEREUM CL.') 
         self.comboBox_2.addItem('DASH')  
         self.comboBox_2.addItem('MONERO') 
         self.comboBox_2.addItem('Zcash')  
         self.comboBox_2.addItem('RIPPLE')  
         self.comboBox_2.addItem('DOGECOIN')  
         self.comboBox_2.addItem('TRON')  

         self.comboBox.view().setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
         self.comboBox_2.view().setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

         global currency1
         currency1 = 'USD'

         global currency2
         currency2 = 'RUB'

        
      def currency1(self):
          global currency1
          get_text1 = self.comboBox.currentText() 
          if get_text1 == 'РУБЛЬ': currency1 = 'RUB'
          if get_text1 == 'БЕЛ.РУБЛЬ': currency1 = 'BYN'
          if get_text1 == 'ДОЛЛАР': currency1 = 'USD'
          if get_text1 == 'ЕВРО': currency1 = 'EUR'
          if get_text1 == 'ТЕНГЕ': currency1 = 'KZT'
          if get_text1 == 'ГРИВНА': currency1 = 'UAH'
          if get_text1 == 'ЮАНЬ': currency1 = 'CNY'
          if get_text1 == 'ЯП.ИЕНА': currency1 = 'JPY'
          if get_text1 == 'ДИРХАМ': currency1 = 'AED'
          if get_text1 == 'АВСТ.ДОЛЛАР': currency1 = 'AUD'
          if get_text1 == 'КАН.ДОЛЛАР': currency1 = 'CAD'
          if get_text1 == 'ФУНТ СТЕРЛ.': currency1 = 'GBP'
          if get_text1 == 'ШВЕЙ.ФРАНК': currency1 = 'CHF'
          if get_text1 == 'BITCOIN': currency1 = 'BTC'
          if get_text1 == 'BITCOIN CASH': currency1 = 'BCH'
          if get_text1 == 'LITECOIN': currency1 = 'LTC'
          if get_text1 == 'ETHEREUM': currency1 = 'ETH'
          if get_text1 == 'ETHEREUM CL.': currency1 = 'ETC'
          if get_text1 == 'DASH': currency1 = 'DASH'
          if get_text1 == 'MONERO': currency1 = 'XMR'
          if get_text1 == 'Zcash': currency1 = 'ZEC'
          if get_text1 == 'RIPPLE': currency1 = 'XRP'
          if get_text1 == 'DOGECOIN': currency1 = 'DOGE'
          if get_text1 == 'TRON': currency1 = 'TRX'
          self.label.setText(currency1)
          
          get_text2 =self.label_2.text()
          get_text2 = get_text2.split('=>')
          self.label_2.setText(currency1+' =>'+get_text2[1])

      def currency2(self):
          global currency2
          get_text1 = self.comboBox_2.currentText() 
          if get_text1 == 'РУБЛЬ': currency2 = 'RUB'
          if get_text1 == 'БЕЛ.РУБЛЬ': currency1 = 'BYN'
          if get_text1 == 'ДОЛЛАР': currency2 = 'USD'
          if get_text1 == 'ЕВРО': currency2 = 'EUR'
          if get_text1 == 'ТЕНГЕ': currency2 = 'KZT'
          if get_text1 == 'ГРИВНА': currency2 = 'UAH'
          if get_text1 == 'ЮАНЬ': currency2 = 'CNY'
          if get_text1 == 'ЯП.ИЕНА': currency2 = 'JPY'
          if get_text1 == 'ДИРХАМ': currency2 = 'AED'
          if get_text1 == 'АВСТ.ДОЛЛАР': currency2 = 'AUD'
          if get_text1 == 'КАН.ДОЛЛАР': currency2 = 'CAD'
          if get_text1 == 'ФУНТ СТЕРЛ.': currency2 = 'GBP'
          if get_text1 == 'ШВЕЙ.ФРАНК': currency2 = 'CHF'
          if get_text1 == 'BITCOIN': currency2 = 'BTC'
          if get_text1 == 'BITCOIN CASH': currency2 = 'BCH'
          if get_text1 == 'LITECOIN': currency2 = 'LTC'
          if get_text1 == 'ETHEREUM': currency2 = 'ETH'
          if get_text1 == 'ETHEREUM CL.': currency2 = 'ETC'
          if get_text1 == 'DASH': currency2 = 'DASH'
          if get_text1 == 'MONERO': currency2 = 'XMR'
          if get_text1 == 'Zcash': currency2 = 'ZEC'
          if get_text1 == 'RIPPLE': currency2 = 'XRP'
          if get_text1 == 'DOGECOIN': currency2 = 'DOGE'
          if get_text1 == 'TRON': currency2 = 'TRX'
          self.label_3.setText('0'+' '+currency2)
          get_text2 =self.label_2.text() 
          get_text2 = get_text2.split('=>')
          self.label_2.setText(get_text2[0]+'=> '+currency2)

      def exchange(self):
          
          url = 'https://min-api.cryptocompare.com/data/price?fsym='+currency1+'&tsyms='+currency2+''
          
          try:
             examination = self.textEdit.toPlainText()
             float(examination) 
             try:
                resp = requests.get(url=url,timeout=3)
                data = json.loads(resp.text)
                data = data[currency2]
                number = self.textEdit.toPlainText() 
                result = float(number)*float(data)
                result = round(result,2) 
                self.label_3.setText(str(result)+' '+currency2)
             except: 
                msg = QMessageBox()
                msg.setWindowTitle("ОШИБКА!")
                msg.setText("Нет подключения к интернету")
                msg.setIcon(QMessageBox.Warning)
                msg.exec_()
          except:
                msg = QMessageBox()
                msg.setWindowTitle("ОШИБКА!")
                msg.setText("Неправильный формат данных")
                msg.setIcon(QMessageBox.Warning)
                msg.exec_()


if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Ui()
    w.show()
    sys.exit(app.exec_())
