'''save file to remote server'''
import subprocess

def send(path_to_file):
    subprocess.run(["scp", "-i", "C:/Users/HP/.ssh/mykey.pem", path_to_file, "ec2-user@3.115.9.253:/home/ec2-user/test/pdf/"])
