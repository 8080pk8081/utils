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



FOR  ${i}  IN   RANGE   ${vrrp_bild_time}    ${vrrp_bild_time_max}
    Login To SDWAN    ${VRRP_backup}
    ${ha_backup}=    API请求    ${HA_requests}      VRRP功能状态   ${VRRP_backup}
    Login To SDWAN    ${VRRP_master}
    ${ha_master}=    API请求    ${HA_requests}      VRRP功能状态   ${VRRP_master}
    exit for loop if    'FAULT' not in ${ha_backup}   and 'MASTER' not in ${ha_backup}  and 'BACKUP' in ${ha_backup}  and  'FAULT' not in ${ha_master}   and 'MASTER' in ${ha_backup}  and 'BACKUP' not in ${ha_master}
END