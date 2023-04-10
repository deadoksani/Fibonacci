#Display numbers divisible by 5 from a list

#initialize a list
num_list = [10, 20, 33, 46, 55]

print("Given list:", num_list)
print('Divisible by 5:')

for num in num_list: #iterate through all elements of the list
    if num % 5 == 0: #using modulus operator, which returns the remainder
        print(num)
