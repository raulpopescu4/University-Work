pkg load statistics

%to solve normal law

miu = input("miu = ")
sigma = input("sigma = ")

%a
% P(X <= 0) = normcdf(0, miu, sigma)
% P(X >= 0) = 1 - P(X <= 0)

xmore = normcdf(0, miu, sigma)
xless = 1 - normcdf(0, miu, sigma)

%b    P(-1 <= X <= 1) = P(X <= 1) - P(X <= -1)
%                                 = normcdf(1, miu, sigma) - normcdf(-1, miu, sigma)
%      P(X <= -1 or X >= 1) = 1 - P(-1 <= X <= 1)

%c

% 0 < alpha < 1

alpha = input("alpha = ")
norminv(alpha, miu, sigma)

%d 

beta = input("beta = ")
norminv(1 - beta, miu, sigma)

% norm -> normal law quantile law, student law, fisher law, just changing prefix
% student -> t chi2-> chi squared law 
