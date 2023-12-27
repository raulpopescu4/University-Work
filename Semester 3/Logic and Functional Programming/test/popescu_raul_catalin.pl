% minList(l1l2...ln, minVal) = 0, l1l2...ln = []
								 %minList(l2l3...ln, l1), l1 < minVal		
								% minList(l2l3...ln, minVal) otherwise
								 
% posMinVal(l1l2...ln, minVal, cnt) = 0, l1l2...ln = []
										%cnt U posMinVal(l2l3...ln, minVal, cnt+1), l1 = minVal
										%posMinVal(l2l3...ln, minVal, cnt+1), otherwise
										
										
%minList(i, i, o)
minList([], MinVal, MinVal).
minList([H|T], CurrentMin, MinVal):-
    H < CurrentMin,
    minList(T, H, MinVal).
minList([H|T], CurrentMin, MinVal):-
    H >= CurrentMin,
    minList(T, CurrentMin, MinVal).

%posMinVal(i, o, i, i)
posMinVal([], [], _, _).
posMinVal([H|T], [Cnt|R], MinVal, Cnt):-
    H =:= MinVal,
    Cnt1 is Cnt + 1,
    posMinVal(T, R, MinVal, Cnt1).
    
posMinVal([H|T], R, MinVal, Cnt):-
    H =\= MinVal,
    Cnt1 is Cnt + 1,
    posMinVal(T, R, MinVal, Cnt1).


% Popescu Raul Catalin
% 936
% PROLOG 23