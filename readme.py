from time import *
s = '''
规则
在输入时输入四个数字
例如
将坐标为（1，7）的炮移动到坐标（4，7）
只需输入“1747”
输入错误时会自动提示
输棋的唯一方式是认输
输入“认输”即可
其它功能有待更新
建议将py文件属性（运行时右击标题栏）
改为
宽20高12缓冲高30
replay作用为复盘
若使用请先下一盘棋
否则报错
以上
'''
for i in range(len(s)):
    print(s[i],end = '')
    sleep(0.1)
print("退出",end = '')
sleep(0.5)
print('i',end = '')
sleep(0.5)
print('n',end = '')
sleep(0.5)
print('g',end = '')
sleep(0.5)
