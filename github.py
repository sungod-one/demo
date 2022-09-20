import itertools

a_list = [1, 3, 5]
b_list = [2, 4, 6]
# 第一步取出a_list、b_list中可能2位数组合
def get_two_number(_list):
    res_list = []
    for index_i, item in enumerate(_list):
        for index_j in range(index_i + 1, len(_list)):
            res_list.append((_list[index_i], _list[index_j]))
    return res_list
a_two_list = get_two_number(a_list)
b_two_list = get_two_number(b_list)
# 全排列组合数字
res_list = []
for item_i in a_two_list:
    for item_j in b_two_list:
        iter_list = list(item_i) + list(item_j)
        tmp_list = list(itertools.permutations(iter_list))
        tmp_list = ["".join(map(str, list(tuple_item))) for tuple_item in tmp_list]
        res_list += tmp_list

print(res_list)
print(len(res_list))
