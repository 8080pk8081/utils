***Settings***

Library           SeleniumLibrary

***Variables***
${BROWSER}
${LOGIN URL}


***Keywords***
Login Device
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Input Text    username_field    ${username}
    Input Text    username_field    ${username}
    Click Button    login_button


***Test Cases***
登录设备
    Login Device
