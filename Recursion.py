#Recursion
# define a sum() in python
def sum(my_list):
	if len(my_list)==0:
		return 0
	if len(my_list) > 1:
		return my_list[0] + sum(my_list[1::])
	else:
		return my_list[0]

#Answer
def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])
sum([1,2,4,5,6])

#define a conunt()

def conut(lis):
    if lis == []:
        return 0
    return 1 + conut(lis[1:])
count([1,2,4,5,6])

'''
今天用visualize python的时候，发现一个很有趣的功能，可以线上求助，然后我就点了求助按钮，果然过了几分钟真的有人回应了！
为了验证他不是机器人，我就问些很简单的问题，比如说不理解递归是啥意思，他就很热情的给我找视频，博客帮我理解。
后来我问他，有没有GitHub，博客什么的，他说没有，然后我就问我们能不能做朋友？
没想到他回答：朋友，我已经是个老人了...
致最真诚的祝福，给那些热爱敲代码的程序员们！
'''
