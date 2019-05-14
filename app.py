# 6-4 讀、寫CSV檔案

file = open('data.txt', 'r')
file_list = file.readlines()
file.close()

# slicing the list 排除第一行(名稱部分) 並且排除換行符號
file_list = [line.strip() for line in file_list[1:]]
file_list_list = [line.split(',') for line in file_list]
# list of list 每個元素是['name', 'age', 'university', 'degree']
# [['rolf', '25', 'mit', 'computer science'], ['jose', '90', 'oxford', 'compu

for element in file_list_list:
    name = element[0].title()
    age = element[1]
    university = element[2].title()
    degree = element[3].capitalize()
    print(f'{name} is {age}, studying {degree} at {university}.')

# 或是這種寫法 time complexity較低
for line in file_list:
    personal_data = line.split(',')
    name = personal_data[0].title()
    age = personal_data[1]
    university = personal_data[2]
    degree = personal_data[3]
    print(f'{name} is {age}, studying {degree} at {university}.')


# 若given['Ryan', '25', 'nccu', 'finance']
# 想將'Ryan,25,nccu,finance'寫入csv file:
sample_csv_value = ','.join(['Ryan', '25', 'nccu', 'finance'])
# 使用.join()即可創造出'Ryan,25,nccu,finance'

file = open('data.txt', 'a')
file.write(sample_csv_value)
file.close()
