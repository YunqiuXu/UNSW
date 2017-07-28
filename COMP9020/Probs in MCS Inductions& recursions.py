# Problems in MCS
# Induction and Recursiong


# Problem for Section 2

#2.4 
Prove: sum(k^2)=n(n+1)(2n+1)/6, k from 0 to n
Proff: 
Use WOP;
C::={n in N|0+1^2+...+n^2 != n(n+1)(2n+1)/6};
thus we can get the minimum of C, we set this value as c;
that is to say, 0+1^2+...+c^2 != c(c+1)(2c+1)/6;
so for (c-1): 0+1^2+...+(c-1)^2 != c(c-1)(2c-1)/6;
c(c-1)(2c-1)/6+c= c(c+1)(2c+1)/6, contradiction!
Thus the proposition should be proved correct.


# Problem for Section 3.6
# 3.22 
(a) 
1 is True, for all x, there exists y=2x;
2 is False, when x is odd , y does not exist;
3 is True;
4 is False, when y>x>100, z does not exist;

(b) 
1 is True;
2 is False;
3 is True;
4 is True;
(c) 
all propositions are True

# 3.26 Which of the following are valid
# method: counter model
(a): valid, x=y 
(b): valid #not sure
    model : x in N,y in N, Q(x,y)=
(c): not valid #not sure 
(d): valid

# 3.30 show this proposition is not valid
counter model: P(x,y)=2x+y is even
when z is odd, P(z,z) can not be satisfied

# Problem for Section 5

