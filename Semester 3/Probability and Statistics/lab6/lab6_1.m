pkg load statistics

%a
% H0: miu = 9
% H1: miu < 9 , 
% this is a left tail test for the mean when sigma is known
% cheat sheet a, 1, first line

alpha = input("give the significance \n");
x = [7, 7, 4, 5, 9, 9, 4, 12, 8, 1, 8, 7, 3, 13, 2, 1, 17, 7, 12, 5, 6, 2, 1, 13, 14, 10, 2, 4, 9, 11, 3, 5, 12, 6, 10, 7];
n = length(x);
%the null hyp is H0: miu = 9 
%the alt hyp is H1: miu < 9
%the left tailed test for the mean, when sigma known
printf("solving 1a\n");
printf("left tailed test for miu when sigma is known\n");
m0 = 9;
sigma = 5;

 %[H, P, CI, Z, ZCRIT] = ztest (X, M, S, NAME, VALUE);
 
 %H - 0 is not rejected - 1 is rejected
 %P - value
 %Z - TS0
 % the rest i am not interested in
 % X - data
 % M - miu0
 % SIGMA - sigma
 % NAME apartine {"alpha", "tail"}
 % VALUE depends on name

 [h, p, ci, z, zcrit] = ztest(x, m0, sigma, "alpha", alpha, "tail", "left");
 
 z2 = norminv(alpha);
 RR = [-inf, z2];
 
 printf("The value of h is %d\n",h);
 if h == 1
   printf("The null hypothesis H0 is rejected\n");
   printf("The data suggests that the standard is not met\n");
 else
   printf("The null hypothesis H0 is not rejected\n");
   printf("The data suggests that the standard is met\n");
 endif
 
 printf("The rej. region is (%4.4f, %4.4f)\n", RR);
 printf("The observed value of the test statistics is %4.4f\n", z);
 printf("The P - value of the test is %4.4f\n", p);
 
 
 %b
 
 % H0: miu = 5.5
 % H1: miu > 5.5
 
 % right tailed test for mean 
  %student's law for n-1 degrees of freedom
 
 m0 = 5.5
 
 %[H, PVAL, CI, STATS] = ttest(X, M);
 % stats - struct     stats.tstat = TS0 
 [h, p, ci, stats] = ttest(x, m0, "alpha", alpha, "tail", "right");
 
 t2 = tinv(1 - alpha, n - 1);
 RR = [t2,inf];

  printf("The value of h is %d\n",h);
 if h == 1
   printf("The null hypothesis H0 is rejected\n");
   printf("The data suggests that the standard is not met\n");
 else
   printf("The null hypothesis H0 is not rejected\n");
   printf("The data suggests that the standard is met\n");
 endif
 
 printf("The rej. region is (%4.4f, %4.4f)\n", RR);
 printf("The observed value of the test statistics is %4.4f\n", stats.tstat);
 printf("The P - value of the test is %4.4f\n", p);
 

 
