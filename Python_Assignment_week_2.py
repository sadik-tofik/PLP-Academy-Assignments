my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.insert(1, 15)
Another_list = [50, 60, 70]
my_list.extend(Another_list)
my_list.pop(-1)
my_list.sort()
for i in range(len(my_list)):
    if my_list[i]==30:
        print(i)
    