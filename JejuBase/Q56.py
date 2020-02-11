nationWidth = {
    'Korea' : 220877,
    'Russia' : 17098242,
    'China' : 9596961,
    'France' : 543965,
    'Japan' : 377915,
    'England' : 242900

}

koreaWidth = nationWidth['Korea']
print(koreaWidth)
nationWidth.pop('Korea')
l = list(nationWidth.items())

for i in l:
    gap = max(nationWidth.values())
    if gap > abs(i[1] - koreaWidth):
        gap = abs(i[1] - koreaWidth) # 최솟값이됨
        item = i
print(item[0], gap)
