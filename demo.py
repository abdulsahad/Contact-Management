from sample_data import generate_contacts
from sorts import bubble_sort, merge_sort, time_sort

def demo(n=1000):
    contacts = generate_contacts(n)
    print(f"Generated {len(contacts)} contacts")
    sample = contacts[:500]
    tb = time_sort(bubble_sort, sample)
    tm = time_sort(merge_sort, sample)
    print(f"Bubble sort: {tb:.6f}s, Merge sort: {tm:.6f}s")
    sorted_sample = merge_sort(sample)[:10]
    print("First 10 contacts sorted by name (merge sort):")
    for c in sorted_sample:
        print(f"{c['name']} - {c['phone']}")

if __name__ == "__main__":
    demo(1000)
