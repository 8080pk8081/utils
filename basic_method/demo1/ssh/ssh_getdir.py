import re

import xlsxwriter
from paramiko import SSHClient, AutoAddPolicy

list = ['10.91.138.140',]
host_ip='10.91.138.140' #不需要带端口

username='tomcat'
password='ldygo@9012!@#$%&*#'


class get_gears:

    def __init__(self,host_ip,username,password):
        self.host_ip = host_ip
        self.username = username
        self.password =password
        self.ssh_client = SSHClient()
        self.ssh_client.set_missing_host_key_policy(AutoAddPolicy())
        self.ssh_client.connect(self.host_ip, port=22, username=self.username, password=self.password)

    def get_boxs(self):
        # t = paramiko.Transport((host_ip,22))
        # t.connect(username=username, password=password)  # 登录远程服务器
        # sftp = paramiko.SFTPClient.from_transport(t)     # sftp传输协议
        # src = remote_path
        # des = local_path
        # sftp.get(src,des)
        # t.close()
        command = 'cd /qhapp/apps/lo-boxs/; ls'
        stdin, stdout, stderr = self.ssh_client.exec_command(command)
        list = stdout.read().decode().strip().split("\n")
        self.boxlist =[]
        for box in list:
            rr =re.compile('^[A-Za-z][0-9a-z][0-9a-z][0-9j][0-9]$')
            if rr.findall(box) != []:
                self.boxlist.append(rr.findall(box)[0])

    def get_gears(self):
        self.get_boxs()
        self.workbook = xlsxwriter.Workbook(filename="gears_data.xlsx")  # 默认输入到当前目录下
        for box in self.boxlist:
            command = 'cd /qhapp/apps/lo-boxs/{boxs}/gears/; ls'.format(boxs=box)
            stdin, stdout, stderr = self.ssh_client.exec_command(command)
            list = stdout.read().decode().strip().split("\n")
            list.insert(0,box)
            print(list)

            worksheet = self.workbook.add_worksheet(box)  # 增加工作表
            b = 1
            for a in range(len(list) - 1):
                worksheet.write("A%s" % (a + 1), list[0])
                worksheet.write("B%s" % (a + 1), list[b])
                b += 1

        self.workbook.close()
        self.ssh_client.close()



if __name__ == '__main__':

    a = get_gears(host_ip=host_ip,password=password,username=username)
    a.get_gears()

'"gears_data.xlsx"'