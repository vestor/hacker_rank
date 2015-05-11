mx = raw_input()
m = int(mx.split(' ')[0])
n = int(mx.split(' ')[1])
to_compare = -1
main_array = []
for x in range(0, m):
    ar = []
    ar.append(x)
    this_one = ar + map(int, raw_input().split(' '))
    main_array.append(this_one)
k = input()
# To sort the list in place...keep the initial order if two elements are same python
main_array.sort(key=lambda y: (y[k+1],y[0]))
for item in main_array:
    print ' '.join(map(str, item[1:]))
