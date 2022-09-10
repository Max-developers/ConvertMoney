#!/usr/bin/python3 

import requests 
import json
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import (QWidget, QLabel,
    QComboBox, QApplication,QLineEdit)
from PyQt5.QtWidgets import QMessageBox
import math


Form, _ = uic.loadUiType("untitled.ui")

Text_file = 'list'

class Ui(QtWidgets.QMainWindow,Form):
      def __init__(self):
         super(Ui,self).__init__()
         self.setupUi(self)

         self.pushButton.clicked.connect(self.exchange)    #Запускаем функцию exchange
         self.lineEdit.setText('0')                        #Устанавливаем текст в поле
         self.label_2.setAlignment(Qt.AlignCenter)         #Устанавливаем текст по центру
         self.label_3.setAlignment(Qt.AlignCenter)         #Устанавливаем текст по центру
         self.comboBox.activated.connect(self.currency1)   #При клике Combo - запускаем функцию currency1
         self.comboBox_2.activated.connect(self.currency2) #При клике Combo - запускаем функцию currency2

         
         #Заполняем ComboBox из списка
         counter = 0
         txt = open(Text_file,'r')
         for line in txt:
             try:                                
               line = line.strip().split('|')[1] 
             except: break
             self.comboBox.addItem(line)         
             end = line
             if counter == 0: bufer = line
             if counter == 1: self.comboBox_2.addItem(line)
             if counter == 2: self.comboBox_2.addItem(bufer)
             if counter  > 2: self.comboBox_2.addItem(bufer)
             counter +=1
             if counter  > 2: bufer = line
         self.comboBox_2.addItem(end) 
         txt.close()


         #Добавляем скролл в СomboBox
         self.comboBox.view().setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
         self.comboBox_2.view().setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
         

         global currency1
         global currency2
         
         #Устанавливаем валюты по умолчанию(доллар к рублю)
         f = open(Text_file,'r')
         currency = f.readlines()
         currency1 = currency[0].strip().split('|')[0]
         currency2 = currency[1].strip().split('|')[0]
         f.close()


      #Получаем сокращённое обозначение валюты
      def serch(self,arg):
          f = open(Text_file,'r')
          for line in f: 
              if arg == line.strip().split('|')[1]:
                 f.close() 
                 return line.strip().split('|')[0] 
   

      #Устанавливаем код валюты в переменную и обновляем параметры в форме
      def currency1(self):
          global currency1
          get_text1 = self.comboBox.currentText() 
          currency1 = self.serch(get_text1)
          self.label.setText(currency1) 
          self.label_2.setText(currency1+' => '+currency2)


      #Устанавливаем код валюты в переменную и обновляем параметры в форме
      def currency2(self):
          global currency2
          get_text1 = self.comboBox_2.currentText() 
          currency2 = self.serch(get_text1)
          self.label_3.setText('0'+' '+currency2)   
          self.label.setText(currency1)
          self.label_2.setText(currency1+' => '+currency2)


      #Функция для вывода сообщения об ошибки    
      def error(self,arg):
          msg = QMessageBox()
          msg.setWindowTitle("ОШИБКА!")
          msg.setText(arg)
          msg.setIcon(QMessageBox.Warning)
          msg.exec_()


      #Функция для форматирования чисел
      def divider(self,number):
          check_type = isinstance(number, float)
          if check_type == True:
             number = round(number, 2)
             number = str(number)      
             number1 = number.split('.')
             number = number1[0]        
          else: number = str(number)    
          if len(number) > 3:
             counter = 0               
             result=''                
             number = number[::-1]     
             for li in number:
                counter += 1          
                result = result + li   
                if counter == 3:       
                   result = result +' '
                   counter = 0         
             result = result[::-1]     
             result = result.strip()  
          else: result = number 
          if check_type == True and number1[1] != '0': return result+','+number1[1] 
          else: return result 
          

      #Функция подаёт запрос на сервис для получения текущего курса валюты 
      def exchange(self):
         try:
             try:
                 url = 'https://min-api.cryptocompare.com/data/price?fsym='+currency1+'&tsyms='+currency2
                 resp = requests.get(url=url,timeout=3)
             except: 
                    self.error('Нет подключения к интернету')
                    return 
             data = json.loads(resp.text)
             result = data[currency2]
             result2 = float(result)
             result2 = '{0:0.8f}'.format(result2)

             if float(result2) < 1:
                result = float(result2)
                result = result * float(self.lineEdit.text())
                self.label_3.setText('{0:0.8f}'.format(result)+' '+currency2)
             else: 
                 result = result * float(self.lineEdit.text())
                 result = self.divider(result)
                 self.label_3.setText(str(result)+' '+currency2)
         except: self.error('Неправильный формат данных')




if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Ui()
    w.show()
    sys.exit(app.exec_())

    
