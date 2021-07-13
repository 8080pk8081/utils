#! /bin/bash
echo "需要查找的信息是:${1}"
var_list=`ps -ef | grep ${1} | awk '{print $2}'`
if [ "$var_list" = "" ]; then
    echo "没有找到相关的进程号"
else
    for var in $var_list
    do
         echo "停止进程号 ${var}.."
         kill -9  ${var}
     done
fi