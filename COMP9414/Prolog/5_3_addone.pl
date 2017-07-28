% addone([1, 2, 7, 2], X). --> X = [2, 3, 8, 3]
addone([],[]).
addone([H1|R1], [H2|R2]) :-
    H2 is H1 + 1,
    addone(R1,R2).
