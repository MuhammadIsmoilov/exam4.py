def sorting_list(list1 = [[1,4,5],[1,3,4],[2,6]]):
    empty_list = []
    empty_list.append(list1[0][0])
    empty_list.append(list1[0][1])
    empty_list.append(list1[0][2])
    empty_list.append(list1[1][0])
    empty_list.append(list1[1][1])
    empty_list.append(list1[1][2])
    empty_list.append(list1[2][0])
    empty_list.append(list1[2][1])
    empty_list.sort()
    return empty_list
print(sorting_list())