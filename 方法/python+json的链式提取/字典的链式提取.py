str1 = '''{
	"message": "成功",
	"data": {
		"paging": {
			"totalCount": 1
		},
		"list": [
			{
				"rxSpeed": 5440,
				"mtu": 1500,
				"packetDelay": 0,
				"peerDevType": "0",
				"localType": "1",
				"time": "2021-07-07 01:17:41",
				"recvDropRate": 0,
				"status": 0,
				"jitter": 0,
				"vpnType": "0",
				"arithName": "AES",
				"groupName": "总部",
				"alarmMsg": 				{},
				"userName": "总部LAN1",
				"sendDropRate": 0,
				"transType": "TCP",
				"tunnelId": 33280,
				"interfaceIp": [
					{
						"Ip": "10.10.10.11"
					},
					{
						"Ip": "10.10.10.21"
					},
					{
						"Ip": "10.10.10.31"
					},
					{
						"Ip": "10.10.10.41"
					}
				],
				"laninfo": [
					{
						"Ip": "96.8.1.4",
						"Mask": 32
					},
					{
						"Ip": "11.11.11.0",
						"Mask": 24
					},
					{
						"Ip": "10.10.10.0",
						"Mask": 24
					}
				],
				"txSpeed": 2472,
				"localName": "总部LAN1"
			}
		]
	},
	"code": 0
}'''


def get_json_data(str1=str1, extraction=''):
    """
        对json格式的字符串进行链式提取，返回提取结果
    @param str1: json格式的字符串
    @param extraction: 链式提取表达式
    @return: 提取结果，或None
    """
    dict_data = eval(str1)
    s = 'dict_data'
    list = extraction.split('.')
    try:
        for i in list:
            if i.isdigit():
                s += f"[{i}]"
            else:
                s += f'.get("{i}")'
        else:
            dict_data = eval(s)
    except Exception as e:
        print(f"提取失败，请排查结果{str1}和提取式{extraction}是否有误")
        dict_data = None
    return dict_data

if __name__ == '__main__':
    print(get_json_data(str1, 'data.list.0.tunnelId'))