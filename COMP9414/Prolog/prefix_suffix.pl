% prefix(P, List)
prefix(P, List) :- append(P,_, List).

% suffix(S, List)
suffix(S, List) :- append(_,S, List).

% sublist(SubL, List) --> find all the sublists
sublist(SubL, List) :- 
    suffix(S, List), % for each suffix S
    prefix(SubL, S). % find the prefix of S as the sublist
