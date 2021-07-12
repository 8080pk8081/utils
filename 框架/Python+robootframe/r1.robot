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
初始
    Set Suite Variable	 @{all_list}

用例步骤
   Should Be Equal As Strings   ${msg}      200     # 断言
   log      参数为：@{list}                          # log 关键字，后面要接字符串。 所以，直接log    @{list} 会报错，可以在变量前加字符串使用； &{} 字典也是一样。
   log      ${list}                                 # 或者使用$ 转为标量。字典也是一样。字典类型的变量也是一样的。
   log      参数为：&{dict}
   log      参数为：${dict.name}                    # $ 字典的取值，链式取值。

   &{dict2}     create dictionary    name=2   age=14
   log      参数为：&{dict2}

   Append To List   ${list}     ${dict2}
   Append To List   ${all_list}         a       3      5       c
   log      参数为：${list}
   关键字
   ${result}=   预期结果     123     123
   Should Be Equal As Strings       ${result}       ture

最后
    log   ${all_list}


条件式赋值
   ${a}     Run keywordIf       '20'=='${msg}'     set variable     23
    ...     ELSE IF             '200'=='${msg}'    set variable     24
    ...     ELSE                set variable     25
    log     ${a}
   ${b}     Run keywordIf       '20' in '${msg}'     set variable     23
    ...     ELSE IF             '200' in '${msg}'    set variable     24
    ...     ELSE                set variable     25
    log     ${b}
