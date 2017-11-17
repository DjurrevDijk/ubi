from ubidots import ApiClient
import random
import math

#Create an "API" 
api = ApiClient(token='A1E-wim4tBnYi78zW9Iqk32FsuXYjYYAJ3')

api.save_collection([
  {'variable': '5a09742ec03f975beec2f99e', 'value': 10*math.sin(10)}, 
  {'variable': '5a0ac048c03f9771162a8cf4', 'value': 20*math.sin(10)},
  {'variable': '5a0ac030c03f977114738e0b', 'value': 20*math.sin(10)}
])
