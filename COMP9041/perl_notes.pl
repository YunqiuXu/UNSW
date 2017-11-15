#!/usr/bin/perl -w
# Perl随笔
# Yunqiu Xu

# 1. Common version
perl -w # 带警告
perl -e 'xxx' # 直接在cmd运行命令
ctrl + c # quit
ctrl + d # stop inputting

# 2 Data type and variable
# $ is variable, @ is array, % is hash
## 2.1 Digits
$var1 = 047; # 0开头为８进制, 相当于10进制39
$var2 = 0x1f; # 0开头为16进制, 相当于10进制31
$var1 = scalar($var1); # change to scalar, 将变量变为可用于计算的数字
## 2.2 Strings
$mix = $str . $num; # 连接字符串和数字
$n_chars = length $line; # 字符串长度
$last_char = substr($line, offset, length); # 截取

## 2.3 Special 
$i # matching string for ith regexp in pattern, e.g. $1 匹配的第一个
$! # last error, open or die("fuck, $!")
$. # line number for input file stream
$/ # line separator
$0 # 执行该程序的文件，同shell; $$进程号, 同shell
$_ #迭代循环中，当前循环的字符串会放在 $_ 中, 然后 通过 print 输出。另外 print 在不指定输出变量，默认情况下使用的也是 $_


## 3. Array
@arr=(1,2,3); # array, 访问其中元素$arr[0]
    # 访问元素用$arr[n], 否则会报警告
$arr[n] = ... ; # 给数组增加或替换元素
# perl里面数组不需要初始化, 直接插值就行
@arr = (a..b); # similar to range(a,b+1) in python, 注意和python不同perl是包括右边界的
$var = @array# 数据类型由等号左边决定: 数组赋值给数组 --> 数组复制; 数组赋值给标量 --> 数组长度
    $size = @arr ; # 数组大小, 注意这个是物理大小, 不是元素长度
    $arr[500] = ...; # 即使中间没被赋值, 该数组大小为501, 最大索引为500
    @arr[0..5] # 数组切分 --> 前六个元素
    @arr[3,4,5]; # 等价于@arr[3..5]
$max_index = $#arr; #最大索引 --> 因此长度也可以为 $#arr + 1
@ARGV # list (array) of command line arguments
push(@arr, LIST); # 将LIST 添加至队尾
    pop(@arr); # 删除最后一个元素
    shift(@arr); # 删除第一个元素, 索引也减少
    unshift(@arr,LIST); # 将list添加只队首
    @arr1 = (@arr2, @arr3); # merge, e.g. @numbers = (1,3,(4,5,6));

# 注意在CSE不能用这个!
splice(@nums, 5, 4, 21..24) # 替换元素: 将从第5个元素开始的4个位置替换为21-24
    splice(@array, $start, $length, @LIST) 
    splice(@array, $index, 0, $element) # insert $element at position $index
    splice(@array, $index, 1) # delete element at position $index
@arr = split('-', 'www-abc-bin'); # string to array
    @str = join('-', @arr); # array to string
    split(//, 'hello') # h, e, l, l, o
    # 也可以 split("", $var)这样, ""和//等价
    split(/[@]+/,'ab@@c@d@@e'); # ab, c, d, e
    split(/([@]+)/, 'ab@@c@d@@e'); # ab, @@, c, @, d, @@, e
    split(/([@])+/, 'ab@@c@d@@e'); # ab, @, c, , d, @, e
@sorted = sort(@arr);
    @sorted = sort { $a <=> $b } @not_sorted; # 自定义排序规则: 比较数字
        # $a <=> $b 从小到大
        # $b <=> $a 从大到小
    @sorted = sort { lc($a) cmp lc($b) } @not_sorted ; # 自定义排序规则: 比较字母, lc为转换为小写
    my @keys = sort { $h{$a} <=> $h{$b} } keys(%h); #sort by value, return sorted keys
    # 若想饭序, $h{$b} <=> $h{$a}即可
    @reverse = reverse(@arr);

## 4. Hash
%data = ('google', 45, 'runoob', 30, 'taobao', 40); # 哈希变量, 用$data{'google'}进行访问, 类似python中字典
# 另一种创建方式: 赋值 $data{'google'} = 45
# 另一种创建方式: %data = ('google'=>'google.com')
%data{'google','runoob'} # 45 30
if( exists($data{'facebook'}) ){} # 检查key是否存在
# 获取哈希大小: 先得到键或者值的数组, 然后计算数组长度
    @values = values %data; # 以数组形式返回所有values, 同理keys %data
    $size = @values;
# 添加或删除元素
       %data{'google'} = 45
       delete $data{'taobao'}
# 注意哈希不能直接打印, 应该转换成变量或数组
print "$data{'google'}\n";

# Hash 两个key
$hash{$key1}{$key2} = value;

       
## 5. Conditions
Condition ? Action1 : Action2;
if(){}elsif(){}else(){}
unless(bool){} # bool 为 false 执行
unless(b1){1}elsif(b2){2}else(b3){3} # b1 false --> 1; b1 true b2 true --> 2; else --> 3

## 6. Loop
while(){}
for($a=0;$a<10;$a=$a+1){}
for( ; ; ), while() # 无限循环
foreach item(@items){} # for item in @items ...

# Control
next # similar to continue
continue
last # similar to break --> break all loops
redo

## 7. Calculating
# digits: +-*/%, == !=
$A <=> $B # 检测AB是否相等, 若等于回复0, 左边小回复-1, 左边大回复1
# strings: lt gt le ge eq ne
$a cmp $b # 检测AB是否相等, 若等于回复0, 左边小回复-1, 左边大回复1

# 赋值: += -= ...
# Bit manipulation: $a^$b, & | ~ << >>
# Logical manipulation: and等价于&&, or等价于||, not
$a.$b # 连接变量为字符串
$a x 3 # 重复三次
$a++ $b-- $c+=1

# 8. Functions --> 这里比较复杂, 之后再看
## 8.1 全局变量和局部变量
our # 包全局
local # 临时全局
my # 私有局部, 函数里一般用这个

## 8.2 Func1: Average(10,20,30) = 20
sub Average{
   # 获取所有传入的参数, 函数参数用特殊数组@_标明
   $n = scalar(@_);
   $sum = 0;
 
   foreach $item (@_){
      $sum += $item;
   }
   $average = $sum / $n;
   print '传入的参数为 : ',"@_\n";           # 打印整个数组
   print "第一个参数值为 : $_[0]\n";         # 打印第一个参数
   print "第二个参数值为 : $_[1]\n";         # 打印第一个参数
   print "传入参数的平均值为 : $average\n";  # 打印平均值
}
## 8.3 Func2: PrintList($a, @b)
# 整个列表都会被打印出来, 无论传递几个参数
# e.g. $a = "fuckfuck";@b = (1,2,3,4,5); --> 列表为 : fuckfuck 1 2 3 4 5
sub PrintList{
   my @list = @_;
   print "列表为 : @list\n"; 
}

# 9. IO
<> 和 <STDIN> 都算是输入, 注意二者区别! # @lines = <>
print STDOUT "Enter your a number:";$x = <STDIN>; # 输入内容
chomp $x; # 去除变量尾部的换行符, 与之相对的是chop: 去除变量尾部的字符不管是什么
print "$x"; # 输出内容
print STDERR "fuck!\n";
printf "String of 2^%d = %d characters created\n", $n, length $string; # 类似python format

# 10. File manipulation
## 10.1 Open & Close
# 一般比较常用的就是 "<", ">", ">>"这三个
open(DATA, '<', "file.txt") or die "file.txt 文件无法打开, $!"; # 建议这样写(<与文件名分开) --> 比较安全
while(<DATA>){ # <DATA> 中每行被赋值给$_
    print "$_";
}
open(DATA, '>', "file.txt")；# 写入,将文件指针指向文件头并将文件大小截为零
open(DATA, '+<', "file.txt"); # +< wr, 指针指头
open(DATA, '+>', "file.txt"); # +> wr, 可删除文件原有内容, 指针指头
open(DATA, '>>', "file.txt"); # 追加数据, 指针指尾
open(DATA, '+>>', "file.txt"); # 读取并追加, 指针指尾
close(DATA) || die "无法关闭文件";

# Another example
open(DATA1, "<file1.txt"); # 只读方式打开文件读取到DATA
open(DATA2, ">file2.txt"); # 写入方式打开文件读取到DATA
while(<DATA1>){ # 拷贝数据
   print DATA2 $_;
}
close( DATA1 );
close( DATA2 );

# Another example
open my $in, '<', $infile or die "Cannot open $infile: $!";
open my $out, '>', $outfile or die "Cannot open $outfile: $!";

## 10.2 Other functions
rename(oldname, newname); # rename the file
unlink(path); # delete the file
glob "path/*.file" # get all files in given path 

# 11. RegExp
# =~匹配, !~不匹配
# m// match, s/// replace, tr/// transform
if ($var =~ /run/){} # check whether $var matches "run", "m" is omitted
# Set "welcome to runoob site." as example
$string = "welcome to runoob site.";
$string =~ m/run/;
print "$`\n"; # welcome to
print "$&\n"; # run
print "$'\n"; # oob site.
# different modes for "m": i忽略大小写, m多行, s单行(.匹配\n), x忽略空格, o仅赋值一次
# 结尾模式: 'e'替换为指定表达式, 'g'替换所有, 'o'只匹配1次(没加g默认这个)
@nums = ($line =~ m/([\d]+)/g); # 获取line 中所有数字
$line =~ s/\d+.\d/int($&+0.5)/eg; # 四舍五入, 当然也可以不这么麻烦 --> 先计算好表达式再把变量填进去替换
$string =~ s/(love)/<$1>/; # 替换love为<love>
$var1 =~ m/$var2/; # 检查两个变量名是否相同

$line =~ s/^\s*//; $line =~ s/\s*$//; # 去除首尾空格
# different modes for "s": imosx, g替换所有匹配字符层,e替换字符串为表达式

$string =~ tr/a-z/A-Z/; # 小写转大写
# different modes for "tr": c转化所有未指定字符, d删除指定字符, s缩减重复字符

