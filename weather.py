from tkinter import *
import requests
import json

root = Tk()
root.title('Air Quality Widget')
root.geometry('400x40')

try:
	api_request = requests.get('https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=3&API_KEY=780A1A21-FCDC-41EC-8123-586D0525F8BE')
	api = json.loads(api_request.content)
	city = api[0]['ReportingArea']
	quality = api[0]['AQI']
	category = api[0]['Category']['Name']

except Exception as e:
	api = 'Error'

label = Label(root, text=city + ', Air Quality ' + str(quality) + ', ' + category, font=('Helvetica', 20), background='lightgreen')
label.pack()

root.mainloop()