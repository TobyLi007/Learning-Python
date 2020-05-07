import itertools

item = []
item.append(list(itertools.permutations('ABCD')))
item.append(list(itertools.combinations('ABCDE', 3)))
item.append(list(itertools.product('ABCD', '123')))
print(item)


from collections import Counter

words = ['look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
	    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
	    'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
	    'look', 'into', 'my', 'eyes', "you're", 'under']
 counter = Counter(words)
 print(counter.most_common(2))

 