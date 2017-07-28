% last(List , X) --> if List is not empty and the last element is X, return true

% method 1, based on reverse
accRev([H|T], A, R) :- accRev(T, [H|A], R).
accRev([], A, A).

last1(List, X) :-
    accRev(List,[],[X|_]).

% method 2, recursion
last2([X], X).
last2(List, X) :-
    [_|Rest] = List,
    last2(Rest, X).
    
