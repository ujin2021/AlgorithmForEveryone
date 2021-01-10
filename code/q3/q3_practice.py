# n명중 두명을 뽑아 짝을 지을 때 짝지을 수 있는 모든 조합(이름은 모두 다를 때)

def find_pair(name_list) :
    pair_set = set()
    n = len(name_list)
    for i in range(n-1) :
        for j in range (i+1, n) :
                pair_set.add(name_list[i] + '-' + name_list[j])
    return pair_set

print(find_pair(['Tom', 'Jerry', 'Mike']))
print(find_pair(['Tom', 'Jerry', 'Mike', 'John']))