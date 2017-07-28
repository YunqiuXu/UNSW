% palindrome([r, o, t, a, t, o, r]). --> true
% based on reverse
accRev([H|T], A, R) :- accRev(T, [H|A], R).
accRev([], A, A).

palindrome(List) :- 
    accRev(List, [], RL),
    RL = List.
    
