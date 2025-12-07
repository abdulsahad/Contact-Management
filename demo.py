from sample_data import generate_contacts
from sorts import time_sort, merge_sort, bubble_sort

def demo(n=1000):
    mgr = generate_contacts(n)
    contacts = mgr.list_contacts()
    print(f"Generated {len(contacts)} contacts")
    # timing comparison on a sample of 500 to keep times reasonable
    sample = contacts[:500]
    tb = time_sort(bubble_sort, sample)
    tm = time_sort(merge_sort, sample)
    print(f"Bubble sort: {tb:.6f}s, Merge sort: {tm:.6f}s")

if __name__ == "__main__":
    demo(1000)
