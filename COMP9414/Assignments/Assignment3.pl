% COMP9414 Assignment 3, 
% Group ID: 240
% Author : Yunqiu Xu && Qihai Shuai 
% ID : z5096489 && z5119437


%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Procedure 1 %%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                       trigger(+Events, -Goals)                   %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Input: 
%		Events = [truffle(X,Y,S),truffle(X1,Y1,S1),restaurant(X2,Y2,S2)]
% Output : 
%		Goals = goals(Goals_rest,Goals_truff), generate the goals based on events

% Case 1: base case
trigger([], goals([], [])).
% Case 2: insert restaurant into Goals_rest
trigger([Head|Rest], goals(Goals_rest, Goals_truff)) :-
    restaurant(X, Y, S) = Head,
    trigger(Rest, goals(Goals_rest_new, Goals_truff)),
    append([goal(X, Y, S)], Goals_rest_new, Goals_rest).
% Case 3: insert truffle into Goals_truff
trigger([Head|Rest], goals(Goals_rest, Goals_truff)) :-
    truffle(X, Y, S) = Head,
    trigger(Rest, goals(Goals_rest, Goals_truff_new)),
    append([goal(X, Y, S)], Goals_truff_new, Goals_truff).



%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Procedure 2 %%%%%%%%%%%%%%%%%%%%%%%%%%%%
%   incorporate_goals(+Goals, +Beliefs, +Intentions, -Intentions1)  %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Input:
%       Goals: goals(Goals_rest,Goals_truff)
%       Beliefs : beliefs(at(X,Y),stock(T))
%       Intentions : intents(Int_sell,Int_pick)
% Output:
%       Intentions1: update the Intentions

% Case 1: no new goals
incorporate_goals(goals([],[]), _, Intentions, Intentions).
% Case 2: we use helper function insert() to insert a list of goals into a list of intentions
incorporate_goals(Goals, Beliefs, Intentions, Intentions1) :-
    goals(Goals_rest, Goals_truff) = Goals,
    intents(Int_sell, Int_pick) = Intentions,
    insert(Goals_rest, Beliefs, Int_sell, Int_sell1),
    insert(Goals_truff, Beliefs, Int_pick, Int_pick1),
    Intentions1 = intents(Int_sell1, Int_pick1).


% insert(+Goals_list, +Beliefs, +Int_list, -Int_list1)
% 	helper procedure for incorporate_goals
% 	transform all elements(goals) of Goals_list as intentions, then insert them into appropriate position of Int_list
%   use a helper function "insert_into([goal(O_X, O_Y, O_V), []], Beliefs, Int_list, Int_list_new)" to insert one intention into intention list.

% Case 1: base case 
insert([], _, Int_list, Int_list).
% Case 2: this goal is already in Int_list, we skip it
insert([Head|Rest], Beliefs, Int_list, Int_list1) :-
    goal(O_X, O_Y, O_V) = Head,
    member([goal(O_X, O_Y, O_V), _], Int_list),
    insert(Rest, Beliefs, Int_list, Int_list1).
% Case 3: this goal is a new goal, we insert it into Int_list
insert([Head|Rest], Beliefs, Int_list, Int_list1) :-
    goal(O_X, O_Y, O_V) = Head,
    insert_into([goal(O_X, O_Y, O_V), []], Beliefs, Int_list, Int_list_new),
    insert(Rest, Beliefs, Int_list_new, Int_list1).


% insert_into(+Intention, +Beliefs, +Int_list, -Int_list_new)
% 	helper procedure for insert
% 	insert the Intention into Int_list to form a new Int_list
% 	note that we have tested that this intention is not in Int_list, otherwise we will skip this procedure
% 	Perform traversal from the start of Int_list, put all elements with larger value into LargerV until we meet a "<=" element
% 	Then we put all of the rest elements into EqualSmallerV
% 	Perform traversal from the start of EqualSmallerV, put all elements with same value into EqualV until we meet a "!=" element
% 	Then we put all of the rest elements into InequalV
% 	Perform traversal from the start of EqualV, put all elements with <= distance into SmallerEqualD until we meet a ">" element
% 	Then we put all of the rest elements into LargerD
% 	Finally we connect the lists: LargerV - SmallerEqualD - [Intention] - LargerD - InequalV
insert_into(Intention, Beliefs, Int_list, Int_list_new) :-
    split_larger_equalsmaller(Int_list, Intention, LargerV, EqualSmallerV),
    split_equal_inequal(EqualSmallerV, Intention, EqualV, InequalV),
    split_smaller_equallarger_distance(EqualV, Intention, Beliefs, SmallerEqualD, LargerD),
    append(LargerV, SmallerEqualD, Temp1),
    append(Temp1, [Intention], Temp2),
    append(Temp2, LargerD, Temp3),
    append(Temp3, InequalV, Int_list_new).


% split_larger_equalsmaller(Int_list, Pivot, LargerV, EqualSmallerV)
% 	helper procedure for insert_into
% 	traverse all of the elements from start until we meet the first one smaller or equal than pivot
% 	note that not all elements in EqualSmallerV are <= pivot, this list just starts from the first element satisfies this constraint
% 	E.G. For [5,4,2,1,3] and pivot = 2 --> LargerV is [5,4], EqualSmallerV is [2,1,3]

% Case 1: Int_list is empty, we do not need split
split_larger_equalsmaller([], _, [], []).
% Case 2: Current intention > Pivot --> put it into LargerV
split_larger_equalsmaller([Head|Rest], Pivot, LargerV, EqualSmallerV) :-
    [goal(_, _, O_V), _] = Head,
    [goal(_, _, P_V), _] = Pivot,
    O_V > P_V,
    split_larger_equalsmaller(Rest, Pivot, LargerVNew, EqualSmallerV),
    append([Head], LargerVNew, LargerV).
% Case 3: Current intention <= Pivot --> put all of the rest into EqualSmallerV
split_larger_equalsmaller([Head|Rest], _, LargerV, EqualSmallerV) :-
    LargerV = [],
    EqualSmallerV = [Head|Rest].


% split_equal_inequal(+Int_list, +Pivot, -EqualV, -InequalV)
% 	helper procedure for insert_into
% 	traverse all of the elements from start until we meet the first one that is not equal to pivot
% 	note that not all elements in InequalV are != pivot, this list just starts from the first element satisfies this constraint
% 	E.G. For [2,2,3,2,1] and pivot = 2 --> [2,2], [3,2,1]

% Case 1: base case, Int_list is empty, we do not need split
split_equal_inequal([], _, [], []).
% Case 2: Current intention \= Pivot --> put all the list into InequalV
split_equal_inequal([Head|Rest], Pivot, EqualV, InequalV) :-
    [goal(_, _, O_V), _] = Head,
    [goal(_, _, P_V), _] = Pivot,
    O_V \= P_V,
    EqualV = [],
    InequalV = [Head|Rest].
% Case 3: Current intention == Pivot --> put head into EqualV
split_equal_inequal([Head|Rest], Pivot, EqualV, InequalV) :-
    split_equal_inequal(Rest, Pivot, EqualVNew, InequalV),
    append([Head], EqualVNew, EqualV).


% split_smaller_equallarger_distance(+Int_list, +Pivot, +Beliefs, -SmallerEqualD, -LargerD)
% 	helper procedure for insert_into
% 	for those with same values, we calculate their distance to belief
% 	partition the Intention list by pivot
%   SmallerEqualD means elements whose diatance is smaller than or equal to pivot, until we meet the first one does not satisfy this constraint
%   LargerD means When we meet the first element whose distance > pivot, add the rest list as LargerD

% Case 1: base case, if the list is empty, we do not need to split
split_smaller_equallarger_distance([], _, _, [], []).
% Case 2: distance of (Head, Beliefs) =< distance of (Pivot, Beliefs), add Head to SmallerEqualD
split_smaller_equallarger_distance([Head|Rest], Pivot, Beliefs, SmallerEqualD, LargerD) :-
    [goal(O_X, O_Y, _),_] = Head,
    [goal(P_X , P_Y, _), _] = Pivot,
    beliefs(at(Be_X,Be_Y),_) = Beliefs,
    distance((O_X,O_Y), (Be_X,Be_Y), D_old),
    distance((P_X,P_Y), (Be_X,Be_Y), D_new),
    D_old =< D_new,
    split_smaller_equallarger_distance(Rest, Pivot, Beliefs, SmallerEqualDNew, LargerD),
    append([Head], SmallerEqualDNew, SmallerEqualD).
% Case 3: distance of (Head, Beliefs) > distance of (Pivot, Beliefs), set all the rest as LargerD
split_smaller_equallarger_distance([Head|Rest], _, _, SmallerEqualD, LargerD) :-
    SmallerEqualD = [],
    LargerD = [Head|Rest].



%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Procedure 3 %%%%%%%%%%%%%%%%%%%%%%%%%%%%
%   get_action(+Beliefs, +Intentions, -Intentions1, -Action)  %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Input:
% 		Beliefs: beliefs(at(X, Y), stock(T))
% 		Intentions: intents(Int_sell, Int_pick)
% Output:
% 		Intentions1: update the Intentions, with the form intents(Int_sell, Int_pick)
% 		Action: the action chosen

% Case 1: Int_sell selected 
get_action(Beliefs, Intentions, Intentions1, Action):-
    intents(Int_sell, Int_pick) = Intentions,
	select_intention(Beliefs, Int_sell, Int_pick, 0, NewIntentions),
	select_action(Beliefs, NewIntentions, 0, UpdatedIntentions, Action),
	Intentions1 = intents(UpdatedIntentions, Int_pick),!.
% Case 2: Int_pick selected 
get_action(Beliefs, Intentions, Intentions1, Action):-
    intents(Int_sell, Int_pick) = Intentions,
	select_intention(Beliefs, Int_sell, Int_pick, 1, NewIntentions),
	select_action(Beliefs, NewIntentions, 1, UpdatedIntentions, Action),
	Intentions1 = intents(Int_sell, UpdatedIntentions),!.
% Case 3: no Intention selected
get_action(Beliefs, Intentions, Intentions, move(X, Y)):- 
	beliefs(at(X, Y), _) = Beliefs,
    intents(Int_sell, Int_pick) = Intentions,
	select_intention(Beliefs, Int_sell, Int_pick, 2, []). 


% select_intention(+Beliefs, +Int_sell, +Int_pick, -Flag, -SelctedIntentions)
% 	helper procedure for get_action 
% 	Flag to determine whether Int_sell or Int_pick selected or no intention selected
% 	SelctedIntentions is the selected intention content
 
% Case 1: Int_sell selected, Flag set to 0 
% 1st intention in Int_sell [goal(X, Y, S), Plan] S <= T , T is the current stock 
select_intention(beliefs(at(_, _), stock(T)), Int_sell, _, 0, Int_sell):- 
	Int_sell \= [], 
	[[goal(_,_,S), _] | _] = Int_sell,  
	S =< T,!.	
% Case 2: Int_pick selected, Flag set to 1 
% else when 1st Int_pick exists, then first [goal(X, Y, S), Plan] is selected
select_intention(_, _, Int_pick, 1, Int_pick):- 
	Int_pick \= [],!.
% Case 3: empty list, Flag set to 2
% else, no intention selected, should just stay and do nothing 	
select_intention(_, _, _, 2, []).


% select_action(+Beliefs, +Intentions, +Flag, -NewIntentions, -Action)
% 	helper procedure for get_action
% 	judging by the Intentions selected then get the action and the update intentions 

% Case 1: 1st action applicable 
select_action(_, [FirstIntent | RestIntents], _, [[Goal, RestPlan] | RestIntents], Action) :-
	decompose_intention(FirstIntent, Goal, [[Action | RestPlan]]), % need double [] 
	applicable(Action).	
% Case 2: otherwise Action is not applicable so create a new Plan for the Goal
select_action(Beliefs, [FirstIntent | RestIntents], Flag, [[Goal, RestPlan] | RestIntents], Action) :-
    decompose_intention(FirstIntent, Goal, [[NonApplicableAction | _]]), % need double [] 
    not(applicable(NonApplicableAction)),
    new_plan(Goal, Beliefs, Flag, NewPlan),	
    rest_plan(NewPlan, Action, RestPlan).
% Case 3: Intention is empty not the intentions list empty
select_action(Beliefs, [[Goal, []] | RestIntents], Flag, [[Goal, RestPlan] | RestIntents], Action) :-
    new_plan(Goal, Beliefs, Flag, NewPlan), 
	rest_plan(NewPlan, Action, RestPlan). 


% rest_plan(+CurrentPlan, -Action, -NewPlan)
%	helper procedure for new_plan
% 	extract the Action from the CurrentPlan then get Action and following NewPlan
rest_plan([Action | NewPlan], Action, NewPlan).  


% decompose_intention(+Intention, -Goal, -Plan)
%	helper procedure for new_plan 
% 	split the Intention with Goal and Plan 
decompose_intention([Goal | Plan], Goal, Plan).


% new_plan(+Goal, +Beliefs, +Flag, -NewPlan)
%	helper procedure for select_action
% 	construct a new plan from empty list 	

% Case 1: base case, no action in the plan, using cut to only generate one available solution
new_plan(Goal, Beliefs, Flag, NewPlan):- 	
	new_plan(Goal, Beliefs, Flag, [], NewPlan),!.
% Case 2: Flag = 1, already at the goal location, just insert the pick action 
new_plan(goal(X, Y, _), beliefs(at(X, Y), _), 1, SoFar, NewPlan) :-
    reverse_list([pick(X, Y) | SoFar], NewPlan). 
% Case 3: Flag = 0, already at the goal location, just insert the sell action 
new_plan(goal(X, Y, _), beliefs(at(X, Y), _), 0, SoFar, NewPlan) :-
    reverse_list([sell(X, Y) | SoFar], NewPlan).
% Case 4: if not at goal location, should keep constructing the way how to move there 
new_plan(Goal, beliefs(at(X, Y), Stock), Flag, SoFar, NewPlan) :-
    move_valid(X, Y, move(XNew, YNew)),
    move_closer(move(XNew, YNew), at(X, Y), Goal), % XNew, YNew should be closer than X, Y to the goal
    new_plan(Goal, beliefs(at(XNew, YNew), Stock), Flag, [move(XNew, YNew) | SoFar], NewPlan).


% reverse_list(+List, -ReversedList)
% 	helper procedure for new_plan
%   adding new aciton in the head and then reverse this list 
reverse_list(List, ReversedList) :-
    reverse_list(List, [], ReversedList).
reverse_list([], ReversedList, ReversedList).
reverse_list([X | Rest], SoFar, TotalReversedList) :-
    reverse_list(Rest, [X | SoFar], TotalReversedList).


% move_valid(+X, +Y, -Move)
% 	helper procedure for new_plan
% 	determine all valid moves for a given X, Y coordinate
% 	first try Y direction then X direction 
move_valid(X, Y, Move) :-
    YNext is Y + 1, Move = move(X, YNext);
    YNext is Y - 1, Move = move(X, YNext);
    XNext is X + 1, Move = move(XNext, Y);
    XNext is X - 1, Move = move(XNext, Y). 


% move_closer(+Move, +Location, +Goal)
% 	helper procedure for new_plan
% 	Move need to be closer to Goal than the current location
move_closer(move(X, Y), at(XCurrent, YCurrent), goal(XGoal, YGoal, _)) :-
    distance((X, Y), (XGoal, YGoal), D1),
    distance((XCurrent, YCurrent), (XGoal, YGoal), D2),
    D1 < D2.



%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Procedure 4 %%%%%%%%%%%%%%%%%%%%%%%%%%%%
%   update_beliefs(+Observation, +Beliefs, -Beliefs1)     % 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Input : 
%       Observation
%       Beliefs
% Output : 
% 		Update beliefs based on Observation
% E.G. Type of Observation:
%       at(3,4) --> Set location as at(3,4)
%       sold(1,6,9) --> Set stock as T - 9
%       picked(0,8,7) --> Set stock as T + 7

% Case 1 : at
update_beliefs(at(X,Y), beliefs(at(_, _),stock(T)), Beliefs1) :-
    Beliefs1 = beliefs(at(X,Y), stock(T)).
% Case 2 : sold
update_beliefs(sold(X,Y,S), beliefs(at(_, _),stock(T)), Beliefs1) :-
    T_new is T - S,
    Beliefs1 = beliefs(at(X,Y), stock(T_new)).
% Case 3 : picked
update_beliefs(picked(X,Y,S), beliefs(at(_, _),stock(T)), Beliefs1) :-
    T_new is T + S,
    Beliefs1 = beliefs(at(X,Y), stock(T_new)).



%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Procedure 5 %%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 	update_intentions(+Observation, +Intentions, -Intentions1)  %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Input : 
%       Observation = at / sold / picked
%       Intentions = intents(Int_sell,Int_pick)
% Output : 
%		Update intentions based on Observation
% E.G. Type of Observation:
%       at(3,4) --> do not change intentions
%       sold(1,6,9) --> find intention from Int_sell, and remove it
%       picked(0,8,7) --> find intention from Int_pick, and remove it

% Case 1: at
update_intentions(at(_,_), Intentions, Intentions).
% Case 2: sold
update_intentions(sold(X,Y,_), intents(Int_sell,Int_pick), Intentions1) :- 
    delete(Int_sell, [goal(X,Y,_),_], Int_sell_new),
    Intentions1 = intents(Int_sell_new, Int_pick).
% Case 3: picked
update_intentions(picked(X,Y,_), intents(Int_sell,Int_pick), Intentions1) :- 
    delete(Int_pick, [goal(X,Y,_),_], Int_pick_new),
    Intentions1 = intents(Int_sell, Int_pick_new).

