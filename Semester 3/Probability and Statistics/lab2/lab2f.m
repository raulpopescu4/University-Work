pkg load statistics

N = input("nb of simulations");
C = rand(3, N);
Y = C < 0.5;
X = sum(Y);
hist(X)