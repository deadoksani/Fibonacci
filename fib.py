def fib(n):
    numbers = [0,1] #create a list where we know the o number of fib sequence is 0 and the first is 1
    for i in range(2, n+1): 
        numbers.append(numbers[i-1] + numbers[i-2]) #we add to prequence numbers to find the wanted fibonnaci number
    return numbers[n]

num = int(input("Enter the nth number: ")) #input from the user

print(fib(num)) #call the function
