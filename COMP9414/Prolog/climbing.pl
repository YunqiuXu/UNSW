% Program:  climbing.pl
% Source:   Prolog
%
% Purpose:  This is the sample program for the Prolog Lab in COMP9414/9814/3411.
% Editor: Yunqiu Xu


    % male(Person)
    % female(Person)
    %
    % The argument term for these predicates is a structure
    % representing a person.  It is in the form:
    % person(FirstName, LastName)
    %
    male(person('Will', 'Bilson')).
    male(person('Jim', 'Fried')).
    male(person('Barry', 'Drake')).
    female(person('Dot', 'Kanga')).

    % climb(Name, Grade, FirstAscentPerson, FirstAscentDate).
    %
    % This predicate records the climb details.
    %
    climb('Happy Go Lucky', 15, person('Barry', 'Drake'), date(11, 9,1996)).
    climb('High n Dry',     16, person('Jim', 'Fried'),   date(1,  4,2001)).
    climb('Roller',         21, person('Will', 'Bilson'), date(15, 9,2005)).
    climb('Naturally',      14, person('Barry', 'Drake'), date(11,10,1997)).
    climb('The Picnic',     10, person('Dot', 'Kanga'),   date(14, 2,1953)).

% 38 Write and execute a query to find the climbs first climbed by Barry Drake.
% climb(Fuck, _, person('Barry', 'Drake'), _).

% 39 climbs first climbed by a female
% female(person(F,L)), climb(Fuck, _, person(F, L), _).

% 40 41 which climbs were first climbed before "High n Dry"
% later: when the first date comes after the second
later(date(Day1, Month, Year), date(Day2, Month, Year)) :-
                Day1 > Day2.
later(date(_, Month1, Year), date(_, Month2, Year)) :-
                Month1 > Month2.
later(date(_, _, Year1), date(_, _, Year2)) :-
                Year1 > Year2.

% climb('High n Dry', _, _, HDDate),climb(_, _, _, FuckDate), later(HDDate, FuckDate), climb(FuckName, _, _, FuckDate).


