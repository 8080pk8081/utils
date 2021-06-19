import requests
import json

loginurl = 'http://10.91.138.100:54020/zuche-management/los/zuche-intf-dmz-web.staffLogin'
data = {
    'userName': '17607660940',
    'loginPwd': 'W++BWTG601dC0fitHPpuBpEz7nDmFRhK5ylHdaTBlGzY9J2tg0/g4pofSeJ6B5p92I+00IJjdFkhgad+JI40t7+'
                'jbwUX9oeoD0g16lgrsaONwjuNwFaEHVJ644AXdvsYboRjASTATP0Wrr0C2atDUcTzvx7Y56KLEdJelddZplhsd6sIDRVSe2PboIWfBQ7w8MlnBG'
                'RcC4C6h7Rep5KsfbZMkJunHvylmqDqkHWudaAOoghTYyRGPSH2grYZrOmJQESVeD63JZWdJ9kFKyfAJ7bDLJKZ3wefaKmY8Nimh7QJDL6sAgJ3HUR1SpjZMAWWoL8q2ATVpLyMJWQ9Wy24aA==',
    '_channel_id': '03'
}
# headers = {
#     'Content-Type': 'application/x-www-form-urlencoded'
# }

s = requests.Session()
r=s.post(loginurl, data)
# print(r.headers)
print(r.cookies.values())
print(r.json())
#
UmListurl = 'http://10.91.138.100:54020/zuche-management/los/zuche-intf-dmz-web.queryUmList'
for umMobile in ('17607660940','13028806080'):
    data = {'umMobile': umMobile,'_channel_id': "03"}
    # headers ={}
    u = s.post(UmListurl,data)
    print(u.json())
    bb = u.json()
    print(bb['model']['umList'][0]['idNo'])
