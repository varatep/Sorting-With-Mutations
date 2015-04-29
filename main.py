import time
from random import randrange
from random import randint


# Knuth's Shuffle
def knuth_shuffle(x):
    for i in range(len(x) - 1, 0, -1):
        j = randrange(i + 1)
        x[i], x[j] = x[j], x[i]
# end of shuffle


# Insertion Sort
def insertion_sort(l):
    c = 0
    for i in xrange(1, len(l)):
        j = i - 1
        key = l[i]
        while (l[j] > key) and (j >= 0):
            l[j + 1] = l[j]
            j -= 1
            c += 1
        l[j + 1] = key
    return c
# end of insertion sort


# merge sort
comp = 0
def merge_sort(m):
    global comp
    if len(m) <= 1:
        return m

    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]

    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))
# end merge sort


def merge(left, right):
    global comp
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        # change the direction of this comparison to change the direction of the sort
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
        comp += 1
    if left:
        result.extend(left[left_idx:])
    if right:
        result.extend(right[right_idx:])
    return result
# end merge


# Mutate
def mutate(m):
    r = randint(0, 9)
    # 10%: r<1
    # 20%: r<2
    # 30%: r<3
    if r < 3:
        f = randint(0, len(m) - 1)
        s = randint(0, len(m) - 1)
        while f == s:
            s = randint(0, len(m) - 1)
        temp = m[f]
        m[f] = m[s]
        m[s] = temp
        return 1
    # endif
    else:
        return 0
# end mutate


def mutateIterate(m):
    c = 0
    a = 0
    start = time.time()
    elapsed = 0
    while elapsed < 20:
        i = 1
        for i in xrange(1, len(m)):
            j = i - 1
            k = i
            if m[j] > m[k]:
                # compare, then mutate
                a += mutate(m)
                temp = m[j]
                m[j] = m[k]
                m[k] = temp
            else:
                a += mutate(m)
            c += 1
            # endif
        # endfor
        elapsed = time.time() - start
    # endwhile
    print("Number of mutates: {}".format(a))
    return c
# end iteration


def mutateBubble(alist):
    c = 0
    a = 0
    flag = 1  # 1 is swapped
    start = time.time()
    elapsed = 0
    while elapsed < 120:
        if flag == 1:
            flag = 0
            for passnum in range(len(alist) - 1, 0, -1):
                for i in range(passnum):
                    if alist[i] > alist[i + 1]:
                        flag = 1
                        a += mutate(alist)
                        temp = alist[i]
                        alist[i] = alist[i + 1]
                        alist[i + 1] = temp
                    else:
                        a += mutate(alist)
                    # endif
                    c += 1
                # endfor
            # endfor
        # endif
        elapsed = time.time() - start
    # endwhile

    print("Number of mutates: {}".format(a))
    return c
# end mutateBubble


# Inversion Count
def getInvCount(arr):
    inv_count = 0
    # Loop through each item in the array and check
    # if the previous item is greater than the next item
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                inv_count += 1

    return inv_count
# end inversion count


# Compute everything
x = list(range(5000))

knuth_shuffle(x)
print("shuffled")
q = getInvCount(x)
print("Number of inversions (pre-sort): {}".format(q))

# comparisons = insertion_sort(x)
# print("insertion sort comparisons: {}".format(comparisons))
# print("insertion sort: {}".format(x))

# x = merge_sort(x)
# print("merge sort comparisons: {}".format(comp))

d = mutateBubble(x)
print("MutateBubble sort comparisons: {}".format(d))

q = getInvCount(x)
print("Number of inversions (post-sort): {}".format(q))
# EOF