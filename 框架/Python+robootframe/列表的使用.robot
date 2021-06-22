***Test Cases***
列表的使用
    @{case_list}   Create List   1      a      avd          # test cases 里创建列表
    log     ${case_list}
    ${length}=   Get Length     ${case_list}       # 获取列表长度
    ${now}        evaluate    int(${length}-1)      
    log       number is ${now}
    FOR  ${index}  IN RANGE  0    ${length}
        sleep      2
        log     ${index}
        log     ${case_list[${index}]}              # 列表索引取值
        Run Keyword If   ${index}==${now}      log     最后一条了           # If 判断          
    END
