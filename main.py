from searches.linear_search import linear_search

arr = list(map(int, input("Enter array elements: ").split()))
target = int(input("Enter element to search: "))

linear_search(arr, target)
