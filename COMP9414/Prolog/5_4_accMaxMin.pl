% accMax
accMax([H|T], Curr, Max) :- 
        H > Curr, 
        accMax(T, H, Max).
accMax([H|T], Curr, Max) :- 
        H =< Curr, 
        accMax(T, Curr, Max).
accMax([], Curr, Curr).


% accMin
accMin([H|T], Curr, Min) :- 
        H < Curr, 
        accMin(T, H, Min).
accMin([H|T], Curr, Min) :- 
        H >= Curr, 
        accMin(T, Curr, Min).
accMin([], Curr, Curr).
