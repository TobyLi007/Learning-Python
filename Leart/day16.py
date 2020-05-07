def select_sort(original_items, comp = lambda x, y : x< y):
    items = original_items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items


def bubble_sort(original_items, comp = lambda x, y: x> y):
    items = original_items
    for i in range(len(items) - 1):
        swapped = False
        for j in range(len(items) - 1 - i):
            if comp(items[i], items[i+1]):
                items[i], items[i+1] = items[i+1], items[i]
                swapped = True
        if swapped:
            swapped = False
            for j in range(len(items) - 2- i, i, -1):
                if comp(items[j-1], items[j]):
                    items[j-1], items[j] = items[j], items[j-1]
                    swapped = True
        if not swapped:
            break
    return items


def merge_sort(original_items, comp = lambda x, y: x<= y):
    items = original_items
    if len(items) <2:
        return items
    mid = len(items)//2
    items_left = merge_sort(items[:mid], comp)
    items_right = merge_sort(items[mid:], comp)
    return merge(items_left, items_right, comp)
def merge(items_left, items_right, comp):
    index_left = 0
    index_right = 0
    items = []
    while index_left < len(items_left) and index_right < len(items_right):
        if comp(items_left[index_left, items_right[index_right]):
            items.append(items_left[index_left])
            index_left += 1
        else:
            items.append(items_right[index_right])
            index_right += 1
    items += items_left[index_left:]
    items += items_right[index_right:]
    return items


def seq_search(items, key):
    for index, item in enumerate(items):
        if key== item:
            return index
    return -1



def bin_search(items, key):
    start = 0
    end = len(items) -1
    while start < = end:
        mid = (start + end) //2
        if key > items[mid]:
            start = mid +1 
        elif key > items[mid]:
            end = mid -1 
        else:
            return mid
    return -1



prices = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}
prices_new ={stock: price for stock, price in prices.items() if price >100}
print(prices_new)


names = ['关羽', '张飞', '赵云', '马超', '黄忠']
courses = ['语文', '数学', '英语']
scores = [[None] * len(courses) for _ in range(len(names))]
for row, course in enumerate(courses):
    for col, name in enumerate(names):
        scores[row][col] = float(input(f'Please enter the {name}s scores of {course} '))
        
print(scores)

