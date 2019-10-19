##############################################################################
### https://www.w3resource.com/python-exercises/python-basic-exercises.php ###
##############################################################################

'''
1.  Write a Python program to print the following string in a specific format
    (see the output).
        Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output :

        Twinkle, twinkle, little star,
            How I wonder what you are! 
                Up above the world so high,   		
                Like a diamond in the sky. 
        Twinkle, twinkle, little star, 
            How I wonder what you are
'''
string = 'Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are'
print(string)

'''
2.  Write a Python program to get the Python version you are using.
'''
import sys

print(sys.version)

'''
3.  Write a Python program to display the current date and time.
        Sample Output :
        Current date and time :
        2014-07-05 14:34:14
'''
from datetime import datetime

date = datetime.now()
print('Current date and time:\n', date)

'''
4.  Write a Python program which accepts the radius of a circle from the user
    and compute the area.
        Sample Output :
        r = 1.1
        Area = 3.8013271108436504
'''
from math import pi

print(pi*float(input('Radius: '))**2)

'''
5.  Write a Python program which accepts the user's first and last name and
    print them in reverse order with a space between them.
'''
print(input('Second name: '), input('Name: '))

'''
6.  Write a Python program which accepts a sequence of comma-separated numbers
    from user and generate a list and a tuple with those numbers.
        Sample data : 3, 5, 7, 23
        Output :
        List : ['3', ' 5', ' 7', ' 23']
        Tuple : ('3', ' 5', ' 7', ' 23')
'''
list = [int(x) for x in input('Data: ').split(', ')]
tuple = tuple(list)
print(list)
print(tuple)

'''
7.  Write a Python program to accept a filename from the user and print the
    extension of that. Go to the editor
        Sample filename : abc.java
        Output : java
'''
print(input('File: ').split('.')[1])

'''
8.  Write a Python program to display the first and last colors from the
    following list.
    color_list = ["Red","Green","White" ,"Black"]
'''
color_list = ["Red","Green","White" ,"Black"]
print(color_list[0], color_list[-1])

'''
9.  Write a Python program to display the examination schedule. (extract the
    date from exam_st_date).
    exam_st_date = (11, 12, 2014)
        Sample Output : The examination will start from : 11 / 12 / 2014
'''
exam_st_date = (11, 12, 2014)
dt = exam_st_date
print('The examination will start from : %d / %d / %d' % (dt[0], dt[1], dt[2]))

'''
10. Write a Python program that accepts an integer (n) and computes the
    value of n+nn+nnn. Go to the editor
        Sample value of n is 5
        Expected Result : 615
'''
sn = str(int(input('n: ')))
print(int(sn) + int(sn+sn) + int(sn+sn+sn))

'''
11. Write a Python program to print the documents (syntax, description etc.) of
    Python built-in function(s).
        Sample function : abs()
        Expected Result :
        abs(number) -> number
        Return the absolute value of the argument.
'''
print(eval(input('Built-in function name: ')).__doc__)

'''
12. Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module.
'''
import calendar
#from datetime import datetime      # prevoiusly imported

now = datetime.now()
print(calendar.month(now.year, now.month))

'''
13. Write a Python program to print the following here document.
        Sample string :
        a string that you "don't" have to escape
        This
        is a ....... multi-line
        heredoc string --------> example
'''
print('''a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example''')

'''
14. Write a Python program to calculate number of days between two dates.
        Sample dates : (2014, 7, 2), (2014, 7, 11)
        Expected output : 9 days
'''
#from datetime import datetime      # prevoiusly imported

date1 = datetime.date(2014, 7, 2)
date2 = datetime.date(2014, 7, 11)
date3 = date2 - date1

print(date3.days, ' days')

