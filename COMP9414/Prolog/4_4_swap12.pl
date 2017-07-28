% swap12(List1, List2) , their elements are same except the first two, which are swapped
% e.g. List1 = [1,2,3,4,5] , List2 = [2,1,3,4,5] --> true

swap12(List1, List2) :-
    [H1,H2|_] = List1,
    [H2,H1|_] = List2.
