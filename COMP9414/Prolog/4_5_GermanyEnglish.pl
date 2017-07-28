% translation between Germany and English
tran(eins, one).
tran(zwei, two).
tran(drei, three).
tran(vier, four).
tran(fuenf, five).
tran(sechs, six).
tran(sieben, seven).
tran(acht, eight).
tran(neun, nine).

listtran([], []).
listtran(Ger, Eng) :-
    [HG|TG] = Ger,
    [HE|TE] = Eng,
    tran(HG,HE),
    listtran(TG,TE).
