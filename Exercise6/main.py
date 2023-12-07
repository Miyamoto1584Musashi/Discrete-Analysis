

def nextk_permutations(used, n, k):
    """ """

    unused = [i for i in range(1, n + 1) if not(i in used)]
    index = len(used) - 1

    while (index >= 0) and (k != 0):
        if used[index] > max(unused + [used[j] for j in range(index + 1, len(used))]):
            index -= 1
        else:
            used[index] = min([unused[j] for j in range(len(unused)) if unused[j] > used[index]] + [used[j] for j in range(index + 1, len(used)) if used[j] > used[index]])
            unused = [i for i in range(1, n + 1) if not (i in used)]
            for i in range(index + 1, len(used)):
                used[i] = min(unused[::] + [used[j] for j in range(i + 1, len(used))])
                unused = [j for j in range(1, n + 1) if not (j in used)]

            print(used, unused)
            k -= 1
            index = len(used) - 1





if __name__ == '__main__':
    n = int(input())
    k = int(input())
    curr = [int(i) for i in input().split()]
    nextk_permutations(curr, n, k)



