% recursion exercise

directTrain(saarbruecken, dudweiler).
directTrain(forbach, saarbruecken).
directTrain(freyming, forbach).
directTrain(stAvold, freyming).
directTrain(fahlquemont, stAvold).
directTrain(metz, fahlquemont).
directTrain(nancy, metz).

% travelFromTo(nancy, saarbruecken). --> true
travelFromTo(Start,End) :- 
        directTrain(Start, End).
travelFromTo(Start,End) :- 
        directTrain(Start, Middle),
        travelFromTo(Middle, End).
