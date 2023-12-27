pkg load statistics

n = input("Input the number of tries");
p = input("Input the probability of success");
x = 0:n;
y = binopdf(x, n, p);

plot(x, y, "*");
hold on;
xx = 0:0.01:n;
yy = binocdf(xx, n, p);
plot(xx, yy);