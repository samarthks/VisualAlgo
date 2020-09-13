import time


def bubblesort(arr, Generate_arr, times):
    for _ in range(len(arr) - 1):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                Generate_arr(
                    arr,
                    [
                        "yellow" if x == j or x == j + 1 else "red"
                        for x in range(len(arr))
                    ],
                )
                time.sleep(5 - times)

    Generate_arr(arr, ["yellow" for x in range(len(arr))])


def insertionsort(arr, Generate_arr, times):
    for _ in range(len(arr)):
        cur = arr[_]
        j = _
        while j > 0 and arr[j - 1] > cur:
            arr[j] = arr[j - 1]
            j -= 1
            Generate_arr(arr, ["yellow" if x == j else "red" for x in range(len(arr))])
            time.sleep(5 - times)
        arr[j] = cur

    Generate_arr(arr, ["yellow" for x in range(len(arr))])


def selectionsort(arr, Generate_arr, times):
    for _ in range(len(arr) - 1):
        min = _

        for j in range(_ + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
                Generate_arr(
                    arr, ["yellow" if x == min else "red" for x in range(len(arr))]
                )
                time.sleep(5 - times)
        temp = arr[min]
        arr[min] = arr[_]
        arr[_] = temp

    Generate_arr(arr, ["yellow" for x in range(len(arr))])


def partition(arr, head, tail, Generate_arr, times):
    border = head
    pivot = arr[tail]
    Generate_arr(arr, swapcolor(len(arr), head, tail, border, border))
    time.sleep(5 - times)
    for j in range(head, tail):
        if arr[j] < pivot:
            Generate_arr(arr, swapcolor(len(arr), head, tail, border, j, True))
            time.sleep(5 - times)
            arr[border], arr[j] = arr[j], arr[border]
            border += 1
        Generate_arr(arr, swapcolor(len(arr), head, tail, border, j))
        time.sleep(5 - times)

    Generate_arr(arr, swapcolor(len(arr), head, tail, border, tail, True))
    time.sleep(5 - times)
    arr[border], arr[tail] = arr[tail], arr[border]
    return border


def quicksort(arr, head, tail, Generate_arr, times):
    if head < tail:
        partitionIndex = partition(arr, head, tail, Generate_arr, times)
        quicksort(arr, head, partitionIndex - 1, Generate_arr, times)
        quicksort(arr, partitionIndex + 1, tail, Generate_arr, times)


def swapcolor(arrlen, head, tail, border, curr, isSwap=False):
    arr = []
    for i in range(arrlen):
        if i >= head and i <= tail:
            arr.append("gray")
        else:
            arr.append("white")
        if i == tail:
            arr[i] = "orange"
        elif i == border:
            arr[i] = "red"
        elif i == curr:
            arr[i] = "yellow"
        if isSwap:
            if i == border or i == curr:
                arr[i] = "green"
    return arr


def mergesort(arr, Generate_arr, times):
    mergesorta(arr, 0, len(arr) - 1, Generate_arr, times)


def mergesorta(arr, left, right, Generate_arr, times):
    if left < right:
        middle = (left + right) // 2
        mergesorta(arr, left, middle, Generate_arr, times)
        mergesorta(arr, middle + 1, right, Generate_arr, times)
        merge(arr, left, middle, right, Generate_arr, times)


def merge(arr, left, middle, right, Generate_arr, times):
    Generate_arr(arr, colorswap(len(arr), left, middle, right))
    time.sleep(5 - times)
    leftp = arr[left : middle + 1]
    rightp = arr[middle + 1 : right + 1]
    leftindex = rightindex = 0

    for index in range(left, right + 1):
        if leftindex < len(leftp) and rightindex < len(rightp):
            if leftp[leftindex] <= rightp[rightindex]:
                arr[index] = leftp[leftindex]
                leftindex += 1
            else:
                arr[index] = rightp[rightindex]
                rightindex += 1

        elif leftindex < len(leftp):
            arr[index] = leftp[leftindex]
            leftindex += 1
        else:
            arr[index] = rightp[rightindex]
            rightindex += 1
    Generate_arr(
        arr, ["green" if x >= left and x <= right else "white" for x in range(len(arr))]
    )
    time.sleep(5 - times)


def colorswap(length, left, middle, right):
    arr = []
    for i in range(length):
        if i >= left and i <= right:
            if i >= left and i <= middle:
                arr.append("yellow")
            else:
                arr.append("orange")
        else:
            arr.append("white")
    return arr

