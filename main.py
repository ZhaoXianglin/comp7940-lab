def main():
    print("Hello World")

# exp2
def print_factor(x):
    for i in range(1, x+1):
        if x % i == 0:
            print("one factor is {0}".format(i))


if __name__ == '__main__':
    main()
    # Find the all factors of x using a loop and the operator % 
    # % means find remainder, for example 10 % 2 = 0; 10% 3 = 1
# exp1
    x = 52633
    for i in range(x+1):
    # your code here
        if i == 0:
            continue
        if x % i == 0:
            print("one factor is {0}".format(i))

# Write a program that be able to find all factors of the numbers in the list l
    l = [52633, 8137, 1024, 999]
    # your code here
    for item in l:
        print_factor(item)
