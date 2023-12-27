pkg load statistics 

% 0.05 <= p <= 0.95

p = input("p = ")

for n = 1:100:10000
    x = 0:n;
    plot(x, binopdf(x, n, p), 'g');
    pause(0.1);
  
endfor

% 