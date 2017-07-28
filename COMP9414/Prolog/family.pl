% Program:  family.pl
% Source:   Prolog
%
% Purpose:  This is the sample program for the Prolog Lab in COMP9414/9814/3411.
%           It is a simple Prolog program to demonstrate how prolog works.
%           See lab.html for a full description.
%
% History:  Original code by Barry Drake, editted by Yunqiu Xu


% parent(Parent, Child)
%
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


% female(Person)
%
female(irene).
female(pat).
female(lee).
female(sandra).
female(jenny).
female(amanda).
female(kate).

% male(Person)
%
male(albert).
male(jim).
male(peter).
male(brian).
male(john).
male(darren).
male(james).
male(kyle).


% yearOfBirth(Person, Year).
%
yearOfBirth(irene, 1923).
yearOfBirth(pat, 1954).
yearOfBirth(lee, 1970).
yearOfBirth(sandra, 1973).
yearOfBirth(jenny, 2004).
yearOfBirth(amanda, 1979).
yearOfBirth(albert, 1926).
yearOfBirth(jim, 1949).
yearOfBirth(peter, 1945).
yearOfBirth(brian, 1974).
yearOfBirth(john, 1955).
yearOfBirth(darren, 1976).
yearOfBirth(james, 1969).
yearOfBirth(kate, 1975).
yearOfBirth(kyle, 1976).

grandparent(Grandparent, Grandchild) :-
parent(Grandparent, Child),
parent(Child, Grandchild).

% older(Person1, Person2) :- Person1 is older than Person2
    %
older(Person1, Person2) :-
        yearOfBirth(Person1, Year1),
        yearOfBirth(Person2, Year2),
        Year2 > Year1.

% siblings(Child1, Child2) :- Child1 \= Child2 and Child1 share parents with Child2 %
% one result can not output twice %
% we need to consider that james does not have mom %
siblings(Child1, Child2) :-
        parent(P,Child1),
        parent(P,Child2),
        Child1 \= Child2.

% olderBrother(Brother, Person) :- return whether Brother is an older brother of Person %
olderBrother(Brother, Person) :-
        siblings(Brother, Person),
        male(Brother),
        older(Brother, Person).

% ------------------------------------------------------------- %
% 28,29 recursion : find all the descendants of a particular person%
% base case%
descendant(Person, Descendant) :-
        parent(Person, Descendant).
% recursive case%
descendant(Person, Descendant) :-
        parent(Person,Child),
        descendant(Child,Descendant).

% 30,31 find the ancestors of Kyle: without using descendant(Ancestor,kyle). %
ancestor(Person, Ancestor) :-
        parent(Ancestor, Person).
ancestor(Person, Ancestor) :-
        parent(P, Person),
        ancestor(P, Ancestor).

% ------------------------------------------------------------- %

% 54 descendant(albert,Descendant).
% 55 Prolog provides a predicate, findall, to put all the responses from such a query into a Prolog list
% findall(D, descendant(albert,D), List).

% 56 children(Parent, ChildList), where ChildList is the list of children of Parent
children(Parent, ChildList) :-
    findall(Child, parent(Parent,Child), ChildList).

% 57 sibling_list(Child, Siblings), which returns a list of the Child's siblings
sibling_list(Child, Siblings) :- 
    % findall(Sibling, siblings(Child, Sibling), Siblings).
    % to remove duplicates we can use setof(variable, constraint, set)
    setof(Sibling, siblings(Child, Sibling), Siblings).

% ------------------------------------------------------------- %

% 58 - 60 Arithmetic: is
% Expr = 1 + 2 * 3 + 4. --> Expr = 1 + 2 * 3 + 4, does not evaluate the expression
% Expr = (a + 5) / b. --> Expr = (a + 5) / b

% then we use 'is'
% Expr is 1 + 2 * 3 + 4. --> Expr = 11.
% Expr is (a + 5) / b . --> error, because this can not be calculated
% Expr is 1 + 2 * 3 + X . --> error, arguments are not sufficiently

% ------------------------------------------------------------- %

% 61 listCount(List, Count) --> count the elements of the list.
% base case
listCount([], Count) :-
    Count is 0.
% recursive case
listCount(List, Count) :-
    [_|Rest] = List,
    listCount(Rest, CountRest),
    Count is CountRest + 1.

% 62 count the number of descendants
countDescendants(Person, Count) :-
    findall(_, descendant(Person, _), DesList),
    listCount(DesList, Count).

% 63 counts all elements in the list and embedded lists
% base case
deepListCount([], Count) :-
    Count is 0.
% recursive case
deepListCount(List, Count) :-
    [Head|Rest] = List,
    deepListCount(Head, HeadCount),
    deepListCount(Rest, RestCount),
    Count is HeadCount + RestCount.
deepListCount(_, Count) :-
    Count is 1.


