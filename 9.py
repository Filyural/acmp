n = int(input())
list_input = list(map(int, input().split()))

res_sum = 0
for i in range(n):
    if list_input[i] > 0:
        res_sum += list_input[i]

max_index = list_input.index(max(list_input))
min_index = list_input.index(min(list_input))

start = min(min_index, max_index)
end = max(min_index, max_index)

res_product = 1

for i in range(start + 1, end):
    res_product *= list_input[i]

print(res_sum, res_product)