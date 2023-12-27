pkg load statistics

% two variables are the same if their pdfs are the same
% we could plot those pdfs to see that

n = input("n(n >= 30) = ")
p = input("p(p  <= 0.05) = ")

lambda = n * p

x = 0:n;
plot(x, binopdf(x, n, p), 'g')
hold on 
plot(x, poisspdf(x, lambda))



