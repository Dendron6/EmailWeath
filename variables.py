import pandas as pd
#retrieve all the private info from notifications
file = pd.read_excel('notification.xlsx')
apiKey = file.apikey[0]
email = file.username[0]
password = file.password[0]
sendto = file.username[1]