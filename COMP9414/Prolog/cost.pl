% cost data
cost(cornflakes, 230).
cost(cocacola, 210).
cost(chocolate, 250).
cost(crisps, 190).

% preorder
total_cost([], 0).                % trivial branch
total_cost([Item|Rest], Cost) :-  % recursive branch
    cost(Item, ItemCost),
    total_cost(Rest, CostOfRest),
    Cost is ItemCost + CostOfRest.

% postorder
total_cost2([], 0).                % trivial branch
total_cost2([Item|Rest], Cost) :-  % recursive branch
    total_cost2(Rest, CostOfRest),
    cost(Item, ItemCost),
    Cost is ItemCost + CostOfRest.
