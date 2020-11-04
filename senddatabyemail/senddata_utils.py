#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Liu Jin Yao"
import traceback
import pymysql
import openpyxl
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import smtplib

class datas:
    pass


class mail:
    """默认以html的格式发送邮件"""
    def __init__(self,css="html"):
        self.css = css
    def create_email(self,email_from, email_to, email_title, email_text, annex_path=None, annex_name=None):
        """
        生成一个空的带附件的邮件实例
        :param email_from: 发件人名称；可非邮箱
        :param email_to:   收件人名称；可非邮箱
        :param email_title: 邮件标题
        :param email_text:  邮件正文
        :param annex_path:  附件的本地目录 为None时，不生成附件。
        :param annex_name:  定义附件名
        :return:
        """
        message = MIMEMultipart()
        #将正文以css的形式插入邮件中,动态，默认时html；
        message.attach(MIMEText(email_text, self.css, 'utf-8'))
        #生成发件人名称（这个跟发送的邮件没有关系）
        message['From'] = Header(email_from, 'utf-8')
        #生成收件人名称（这个跟接收的邮件也没有关系）
        message['To'] = Header(email_to, 'utf-8')
        #生成邮件主题
        message['Subject'] = Header(email_title, 'utf-8')
        if annex_path  is not None:
            #读取附件的内容
            with open(annex_path, 'rb') as file:
                content = file.read()
            att1 = MIMEText(content,'base64','utf-8')
            att1["Content-Type"] = 'application/octet-stream'
            #生成附件的名称
            att1["Content-Disposition"] = 'attachment; filename=' + annex_name
            #将附件内容插入邮件中
            message.attach(att1)
        #返回邮件
        return message

    def send_email(self,sender, password, receiver, msg):
        # 一个输入邮箱、密码、收件人、邮件内容发送邮件的函数
        try:
            #找到你的发送邮箱的服务器地址，已加密的形式发送
            server = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)  # 发件人邮箱中的SMTP服务器
            server.ehlo()
            #登录你的账号
            server.login(sender, password)  # 括号中对应的是发件人邮箱账号、邮箱密码
            #发送邮件
            server.sendmail(sender, receiver, msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号（是一个列表）、邮件内容
            print("邮件发送成功")
            server.quit()  # 关闭连接
        except Exception:
            print(traceback.print_exc())
            print("邮件发送失败")



class html_utils:
    """查询数据，组装html"""

    def html_table(self,title,data: dict):
        """
        组装html中的table标签部分
        :param title:  table的标题。以h2的样式来展示。
        :param data:   将pymysql以字典的样式查询出来的结果，传入进来进行解析。
        :return:  返回一串str。html标签语言。
        """
        str0 = "<tr>"
        str1 = "</tr>"
        str2 = ""
        for i in data[0].keys():
            str2 = str2 + f"<th> {i}</th>"
        tablehead = str0 + str2 + str1
        tablebody = ""
        for j in data:
            str3 = ""
            for jj in j.values():
                str3 = str3 + f"<td text-align: center > {jj}</td>"
            body = str0 + str3 + str1
            tablebody = tablebody + body
        table = f"<h2>{title}</h2><table>" + tablehead + tablebody + "</table>"
        return table

    def html_base(self,_str):
        """
        将html的框架和body内的语言进行拼接
        :param _str: body
        :return:html框架语言。
        """
        basehtml = f'<html lang="han-ZH"> <head> <meta charset="UTF-8"> <meta name="viewport" content="width=device-width, initial-scale=1.0">  ' \
                   f'<title>报告</title> <style> table,table tr th, table tr td {{ border:1px solid #00070c;text-align: center; }}</style> </head> <body>{_str}</body> </html>'
        return basehtml

    def html(self,sqllist:list,title:list):
        """
        处理多个sql，从而多个title。
        :param sqllist:  sql列表
        :param title:       table标题列表
        :return:
        """
        table_str = ""
        index = 0
        if len(sqllist) == len(title):
            pass
        else:
            for z in range(len(sqllist)-len(title)):    #以默认标题:补全titlelist。
                title.append("默认标题:")
        for sql in sqllist:
            data = self.getData(sql)
            tableHtml = self.html_table(title[index],data)
            table_str = table_str + tableHtml
            index += 1
        return self.html_base(table_str)

    """查询sql获取数据"""
    def getData(self,sql):
        conn = pymysql.connect(host='123.56.126.125',
                               port=3306,
                               user='txy',
                               password='123456',
                               db='zentao', cursorclass=pymysql.cursors.DictCursor)
        curr = conn.cursor()
        curr.execute(sql)
        result_sql = curr.fetchall()
        curr.close()
        conn.close()
        return result_sql

    def getYesterday(self,):
        # 获取昨天日期的字符串格式的函数
        #获取今天的日期
        today = datetime.date.today()
        #获取一天的日期格式数据
        oneday = datetime.timedelta(days=1)
        #昨天等于今天减去一天
        yesterday = today - oneday
        #获取昨天日期的格式化字符串
        yesterdaystr = yesterday.strftime('%Y-%m-%d')
        #返回昨天的字符串
        return yesterdaystr



if __name__ == '__main__':
    sqllist = ["SELECT  t2.realname as 研发,count(DISTINCT case when t1.`status`='active' then t1.id end ) 激活," \
               "count(DISTINCT case when t1.`status`='resolved' then t1.id end) 已解决,count(DISTINCT case when t1.`status`='closed' then t1.id end) 已关闭," \
               "count(DISTINCT case when t1.`status`='active'and to_days(t1.openedDate) = to_days(now()) then t1.id end ) 今日待解决," \
               "count(DISTINCT CASE WHEN t1.`status`!='active' and t1.resolution IN ('fixed', 'xn', 'aq','postponed') THEN t1.id end ) '技术问题' , " \
               "count(DISTINCT CASE WHEN t1.`status`!='active' and t1.resolution IN ('bydesign','01','tostory','story') THEN t1.id end ) '需求相关'," \
               "count(DISTINCT CASE WHEN t1.`status`!='active' and t1.resolution IN ('jg', 'pz', 'sj', 'jxx','bz') THEN t1.id end )'受限问题'," \
               "count(DISTINCT CASE WHEN t1.`status`!='active' and t1.resolution IN ('duplicate', 'external', 'willnotfix', 'set','wc','hj') THEN t1.id end )'不是问题'," \
               "COUNT(DISTINCT CASE WHEN t1.severity IN ('6', '5') THEN t1.id end )'严重问题',COUNT(DISTINCT CASE WHEN t1.severity IN ('4', '3') THEN t1.id end )'中级问题',"
               "COUNT(DISTINCT CASE WHEN t1.severity IN ('1', '2') THEN t1.id end )'一般问题',        count(DISTINCT t1.id) AS BUG总数量 FROM        zt_bug t1,zt_user t2 " \
               " WHERE t2.account in(t1.assignedTo,t1.resolvedBy) and  t1.deleted='0' and t2.realname in ('何伟','刘元雄','郑子峰') GROUP BY  研发 ORDER BY BUG总数量 DESC"]
    print(html_utils().html(sqllist,["禅道bug:"]))
