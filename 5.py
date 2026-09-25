# 1
# fruits = ["apple", "banana", "cherry" , 'peach', 'grapes']
# fruits.remove('grapes')
# print(fruits)

# 2
# names = ['muhammad','ali','yahyo','abdurazzoq','usmon']
# ism = 'Abdulloh'
# # yangilik!! append qo'shuvchi
# names.append(ism)
# print(names)

# 3
# number = [10 ,25,7,30, 52 , 35646446 , 64 ,-9]
# print(max(number))
# print(min(number))
# print(len(number))

# 4
# colours = ['yellow', 'blue', 'red', 'green', 'pink']
# colours[0]='dark green'
# print(colours)

# 5
# cars = ['BMW', 'Ford', 'Volvo', 'Nissan', 'Toyota','Honda','Hyundai','Suzuki']
# del cars[0]
# print(cars)

# 6
numbers = [12, 5, 8, 21, 34, 7, 10, 15]
# juft sonlar
# for num in numbers:
#     if num %2 == 0:
#         print(num)
# toq sonlar
# for num in numbers:
#     if num % 2 == 1:
#         print(num)

# 7
# baholar = [3,2,5,6,4,5,7,8,5]
# print(sum(baholar)/len(baholar))
# print(baholar.count(5))
# print(2 in baholar)

# 8
# tushunmadim
numbers = []


for i in range(5):
    num = int(input(f"{i+1}-sonni kiriting: "))
    numbers.append(num)


max_number = numbers[0]

for num in numbers:
    if num > max_number:
        max_number = num

print("Eng katta son:", max_number)

