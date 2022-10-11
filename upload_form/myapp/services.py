'''save file to remote server'''
import subprocess

def send_to_server(send_from):
    subprocess.run(["scp", "-i", "C:/Users/HP/.ssh/mykey.pem", send_from, "ec2-user@3.115.9.253:/home/ec2-user/test/pdf/*"])
