# Exercise 1
gcd(a,b)=max{d in N:  d|a and d|b}

# using set
1. gcd(m,m)=max{d in N: d|m and d|m}
    as d|m is equal to d|m
    and min{d|m}=1 when d=m is the maximum of d
    so gcd(m,m)=m

2. gcd(m,0)=max{d in N: d|m and d|0}
    as for all d in R, 0 can devided by d because 0=0*d
    so what we need to find is just max{d| d|m}
    then gcd(m,0)=m

3. gcd(m,n)=max{d in N: d|m and d|n} <=> max{d in N: d|n and d|m}=gcd(n,m)

4. gcd(m+n,n)=max{d in N: d|m+n and d|n}
    we set the maximum of gcd(m+n,n)=dd 
    so (m+n)=a*dd and n=b*dd
    then m=(a-b)dd and n=b*dd
#Still has some questions

#Exercise 2
gcd(m,n)={d in N: d|m and d|n};
lcm(m,n)={l in N: m|l and n|l};
    we set g1=d|m and g2=d|n, then m=g1*d, n=g2*d
    we set l1=m|l and l2=n|l, then l=m*l1=n*l2
    as lcm(m,n)=g1g2d
    lcm(m,n)*gcd(m,n)=g1dg2d=mn 


#Exercise 3
a. pow(A and B)=pow(A) and pow(B)
Proof:
    assume that there is a subset X belongs to A and B but not in {pow(A) and pow(B)}

    then:
        X is not in pow(A) or pow(B)
        X is not in {A or B}
        that is conflict with X in {A and B}
    thus our assumption should be False,
    the proposition is True

b. (pow(A) or pow(B)) belongs to pow(A or B) is True even A belongs to B
Proof:
    We assumed that A is a subset of B
    So A belongs to B belongs to {A or B}
    thus we can get (pow(A) or pow(B)) belongs to pow(A or B)


#Exercise 4:
|A and B|>=1 means that A and B are not disjoint

When R is transitive, for ARB, BRC we can get ARC
That means for all |A and B|>=1 and |B and C|>=1 we can get |A and C|>=1

So if A and B are not disjoint, B and C are not disjoint then A and C should also not disjoint

#Exercise 5:
Relation R: aRb for {a in [b-0.5,b+0.5]}

Reflexive: True
    for all a, a is in [a-0.5,a+0.5]

Anti-reflexitive: False

Symmetric: True
    if {a in [b-0.5,b+0.5]}, b-0.5<=a<=b+0.5
    then  a-0.5<=b<=a+0.5
    thus aRb implies bRa

Asymmetric: False
    if b-0.5<=a<=b+0.5 and a-0.5<=b<=a+0.5 can we get a=b?
    no, we set a=1,b=0.5 then they satisfy {b-0.5<=a<=b+0.5}
    and {a-0.5<=b<=a+0.5}, but a != b

Transitive: 
    if {b-0.5<=a<=b+0.5} and {c-0.5<=b<=c+0.5} can we get {c-0.5<=a<=c+0.5}?
    #this should be true but I am not sure

Linearity(Comparable): False
    for all (a,b) either aRb or bRa
    e.g.(a=100,b=0)

a. Partial order: R+AS+T --> False
b. Total order : R+AS+T+L --> False
c. Equivalence: R+S+T --> True

#Exercise 6
The difference of partial order and total order is that all elements in total order is Comparable

Linearity:
    for all (a,b) can we get aRb or bRa?
    e.g.(a=0,b=0.25)

So this should only a partial order(R+AS+T)

#Exercise 7
xRy: for x,y in N there have prime deviser x1, y1, max{x1,y1}<min{x,y}

reflexive: False
    if x is a prime

anti-reflexive: False

symmetric: True
    for all xRy we can get yRx

anti-symmetric: False
    if xRy and yRx we can get x==y 

transitive: False
    if xRy and yRz then xRz
    (x=4,y=100)-->max{2,2}<min{4,100}
    (y=100,z=35)-->max{5,7}<min{100,35}
    but(x=4,z=35) is not True --> max{2,5}>min{4,35}

#Exercise 8
--
