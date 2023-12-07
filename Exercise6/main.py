

def next_placements(used, n, k):
    """Output k of the following placements"""

    unused = [i for i in range(1, n + 1) if not(i in used)]
    index = len(used) - 1

    while (index >= 0) and (k != 0):
        if used[index] > max(unused + [used[j] for j in range(index + 1, len(used))]):
            index -= 1
        else:
            used[index] = min([unused[j] for j in range(len(unused)) if unused[j] > used[index]] + [used[j] for j in range(index + 1, len(used)) if used[j] > used[index]])
            unused = [i for i in range(1, n + 1) if not (i in used)]
            for i in range(index + 1, len(used)):
                used[i] = min(unused + [used[j] for j in range(i + 1, len(used))])
                unused = [j for j in range(1, n + 1) if not (j in used)]

            print(used)
            k -= 1
            index = len(used) - 1





if __name__ == '__main__':
    n = int(input("Enter n: "))
    k = int(input("Entet k: "))
    currentPlacements= [int(i) for i in input("Output k of the following placements: ").split()]
    next_placements(currentPlacements, n, k)



