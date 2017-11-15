#!/bin/bash

# 总结下自己写shell脚本中出的坑

# 1. sh 和　bash 不能混用, 比如　[[]] 以及数组的() 都只能用bash或者./解决
# 一般还是用下面两种处理判断
if [ .. -gt .. -a .. -lt .. ]
if test $str1 = $str2

# 2. 对于命令行
my_array=(1 2 3)
echo ${my_array[x]} #这才是合理的！
# 注意array不需要初始化, 直接对一个不存在的array赋值就能生成了, e.g. arr[100]=10

# 3. 打印数组时, 注意要用 ${array[@]} 或者 ${array[*]} 不能直接 echo $array, 否则只能打印第一个元素

# 4. egrep(等价于 grep -E) 要接单引号, 否则很多都不能用

# 5. wc / cut / tr 等不能直接跟非文件
echo "Fuck" | cut -c3

# 6. 检查变量是否为数字
var1test=$(echo $1 | bc) # 若非数字, bit count = 0
if [ "$var1test" = "$1" ] --> YES

# 7. 输出标准错误信息
echo "./echon.sh: argument 1 must be a non-negative integer" 1>&2
exit 1

# 8. 用tab分割
cut -d$'\t' ...

# 9. 标准输入
cat file | while read line do ...
sh "包含while read line ... 的脚本" < file

# 10. Check the permission
ls -la
chmod 751 
        # 文件主用户 - 文件所属组用户 - 其他用户
        # 4 r , 2 w, 1 execute
        
# 11. check whether the file is readable
if [ ! -r $file ] # not readable
查询 man [

# 12. check whether file is exist and excutable
test -x filename
test -r filename # exist and readable
test -d filename # exist and is directory 

# 13. 递归列出文件
find "dir" -type d # all dir / subdirs
find "dir" -type f # all files

# 14. 输入有空格的文件
+ 输入时加双引号 sh xxx.sh "arg1" "arg2   ss"
+ 使用时加双引号
for arg in "$@"
do  command "$arg"
...

# 15. convert
convert -gravity south -pointsize 36 -draw "text 0,10 'Andrew rocks'" penguins.jpg temporary_file.jpg

-gravity type : horizontal and vertical text placement
-pointsize value : font point size
-draw string : annotate the image with a graphic primitive

# 16. sed 读取两行之间的所有行
sed -n '/起始行关键词/,/结束行关键词/p'

# 17. sed 不支持非贪婪匹配, 如果一定要做的话
e.g. 遇到|则删除[[xxx|之间的内容

tr "\[\[" "\n" # 将[[替换为换行
sed 's/^.*|//g' # 删除内容
sed ':a;N;s/\n/\[\[/;ba;' # 合并为一行

# 18. Parent shell and child shell
# set_var.sh, 将变量设为42
variable=21
. ./set_var.sh # 两个点意为parent shell
echo $variable # ./ --> 21, ../ --> 42

# 19. shell 函数
func(){ 
    para1=$1
    para2=$2
    # 注意在函数内部不能出现小括号(), i.e.不能出现数组!
}

# 调用
func para1 para2

# 20. 算数运算
+ Method 1 : expr, 注意乘法要对*转义"expr $x \* $y" , 且不能处理次方 $a ** 2
a=`expr $x + $y`
+ Method 2 : $(()), 不需要转义, 适用性更好
a=$(( $x + $y ))
b=$(( $x ** 2 + $y ** 2 ))
+ Method 3 : $[], 同Method2

# 21. cgi and html
cat <<eof
<!-- 这里面可以放任意html, 需要加变量的地方直接加就行 -->
Your browser is running at IP address:  <b>$SERVER_ADDR</b>
eof

# 22. 在shell中运行shell
. ./file.sh # 注意两个点的空格!
source ./file.sh # 与上面功能相同




