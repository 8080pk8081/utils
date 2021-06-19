
from paramiko import SSHClient, AutoAddPolicy

username='tomcat'
password='ldygo@9012!@#$%&*#'
# hostlist = ['10.91.138.140','10.91.18.117','10.91.18.140','10.91.18.141','10.91.18.142','10.91.138.100','10.91.18.101','10.91.18.102']
host_ip = ["10.91.18.100"]
class get_gears:
    def  get_gears(self):
        self.username = username
        self.password = password
        self.ssh_client = SSHClient()
        self.ssh_client.set_missing_host_key_policy(AutoAddPolicy())
        self.ssh_client.connect(host_ip[0], port=22, username=self.username, password=self.password)
        command = 'cd /qhapp/apps/lo-boxs/; ls; top'
        stdin, stdout, stderr = self.ssh_client.exec_command(command)
        # list = stdout.read().decode().strip().split("\n")
        text = stdout.read().decode()
        print(text)
if __name__ == '__main__':
    a=get_gears().get_gears()
