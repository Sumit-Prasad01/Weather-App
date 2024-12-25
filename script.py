import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton, QHBoxLayout
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt

# Your OpenWeather API key
API_KEY = ""  # Replace with your actual API key

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Weather App")
        self.setGeometry(100, 100, 500, 400)  
        
        
        self.init_ui()
        
    def init_ui(self):
        
        self.city_input = QLineEdit(self)
        self.city_input.setPlaceholderText("Enter city name")
        self.city_input.setStyleSheet("font-size: 18px; padding: 10px; color: white; background-color: #333; border-radius: 5px;")
        
        self.search_button = QPushButton("Get Weather", self)
        self.search_button.setStyleSheet("""
            font-size: 18px;
            background-color: #4CAF50;
            color: white;
            padding: 10px;
            border-radius: 5px;
        """)
        self.search_button.clicked.connect(self.get_weather)
        
        
        self.weather_label = QLabel("Weather Info will be displayed here.", self)
        self.weather_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #4CAF50;")
        
        self.temp_label = QLabel("", self)
        self.temp_label.setStyleSheet("font-size: 20px; color: #4CAF50;")
        
        self.humidity_label = QLabel("", self)
        self.humidity_label.setStyleSheet("font-size: 20px; color: #4CAF50;")
        
        self.description_label = QLabel("", self)
        self.description_label.setStyleSheet("font-size: 20px; color: #4CAF50;")
        
        self.wind_speed_label = QLabel("", self)
        self.wind_speed_label.setStyleSheet("font-size: 20px; color: #4CAF50;")
        
        
        self.weather_image = QLabel(self)
        self.weather_image.setAlignment(Qt.AlignCenter)
        
        
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)  # Add padding to the layout
        
        
        layout.addWidget(self.city_input)
        layout.addWidget(self.search_button)
        layout.addWidget(self.weather_image, alignment=Qt.AlignCenter)
        layout.addWidget(self.weather_label)
        layout.addWidget(self.temp_label)
        layout.addWidget(self.humidity_label)
        layout.addWidget(self.description_label)
        layout.addWidget(self.wind_speed_label)
        
        
        self.setLayout(layout)
        self.setStyleSheet("""
            background-color: #121212;  # Black background
            color: white;               # White text for general elements
            border-radius: 10px;
        """)
    
    def get_weather(self):
        city = self.city_input.text()
        
      
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}"
        
        
        response = requests.get(url)
        
        
        if response.status_code == 200:
            data = response.json()
            
            
            city_name = data['name']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            description = data['weather'][0]['description']
            wind_speed = data['wind']['speed']
            icon_code = data['weather'][0]['icon']
            
           
            self.weather_label.setText(f"Weather in {city_name}:")
            self.temp_label.setText(f"Temperature: {temperature}°C")
            self.humidity_label.setText(f"Humidity: {humidity}%")
            self.description_label.setText(f"Description: {description}")
            self.wind_speed_label.setText(f"Wind Speed: {wind_speed} m/s")
            
           
            icon_url = f"http://openweathermap.org/img/wn/{icon_code}.png"
            icon = QPixmap()
            icon.loadFromData(requests.get(icon_url).content)
            self.weather_image.setPixmap(icon)
        else:
           
            self.weather_label.setText("Error: City not found or invalid API key.")
            self.temp_label.clear()
            self.humidity_label.clear()
            self.description_label.clear()
            self.wind_speed_label.clear()
            self.weather_image.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    sys.exit(app.exec_())
