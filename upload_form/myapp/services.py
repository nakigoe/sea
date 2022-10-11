'''save file to remote server'''
import subprocess

def send_to_server(local_path):
    database_items_path="D:/Docs/Website/sea/upload_form"
    absolute_path= database_items_path + local_path
    subprocess.run(["scp", "-i", "C:/Users/HP/.ssh/mykey.pem", absolute_path, "ec2-user@3.115.9.253:/home/ec2-user/test/pdf/"])
