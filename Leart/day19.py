"""
假设小偷有一个背包，最多能装20公斤赃物，他闯入一户人家，发现如下表所示的物品。
很显然，他不能把所有物品都装进背包，所以必须确定拿走哪些物品，留下哪些物品。
贪婪法：在对问题求解时，总是做出在当前看来是最好的选择，不追求最优解，快速找到满意解。
输入：
20 6
电脑 200 20
收音机 20 4
钟 175 10
花瓶 50 2
书 10 1
油画 90 9
"""


class Thing(object):
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    @property
    def value(self):
        return self.price / self.weight

def input_thing():
    name_str, price_int, weight_str = input().split()
    return name_str, int(price_int), weight_str


def main():
    max_weight, num_of_things = map(int, input().split())
    all_things = []
    for _ in range(num_of_things):
        all_things.append(Thing (*input_thing()))
    all_things.sort(key= lambda x: x.value, reverse= True)
    total_weight, total_value = 0, 0
    for thing in all_things:
        if total_weight + thing.weight <= max_weight:
            total_value += thing.value
            total_weight += thing.weight
            print(f'小偷拿走了{thing.   name}')
        else:
            print(f'总价值: {total_value}美元')
            break 


if __name__ == '__main__':
    main()
"""
快速排序 - 选择枢轴对元素进行划分，左边都比枢轴小右边都比枢轴大
"""


def quick_sort(origin_items, comp = lambda x,y: x<= y):
    items = origin_items[:]
    _quick_sort(items, 0, len(items) - 1, comp)
    return items


def _quick_sort(items, start, end, comp):
    if start<end:
        pos = _partition(items, start, end, comp)
        _quick_sort(items, start, pos -1, comp)
        _quick_sort(items, pos+1, end, comp)


def _partition(items, start, end, comp):
    pivot = items[end]
    i = start -1
    for j in range(start, end):
        if comp(items[j], pivot):
            i+1
            items[i], items[j] =  items[j], items[i]
    items[i+1], items[end] = items[end] , items[i+1]
    return i+1

