% scalarMult(3, [2, 7, 4], Result). --> Result = [6, 21, 12]
scalarMult(A,[],[]).
scalarMult(A,[H1|R1],[H2|R2]) :-
        H2 is H1 * A,
        scalarMult(A, R1, R2).
