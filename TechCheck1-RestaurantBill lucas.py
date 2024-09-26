#PROG 1700 – Tech Check #1
#Variables, Operators, Input/Output & Casting

# Restaurant Bill 
# You will create a console-based Python program that will calculate the amount of the tip, the tax, and the 
# total amount of a restaurant bill. The program will prompt the user to input the original amount of the bill. 
# The program will then output the amount of the tax (15% of the original amount) and a tip (20% of the original amount). 
# Finally, the program will output the new total of the bill.


def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    input("how much is your bill?")
    input =float
    tax = float(input*0.15)
    tip = float(input*0.20)
    def totalbill():
        totalbill= (input+float)+tax+tip
        print(input)
        print(tax)
        print(tip)
        print(totalbill)
        







    # YOUR CODE ENDS HERE

main()