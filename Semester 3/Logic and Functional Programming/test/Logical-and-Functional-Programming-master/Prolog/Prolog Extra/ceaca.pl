%(i,i,o)
gcd(A,0,A).
gcd(A,B,R):- A>B, gcd(B,A,R).
gcd(A,B,R):- M is B mod A, gcd(A,M,R).

%(i,i,o)
gcd2([],A,A).
gcd2([H|T],AUX,R):- gcd(H,AUX,R2), gcd2(T,R2,R).
