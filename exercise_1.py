"""

Name: largest_num

Input: a list of numbers

Output: the largest number possibly made of the digits from the list

Algorithm:  1- sorts the given list from lowest to highest using sort() function
            2- sorst the given list from highest to lowest using reverse() function
            3- starts "num" as 0, and in a while loop, runs as long as the length of the list is larger than 1.
            4- in the loop, adds the first digit to "num", mutiplied by 10 in the power of the length of the list, minus 1
            5- slices off the last digit
            6- returns "num"
            
Time complications: O(n**2)

storage complications: O(n)





Name: main()

Input: numbers, ending with -1

Output: the largest number possibly made of the given digits

Algorithm:  1- prints text
            2- starts n as 0 and a empty list
            3- in a while loop, as long as n is not -1, inputs a number and adds it to the list
            4- if recived -1, and the length of the list is 1, prints a text
            5- else, prints a text with applying the largest_num function on the list, then devides it by 10 wholls
            
            
            
            
"""


#Enter digits:
#The largest number is: 
#Input Error


def largest_num(l):
    l.sort()
    l.reverse()
    num = 0
    while len(l) >1:
        num += (l[0])*(10**(len(l)-1))
        l = l[1::]
    return num    




def main():
    print("Enter digits:")
    n = 0
    l = []
    while n != -1:
        n = int(input())
        l.append(n)
        if n == -1:
            if len(l) == 1:
                print("Input Error")
                return
            else:
                print("The largest number is: ", (largest_num(l))//10)
    
main()    
