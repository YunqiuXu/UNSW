% Russian dolls
% directlyIn(A,B) --> B is directly in A
% so the cover relation can be i in n, n in o, o in k
directlyIn(katarina, olga).
directlyIn(olga, natasha).
directlyIn(natasha, irina).

% in(A, B) --> check whether B is in A(not must directly)
in(Outer,Inner) :- directlyIn(Outer,Inner).
in(Outer,Inner) :-
    directlyIn(Outer, Sub),
    in(Sub, Inner).
