# Problems in MCS
# Sets & Functions

# Problem for Section 4.1
# 4.1 
a. pow({1,2})={{1},{2},{1,2},None}
b. pow({None,{None}})={{None},{{None}},{None,{None}},None}
c. 2^8

# 4.3 
# this is similar to what we learn from week 1
(a) (P and not Q) or (P and Q)
    = P and (Q or not Q)
    = P and True
    = P

# 4.5 
a. Prove pow(A and B)=pow(A) and pow(B)
pow(A and B) --> all subsets of (A and B)

    a.1 a subset in pow(A and B) --> it is in (pow(A) and pow(b)):
        if there is a subset X is not in (pow(A) and pow(b)), it should be a subset of A but not a subset of B, or a subset of B but not a subset of A, thus X is not in (A and B) then X is not s subset in pow(A and B)
    a.2 a subset in (pow(A) and pow(b)) --> it is in pow(A and B):
        ...
b. Prove (pow(A) or pow(B)) belongs to pow(A or B)

# 4.8 
Prove: A or B or C=(A-B) or (B-C) or (C-A) or (A and B and C) 
Hint: (P and not Q)or(Q and not R) or (R and not P) or (P and Q and R)=P or Q or R

Solution: as A-B=A and not B , we can get the hind, thus prove

# Problem for Section 4.2

# 4.13 
Prove if (A x B) and (C x D) are disjoint, then A and C are disjoint or B and D is disjoint

Proff: 
(A x B)={(a,b)|a in A and b in B}
(C x D)={(c,d)|c in C and d in D}
if they are disjoint then there for all (a,b) not in (C x D)
--> not (a in C and b in D)
--> not (a in C) or (b in D)
--> (for all a in A , a not in C) or (for all b in B, b not in D)
--> proved!

# Problem for Section 4.3
# Problem for Section 9 
