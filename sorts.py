from typing import List, Dict
import time

def bubble_sort(contacts: List[Dict], key='name') -> List[Dict]:
    arr = contacts[:]
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j][key].lower() > arr[j+1][key].lower():
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def merge_sort(contacts: List[Dict], key='name') -> List[Dict]:
    if len(contacts) <= 1:
        return contacts[:]
    mid = len(contacts)//2
    left = merge_sort(contacts[:mid], key)
    right = merge_sort(contacts[mid:], key)
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][key].lower() <= right[j][key].lower():
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def time_sort(func, contacts, key='name'):
    start = time.perf_counter()
    func(contacts, key)
    end = time.perf_counter()
    return end - start
