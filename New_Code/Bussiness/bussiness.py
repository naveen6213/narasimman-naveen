import configparser as cp
import json
from threading import Thread
import os


''' Application modules '''
from objectDetection import inference



''' Get user name and password from config '''
parser = cp.SafeConfigParser()
parser.read(os.getcwd()+"\Bussiness\login.ini")

_user = parser.get('login', 'user')
_password = parser.get('login', 'password')


''' Thread opration for operation to start '''
class Process(Thread):
    def __init__(self, imgage_file,file_name,json_file_name):
        Thread.__init__(self)
        self.__imgage_file = imgage_file
        self.__file_name = file_name
        self.__json_file_path = json_file_name

    def run(self):
        #print("file path and name is {0} {1}",filepath,filename)
        output_path = os.getcwd()+"/static/output/"+self.__file_name+"__.jpg"
        inference.detect_object(self.__imgage_file,output_path)
        
        with open(self.__json_file_path, "r") as jsonFile:
            data = json.load(jsonFile)
        
        data["status"] = True
        data["ouputFilePath"] = self.__file_name+"__.jpg"
        
        jsonFile = open(self.__json_file_path, "w+")
        jsonFile.write(json.dumps(data))
        jsonFile.close()   

''' applicatoin logni functionality '''
def _login(userName,password)->bool:
    try:
        ''' user name and password check '''
        if userName == _user and password == _password:
            return True
        else:
            return False
    except Exception as ex:
        print(ex)

''' after upload image generate sjon file for status maintain '''
def fileupload(guid,filePath,fileName) -> str:

    try:
        file_object ={
            "guid" : guid,
            "filePath" : filePath,
            "fileName" : fileName,
            "status" : False,
            "ouputFilePath":""
        }

        file_object_json = json.dumps(file_object, indent = 4)

        json_file_name = os.getcwd()+"/json_dumps/"+guid+".json"

        with open(json_file_name, "w") as outfile:
            outfile.write(file_object_json)

        thread_a = Process(filePath+fileName,guid,json_file_name)
        thread_a.start()

        return guid
    except Exception as ex:
        print(ex)
        return ""

''' check the process every five secound '''
def process_check(guid):

    json_file_name = os.getcwd()+"/json_dumps/"+guid+".json"

    with open(json_file_name, 'r') as openfile:
        json_object = json.load(openfile)

    if json_object['status'] == False:
        return ""
    else:
        return json_object['ouputFilePath'] ### to by narasimman part