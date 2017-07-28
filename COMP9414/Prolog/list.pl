% Program:  list.pl
% Source:   Prolog
%
% Purpose:  This is the sample program for the Prolog Lab in COMP9414/9814/3411.
% Editor: Yunqiu Xu


% X = .(3,[4]). --> X = [3 , 4]
% .(Head,Tail) = .(3,[5,6]). --> Head = 3, Tail = [5,6]


% 42 define a predicate is_a_list
is_a_list([]).
    is_a_list(.(Head, Tail)) :-
        is_a_list(Tail).

% 43 test
% ?- is_a_list([]). --> true
% ?- is_a_list(.(a, [])). --> true
% ?- is_a_list(.(a, b)). --> false
% ?- is_a_list(a). --> false

% 44 head_tail(List, Head, Tail), which will extract the Head and Tail from the List

head_tail(List, Head, Tail) :-
    .(Head,Tail) = List.

% 45 - 47 an element for membership in a list.
% base case
is_member(Element, list(Element, _)).
% recursion
is_member(Element, list(_,Tail)) :-
    is_member(Element, Tail).
% is_member(1, list(1, list(2, list(3, nil)))). --> true.
% is_member(3, list(1, list(2, list(3, nil)))). --> true.
% is_member(5, list(1, list(2, list(3, nil)))). --> false
% is_member(nil, list(1, list(2, list(3, nil)))). --> false.
% is_member(X, list(1, list(2, list(3, nil)))). --> X = 1, X = 2, X = 3

% 48-50
% [X, Y, Z] = [1, 2, 3]. --> X = 1, Y = 2, Z = 3
% [1, 2, 3, 4, 5, 6] = [Head | Tail]. --> Head = 1, Tail = [2,3,4,5,6]
% [1, 2] = [Head | Tail].
% [1] = [Head | Tail]. --> Head = 1, Tail = []
% [] = [Head | Tail]. --> false
% [Head| Tail] = [[]] --> Head = Tail, Tail = []
% [Head|Tail] = [[],[]]. --> Head = [], Tail = [[]]
% [Head|Tail] = [[[1]],[[2]]]. --> Head = [[1]], Tail = [[2]]
% [Head | Tail] = [[1, 2], [3, 4, [5, 6]], [7, 8], 9].
% What = [a | [b, c, d]].
% What = [a | [b]].
% What = [[a] | [b]]. --> What = [[a], b]
% What = [a | b]. --> What = [a|b]

% 51-52 build-in predicate member()
% member(1, [1, 2, 3]).
% member([], [1, 2, 3]). --> false
% member([1], [1, 2, 3]). --> false
% member(X, [a, b, c]). --> X = a, X = b, X = c
% member(a, List). -->
%   List = [a|_48] ;
%   List = [_46, a|_54] ;
%   List = [_46, _52, a|_60] ;
%   List = [_46, _52, _58, a|_66] ;
%   List = [_46, _52, _58, _64, a|_72] ;
%   List = [_46, _52, _58, _64, _70, a|_78] ;
%   List = [_46, _52, _58, _64, _70, _76, a|_84] ;
%   List = [_46, _52, _58, _64, _70, _76, _82, a|_90] ;
%   List = [_46, _52, _58, _64, _70, _76, _82, _88, a|...] ;
%   List = [_46, _52, _58, _64, _70, _76, _82, _88, _94|...] ;
%   List = [_46, _52, _58, _64, _70, _76, _82, _88, _94|...] ;
%   List = [_46, _52, _58, _64, _70, _76, _82, _88, _94|...] ;



% 53 concatenate two lists.
%base case
cons([], List, List).
%recursion: do until the first list is [] --> result = List --> then trace back
cons([Head | Tail], List, [Head|Result]) :-
    cons(Tail, List, Result).


    

