#COMP9020 PROB04

#E1
1. (A and not A) iff not(A or not A)
	= False iff False
	= True --> valid
2. (A and B) or C iff (A or C) and (B or C)
	= (A or C) and (B or C) iff (A or C) and (B or C)
	= True --> valid


#E2
f=f1 or f2
	= (p implies(q and r)) or (s implies(q and p))
	= not p or (q and r) or not s or (q and p)
	= (q and r) or (q and p) or not p or not s
	= q and (r or p) or not p or not s

# Question : the difference of CNF and DNF

#E3
Propositional logic:
	g is True iff p is in golden casket
	s is True iff p is in golden casket
	G is True iff the inscription on golden casket is True
	S is True iff the inscription on golden casket is True

Now the propositions need to be satisfied are:
	g iff not s #only one of g and s is true
	G iff not g
	S iff (S iff not G) #S said only one of G and S is True
 
if s is True:
	g is False
	G is True
	S iff not S --> can not be satisfied

Result:
	g is True
	s is False
	G is False
	S is True

#E4 find the mistake of proof
This proof uses matimatical induction