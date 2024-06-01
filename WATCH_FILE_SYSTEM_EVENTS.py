import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

source="c:/Users/Admin/Downloads"
desti="C:/Users/Admin/Desktop/C Pro/C103_P/C103"

dir_tree={
"Image_Files":[".png",".jpg",".gif",".jfig",".jpeg"],
"Video_Files":[".mp4",".avi","mpe4"],
"Docunent_Fils":[".xls",".ppt",".pdf"],
"Setup_Files":[".exe",".bin"]
}

class FileMovementHandler(FileSystemEventHandler):
    def on_created(self, event):
        name,extension=os.path.splitext(event.src_path)
        time.sleep(1)
        for key,value in dir_tree.items():
            if extension in value:
                file_name=os.path.basename(event.src_path)
                print("File Downloade"+file_name)
                path1=source + '/' + file_name
                path2=desti + '/' + key
                path3=desti + '/' + key + '/' + file_name
                print (path1,path1)
                print(path3,path3)
                if os.path.exists(path2):
                    print("Moving " + file_name)
                    shutil.move(path1,path3)
                    time.sleep(1)
                else:
                    os.mkdir(path2)
                    print("Moving" + file_name)
                    shutil.move(path1,path3)
                    time.sleep(1)                    
    def on_modified(    self, event):
        name,extension=os.path.splitext(event.src_path)
        time.sleep(1)
        for key,value in dir_tree.items():
            if extension in value:
                file_name=os.path.basename(event.src_path)
                print("File Downloade"+file_name)
                path1=source + '/' + file_name
                path2=desti + '/' + key
                path3=desti + '/' + key + '/' + file_name
                print (path1,path1)
                print(path3,path3)
                if os.path.exists(path2):
                    print("Moving " + file_name)
                    shutil.move(path1,path3)
                    time.sleep(1)
                else:
                    os.mkdir(path2)
                    print("Moving" + file_name)
                    shutil.move(path1,path3)
                    time.sleep(1)
    

event_handler=FileMovementHandler()
observer=Observer() 
observer.schedule(event_handler,source,recursive=True)
observer.start()
try:
    while True:
        time.sleep(2)
        print("Running")

except KeyboardInterrupt:
    print("Stop")
    observer.stop()