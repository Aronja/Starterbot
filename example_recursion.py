def recursion (message):
    count = 0
    while count < 5:
        print message
        count += 1
        recursion("Hi")

recursion("Hello")
