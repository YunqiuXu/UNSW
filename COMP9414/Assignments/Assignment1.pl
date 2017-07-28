% COMP9414 Assignment 1 - Prolog Programming
% Author : Yunqiu Xu
% StudentID : z5096489
% Contact : yunqiuxu1991@gmail.com

% ----------------------------------------------------------------- %
% Question 1 : weird_sum(List, Result)
    % takes a List of numbers
    % computes the sum of the squares of the numbers in the list that are >= 5
    % then minus the sum of the absolute values of the numbers that are <= 2

% function sumSquare(List, Result) : return the sum of the squares of the numbers in the list 
sumSquare([], 0).
sumSquare([Head | Rest], Result) :-
   sumSquare(Rest, RestResult),
   Result is Head * Head + RestResult.

% function sumAbs(List, Result) : return the sum of absolute values of the numbers in the list
sumAbs([], 0).
sumAbs([Head | Rest], Result) :-
   sumAbs(Rest, RestResult),
   Result is abs(Head) + RestResult.

% consider the empty list, we can regard this as there just does not exist element >= 5 / <= 2
weird_sum([], 0).
% more general case: collect all elements >=5 and all those <=2 then perform calculation
weird_sum(List, Result) :-
    findall(GE, (member(GE , List), GE >= 5), GE5List), % get all elements >= 5
    findall(LE, (member(LE , List), LE =< 2), LE2List), % get all elements <= 2
    sumSquare(GE5List, R1),
    sumAbs(LE2List, R2),
    Result is R1 - R2.

% Question 1 test cases
% sumSquare([], R). --> R = 0
% sumSquare([1, 2, 3], R) --> R = 14
% sumSquare([0, 1, -2, 3], R) --> R = 14
% sumAbs([], R). --> R = 0
% sumAbs([1, 2, 3], R). --> R = 6
% sumAbs([0, 1, -2, 3], R). --> R = 6
% weird_sum([], R). --> 0
% weird_sum([3,6,2,-1], R). --> R = 33
% weird_sum([0,1,2,3,4,5,-6], R). --> 5*5 - 0 - 1 - 2 - 6 = 16
% weird_sum([0,-1,-2,-3,-4,-5,-6], R). --> -21
% weird_sum([0,0,1,1,2,2,4,4,6,-6], R). --> 6 * 6 - 0 - 0 - 1 - 1 - 2 - 2 - 6 = 24
% weird_sum([1,3,5,7,9,10,8,6,4,2,2,2,2,2,2], R). --> 5^2 + 6^2 + 7^2 + 8^2 + 9^2 + 10^2 - 1 - 2 - 2 - 2 - 2 - 2 - 2 = 342
% weird_sum([-1,3,-5,7,-9,9], R). --> 7^2 + 9^2 -1 - 5 - 9


% ----------------------------------------------------------------- %
% Question 2 : same_name(Person1,Person2)

% same family name as their father
% married women retain their original birth name
% True if it can be deduced from the facts in the database that Person1 and Person2 will have the same family name.

% mom's family name is different from her children

% they will have same family name if they have common ancestor or one of them are another one's male ancestor

% function maleAncestor(Person, Ancestor) --> return the maleAncestor of given person
maleAncestor(Person, Ancestor) :-
        parent(Ancestor, Person),
        male(Ancestor).
maleAncestor(Person, Ancestor) :-
        parent(P, Person),
        male(P),
        maleAncestor(P, Ancestor).
highestMaleAncestor(Person, Ancestor) :-
    findall(Ancestors, maleAncestor(Person, Ancestors), AList),
    length(AList, L),
    L =:= 0,
    Ancestor = Person.

% same_name(Person1, Person1).
% Person2 is Person1's male ancestor
same_name(Person1,Person2) :-
    maleAncestor(Person1, Person2).

% Person1 is Person2's male ancestor
same_name(Person1,Person2) :-
    maleAncestor(Person2, Person1).

% they have common male ancestor
same_name(Person1,Person2) :- 
    %findall(Ancestor1, maleAncestor(Person1, Ancestor1), A1List),
    %findall(Ancestor2, maleAncestor(Person2, Ancestor2), A2List),
    %intersection(A1List,A2List, Intersection),
    %length(Intersection, Length),
    %Length > 0.
    %method 2
    maleAncestor(Person1, A),
    maleAncestor(Person2, A).
same_name(Person1,Person2) :-
    highestMaleAncestor(Person1 , Person2).



% Question 2 test case 1
% Test code 1
parent(albert, jim).
parent(albert, peter).
parent(jim, brian).
parent(john, darren).
parent(peter, lee).
parent(peter, sandra).
parent(peter, james).
parent(peter, kate).
parent(peter, kyle).
parent(brian, jenny).
parent(irene, jim).
parent(irene, peter).
parent(pat, brian).
parent(pat, darren).
parent(amanda, jenny).
female(irene).
female(pat).
female(lee).
female(sandra).
female(jenny).
female(amanda).
female(kate).
male(albert).
male(jim).
male(peter).
male(brian).
male(john).
male(darren).
male(james).
male(kyle).
% same_name(albert, lee). --> true
% same_name(jim, kyle). --> true
% same_name(kyle, jim). --> true
% same_name(jenny, kyle). --> true
% same_name(darren, brian). --> false
% same_name(jim, peter). --> true
% same_name(X,jim). --> all those have same family name with jim
% same_name(albert, X). --> all decendants of albert


% Test code 2 : see ass1q2test2.pl


% ----------------------------------------------------------------- %
% Question 3 log_table(NumberList, ResultList)
log_table([],[]). 
log_table(NumberList, ResultList) :-
    [Head|Rest] = NumberList,
    [ResultHead|ResultRest] = ResultList,
    Head > 0, % if our input contains 0 or negative numbers, return false
    LogHead is log(Head),
    ResultHead = [Head | [LogHead]],
    log_table(Rest, ResultRest).

% Question 3 test cases
% log_table([1,3.7,5], Result). --> Result = [[1, 0.0], [3.7, 1.308332819650179], [5, 1.6094379124341003]].
% log_table([1,2,3,4,5], Result).
% log_table([64],Result).
% log_table([100000000,2], Result).

% ----------------------------------------------------------------- %
% Question 4 parity runs
% (maximal) sequence of consecutive even or odd numbers within the original list. 

% function removeEvenHead(List, Result, RestList): remove the even numbers from Head until we meet the first odd number or the List is empty, then we return both result(odd numbers) and RestList
removeEvenHead([], [], []).
removeEvenHead([Head|Rest], Result, RestList) :- 
    Head mod 2 =:= 0,
    removeEvenHead(Rest, RestResult, RestList),
    append([Head],RestResult,Result);
    Head mod 2 =:= 1,
    RestList = [Head|Rest],
    Result = [].

% function removeOddHead(List, Result, RestList): remove the odd numbers from Head until we meet the first even number or the List is empty, then we return both result(odd numbers) and RestList
removeOddHead([], [], []).
removeOddHead([Head|Rest], Result, RestList) :- 
    Head mod 2 =:= 1,
    removeOddHead(Rest, RestResult, RestList),
    append([Head],RestResult,Result);
    Head mod 2 =:= 0,
    RestList = [Head|Rest],
    Result = [].

% If we find the head is even --> we remove all the even number from the head of rest until we reach the first odd number
% If we find the head is odd --> we remove all the odd number from the head of rest until we reach the first even number
% case 1 : empty list since start
paruns([],[]).
% case 2 : even start
paruns(List, RunList) :-
    [Head|_] = List,
    Head mod 2 =:= 0,
    removeEvenHead(List, EvenResult, RestList),
    paruns(RestList, NewList),
    [EvenResult|NewList] = RunList.
% case 3 : odd start
paruns(List, RunList) :-
    [Head|_] = List,
    Head mod 2 =:= 1,
    removeOddHead(List, OddResult, RestList),
    paruns(RestList, NewList),
    [OddResult|NewList] = RunList.

% Question 4 test cases
% removeEvenHead([], R, RL). --> R = [], RL = []
% removeEvenHead([1,2,3], R, RL). --> R = [], RL = [1,2,3]
% removeEvenHead([2,4,3], R, RL). --> R = [2,4], RL = [3]
% removeEvenHead([2,-4,6,0,5,4,3,2,6,8], R, RL). --> R = [2,-4,6,0], RL = [5,4,3,2,6,8]
% removeOddHead([], R, RL). --> R = [], RL = []
% removeOddHead([1,2,3], R, RL). --> R = [1], RL = [2,3]
% removeOddHead([-1,3,5,0,7], R, RL). --> R = [-1,3,5], RL = [0,7]
% List = [8,0,4,3,7,2,-1,9,9] --> [[8, 0, 4],[3, 7],[2],[-1, 9, 9]]
% List = [-1,-2,-2,-3,3,-3,4,-4,-4,4,-5,5,-5,5,6,-5]
% List = [8,0,4,3,7,2,-1,9,9,6,8,0,2,-1,7,8,0,1,1,2]

% ----------------------------------------------------------------- %
% Question 5 is_heap(Tree) which returns true if Tree satisfies the heap property, and false otherwise.

is_heap(empty).
is_heap(tree(empty,_,empty)).
is_heap(tree(tree(LL,NumL,RL), Num, empty)) :-
    NumL >= Num,
    is_heap(tree(LL,NumL,RL)).
is_heap(tree(empty, Num, tree(LR,NumR,RR))) :-
    NumR >= Num,
    is_heap(tree(LR,NumR,RR)).
is_heap(tree(tree(LL,NumL,RL), Num, tree(LR,NumR,RR))) :-
    NumL >= Num,
    NumR >= Num,
    is_heap(tree(LL,NumL,RL)),
    is_heap(tree(LR,NumR,RR)).


% Question 5 test cases
%tree(empty,5,empty).
%tree(empty,3,tree(tree(empty,8,empty),5,tree(empty,7,empty))).
%tree(tree(tree(empty,4,empty),3,tree(empty,5,empty)),6,tree(tree(empty,9,empty),7,empty)).
%tree(tree(tree(tree(empty,20,empty), 12, empty),1,tree(empty, 3, empty)), 0, tree(empty,1,tree(tree(tree(tree(empty, 10, empty), 10, empty)), 10, tree(empty, 10, empty)))).
%tree(tree(tree(empty,20,empty), 12, empty),1,tree(empty, 3, empty)).
%tree(tree(empty, 10, empty), 10, empty).
%tree(empty, 10, empty).
%tree(tree(tree(empty,10,empty),10,empty),10,tree(empty,10,empty)).
%tree(tree(tree(empty, 10, empty), 10, empty),1,tree(empty, 10, tree(tree(tree(empty,10,empty),10,empty),10,tree(empty,10,empty)))).
%tree(tree(tree(tree(empty,20,empty), 12, empty),1,tree(empty, 3, empty)), 0, tree(tree(tree(empty, 10, empty), 10, empty),1,tree(empty, 10, tree(tree(tree(empty,10,empty),10,empty),10,tree(empty,10,empty))))).

% is_heap(tree(empty,5,empty)). --> true
% is_heap(tree(tree(tree(empty,4,empty),3,tree(empty,5,empty)),6,tree(tree(empty,9,empty),7,empty))). --> false
% is_heap(tree(empty,3,tree(tree(empty,8,empty),5,tree(empty,7,empty)))). --> true 
% is_heap(tree(tree(tree(empty,1,empty),1,tree(empty,1,empty)),1,tree(tree(empty,1,empty),1,empty))). --> true
