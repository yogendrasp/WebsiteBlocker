import time
from datetime import datetime as dt 


print('Hello')
#host_path_temp="E:\Python\Python-App\Website-blocker\hosts"
host_path="C:\Windows\System32\drivers\etc\hosts"
redirect= "127.0.0.1"
website_lists=["wwww.facebook.com","facebook.com","wwww.youtube.com","youtube.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,17):
        print('working hours')
        with open(host_path,'r+') as file:
            data=file.read()
            for dt in website_lists:
                if dt in data:
                    pass
                else:
                    file.write(redirect+" "+dt+"\n")        
    else: 
         with open(host_path,'r+') as file:
             dataline=file.readlines()
             file.seek(0)
             for line in dataline :
                if not any (website in line for website in website_lists):
                 file.write(line)
             file.truncate()
         print("Its not working hours")                   
    time.sleep(10)    


