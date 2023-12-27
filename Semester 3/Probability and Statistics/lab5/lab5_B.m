pkg load statistics

%1

x = [7, 7, 4, 5, 9, 9, 4, 12, 8, 1, 8, 7, 3, 13, 2, 1, 17, 7, 12, 5, 6, 2 , 1, 13, 14, 10 ,2 ,4 ,9 , 11, 3, 5, 12, 6, 10, 7];
n = length(x);
xbar = mean(x);
sigma = 5;
confidenceLevel = input("Give the value of 1 - alpha: ");
alpha = 1 - confidenceLevel;
z = norminv(1 - alpha/2);

m1 = xbar - (sigma/sqrt(n)) * z;
m2 = xbar + (sigma/sqrt(n)) * z;

printf("The conf int for the pop mean when sigma is known is(%4.3f, %4.3f)\n",  m1, m2);

t = tinv(1 - alpha/2, n - 1);
s = std(x);

mb1 = xbar - (s/sqrt(n)) * t;
mb2 = xbar + (s/sqrt(n)) * t;


printf("The conf int for the pop mean when sigma is not known is (%4.3f, %4.3f)\n ", mb1, mb2);

chiSquared1 = chi2inv(1 - alpha/2, n - 1);
chiSquared2 = chi2inv(alpha/2, n - 1);
sSquared = var(x);

mc1 = ((n - 1) * sSquared) / chiSquared1;
mc2 = ((n - 1) * sSquared) / chiSquared2;

printf("The conf int for the pop variance is (%4.3f, %4.3f)\n ", mc1, mc2);

printf("The conf int for the pop variance is (%4.3f, %4.3f)\n ", sqrt(mc1), sqrt(mc2));




%2 

