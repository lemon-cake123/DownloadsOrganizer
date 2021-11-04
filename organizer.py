#an app to sort the downloads folder
import os
import shutil
import time
from datetime import datetime

clock = datetime.now()
Downloads_folder = os.path.join(os.path.expanduser('~'),'downloads')

with open('logs.txt','w') as f:
    print(f"[{clock.ctime()}] created logs.txt")

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
                            if os.path.splitext(entry)[1] in Document_types['text documents']:
                                shutil.move(entry,os.path.join(Downloads_folder,"text documents"))
                                f.write(f'\n [{clock.ctime()}] moved entry {entry.name} to text documents')                            
                            elif os.path.splitext(entry)[1] in Document_types['PDF files']:
                                shutil.move(entry,os.path.join(Downloads_folder,"PDF files"))
                                f.write(f'\n [{clock.ctime()}] moved entry {entry.name} to PDF files')

                            elif os.path.splitext(entry)[1] in Document_types['media files']:
                                shutil.move(entry,os.path.join(Downloads_folder,"media files"))
                                f.write(f'\n [{clock.ctime()}] moved entry {entry.name} to media files')

                            elif os.path.splitext(entry)[1] in Document_types['compressed files']:
                                shutil.move(entry,os.path.join(Downloads_folder,"compressed files"))
                                f.write(f'\n [{clock.ctime()}] moved entry {entry.name} to compressed files')
                                
                            else:
                                if not entry.is_dir():
                                    
                                    shutil.move(entry,os.path.join(Downloads_folder,"other files"))
                                    f.write(f'\n [{clock.ctime()}] moved entry {entry.name} to other files')
                                else:
                                    f.write(f'\n [{clock.ctime()}] {entry.name} was a folder. aborted move')
                                    
                    
                
            time.sleep(300)
            clock = datetime.now()
        except Exception as exc:
            f.write(f'\n [{clock.ctime()}] FATAL: {exc}, aborting task')
            f.close()
            exit()
            
            
    
    
