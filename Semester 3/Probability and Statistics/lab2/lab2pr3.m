pkg load statistics

binopdf(0, 3, 0.5)
1 - binopdf(0, 3, 0.5)
binocdf(2, 3, 0.5)
binocdf(1, 3, 0.5)

1 - binocdf(0, 3, 0.5)
 x = 1 - binocdf(1, 3, 0.5)
print("The probability of the event (X > 1) is %f", x)