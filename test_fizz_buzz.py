#!/usr/bin/env python3

"""
Escribe un programa que imprima los números del 1 al 100.
Pero para múltiplos de tres, imprima "Fizz" en lugar de
número y para los múltiplos de cinco imprima “Buzz”. Para
Números que son múltiplos de tres y cinco.
“FizzBuzz”.
"""


# Mi script fizz_buzz
def fizz_buzz(num_max):
    for n in range(1, num_max + 1):
        if n % 3 == 0 and n % 5 == 0:
            print('FizzBuzz')
        elif n % 3 == 0:
            print('Fizz')
        elif n % 5 == 0:
            print('Buzz')
        else:
            print(n)

fizz_buzz(100)

"""
Write a program that prints the numbers from 1 to 100.
But for multiples of three print “Fizz” instead of the
number and for the multiples of five print “Buzz”. For
numbers which are multiples of both three and five print
“FizzBuzz”.
"""

def fizz_buzz(max_num):
  for num in range(1, max_num + 1):
    if num % 3 == 0 and num % 5 == 0:
      print('FizzBuzz')
    elif num % 5 == 0:
      print('Buzz')
    elif num % 3 == 0:
      print('Fizz')
    else:
      print(num)


fizz_buzz(100)