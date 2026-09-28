def input_data():
    global data

    print("Getting data from user")

    print("1. For 1D array")
    print("2. For 2D array")

    choice = int(input("Enter the choice: "))

    if choice == 1:
        nums = input("Enter the numbers with separated by spaces: ").split()
        data = list(map(int, nums))
        print("Input data added successfully.")

    elif choice == 2:
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of cols: "))

        data = []

        for i in range(rows):
            l = []

            for j in range(cols):
                num = int(input("Enter the number: "))
                l.append(num)

            data.append(l)

        print("Input data added successfully.")

    else:
        print("Invalid input")


def display_summary(data):
    row_data = []

    if len(data) > 0:
        for i in data:
            if type(i) == list:
                row_data.extend(i)
            else:
                row_data.append(i)

        print("Data Summary")
        print("Total elements:", len(row_data))
        print("Minimum value is:", min(row_data))
        print("Maximum value is:", max(row_data))
        print("Sum of all values is:", sum(row_data))
        print("The average is:", sum(row_data) / len(row_data))

    else:
        print("No data available")


def fact(num):
    if num <= 1:
        return 1

    return num * fact(num - 1)


def factorial():
    num = int(input("Enter the number: "))

    num_fact = fact(num)

    print("Factorial of", num, "is", num_fact)


def threshold_value(data):
    row_data = []

    for i in data:
        if type(i) == list:
            row_data.extend(i)
        else:
            row_data.append(i)

    threshold = int(input("Enter the threshold value: "))

    threshold_data = list(filter(lambda x: x > threshold, row_data))

    print("Values greater than threshold are:", threshold_data)


def sorting_data(data):
    row_data = []

    for i in data:
        if type(i) == list:
            row_data.extend(i)
        else:
            row_data.append(i)

    print("Select an option:")
    print("1. Ascending")
    print("2. Descending")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        row_data.sort()
        print(row_data)

    elif choice == 2:
        row_data.sort(reverse=True)
        print(row_data)

    else:
        print("Invalid choice")


def calculate_data(data):
    row_data = []

    for i in data:
        if type(i) == list:
            row_data.extend(i)
        else:
            row_data.append(i)

    total = len(row_data)
    sum_value = sum(row_data)
    minimum = min(row_data)
    maximum = max(row_data)
    avg = sum_value / total

    return sum_value, minimum, maximum, avg


def statistics_data(data):
    sum_value, minimum, maximum, avg = calculate_data(data)

    print("Sum:", sum_value)
    print("Minimum:", minimum)
    print("Maximum:", maximum)
    print("Average:", avg)


data = []

while True:
    print()
    print("Welcome")
    print("1. Input Data")
    print("2. Display Data Summary")
    print("3. Calculate Factorial")
    print("4. Threshold Value")
    print("5. Sorting Data")
    print("6. Statistics Data")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        input_data()

    elif choice == 2:
        display_summary(data)

    elif choice == 3:
        factorial()

    elif choice == 4:
        threshold_value(data)

    elif choice == 5:
        sorting_data(data)

    elif choice == 6:
        statistics_data(data)

    elif choice == 7:
        print("Thank you")
        break

    else:
        print("Invalid choice")