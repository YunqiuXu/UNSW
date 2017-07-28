accRev([H|T], A, R) :- accRev(T, [H|A], R).
accRev([], A, A).

% accRev([a,b,c,d,e],[],R) --> R = [e,d,c,b,a]
