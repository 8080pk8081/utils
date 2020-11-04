
"""pip install XlsxWriter     先要安装Xlsxwriter
"""
dic = {
        "APP_allow" :              ['id','//*[@resource-id="com.android.packageinstaller:id/permission_allow_button"]'] ,   #第一次打开APP同意权限
        "privacy" :                ["id",'com.ldygo.qhzc:id/txt_msg'],   #隐私政策文本框
        "agree_privacy":          ["id",'com.ldygo.qhzc:id/btn_pos'],  #隐私政策框中同意按钮
        "Close_homepage_ad":      ['id','com.ldygo.qhzc:id/iv_moregift_close'],   #首页弹屏封图(广告）的关闭按钮
        "Homepage_me":                  ["id",'com.ldygo.qhzc:id/iv_home_me'],  #个人中心按钮
        "Homepage_now" :                ["id","com.ldygo.qhzc:id/rb_servicetype_instant"], #首页现在按钮
        "Homepage_book" :               ["id",'com.ldygo.qhzc:id/rb_servicetype_book'],  #首页预约按钮
        "Homepage_location":      ["id","com.ldygo.qhzc:id/iv_location"],  #首页定位按钮
        "Homepage_help":          ["id","com.ldygo.qhzc:id/iv_server_help"],  #首页帮助中心页的按钮
        "Home_searchpark" :      ["id",'d(resourceId="com.ldygo.qhzc:id/svga_view_search")'],  #首页搜索网点按钮
        "Homepage_refresh" :           ['id',"com.ldygo.qhzc:id/iv_refresh_parks" ],  #首页刷新按钮
        "Homepage_Use_car" :           ['x','xpath/id'], #首页现在用车
        "Select_fristcar" :     ["x",'//*[@resource-id="com.ldygo.qhzc:id/parkCarListView"]'
                                     '/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/'
                                     'android.widget.RelativeLayout[1]'],   #选择第一台车
        "Now_min_way":           ['x','//*[@resource-id="com.ldygo.qhzc:id/fsSetMealView"]'], #计费方式选择现在分时
    }
import xlsxwriter
workbook = xlsxwriter.Workbook(filename="element_data.xlsx")  # 默认输入到当前目录
worksheet = workbook._add_sheet("sheet1")   #增加工作表
i = 1
for word in dic:
    worksheet.write("A%s"%i,word)            #A列写key
    worksheet.write("B%s"%i,dic[word][0])   #B列写value[0]
    worksheet.write("C%s"%i,dic[word][1])   #C列写value[1]
    i = i + 1
workbook.close()
