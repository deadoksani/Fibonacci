#accept user input of 2 numbers and calculate their product
#if their product is greater than 1000, return their sum


def multiplication_or_sum(num1, num2): #define the function with 2 parameters
    product = num1 * num2 
    
 #add the condition   
    if product <= 1000:
        return product
    else:
        return num1 + num2


      #test with different number
result = multiplication_or_sum(2, 31)
print("The result is", result)


result = multiplication_or_sum(37, 30)
print("The result is", result)
