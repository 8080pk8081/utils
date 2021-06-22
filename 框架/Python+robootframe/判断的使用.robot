****Variables***
${var}          VPN-连接管理
@{var_list}         VP    连接管理     总部

***Test Cases***
判断字符是否存在
    Run Keyword If   'VPN' in '${var}'   log      nice
    log         ${var_list}
    Run Keyword If    'VPN' in '${var_list[0]}'   log      nice

Run Keyword If后执行多个关键字
    Run Keyword If   'VPN' in '${var}'   
    ...         Run Keywords    log    nice 
    ...         AND     log      nice2
    ...         AND     log         nice3
