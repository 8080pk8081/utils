# import random
# #
# # from openpyxl import load_workbook
# #
# # for B in ('ABCDEFGHIJKLMN'):
# #     print(B)
# #
# # gears =['gwb01', 'zuche-gw-alizmxy', 'zuche-gw-base', 'zuche-gw-email', 'zuche-gw-gas', 'zuche-gw-gd', 'zuche-gw-gpsobd', 'zuche-gw-monet', 'zuche-gw-tongdun', 'zuche-gw-wz', 'zuche-notify-gw']
# # for a in range(len(gears)):
# #     print(a)
# #
# #
# # # def write_excel(file,sheet,cell,value):
# # #     wb = load_workbook(file)
# # #     ws = wb[sheet]
# # #     ws[cell] = value
# # #     wb.save(file)
# # # def test_write_excel():
# # #     file = 'data.xlsx'
# # #     for i in range(35):
# # #         cell = "I" + str(i+2)
# # #         value = "粤" + random.choice(("A","B","C","D")) + str(random.randint(11111,99999))
# # #         write_excel(file,"data",cell,value)
# #
# # import   xlsxwriter
# #
# # workbook = xlsxwriter.Workbook(filename="gears_data.xlsx")  # 默认输入到当前目录下
# # for sheet in ["qeer",'werwa','etqew']:
# #     worksheet = workbook._add_sheet(sheet)   #增加工作表
# # workbook.close()
import re

import xlsxwriter
from paramiko import SSHClient, AutoAddPolicy

username='tomcat'
password='ldygo@9012!@#$%&*#'
# hostlist = ['10.91.138.140','10.91.18.117','10.91.18.140','10.91.18.141','10.91.18.142','10.91.138.100','10.91.18.101','10.91.18.102']
hostlist = ["10.91.18.100"]
class get_gears:
    def  get_gears(self):
        self.workbook = xlsxwriter.Workbook(filename="gears_data.xlsx")  # 默认输入到当前目录下
        self.username = username
        self.password = password
        self.ssh_client = SSHClient()
        self.ssh_client.set_missing_host_key_policy(AutoAddPolicy())
        for host_ip in hostlist:
            self.ssh_client.connect(host_ip, port=22, username=self.username, password=self.password)
            command = 'cd /qhapp/apps/lo-boxs/; ls'
            stdin, stdout, stderr = self.ssh_client.exec_command(command)
            list = stdout.read().decode().strip().split("\n")
            self.boxlist = []
            for box in list:
                rr = re.compile('^[A-Za-z][0-9a-z][0-9a-z][0-9j][0-9]$')
                if rr.findall(box) != []:
                    self.boxlist.append(rr.findall(box)[0])
            for box in self.boxlist:
                command = 'cd /qhapp/apps/lo-boxs/{boxs}/gears/; ls'.format(boxs=box)
                stdin, stdout, stderr = self.ssh_client.exec_command(command)
                list = stdout.read().decode().strip().split("\n")
                list.insert(0, box)
                print(list)
                worksheet = self.workbook.add_worksheet(box)  # 增加工作表
                b = 1
                for a in range(len(list) - 1):
                    worksheet.write("A%s" % (a + 1), host_ip)
                    worksheet.write("B%s" % (a + 1), list[0])
                    worksheet.write("C%s" % (a + 1), list[b])
                    b += 1
            self.ssh_client.close()
        self.workbook.close()


if __name__ == '__main__':
    # test_write_excel()
    a = get_gears()
    a.get_gears()

