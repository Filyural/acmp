list_input = input().split()
# сделаем вид, что питон не умеет сравинвать строки или такие большие числа
# и для практики пропишем это вручную
max_length = 0
for string in list_input:
    if len(string) > max_length:
        max_length = len(string)

max_strings = []
for string in list_input:
    if len(string) == max_length:
        max_strings.append(string)

if len(max_strings) == 0:
    print(max_strings[0])
    exit()

for i in range(max_length):
    max_tmp_elem = 0
    index = -1
    for j in range(len(max_strings)):
        if int(max_strings[j]) > max_tmp_elem:
            max_tmp_elem = int(max_strings[j])
            index = j
    if index != -1:
        print(max_strings[index])
        exit()
print(max_strings[0])