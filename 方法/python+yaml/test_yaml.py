# -*- coding: utf-8 -*-
import yaml

def  test_yaml():
    aa = yaml.safe_load(open("test.yaml", "r", encoding='utf8'))
    print(aa["device1"]["platformName"])


# print('123')