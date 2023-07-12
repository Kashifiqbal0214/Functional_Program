# Name: Kashif Iqbal
# Date: 12/7/2023 | Wednesday
# Progam: Chapter 7 - Lists
# Description: Progam Assignment Instruction Series, Pure Python Assignment...

# CONSTANT
TITLE = "Welcom to Number Analysis Program!\n"
LINE = "-" * len(TITLE)
LIST_SIZE = 5


def main():
    """
    main Function description goes here...
    Including the all function in this function for calling
    """
    print(TITLE + LINE)
    numsList = getNums()
    lo = findLo(numsList)
    hi = findHi(numsList)
    total = findTotal(numsList)
    avg = findAvg(total)
    displayData(numsList, lo, hi, total, avg)


def getNums():
    """
    This function Describes..
    get numbers from user and append the number input to numsList through for loop,
    and return a List
    """
    numsList = []
    # For loop.. Collect Integer numbers from user which range is 5 List_size variable
    for nums in range(LIST_SIZE):
        numsList.append(int(input("Please Enter Number: ")))

    return numsList


def findLo(numsList):
    """
        This is function find a Lowest number,
    use a for loop iterating through  every element in numsList,
    Use if to check if the element is less then to  lo variable,
    then assign the list element to lo variable,
    and finally a return lowest number in lo variable
    """
    lo = numsList[0]
    for num in numsList:
        if num < lo:
            lo = num
    return lo


def findHi(numList):
    """
    findHi function  same as  work of the above function
    findLo but this find a Highest     numbers in the list,
    using a if to check if element is greater
    then hi variable then assign the list element to hi variable
    """
    hi = numList[0]
    for num in numList:
        if num > hi:
            hi = num
    return hi


def findTotal(numsList):
    """
    findTotal describes ,
    all element sums of numslist  through for loop then assign total
    variable and finally return total vairable
    """
    total = 0
    for num in numsList:
        total += num
    return total


def findAvg(total):
    """
    findAvg  describes.. how many  Average is total numbers in list
    """

    avg = total / LIST_SIZE
    return "{:.2f}".format(avg)


def displayData(numsList, lo, hi, total, avg):
    """
    This function displays the data..
    """
    print(LINE)
    print("Your Input Data:", numsList)
    print("Lowest Numbers: ", lo)
    print("Highest Number:", hi)
    print("Total Numbers: ", total)
    print("Average Numbers: ", avg)
    print(LINE)


main()
