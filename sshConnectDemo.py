import paramiko as paramiko
from utilities.configurations import *
import csv

# Start connection
username = getConfig()['Server']['username']
password = getConfig()['Server']['password']
host = getConfig()['Server']['host']
port = getConfig()['Server']['port']
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(host, port, username, password)


#upload files
sftp = ssh.open_sftp()
destinationPath = "script.py"
localPath = "batchFiles/script.py"
sftp.put(localPath, destinationPath)

destinationPath = "loanasa.csv"
localPath = "batchFiles/loanasa.csv"
sftp.put(localPath, destinationPath)

# Trigger the batch command
stdin, stdout, stderr = ssh.exec_command("python script.py")


# Download the file to local system
sftp.get("loanasa.csv", "outputFiles/loanasa.csv")

with open('outputFiles/loanasa.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    for row in csvReader:
        if row[0] == '32321':
            assert row[1] == 'rejected'

ssh.close()