#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Liu Jin Yao"
import datetime
from senddatabyemail.senddata_utils import html_utils
from senddatabyemail.senddata_utils import mail

#sql列表
sqllist = ["SELECT  t2.realname as 研发,count(DISTINCT case when t1.`status`='active' then t1.id end ) 激活," \
               "count(DISTINCT case when t1.`status`='resolved' then t1.id end) 已解决,count(DISTINCT case when t1.`status`='closed' then t1.id end) 已关闭," \
               "count(DISTINCT case when t1.`status`='active'and to_days(t1.openedDate) = to_days(now()) then t1.id end ) 今日待解决," \
               "count(DISTINCT CASE WHEN t1.`status`!='active' and t1.resolution IN ('fixed', 'xn', 'aq','postponed') THEN t1.id end ) '技术问题' , " \
               "count(DISTINCT CASE WHEN t1.`status`!='active' and t1.resolution IN ('bydesign','01','tostory','story') THEN t1.id end ) '需求相关'," \
               "count(DISTINCT CASE WHEN t1.`status`!='active' and t1.resolution IN ('jg', 'pz', 'sj', 'jxx','bz') THEN t1.id end )'受限问题'," \
               "count(DISTINCT CASE WHEN t1.`status`!='active' and t1.resolution IN ('duplicate', 'external', 'willnotfix', 'set','wc','hj') THEN t1.id end )'不是问题'," \
               "COUNT(DISTINCT CASE WHEN t1.severity IN ('6', '5') THEN t1.id end )'严重问题',COUNT(DISTINCT CASE WHEN t1.severity IN ('4', '3') THEN t1.id end )'中级问题',"
               "COUNT(DISTINCT CASE WHEN t1.severity IN ('1', '2') THEN t1.id end )'一般问题',        count(DISTINCT t1.id) AS BUG总数量 FROM        zt_bug t1,zt_user t2 " \
               " WHERE t2.account in(t1.assignedTo,t1.resolvedBy) and  t1.deleted='0' and t2.realname in ('何伟','刘元雄','郑子峰') GROUP BY  研发 ORDER BY BUG总数量 DESC",
               "SELECT realname,score from zt_user WHERE deleted='0' ORDER BY score desc"]
#邮件上的表格的标题；以h2的样式来显示，如果标题不太够，就以”默认标题“命名。
titlelist =["禅道bug：","禅道积分："]
receiver = ['ldy_liujy001@ldygo.com']#接收人邮箱列表

def main():
    u = html_utils()
    m = mail()
    print(datetime.datetime.now())
    my_email_from = '测试部'
    my_email_to = '研发工单组'
    # 邮件标题
    my_email_title = '研发工单组BUG报告' + u.getYesterday()
    # 邮件正文
    my_email_text = u.html(sqllist,titlelist)
    # 生成邮件
    my_msg = m.create_email(my_email_from, my_email_to, my_email_title,
                          my_email_text,)
    my_sender = 'testbug@ldygo.com'
    my_password = 'Test@1234'
    # 发送邮件
    m.send_email(my_sender, my_password, receiver, my_msg)
    print(datetime.datetime.now())

if __name__ == "__main__":
    main()