* Settings *
Library     Kw_1.py
Library     BuiltIn
Library     Collections

* Variables *
${msg}     200              # 定义一个rf标量（字符串）
@{list}     2   4   5       # 定义一个rf列表
&{dict}     name=1      age=12      #定义一个rf字典
@{all_list}


* Test Cases *
#for循环及打断循环
#    FOR  ${i}   IN RANGE  2  61   2
#        sleep    2
#        log     ${i}
#        exit for loop if   "8" == '${i}'
#    END

run keyword if的使用
    run keyword if  ${msg} > 1      log     'nice'
    ${msg}   run keyword if     ${msg} > 1000         set variable        失败
    ...     ELSE                set variable     ${msg}
    log     ${msg}

