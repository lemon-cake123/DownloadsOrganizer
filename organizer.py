#an app to sort the downloads folder
'''
Author : lemon-cake123
'''
import os
import shutil
import time
from datetime import datetime
import json

clock = datetime.now()
Downloads_folder = os.path.join(os.path.expanduser('~'),'downloads')

with open('logs.txt','w') as f:
    print(f"[{clock.ctime()}] created logs.txt")

try:
    with open('settings.json','r') as f:
        json_data = json.load(f)
        Document_types = json_data['settings']
except FileNotFoundError as e:
    #file does not exist,create it and use the following settings
    with open('settings.json','w') as f:
        f.write('''
{
	"Comment":"JSON file used for customizing DownloadsOrganizer format is folder_name:[list,of,extentions]",
	"settings":
	{
	"text documents":[".txt",".doc",".docx"],
        "PDF files":[".pdf"],
        "media files":[".jpeg",".jpg",".svg",".png",".PNG",".mp4",".mp3",".wav"],
        "compressed files":[".zip"],
        "powerpoint files":[".pptx",".ppt"],
        "excel files":[".xlsx",".xls"]
	}
}

''')
    Document_types={
        "text documents":[".txt",".doc",".docx"],
        "PDF files":[".pdf"],
        "media files":['.jpeg','.jpg','.svg','.png','.PNG',".mp4",".mp3",".wav"],
        "compressed files":['.zip'],
        "powerpoint files":['.pptx','.ppt'],
        "excel files":['.xlsx','.xls'],
        }
    
with open('logs.txt','a') as f:
    while True:
        try:
            #code here
            if os.listdir(Downloads_folder):
                f.write(f'\n [{clock.ctime()}] files in downloads folder detected')
                for folder in Document_types.keys():
                    try:
                        os.mkdir(os.path.join(Downloads_folder,folder))
                        f.write(f'\n [{clock.ctime()}] created folder : {folder}')
                    except FileExistsError as e:
                        pass

                try:
                    os.mkdir(os.path.join(Downloads_folder,"other files"))
                    f.write(f'\n [{clock.ctime()}] created folder : other files')
                    
                except FileExistsError as e:
                    pass
                
                with os.scandir(Downloads_folder) as entries:
                    for entry in entries:
                        f.write(f"\n [{clock.ctime()}] preparing to move {entry.name}")
                        if entry.is_file:
                            moved = False

                            for key,value in Document_types.items():
                                if os.path.splitext(entry)[1] in value:
                                    if not os.path.exists(os.path.join(Downloads_folder,key,entry)):
                                        shutil.move(entry,os.path.join(Downloads_folder,key))
                                        moved = True
                                        f.write("\n [{clock.ctime()}] moved {entry.name} to {key}")
                                    else:
                                        f.write(f"\n [{clock.ctime()}] {entry.name} already exist in {key}, aborted move")
                                        moved = True # to avoid moving to other files
                                        
                            
                                
                            
                            if not moved:
                                if not entry.is_dir():
                                    if not os.path.exists(os.path.join(Downloads_folder,"other files",entry)):
                                        
                                        shutil.move(entry,os.path.join(Downloads_folder,"other files"))
                                        f.write(f'\n [{clock.ctime()}] moved entry {entry.name} to other files')
                                    else:
                                        f.write(f"\n [{clock.ctime()}] {entry.name} already exist in other files, aborted move")
                                else:
                                    f.write(f'\n [{clock.ctime()}] {entry.name} was a folder. aborted move')
                                                       
                    
                
            time.sleep(300)
            clock = datetime.now()
        except Exception as exc:
            f.write(f'\n [{clock.ctime()}] FATAL: {exc}, aborting task')
            f.close()
            exit()
            
            
    
    
