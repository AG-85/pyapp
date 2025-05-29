#Refactor duplicate logic into 1 function - this one was added to make sure you can remember what needs to be completed, like a reminder. You need to add todo in upper case with a colon

# addition
def addition(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
#print(addition(numbers))


#subtraction
def subtraction(numbers):
    total = numbers[0]
    for num in numbers[1:]:
        total -= num
    return total


#multiplication
def multiplication(numbers):
    total = 1
    for num in numbers:
        total *= num
    return total


#division
def division(numbers):
    total = numbers[0]
    for num in numbers[1:]:
        if num == 0:
            return 0
        total /= num
    return total

if __name__ == "__main__":
    print("calculating")
    print(addition([1, 2, 3]))
    print(subtraction([1, 2, 3]))