from decimal import Decimal as d
import decimal
# Generator used to create my_first_calculator

# Open a file that we can write to
goFile = open('main.go', 'w')
# The minimum and maximum numbers we can use
min_num = 0
max_num = 30
nums = range(min_num, max_num+1)
signs = ['+', '-', '/', '*']
num_of_ifs = len(signs)*(max_num-min_num+1)**2

print("""
package main

import "fmt"

func main() {
    fmt.Println("Welcome to this calculator!")
    fmt.Println("It can add, subtract, multiply and divide whole numbers from #min to #max")
   	var num1,num2 int
	var sign string
	fmt.Print("Please choose your first number: ")
	fmt.Scanln(&num1)
	fmt.Print("What do you want to do? +, -, /, or *: ")
	fmt.Scanln(&sign)
	fmt.Print("Please choose your second number: ")
	fmt.Scanln(&num2)""".replace("#min",str(min_num)).replace("#max",str(max_num)), file=goFile)

# For all the numbers and all the
for sign in signs:
    for num1 in nums:
        for num2 in nums:
            equation = "d({}){}d({})".format(num1, sign, num2)
            try:
                equals = eval(equation)
            except ZeroDivisionError:
                equals = 'Inf'
            except decimal.InvalidOperation as error:
                if error == decimal.DivisionByZero:
                    equals = 'Inf'
                else:
                    equals = 'Undefined'
            # No elif's used to be true to the story and also because
            # Python will throw a recursion error when too many are used
            print("""
            	if num1==#num1 && sign=="#sign" && num2==#num2 {
		            fmt.Println("#num1 #sign #num2 = #equals")
	            }""".replace("#num1",str(num1),2).replace("#num2",str(num2),2).replace("#sign",sign,2).replace("#equals",str(equals)), file=goFile)

print('fmt.Println("Thanks for using this calculator, goodbye :)")', file=goFile)
print('}', file=goFile)
# Close the file we have written to
goFile.close()