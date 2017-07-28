% basic terminologies
tree(leaf(X), leaf(Y)) :- integer(X), integer(Y).
tree(tree(X1, X2), leaf(Y)) :- tree(X1, X2), integer(Y).
tree(leaf(Y), tree(X1, X2)) :- integer(Y), tree(X1, X2).
tree(tree(X1, X2), tree(Y1, Y2)) :- tree(X1, X2), tree(Y1, Y2).

% swap the left and right child
swap(tree(leaf(X1), leaf(X2)), tree(leaf(X2), leaf(X1))) :-
    integer(X1), integer(X2).
swap(tree(Tree1, leaf(X1)), tree(leaf(X1), Tree2)) :- 
    integer(X1), swap(Tree1, Tree2).
swap(tree(leaf(X1), Tree1), tree(Tree2, leaf(X1))) :-
    integer(X1), swap(Tree1, Tree2).
swap(tree(Tree1, Tree2), tree(Tree3, Tree4)) :- 
    swap(Tree1, Tree4), swap(Tree2, Tree3).

% swap(tree(tree(leaf(1),leaf(2)), leaf(4)), T). --> T = tree(leaf(4), tree(leaf(2),leaf(1))). --> true
