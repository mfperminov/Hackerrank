n = input()
list1 = [int(x) for x in input().split()]
m = input()
list2 = [int(x) for x in input().split()]
list3 = []
for i in range(m):
	if (list2.count(list2[i])>list1.count(list2[i])):
	 list3.append(list2[i])
list3 = sorted(list(set(list3)),key=int)
print (*list3)