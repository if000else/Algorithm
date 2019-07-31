#Recursion
# define a sum() in python
def sum(my_list):
	if len(my_list)==0:
		return 0
	if len(my_list) > 1:
		return my_list[0] + sum(my_list[1::])
	else:
		return my_list[0]


