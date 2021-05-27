import re
from threading import Thread

''' application modules '''
from Database.application_db import insert_file_detatils, check_process, login_check


''' Thread opration for operation to start '''
class Process(Thread):
    def __init__(self, filename,path):
        Thread.__init__(self)
        self.__filename = filename
        self.__path = path

    def run(self):
        filename = self.__filename
        filepath = self.__path
        print("file path and name is {0} {1}",filepath,filename)

def _login(username,password) -> bool:
    return login_check(username,password)


def _file_upload(guid,filename,path) -> bool:

    insert_file_detatils(guid,filename,path)
    thread_a = Process(guid,filename,path)
    thread_a.start()

    return True


def _check_process(process_id):
    result = check_process(process_id=process_id)
    try:
        if result[0][6] == 1:
            ### to do for opencv task ###
            return "processed_image_path"
        else:
            return "running"
    except:
        return "invalide process id..."
