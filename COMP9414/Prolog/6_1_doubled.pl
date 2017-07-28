% check the doubled list
% doubled([1,2,3,1,2,3]) --> true
% doubled([a,b,c]) --> false

doubled(List) :- append(Subl,Subl,List).
