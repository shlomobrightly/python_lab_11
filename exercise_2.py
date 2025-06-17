"""

Name: place_num

Input: a list of sorted numbers and a number (n)

Output: a new list with inserted the given number in corret order

Algorithm:  1- recieves a sorted list of numbers and a number "n"
            2- if the list is empty, returns the number "n", plus the list
            3- else, if first number in the list is greater than "n" or equal to it, returns the number "n", plus the list
            4- else, recursively returns the first number of the list plus the value from aplying the place_num function on the list with the first number sliced out



Name: main():

Input: 5 numbers, then another one

Output: text and a new list with inserted the given number in corret order

Algorithm:  1- prints text
            2- starts a empty list
            3- in a for loop, in the range of 5, inputs numbers to the created List
            4- prints text and the built List
            5- inputs a new number within text
            6- prints text and applies the place_num function on the built list and new inputed number
            
            
            
            
            

"""


def place_num(lst,n):
    if len(lst) == 0:
        return [n] + lst
    elif lst[0] >= n : 
        return [n] + lst
    else:
        return [lst[0]] + place_num(lst[1::],n)
    


        
def main():
    print("Enter elements:") 
    lst = []
    for i in range(5):
        lst.append(int(input()))
    print("The List:", lst)
    n = int(input("Enter new number: "))
    print("The New List:", place_num(lst,n))
    
    
main()    
