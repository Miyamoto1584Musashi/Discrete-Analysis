

def nextk_permutations(used, n, k):
    unused = [i for i in range(1, n + 1) if not(i in used)]
    index = len(used) - 1
    while index >= 0 and k != 0:
        if used[index] > max(unused + [used[j] for j in range(index + 1, len(used))]):
            index -= 1
        else:
            element = used[index]
            used[index] = min([j for j in unused if j > used[index]] + [used[j] for j in range(index + 1, len(used)) if used[j] > used[index]])
            if used[index] in unused:
                unused.remove(used[index])
                unused.append(element)
            for i in range(index + 1, len(used)):
                element = used[i]
                used[i] = min(unused)
                if used[i] in unused:
                    unused.remove(used[i])
                    unused.append(element)
            k -= 1
            index = len(used) - 1
            print(used, unused)





if __name__ == '__main__':
    n = int(input())
    k = int(input())
    curr = [int(i) for i in input().split()]
    nextk_permutations(curr, n, k)



