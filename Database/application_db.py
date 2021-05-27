import configparser as cp
import os

''' application modules '''
from Database.db_utils import Database_Connection


# ''' database configuration parser and connections '''
# parser = cp.SafeConfigParser()
# print("path === ",os.getcwd()+'/Database/db.ini')
# parser.read(os.getcwd()+'/Database/db.ini')

''' GLOBAL QUERY STRING '''
user_exist = 'select name from user where name = "{0}";'  # parser.get('database_query_details', 'user_exist')
# parser.get('database_query_details', 'insert_new_user')
insert_new_user = 'insert into user (name,email_id,mobile_no,password,status) values ("{0}","{1}",{2},"{3}",True);'
# parser.get('database_query_details', 'login_user')
login_user = 'select name from user where name = "{0}" and password = "{1}";'
# parser.get('database_query_details', 'file_upload')
file_uploads = 'insert into result (process_id,file_name,file_path,status) values ("{0}","{1}","{2}",False);'
# parser.get('database_query_details', 'process_status')
process_status = 'select * from result where process_id = "{0}";'

''' login flow '''


def login_check(username,password) -> bool:
    my_connection = Database_Connection()

    _login_user = login_user.format(username,password)
    is_exist = len(my_connection._select_query(_login_user))
    my_connection._disconnect_database()

    if is_exist == 1:
        return True
    else:
        return False


def insert_file_detatils(guid,filename,path) -> bool:
    my_connection = Database_Connection()

    _file_upload = file_uploads.format(guid,
                                       filename, path)

    my_connection._insert_query(_file_upload)
    my_connection._disconnect_database()
    return True


def check_process(process_id: str):
    my_connection = Database_Connection()
    _process_status = process_status.format(process_id)

    result = my_connection._select_query(_process_status)
    return result
