#COMP9020 QUESTIONS


#################################################
CHPATER 1
#################################################

#####PASS
Problem 1.9
Prove that for any n > 0, if a^n is even, then a is even.
Hint: Contradiction.

Proff: 
We use proff by contradiction;
Suppose the argument is false, then there exists n>0
for an odd number a, a^n is even;
However "a^n is even" --> "a^(n-1)*a is even"-->"a^(n-1) is even";
...
a is even which results in contradiction in the fact 'a is odd';
Therefore the original argument must be true.

#####PASS
Problem 1.11
1. Prove if n^2 is even then n is even
Proff:
We use proff by contradition;
Suppose that the argument is false;
if n^2 is even then n is odd;
but odd*odd is odd-->contradition;
so the original argument shoulld be true

2. Prove if n^2 is a multiple of 3 the n must be a multiple of 3

Proff:
We use proff by contradition;
Assume that existing a number n which is not a multiple of 3
And n^2 is a multiple of 3;
We transfer n^2=3*k where k is integer;
then n=(3k)/n is a multiple of 3;
That is contradicting, so the original argument is true.


#################################################
CHPATER 3
#################################################


#####PASS
Problem 3.2
1. R and not Q;
2. P and Q and R;
3. R implies P;
4. P and not Q and R;

#####
Problem 3.8
1. M IMPLIES Q
	= NOT(M AND NOT Q)
	= NOT M OR Q
Answer: S 

2. M IMPLIES (NOT P OR NOT Q)
	= NOT M OR (NOT P OR NOT Q)
	= NOT M OR NOT P OR NOT Q
Answer: S

3. M IMPLIES [M AND (P IMPLIES M)]
	= M IMPLIES [M AND (NOT P OR M)]
	= NOT M OR [M AND (M OR NOT P)]
	= (NOT M OR M) AND [NOT M OR (M OR NOT P)]
	= True AND [NOT M OR (M OR NOT P)]
	= NOT M OR (M OR NOT P)
	= NOT M OR M OR NOT P
	= True OR NOT P 
	= True
Answer: V

4. (P OR Q) IMPLIES Q
	= NOT(P OR Q) OR Q
	= (NOT P AND NOT Q) OR Q
	= (Q OR NOT Q) AND (Q OR NOT P)
	= True AND (Q OR NOT P)
	= Q OR NOT P
Answer: S

5. (P OR Q) IMPLIES (NOT P AND NOT Q)
	= NOT(P OR Q) OR (NOT P AND NOT Q)
	= (NOT P AND NOT Q) OR (NOT P AND NOT Q)
	= NOT P AND NOT Q
Answer: S

6. (P OR Q) IMPLIES [M AND (P IMPLIES M)]
	= (P OR Q) IMPLIES [M AND (NOT P OR M)]
	= NOT(P OR Q) OR [M AND (NOT P OR M)]
	= (NOT Q AND NOT P) OR (M AND NOT P) OR M
	= NOT P AND (M OR NOT Q) OR M
Answer: S

7. (P XOR Q) IMPLIES Q
	= NOT [(P AND NOT Q) OR (NOT P AND Q)] OR Q
	= [NOT(P AND NOT Q) AND NOT(NOT P AND Q)] OR Q
	= [(NOT P OR Q) AND (P OR NOT Q)] OR Q
	= [Q OR (NOT P OR Q)] AND [Q OR (P OR NOT Q)]
	= (Q OR NOT P) AND True
	= Q OR NOT P
Answer: S

8. (P XOR Q) IMPLIES (NOT P OR NOT Q)
	= [(P AND NOT Q) OR (NOT P AND Q)] IMPLIES (NOT P OR NOT Q)
	= NOT [(P AND NOT Q) OR (NOT P AND Q)] OR (NOT P OR NOT Q)
	= {[(NOT P OR Q) AND (P OR NOT Q)] OR NOT P }OR NOT Q
	= {[NOT P OR (NOT P OR Q)] AND [NOT P OR (P OR NOT Q)]}OR NOT Q
	= [(NOT P OR Q) AND (True OR NOT Q)] OR NOT Q
	= [(NOT P OR Q) AND True]OR NOT Q
	= NOT P OR Q OR NOT Q 
	= NOT P OR True
	= True
Answer: V

9. (P XOR Q) IMPLIES [M AND (P IMPLIES M)]
	= [(P AND NOT Q) OR (NOT P AND Q)] IMPLIES [M AND (NOT P OR M)]
	= NOT [(P AND NOT Q) OR (NOT P AND Q)] OR [M AND (NOT P OR M)]
	= [NOT(P AND NOT Q) AND NOT(NOT P AND Q)] OR [(M AND NOT P) OR M]
	= {[(NOT P OR Q) AND (P OR NOT Q)] OR M} OR (M AND NOT P)
	= {[M OR (NOT P OR Q)] AND [M OR P OR NOT Q]} OR (M AND NOT P)
	= (M AND NOT P) OR [(M OR NOT P OR Q) AND (M OR P OR NOT Q)]
	= [(M AND NOT P) OR M OR NOT P OR Q] AND [(M AND NOT P) OR M OR P OR NOT Q]
	= [(M AND NOT P) OR M OR NOT P OR Q] AND [[(P OR M) AND (P OR NOT P)]OR M OR NOT Q]
	= (P OR M OR NOT Q) AND [(M AND NOT P) OR (M OR NOT P OR Q)]
	= [(P OR M OR NOT Q) AND (M AND NOT P)] OR [(P OR M OR NOT Q) AND (M OR NOT P OR Q)]
Answer: ???
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#####PASS
Problem 3.9

NOT (P IFF Q)
=NOT [(P IMPLIES Q) AND (Q IMPLIES P)]
=NOT(P IMPLIES Q) OR NOT(Q IMPLIES P)
=NOT(NOT P OR Q) OR NOT(NOT Q OR P)
=(P AND NOT Q) OR (Q AND NOT P)
=P XOR Q


#####
# not pass
Problem 3.10

(P AND NOT Q) OR (Q AND NOT R) OR [(R AND NOT P) OR (P AND Q AND R)]
	= (P AND NOT Q) OR (Q AND NOT R) OR {R AND [NOT P OR (P AND Q)]}
	= 



#####
Problem 3.12
(A) (P IMPLIES Q) OR (Q IMPLIES P)
	= (NOT P OR Q) OR (NOT Q OR P)
	= NOT P OR P OR NOT Q OR Q
	= T 

#####
