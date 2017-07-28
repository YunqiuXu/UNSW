% increment(Smaller, Larger) --> Smaller = Larger - 1
increment(Smaller, Larger) :-
    Smaller is Larger - 1.

% sum(A,B,S) --> S = A + B
sum(A, B, S) :- 
    S is A + B.
