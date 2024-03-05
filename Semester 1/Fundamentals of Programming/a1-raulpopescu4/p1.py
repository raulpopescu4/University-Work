# Solve the problem from the first set here

#For a given natural number n find the largest natural number written with the same digits.


def freq_digit(number):
    nubmer = 12030230
    freq_arr={
        1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,0:0
    }
    while number != 0:
        freq_arr[number % 10] += 1
        number /= 10

  print(freq_arr)
