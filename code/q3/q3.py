# 첫째마당 - 알고리즘 기초
# 문제 03 동명이인 찾기

# 책 코드
def find_same_name(a) :
    n = len(a)
    result = set()
    for i in range(n) :
        for j in range(i+1, n) :
            if(a[i] == a[j]) :
                result.add(a[i])
    return result

# 내 코드
def find_same(name_list) :
    same = set()
    for i in name_list :
        if(name_list.count(i) > 1) :
            same.add(i)
    return list(same)

print(find_same_name(['Tom', 'Jerry', 'Mike', 'Tom']))
print(find_same_name(['Tom', 'Jerry', 'Mike', 'Tom', 'Jerry']))
print()
print(find_same(['Tom', 'Jerry', 'Mike', 'Tom']))
print(find_same(['Tom', 'Jerry', 'Mike', 'Tom', 'Jerry']))