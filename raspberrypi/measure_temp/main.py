from dotenv import load_dotenv
import os
import paramiko
import paramiko.client
    
load_dotenv()

host = os.getenv('HOST')    
username = os.getenv("SSH_USERNAME")
password = os.getenv("SSH_PASSWORD")
command = "vcgencmd measure_temp"


def ssh_connection():
    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host,username=username,password=password)
    return client

def run_temperature_command(command):
    client = ssh_connection()
    stdin, stdout, stderr = client.exec_command(command=command)
    print(stdout.read().decode())
    client.close()

if __name__ == "__main__":
    run_temperature_command(command=command)
