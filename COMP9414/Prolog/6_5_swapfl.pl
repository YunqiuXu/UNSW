% swapfl(List1, List2) --> swap the head and tail
swapfl_recursive([H1, H2], [H2, H1]).
swapfl_recursive([H1, H | T1], [H2, H | T2]) :-
    swapfl_recursive([H1 | T1], [H2 | T2]).
