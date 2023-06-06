list = []
dict = {}
file_name_1 = '1.txt'
file_name_2 = '2.txt'
file_name_3 = '3.txt'


with open('2.txt', 'r', encoding = 'UTF-8') as file:
    count_2 = 0
    while True:
        s = file.readline()
        if not s:
            break
        count_2 += 1
list.append(count_2)
dict[count_2] = '2.txt'

with open('1.txt', 'r', encoding = 'UTF-8') as file:
    count_1 = 0
    while True:
        s = file.readline()
        if not s:
            break
        count_1 += 1
list.append(count_1)
dict[count_1] = '1.txt'

with open('3.txt', 'r', encoding = 'UTF-8') as file:
    count_3 = 0
    while True:
        s = file.readline()
        if not s:
            break
        count_3 += 1
list.append(count_3)
dict[count_3] = '3.txt'
max = max(list)
min = min(list)

new_file = open('new.txt', 'w')
for n in dict:
    if n == min:
        new_file.write(dict[n]+ '\n')
        new_file.write(str(n) + '\n')
        with open(dict[n], 'r', encoding = 'UTF-8') as file:
            while True:
                s = file.readline()
                new_file.write(s + '\n')
                if not s:
                    break
    elif n != min and n != max:
        new_file.write(dict[n] + '\n')
        new_file.write(str(n) + '\n')
        with open(dict[n], 'r', encoding='UTF-8') as file:
            while True:
                s = file.readline()
                new_file.write(s + '\n')
                if not s:
                    break
    elif n == max:
        new_file.write(dict[n] + '\n')
        new_file.write(str(n) + '\n')
        with open(dict[n], 'r', encoding='UTF-8') as file:
            while True:
                s = file.readline()
                new_file.write(s + '\n')
                if not s:
                    break
new_file.close()