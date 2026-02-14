import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel('Wpisz nazwe miasta: ',self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton('Pobierz pogodę', self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Pogodynka')
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family : calibri
            }
            QLabel#city_label{
                font-size: 30px;
            }
            QLineEdit#city_input{
                font-size: 30px
            }
            QPushButton#get_weather_button{
                font-size: 20px;
                font-weight: bold;
            }
            QLabel#temperature_label{
                font-size: 75px;
            }
            QLabel#emoji_label{
                font-size: 100px;
            }
            QLabel#description_label{
                font-size: 50px;
            }
        
        """)

        self.get_weather_button.clicked.connect(self.get_weather)
        self.adjustSize()
        self.setFixedSize(self.size())

        


    def get_weather(self):
        
        api_key = '1b38001e4a6cb0b9cc2067e772a73111'
        city = self.city_input.text()
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)
            else:
                self.display_error('Wystąpił błąd połączenia')


        except requests.exceptions.HTTPError:
            
            match response.status_code:
                case 404:
                    
                    self.display_error('Miasto nieznalezione, \nsprawdź poprawność wpisu')
        

    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size: 25px;")
        self.temperature_label.setText(message)



    def display_weather(self,data):
        temperature = round(data["main"]["temp"] - 273.15, 1)
        
        self.temperature_label.setStyleSheet("font-size: 100px;")
        self.temperature_label.setText(f'{temperature}°C')

      
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())