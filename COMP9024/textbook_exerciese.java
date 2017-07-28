///////////////////////////////////////
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Chapter 3 Fundamental Data Structures(Array List & Linked List)
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
///////////////////////////////////////
R_3_5 PASSED
Answer: from the method addFirst() we can see a special case,
    when there is only one node the head is also tail,
    so when we remove the only one node ,
    we should not just set head=null, tail should also be null

///////////////////////////////////////
R_3_6 PASSED
Algorithm FindSecondToLast(LinkedList LL)
Input: SLL LL
Output: the second to last node
{
    if(LL.size<2){
        return null;
    }
    Node prevNode=head;
    Node currNode=head.getNext();//find the last node
    while(currNode.getNext()!=null){
        prevNode=currNode;
        currNode=currNode.getNext()
    }
    return prevNode;//when break, currNode=last and prevNode is the second to last
}

///////////////////////////////////////
R_3_12/C_3_28 PASSED

//Resursive
Algorithm Rotate(head)
Input: SLL LL.head
Output: LL with all elements reversed
{

    if(head==null||head.getNext()==null){
        return head;
    }

    //reverse the rest, then "head.getNext" becomes the last node" in this reversed LL
    Node newHead=Rotate(head.getNext());
    
    //put head in reversed LL, set it as the last Node
    Node lastNode=head.getNext();
    lastNode.setNext(head);
    head.setNext(null);
    return newHead;
}

//Non-recursive
{
    if(head==null||head.getNext()==null){
        return head;
    }

    Node prevNode=head;
    Node currNode=head.getNext();
    Node nextNode=null;
    while(currNode!=null){//break when currNode is the last one
        //reverse currNode and prevNode
        nextNode=currNode.getNext();
        currNode.setNext(prevNode);
        prevNode=currNode; //at the head 
        currNode=nextNode;
    }
    head.setNext(null);
    head=prevNode;
    return head;
}

//Example:
{1-2-3-4-5-6-7-8-9}
prev=1;
curr=2;
loop1:
    next=3;
    curr.setNext(1);//2-1
    prev=2;
    curr=3;
loop2:
    next=4;
    curr.setNext(2);//3-2-1
    prev=3;
    curr=4;
loop3:
    next=5;
    curr.setNext(3);//4-3-2-1
    prev=4;
    curr=5;
...
loop7:
    next=9;
    curr.setNext(7);//8-7-6-5-4-3-2-1
    prev=8;
    curr=9;
loop9:
    next=null;
    curr.setNext(8);//9-8-7-6-5-4-3-2-1
    prev=9;
    curr=null;
break loop;
1.setNext(null);
head=9;

///////////////////////////////////////
C_3_17 PASSED
//Similar to selection sort
{
    for(int i=0;i<L.length-1;i++){ //0,1,2,...L.length-2
        for(int j=i+1;j<L.length;j++){//1,2,...L.length-1
            if(L[j]==L[i]){
                return L[j];
            }
        }
    }
}



///////////////////////////////////////
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Chapter 4 Algorithm Analysis
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
///////////////////////////////////////
f=O(g) : if for all n>n0 , f(n)<=cg(n), then we have f=O(g)
another defination: lim(f/g)<inf 

///////////////////////////////////////
R_4_2 PASSED
R_4_3 PASSED

R_4_8 PASSED
///////////////////////////////////////
R_4_9 TO R_4_13 PASSED
A. O(n)
B. O(n)
C. O(n^2)
D. O(n)
E. O(n^3)

///////////////////////////////////////
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Chapter 5 Recursion
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
///////////////////////////////////////

C_5_16 PASSED
Algorithm Hanoi(A,B,C,n)
Input: Towers A,B,C, A has n disks;
Output: Move all disks from A to C via B;
{
    if(n==1){
        System.out.print(A+" --> "+C);
    }

    /** move n-1 disks from A to B via C;
    *  then move the largest from A to C;
    *  finally move n-1 disks from B to C via A;
    */
    else{
        Hanoi(A,C,B,n-1);
        System.out.print(A+" --> "+C);
        Hanoi(B,A,C,n-1);
    }
}


///////////////////////////////////////
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Chapter 6 Stacks & Queues
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
///////////////////////////////////////

R_6_1 PASSED
R_6_7 PASSED
///////////////////////////////////////
C_6_19 PASSED
Original version : ((5 + 2) ∗ (8 − 3))/4 
Postfix version : 5 2 + 8 3 - * 4 /
Algorithm EvaPostfix
Input: expression in postfix notation
Output: evaluation
{
    String[] expression;
    Stack myStack=new Stack();

    for(int i=0;i<expression.length;i++){
        if(expression[i] is a digit){
            myStack.push(toInt(sList[i]));
        }
        else if(expression[i] is an operator){
            int A =myStack.pop();
            int B =myStack.pop();
            int result=A operator B;
            myStack.push(result);
        }
    }
    return myStack.pop();
}

Visualization:
push(5)
push(2)
pop(2)
pop(5)
push(5+2)
push(8)
push(3)
pop(3)
pop(8)
push(8-3)
pop(5)
pop(7)
push(5*7)
push(4)
pop(4)
pop(35)
push(35/4)
return pop(35/4)
///////////////////////////////////////
C_6_20 PASSED
given 3 stacks R/S/T,put all the elements in T in front of S with the same order
Input: R={1,2,3}, S={4,5},T={6,7,8,9}
Output: R={1,2,3}, S={6,7,8,9,4,5} 
Solution:
    pop all the elements in S and then push them in R
        R={1,2,3,5,4}
    pop all the elements in T and then push them in R
        R={1,2,3,5,4,9,8,7,6}
    pop elements needed and then push them in S
        R={1,2,3}, S={6,7,8,9,4,5}

///////////////////////////////////////
C_6_21
Get all permutions of {1,2,...n} , non-recursive, using a stack

//Recursive method:
put 1 at head, then get the permution of {2,3,...,n}
put 2 at head, then get the permution of {1,3,...,n}
...
put n at head, then get the permution of {2,3,...,n-1}

//Non-recursive method:
Still Has Some Questions

///////////////////////////////////////
C_6_23 HOMEWORK 
Get all subsets of set T, non-recursive, using a stack S and a queue Q 
Algorithm subsetGenerator(T)
Input: set T with n elements;
Output: all the subsets of T storing in S;
{
    create an empty queue Q;
    create an empty stack S;
    let a1, a2, …, an be all the elements in T;
    S.push({}); // Push the empty subset into the stack
    S.push({a1});
    for (each element ai in {a2,a3,...an})
    { 
        while (S is not empty )
        { 
            x=S.pop();
            Q.enqueue(x);
            x=x ∪ {ai};
            Q.enqueue(x);
        }
        if(ai is not the last element)//再将Q中所有的元素输入S(S长得和Q一样)
        {
            while (Q is not empty )
            { 
                x=Q.dequeue();
                S.push(x);
            }
        }
    }
    return S;
} 

//Simulation:
T = {1,2,3,4,5}
S = {{},{1}}
ai=2
    x={1};
    Q.enqueue({1});
    x={1,2};
    Q.enqueue({1,2});
    x={};
    Q.enqueue({});
    x={2};
    Q.enqueue({2});
    S={{1},{1,2},{},{2}};
ai=3
    x={2};
    Q.enqueue({2});
    x={2,3};
    Q.enqueue({2,3});
    Q.enqueue({});
    Q.enqueue({3})
    Q.enqueue({1,2});
    Q.enqueue({1,2,3});
    Q.enqueue({1});
    Q.enqueue({1,3});
    S={{2},{2,3},{},{3},{1,2},{1,2,3},{1},{1,3}};
a1=4
    Q={{1,3},{1,3,4},{1},{1,4},{1,2,3},{1,2,3,4},{1,2},{1,2,4},{3},{3,4},{},{4},{2,3},{2,3,4},{2},{2,4}};
    S={{1,3},{1,3,4},{1},{1,4},{1,2,3},{1,2,3,4},{1,2},{1,2,4},{3},{3,4},{},{4},{2,3},{2,3,4},{2},{2,4}};
//Simulation2:
S1={A,B};
S2={B,B1,A,A1};
S3=(A1,A12,A,A2,B1,B12,B,B2);
S4={B2,B23,B,B3,B12,B123,B1,B13,A2,A23,A,A3,A12,A123,A1,A13}
...

///////////////////////////////////////
C_6_24 HOMEWORK PASSED
Algorithm Scanner(S,x)
Input: Stack S storing n elements, element x;
Output: check if S contains x;
{
    Queue Q=new Queue();
    Boolean match=False;
    //scanning
    while(!S.isEmpty()){
        y=S.pop();
        if(y==x){
            match=True;
        }
        Q.enqueue(y);
    }
    //return the order
    Q->S->Q->S;
    return match;
}

//Simulation:
S={5,4,3,2,1}, x=4;
y=1;
Q={1};
y=2;
Q={1,2};
y=3;
Q={1,2,3};
y=4, match;
Q={1,2,3,4};
...
Q={1,2,3,4,5};
S={};
Q->S 
S={1,2,3,4,5};
S->Q
Q={5,4,3,2,1};
Q->S;
S={5,4,3,2,1};

///////////////////////////////////////
C_6_25 PASSED
Implement Stack S using Queue Q;
//hint: rotate elements within the queue
Q={1,2,3,4,5}
if we perform push as S, then Q={1,2,3,4,5,6}
if we perform pop as S, then Q={1,2,3,4,5}
if we perform top as S, then return 5

Algorithm push(element)
{
    Q.enqueue(element);
}
Algorithm pop(){
    Queue qq=new Queue();
    while(Q.size()!=1){
        qq.enqueue(Q.dequeue());
    }
    last=Q.dequeue();
    Q=qq;
    return last;
}
Algorithm top(){
    Queue qq=new Queue();
    while(Q.size()!=1){
        qq.enqueue(Q.dequeue());
    }
    last=Q.dequeue();
    qq.enqueue(last);
    Q=qq;
    return last;
}

///////////////////////////////////////
C_6_27 PASSED
Algorithm StackClone(Stack S)
Input: Stack S;//S={1,2,3,4,5}
Output: Stack cloned from S;
{
    Stack S1=new Stack();
    Stack S2=new Stack();
    while(!S.isEmpty()){
        S1.push(S.pop());
    }//S1={5,4,3,2,1}
    while(!S1.isEmpty()){
        S2.push(S1.pop());
    }//S2={1,2,3,4,5}
    return S2;
}
C_6_28 PASSED
///////////////////////////////////////
C_6_31 PASSED
Implement Queue using Stack
Stack A ={1,2,3,4,5}
Stack B ={}
enqueue(6)-->{1,2,3,4,5,6}
dequeue-->1


Algorithm enqueue(element){
    A.push(element);
}
Algorithm dequeue(){
    while(A.size()!=1){
        B.push(A.pop());
    }//B={6,5,4,3,2}
    last=A.pop();
    while(!B.isEmpty()){
        A.push(B.pop());
    }
    return last;
}

///////////////////////////////////////
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Chapter 7 List and Iterator
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
///////////////////////////////////////

///////////////////////////////////////
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Chapter 8 Trees
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
///////////////////////////////////////

1. the difference between proper binary tree and full binary tree
2. the relationship between different terminations
3. preOrder/postOrder/inOrder/BFS

///////////////////////////////////////
R_8_2 PASSED
e.g. all the nodes has only one child
O(n)

///////////////////////////////////////
R_8_5 PASSED
Count the number of leaves that are all left-children
Algorithm CountLeftChild
Input: Binary Tree T
Output: All the nodes in T that are 'left child'
{
	if(the node is external){return null};
	else if(the node has left child){ count++;}
	recursively perform this process via inorder traversal;
}

Java Implementation:
public class BinaryTree{
	class Node{
		int data;
		Node left,right;
		public Node(int item){
			data=item;
			left=null;
			right=null;
		}
	}

	Node root;

	int CountLeftChild(){ return CountLeftChild(root); }

	int CountLeftChild(Node node){
		if(node==null){
			return 0;
		}
		else if(node.left!=null){
			return 1+getLeafCount(node.left)+getLeafCount(node.right);
		}
		else{
			return getLeafCount(node.right);
		}
	}
}
///////////////////////////////////////
R_8_7 PASSED
Improper binary tree with n nodes:
Ne: 1<=Ne<=n/2+1
Ni:n/2-1<=Ni<=n-1

///////////////////////////////////////
R_8_8 PASSED
a&b. proper binary tree, height h
    h+1<=ne<=2^h
    h<=ni<=2^h-1
c. proper binary tree, h/n:
As 2h+1<=n<=2^(h+1)-1
We can get log(n+1)−1≤ h ≤ (n − 1)/2.

///////////////////////////////////////
R_8_12 PASSED

///////////////////////////////////////
R_8_14 PASSED
p is root: f(p)=0
p is left child of q: f(p)=2f(q)+1
p is right child of q: f(p)=2f(q)+2

Solution:
a. mathmatical induction
b. all the left children are external nodes
///////////////////////////////////////
R_8_16 Array based tree
//Root is index 0
Algorithm root(){
	return Array[0];
}

Algorithm parent(p){
	if(p==0){
		return null;
	}
	else if(p%2==0){//right child
		return Array[(p-2)/2];
	}
	else{//left child 
		return Array[(p-1)/2];
	}
}

Algorithm left(p){
	if(2*p+1>=Array.length){
		return null;
	}
	return Array[2*p+1];
}

Algorithm right(p){
	if(2*p+2>=Array.length){
		return null;
	}
	return Array[2*p+2];
}

Algorithm isExternal(p){
	if(right(p)==null && left(p)==null){
		return True;
	}
	return False;
}

///////////////////////////////////////
R_8_18 PASSED
Algorithm PreorderTraversal(p){
	visit(p);
	for each child c of p{
		PreorderTraversal(c);
	}
}

Solution: - / * + 3 1 3 + - 9 5 2 ...
///////////////////////////////////////
R_8_19 PASSED
Algorithm PostorderTraversal(p){
	for each child c of p{
		PostorderTraversal(c);
	}
	visit(p);
}

Solution: 3 1 + 3 * 9 5 - 2 + / ...

///////////////////////////////////////
R_8_20&R_8_21 PASSED

Tree with more than one node
a. postOrder==preOrder?
Solution: impossible

b. preOrder == reverse(postOrder)?
Solution: when all the internal nodes have only one child

c. when the tree is proper?
Solution: both a and b are impossible
///////////////////////////////////////
R_8_22 PASSED
Locate root E: the first element in preOrder;
Find the location of root in inOrder, partition the inOrder as leftSubtree{MAFXU} and rightSubtree{N}
Recursion on the preOrder {XAMFUN} until the subroot is external
///////////////////////////////////////
R_8_23 PASSED
Algorithm BreadthFirstTraversal(root)
Input: root;
Output: BFT of this tree;
{
    Queue Q=new Queue();
    LinkedList result=new LinkedList();
    Q.enqueue(root);
    while(!Q.isEmpty){
        Node curr=Q.dequeue();
        result.addLast(curr);
        if(curr.left!=null){
            Q.enqueue(curr.left);
        }
        if(curr.right!=null){
            Q.enqueue(curr.right);
        }
    }
    return result;
}

///////////////////////////////////////
R_8_24 - R_8_27 PASSED
Give the output of the method parenthesize(T, T.root( )), as described in Code
Fragment 8.26, when T is the tree of Figure 8.6.

((((3 + 1) ∗ 3)/((9 − 5) + 2)) − ((3 ∗ (7 − 4)) + 6))
Time complexity: 

///////////////////////////////////////
C_8_28 PASSED But Still Need Revision
Sum the sum of depths of all nodes in T in O(n)

Path length of tree {A,B,C,D,E,F,G}
= PL(A)
= PL(B)+PL(C)+ (7-1) //size(B)+size(C): all others have atleast depth 1

PL(B)=PL(D)+PL(E)+(3-1) //D/E's depth is at least 1
PL(C)=PL(F)+PL(G)+(3-1)
-->PL(A)=6+2+2=10

Algorithm PathLength(Node currentRoot,int currentSize)
{
	if(currentSize==1){ return 0; }//external or only one node
	int sum=0;
	for each child c of currentRoot{
		childSize=c.size();
		sum += PathLength(c,childSize);
	}
	return sum+currentSize-1;
}

//Theory, for each node X
PathLength(X)=sum(PathLength(X.child))+(X.size()-1)

///////////////////////////////////////
C_8_29 PASSED
Solution: mathmatical induction
[B]: n=3,ne=2,ni=1 -> E(T)=I(T)+n-1;
[I]: Assume that E(T)=I(T)+n-1 is true for small trees
	E(left)=I(left)+left-1, left is the size
	E(right)=I(right)+right-1, right is the size
	left+right+1=n
Then for the large tree 
E(L)-I(L) = [E(left)+(left+1)/2+E(right)+(right+1)/2]
		-[I(left)+(left-1)/2+I(right)+(right-1)/2]
		  = [E(left)-I(left)]+[E(right)-I(right)]+2
		  = left+right
		  = totalSize-1
//相当于用一个root将两个子树联结起来

///////////////////////////////////////
C_8_30 Still Has Some Questions!!!
For general binary tree, minNe=1, maxNe=n/2+1
When T has the minimum number of external nodes:
    all the internal nodes only have one child;
    and there is only one external node;
    then D(T)=depth(external node);
When T has the maximum number of external nodes:
    all the internal nodes have 2 children;
    ...


///////////////////////////////////////
C_8_32 PASSED
Proff: mathmatical induction
[B]: 1 root with 3 external nodes--> ne=2ni+1
[HI]: assume that the child Tleft with Nl nodes
and child Tright with Nr nodes satisfy the proposition

i.e. Nl=Nle+Nli=3*Nli+1, Nr=3*Nri+1
Then connect these small trees with a root 
to form a large tree T

NTi=Nli+Nri+1
NTe=Nle+Nre=2*Nli+1+2*Nri+1=2*NTi+1

The proposition is true 
///////////////////////////////////////
C_8_33 PASSED
Check if 2 trees are isomorphic
Algorithm areIsomorphic(Tree T1, Tree T2)
Input: T1,T2;
Output: If T1&T2 are isomorphic, return True;
{
    if(T1.size()<=1 && T2.size()<=1){
        if(T1.size()==T2.size()){
            return True;
        }
        else{
            return False;
        }
    }

    Queue Q1=new Queue();
    Queue Q2=new Queue();
    put all subtree of T1.root into Q1;
    put all subtree of T2.root into Q2;
    if(Q1.size()!=Q2.size()){
        return False;
    }
    while(!Q1.isEmpty()){
        Boolean check=areIsomorphic(Q1.dequeue(), Q2.dequeue());
        if(check==False){
            return False;
        }
    }
    return True;
}

Running Time: O(n), all the node are compared once 
///////////////////////////////////////
C_8_36 PASSED
//Theory:
1. set p in original tree as null;
2. create a new tree pTree root at p;
3. unpate the size of tree as T.size()-pTree.size();

Algorithm pruneSubtree(p)
Input: position p;
Output: the entire subtree rooted at p;
{
    Node newRoot=get node at position p;
    if (newRoot.getParent()==null){
        //position p is root
        newRoot.setElement(null);
        size=0;
        return;
    }
    //原来的位置设为null
    if (newRoot==newRoot.getParent().getLeft()){
        newRoot.getParent().setLeft(null);
    }
    else{
        newRoot.getParent().setRight(null);
    }
    //得到删除结点的数量并对原结点进行更新
    LinkedBinaryTree newTree=new LinkedBinaryTree();
    newTree.root=newRoot;
    size=size-newTree.size();
}

///////////////////////////////////////
C_8_37 PASSED

Algorithm swap(p,q)
Input: 2 positions p,q;
Output: swap the subtrees at p and q;
{
    Node<E> nodeP=validate(p);
    Node<E> nodeQ=validate(q);
    //special case 1: adjacent(q is the parent of p)
    if(nodeQ==nodeP.getParent()){
        Node<E> parentQ=nodeQ.getParent();
        
        if(nodeQ==parentQ.getLeft()){
            parentQ.setLeft(nodeP);
        }
        else{
            parentQ.setRight(nodeP);
        }
            
        Node<E> pL=nodeP.getLeft();
        Node<E> pR=nodeP.getRight();
        if(nodeP==nodeQ.getRight()){
            //p is q's right child
            nodeP.setLeft(nodeQ.getLeft());
            nodeP.setRight(nodeQ);
        }
        else{
            //p is q's left child
            nodeP.setRight(nodeQ.getRight());
            nodeP.setLeft(nodeQ);
        }
        nodeQ.setLeft(pL);
        nodeQ.setRight(pR);
        nodeQ.setParent(nodeP);
    }
    
    //special case 2: adjacent(p is the parent of q)
    else if(nodeP==nodeQ.getParent()){
        //similar to above!
    }
        
    else{
        //general case: change the parent
        Node<E> parentQ=nodeQ.getParent();
        Node<E> parentP=nodeP.getParent();
        if(nodeQ==parentQ.getLeft()){
            parentQ.setLeft(nodeP);
        }
        else{
            parentQ.setRight(nodeP);
        }
            
        if(nodeP==parentP.getRight()){
            parentP.setLeft(nodeQ);
        }
        else{
            parentP.setRight(nodeQ);
        }
            
        Node<E> pL=nodeP.getLeft();
        Node<E> pR=nodeP.getRight();
        Node<E> qL=nodeQ.getLeft();
        Node<E> qR=nodeQ.getRight();
        nodeP.setLeft(qL);
        nodeP.setRight(qR);
        nodeQ.setLeft(pL);
        nodeQ.setRight(pR);
    }
}

///////////////////////////////////////
C_8_42 PASSED
Algorithm print()
Input: Tree T;
Output: Nodes and their height at every position;
{
    LinkedList resultList=new LinkedList();
    return PreorderTraversalModified(resultList,T.root,0);
}

Algorithm PreorderTraversalModified(resultList,root,height)
Input: Node root and current height;
Output: PreorderTraversalModified of root;
{
    Entry entry=new Entry(root,height);
    resultList.addLast(entry);
    for each child of root:
        PreorderTraversalModified(resultList,child,height+1);
    return resultList
}
C_8_43 PASSED, SIMILAR TO C_8_42
///////////////////////////////////////
C_8_45 PASSED
//given position p, return the position after p in different traversals
public Position<E> preorderNext(Position<E> p){
    /*
     * case 1 : v is internal-->v.getLeft();
     * case 2 : v is external and root --> null;
     * case 3 : v is external且是父结点的右子结点 --> 不断上溯直到得到case 4/5
     * case 4 : v is external, 且是root的右子结点--> null
     * case 5 : v is external and v is z's left child --> z's right child
     */
    Node<E> v= validate(p);
    if(isInternal(v)){//case 1
        return v.getLeft();
    }
    else{
        if(isRoot(v)){ //case 2
            return null;                
        }
        else{
            Node<E> z = v.getParent();
            Node<E> current=v;
            while(current==z.getRight()){
                if(isRoot(z)){//case 4
                    return null;
                }
                else{//case 3
                    current=z;
                    z=current.getParent();
                }
            }
            return z.getRight();//case 5
        }
    }
}    
public Position<E> inorderNext(Position<E> p){
    /*
     * case 1 : v has right child --> 返回v右子树最左下子节点(大于v的最小结点)
     * case 2 : v 不存在右子节点且v是root --> null
     * case 3 : v 不存在右子节点但是v存在父结点z -->  不断向上回溯返回某个祖先结点z,其中v在z的左子树内
     * case 4 : 找不到符合case 3条件的z(go to case 2)-->null
     */
    Node<E> v =validate(p);
    if(v.getRight()!=null){//case 1
        Node<E> current=v.getRight();
        while(isInternal(current)){
            current=current.getLeft();
        }
        return current;
    }
    else{
        if(isRoot(v)){
            return null;
        }
        else{
            Node<E> current2=v;
            Node<E> z=current2.getParent();
            while(current2==z.getRight()){
                if(isRoot(z)){//case 2
                    return null;
                }
                else{
                    current2=z;
                    z=z.getParent();
                }
            }
            return z;//case 3
        }
    }
}
public Position<E> postorderNext(Position<E> p){
    Node<E> v=validate(p);
    /*
     * case 1 : v is root --> null
     * case 2 : v is not root,父结点为z且v是z的左子节点 --> z右子结点的左子树的最左侧
     * case 3 : v is not root,父结点为z且v是z的右子节点 --> 返回z
     */
        
    if(isRoot(v)){//case 1
        return null;
    }
    else{
        Node<E> z=v.getParent();
        if(v==z.getLeft()){//case 2
            if(z.getRight()==null){
                return z;
            }
            else{
                Node<E> current=z.getRight();
                while(isInternal(current)){
                    current=current.getLeft();
                }
                return current;
            }
        }
        else{
            return z;
        }
    }
}
///////////////////////////////////////
C_8_46 PASSED
Nonrecursive inorder traversal, linear time
Based on C_8_45
Assume v is a node in T, then we need to get next node until null
case 1 : v 存在右子节点 --> 返回v右子树最左下子节点(大于v的最小结点)
case 2 : v 不存在右子节点且v是root --> null
case 2 : v 不存在右子节点但是v存在父结点z --> 不断向上回溯返回某个祖先结点z,其中v在z的左子树内
case 3 : 找不到符合case 2条件的z --> null

///////////////////////////////////////
C_8_50 PASSED
Similar to C_8_42
preorderDraw()
for each position p in T:
	x(p): the number of nodes preceding p
	y(p): the depth of p
A. show that there is no crossing edges in T drawed by this method;
B. redraw the tree of F8.19

Algorithm PreorderTraversalModified(resultList,root,depth)
Input: Node root and current height;
Output: PreorderTraversalModified of root;
{
    Entry entry=new Entry(root,depth);
    resultList.addLast(entry);
    for each child of root:
        PreorderTraversalModified(resultList,child,depth+1);
    return resultList;
}

Algorithm preorderDraw(Tree T)
{
    Node curr=T.root;
    LinkedList resultList=new LinkedList();
    resultList=PreorderTraversalModified(resultList,curr,0);
    int i=0;
    while(!resultList.isEmpty()){
        int x=i;
        int y=resultList.removeFirst().depth;
        i++;
    }
}
C_8_51 PASSED, SIMILAR TO C_8_50
///////////////////////////////////////
C_8_52 PASSED
Theory:
	1. q is the first child of p-->p.setLeft(q)
	2. q is the first sibling of p-->p.setRight(q)

Q1. preorder traversal of Tr = T;
Q2. postorder traversal of Tr != T;
Q3. inorder traversal of Tr == postorder travesal of T

///////////////////////////////////////
C_8_55 PASSED
/*
 * LCA: the lowest common ancester of 2 positions p,q
 * 思路:
 * 首先求取p,q的深度->将深度较小的一个提升到和另一个深度相同的层次
 * 若提升到深度相同时两个结点相同-->返回该结点的父结点
 * 深度相同时两个结点不同-->不断求父结点直到两个结点相同
 * 复杂度为线性
 */
public class C_8_55<E> extends LinkedBinaryTree<E>{ 

    public Node<E> findLCA(Position<E> p,Position<E> q){
        Node<E> pp=validate(p);
        Node<E> qq=validate(q);
        if(isRoot(pp) || isRoot(qq)){
            return null;
        }
        while(depth(pp)!=depth(qq)){
            if(depth(pp)>depth(qq)){
                qq=qq.getParent();
            }
            else{
                pp=pp.getParent();
            }
        }
        if(pp==qq){
            return pp.getParent();
        }
        else{
            while(pp!=qq){
                pp=pp.getParent();
                qq=qq.getParent();
            }
            return pp;
        }
    }
    
    //递归算法: 不使用depth,from leetcode
    public Node<E> findLCA2(Node<E> root, Node<E> p, Node<E> q){
        if(root==null){
            return null;
        }
        if(root==p || root==q){
            return root;
        }
        Node<E> l = findLCA2(root.getLeft(), p, q);
        Node<E> r = findLCA2(root.getRight(), p, q);
     
        if(l!=null && r!=null){ //两个共同的祖先
            return root;
        }
        else if(l==null && r==null){
            return null;
        }
        else{
            return l==null?r:l; //其中一个是另一个的祖先
        }
    }
    
}

///////////////////////////////////////
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Chapter 11 Search Trees
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
///////////////////////////////////////

R_11_1 PASSED
R_11_2 PASSED
R_11_3 PASSED
R_11_19 PASSED
///////////////////////////////////////
R_11_4 PASSED
	[1,2,3],[3,2,1] will be different
R_11_5 PASSED
	[1,2,3,4],[4,3,2,1] will be different

///////////////////////////////////////
R_11_6 PASSED 
Perfrom TreeSearch Without Recursion 
Algorithm TreeSearch
Input: Tree T, key k
Output: if k can be found in T, return its position;
	otherwise return the position of final leaf 
{
	currentPosition=T.root;
	while(currentPosition!=null){
		if (k==currentPosition){ //match
			break;
		}
		else if (k>currentPosition){
			currentPosition=right(currentPosition);
		}
		else{
			currentPosition=right(currentPosition);
		}
	}
	return currentPosition;
}
///////////////////////////////////////
R_11_7 PASSED
F11.11: double rotation
F11.13: single rotation

R_11_8 PASSED 
Insert 52
R_11_9 PASSED
Remove 62
///////////////////////////////////////
R_11_11 PASSED
double rotation: origin --> insertion --> reconstruction
	z: h+2 --> h+3 --> h+1
	y: h+1 --> h+2 --> h+1
	x: h --> h+1 --> h+1
R_11_12 PASSED

///////////////////////////////////////
R_11_14 PASSED
Decreasing 5-4-3-2-1...
R_11_15 PASSED
Insert: splay start from this key;
Find: if we can find key k, then we start from k;else, we start from the parent of the end leaf;
Delete: if we can find key k, replace k with predecessor w, start from the parent of w; else we can not find k, same to contidition 2 of Find
///////////////////////////////////////
R_11_17 PASSED
it is not a (2,4) tree, because the depth of external nodes are not same
///////////////////////////////////////
R_11_21 PASSED
a. greatest: all the nodes are 2-nodes
b. fewest: all the nodes are 4-nodes
///////////////////////////////////////
R_11_22_A PASSED
///////////////////////////////////////
R_11_23 PASSED
A. false: the root can not be red 
B. true: if its sibling is black, the black depth can be different
C. true:
D. false: 3-node can be different 

/////////////////////////////////////// 
R_11_24 HOMEWORK 
A. 100000-1, unbalanced
B. 23 Still Has Some QUestions Here
    n(H)=1+n(H-1)+n(H-2)

C. 100000-1, ascending order insertion
D. log(100000+1), no 3-node or 4-node, a proper binary tree 
    Note the entries are all internal nodes;
E. log(100000+1), similar to (2-4) tree

///////////////////////////////////////
R_11_25 PASSED
with left subtree containing 2 red and no red in right subtree,
the height of left will be 2 larger than right

///////////////////////////////////////
C_11_28 PASSED
in BST , left<parent<right
///////////////////////////////////////
C_11_29 PASSED
removeMin() takes O(logn) time for performing TreeSearch in balanced tree
and perform n removeMin()
thus the total time complexity should be O(nlogn)

C_11_30 PASSED 
find the minimum-> the minimum becomes the root;
remove the minimum-> its predecessor should be the root;
...
///////////////////////////////////////
C_11_32 PASSED
get all the entries into a sorted list: O(n)
shuffle the list into any order: O(n)
construct a new binary tree: O(n)
so the total time complexity should be O(n)

///////////////////////////////////////
C_11_37 Still Has SOme Questions
Algorithm countRange(k1,k2)
Input: 
Output:
{
    find k1 and count how many nodes n1 are passed: O(h) 
    find k2 and count how many nodes n2 are passed: O(h)
    return 
}

///////////////////////////////////////
C_11_47 PASSED
1. Get height of two trees: O(log N + log M)
2. hT<hU : add T to the leftmost node at level hU - hT - 1 in U
        E.G. hT=2,hU=4, then put T at level 1 in U
   hT=hU : join them at the top by creating a new root node.)
   hT>hU : add U to the leftmost node at level hT - hU - 1 in T
3. After joining, split the 4-nodes
Complexity:
Get heights: O(log N + log M)
Joining: O(1).
Split every node toward the root: O(log N + log M).
Total: 	O(log N + log M)


///////////////////////////////////////
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Chapter 9 Priority Queue
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
///////////////////////////////////////

R_9_1 PASSED
each operation is O(log n)
so the total operations can be O((log n)^2)
///////////////////////////////////////
R_9_2 PASSED
always, as the parent node will always have a smaller value than its children
///////////////////////////////////////
R_9_3 PASSED
(1,D);(3,J);(4,B);(5,A);(6,L),....
///////////////////////////////////////
R_9_4 PASSED
insert();
removeMin();

///////////////////////////////////////
R_9_7 PASSED
(22, 15, 36, 44, 10, 3, 9, 13, 29, 25) SWAP(22,3)
(3, 15, 36, 44, 10, 22, 9, 13, 29, 25) SWAP(15,9)
(3, 9, 36, 44, 10, 22, 15, 13, 29, 25)
....
So selection sort is unstable

///////////////////////////////////////
R_9_8 PASSED
([22], 15, 36, 44, 10, 3, 9, 13, 29, 25)
([22, 15], 36, 44, 10, 3, 9, 13, 29, 25) -> (15, 22, 36, 44, 10, 3, 9, 13, 29, 25)
([15, 22, 36], 44, 10, 3, 9, 13, 29, 25) -> (15, 22, 36, 44, 10, 3, 9, 13, 29, 25)
...
So insertion sort is stable
///////////////////////////////////////
R_9_9 PASSED

worst insertion case of insertion:
the list is in descending order e.g.(5,4,3,2,1)
///////////////////////////////////////
R_9_10 PASSED
Root
R_9_11 PASSED
External Node
///////////////////////////////////////
R_9_12 PASSED
min-oriented PQ -> max-oriented PQ
just change the comparator
///////////////////////////////////////
R_9_13 PASSED 
inplace heap sort
///////////////////////////////////////
R_9_15 PASSED
if a position do not have left child it will not have right child either

///////////////////////////////////////
R_9_16 PASSED
example:
	    1
	 2     3
    4 6   7 9

preorder: 1 2 4 6 3 7 9
inorder: 4 2 6 1 7 3 9
postorder:4 6 2 7 9 3 1

no order , fuck!

R_9_17 PASSED
R_9_19 PASSED 
he is wrong
R_9_20 PASSED
she is wrong
	    100
	 50     6
    1  2   3 4
///////////////////////////////////////
R_9_23 PASSED
R_9_24 PASSED
the one being inserted is the smallest one
and each insertion will cause a O(log n) upheap
///////////////////////////////////////
C_9_25 PASSED
Use max-oriented PQ 
给每个元素赋予优先级, 形成键值对, 在栈中一个元素插入越晚优先级越高
initialize the maxKey variable as 0
push() : insert(e, --maxKey) //maxKey越小 优先级越高
pop() : remove(e,maxKey--)

C_9_26 PASSED
所以可以用增量设置，因为在最小优先队列里元素值越大，优先级越低，
这样子就可以实现队列一边插入，一边进入优先队列被设置成低的优先级；
当出队的时候，extract_min()就可以把最先进入队列的元素出队了！
///////////////////////////////////////
C_9_31 PASSED
up and down search
3 cases:
case 1: w is the left child,
	then z should be right child.
case 2: right up until it reach someone left node,
	jump to sibling and then left down -> left down -> left down..

case 3: w is the right child go up right->up right->right->root
	that means w is the last node of current level,
	so z should be the first node of next level,
	so go left down from root until it reach the newlevel

the time complexity can be 2*logn-->O(logn)
///////////////////////////////////////
C_9_33 Still Has Some Questions

///////////////////////////////////////
C_9_34 PASSED
Find all entries <= k

I think we should traversal all the nodes except given key''s children

and time complexity should be O(k)--> there are only k entries that <= k

Solution: start from root, recursively perform this algorithm in every "root's" left child and right child


Algorithm lessThanKEntries(H, v)
Input: A heap H and a node v(start from root)
Output: A node list L that contains all the entries with keys less than k
{
 	if(v.key<k){
 		L.add((v.value, v.key));
		if (v.leftchild !=null) L.add(LessThanKEntries(H, v.leftchild));
		if (v.rightchild !=null) L.add(LessThanKEntries(H, v.rightchild));
	}
    return L;
}

///////////////////////////////////////
C_9_37 Still Have Some Questions

This is in UNSW homework
combine two trees(in heap order but not proper) into a heap

Algorithm Combine(Tree1, Tree2)
Input: 2 trees 
Output: a heap including all nodes of 2 trees 
{
	v=removeMin(Tree1); //this should be the root of Tree1 because tree1 is in heap order
	let v be the root of heap;
	v.setLeft(Tree1.root);
	v.setRight(Tree2.root);
	perform downheap of 
}

BUT for these 2 unproper binary tree, how to locate the last position???

///////////////////////////////////////
C_9_39 PASSED
Find k largest elements in O(n + k logn) using a maximum-oriented heap.

Step 1: construct the heap: O(n), see BU heap construction
Step 2: perform removeMax(): O(log n)
So the total time complexity can be O(n+klogn)
///////////////////////////////////////
C_9_40 PASSED
Step 1: construct a heap H whose size is k
Step 2: insert the n elements into H, perform upheap
Step 3: is H is full, perform removeMin() and downheap
Finally the elements in heap are the k largest ones in set  

///////////////////////////////////////
C_9_43 Still Have Some Questions!!
implement MaxPQ using MinPQ

Hint: Create a key type internally that wraps the provided keys to
invert comparisons.
///////////////////////////////////////
C_9_44 PASSED
In-Place Selection Sort
additional instance variable: minElement
find the minElement in the unordered part of list 
and then perform swapping
///////////////////////////////////////
C_9_45 PASSED
Inplace SelectionSort
///////////////////////////////////////
C_9_47 Still Have Some Questions!!
Unmonopoly: each turn the max one give half to the least one 
for each turn you need to find the largest and smallest one 

there are answers online, but I have not got access to it!!

///////////////////////////////////////
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Chapter 12 Sort
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
///////////////////////////////////////

R_12_2 PASSED
downward: devide
upward: conquer

///////////////////////////////////////
R_12_4 PASSED
MergeSort is stable, the relevent position of equal elements will not change

R_12_5 PASSED
R_12_6 PASSED
make the merge sort unstable
for the equal case: exchange their positions
///////////////////////////////////////
R_12_7 PASSED
Algorithm UnionAB
INPUT: sorted sequence A,sorted sequence B (some elements in A&B can be equal)
OUTPUT: sorted sequence A&B with no duplicates, time complexity should be O(n)
{
	create an empty sequence C;
	while(!A.isEmpty() && !B.isEmpty()){
		currentA=A.first();
		currentB=B.first();
		if(currentA>currentB){
			C.addLast(A.remove(A.first()));
		}
		else if(currentA==currentB){
			C.addLast(A.remove(A.first()));
			B.remove(B.first);
		}
		else{
			C.addLast(B.remove(B.first));
		}
	}
	while(!A.isEmpty()){
		C.addLast(A.remove(A.first()));
	}
	while(!B.isEmpty()){
		C.addLast(B.remove(B.first()));
	}
	return C;
}  

TestCode: A=[1,3,6,7,9,11],B=[2,6,7]
C=[1,2,3,6,7,9,11]

///////////////////////////////////////
R_12_9 PASSED
the sequence S is already sorted, the pivot is S[n/2]
the time complexity should be O(nlogn) 
S[0:n/2-1]<S[n/2]<S[n/2+1:]
>>>
T(n)=2T(n/2)+n-1
>>> T(n)=nlogn-n+1


R_12_10 PASSED
In which condition will this be n^2 time
S=[8, 6, 4, 2, 1, 3, 5, 7]

The condition should be: middle one is the smallest one or largest one
//This is similar to regular one: worst condition is the list can not be partitioned

///////////////////////////////////////
R_12_11 PASSED
General quick sort: Omega(n^2)
	partition can not be performed
	comparation time can be: (n-1)+(n-2)+...+1
Three-direction quick sort: O(n)
	all elements equal to pivot are put into middle subarray

///////////////////////////////////////
R_12_13 PASSED
Flaw: boundary condition will be omitted
R_12_14 SIMILAR
Flaw: the pointer will go out of boundary
///////////////////////////////////////
R_12_17 Not Sure 
In my view the largest k should only be 1
because when we find the kth element it costs O(n)
///////////////////////////////////////
R_12_18 PASSED
No, we need additional data structures to store the buckets

///////////////////////////////////////
R_12_19 PASSED
Algorithm TripletSort(S)
Input: S with n triplets(k,l,m)
Output: sorted S 
{
	for(i=3;i>=1;i--){
		BucketSort(S,3); 
		//sort the elements by m
		//sort the elements by l
		//sort the elements by k
	}
}

if the length of tuples is d(k1,k2,...,kd),
the algorithm should be:
for(i=d;i>=1;i--){
	...
}

///////////////////////////////////////
R_12_20 PASSED
MergeSort: O(nlogn) in any condition
General QuickSort: 
Three-Way QuickSort: O(n)

R_12_21 PASSED
BucketSort: O(n)
///////////////////////////////////////
R_12_22 PASSED
if we find 1,put 1 to the tail, else put 0 to the head

///////////////////////////////////////
R_12_23 PASSED
for a ascending sorted list, the InsertionSort is O(n)
but if we reverse it, the InsertionSort is O(n^2)

while for HeapSort and MergeSort, the time complexity should always be O(nlogn)
///////////////////////////////////////
C_12_26 PASSED
Maybe bucket sort should be a good method
///////////////////////////////////////
C_12_28 PASSED
A. test in O(n) whether T is sorted
Algorithm isSorted(T)
Input: sequence T
Output: true if T is sorted
{
	for(int i=0;i<T.length-1;i++){
		if (T[i]>T[i+1]){
			return false;
		}
	}
	return true;
} 

B. 
C.
///////////////////////////////////////
C_12_30 Need To Be Implemented Later
//好好看下BU-merge
C_12_34 Three-Way QuickSort
///////////////////////////////////////
C_12_35 PASSED
Sort the sequence: O(nlogn)
fond the largest votes: O(n)
>>> O(logn)
///////////////////////////////////////
C_12_36 PASSED
Use bucket sort: //we do not know the id of 1-k
put all elements into k buckets and get count: O(n)
sort the buckets: O(nlogk)
///////////////////////////////////////
C_12_37 PASSED
//we know the id of 1-k
put all elements into k buckets and get count: O(n)
select the max one: O(n)
///////////////////////////////////////
C_12_39 OUR HOMEWORK!! PASSED
Algorithm Intersection(A, B)
Input: two arrays A and B of n elements each
Output: 1 if A and B contain the same set of elements; 0 if A and B do not
{
 	Sort A in nondescending order;
 	Sort B in nondescending order;
 	i=0;
 	j=0;
 	while (i<n and j<n){
 		exit=true;
		while (exit=true and i<n-1) // Skip duplicates in A
 		{
 			if ( A[i]=A[i+1])
 				i=i+1;
 			else
 				exit=false;
 		}
 		exit=true;
 		while (exit=true and j<n-1 ) // Skip duplicates in B
 		{
 			if ( B[j]=B[j+1])
 				j=j+1;
 			else
 				exit=false;
 		}
 		if ( A[i]!=B[j])
 			return 0; // A and B do not contain the same set of elements
 		i=i+1;
 		j=j+1;
 	}
 	return 1; // A and B contain the same set of elements
}
///////////////////////////////////////
C_12_40 OUR HOMEWORK!! PASSED

radix sort on the digits of each of the n elements,
viewing them as pairs (i, j) 
such that i and j are integers in the range [0, n − 1]

Time Complexity: O(2(n+n-1))=O(n)
///////////////////////////////////////
C_12_41 Still Have Some Questions!!

///////////////////////////////////////
C_12_42 PASSED
determine whether there are two equal elements in S
My solution: 
	Sort: O(nlog n)
	comparation: if a[i]==a[i+1] return true , O(n)
Total time complexity:O(n log n)

///////////////////////////////////////
C_12_43 PASSED BUT STILL NEED REVISION
Hint: modify the merge sort

//this is the solution in homework
/* inversion in S=
* inversion in S1 +
* inversion in S2 +
* one in S1 another in S2
*/
Algorithm countInversions(S)
Input: A Sequence S of length n
Output: The number of inversions in S (S is also sorted)
{
	if(S.size()<2){
		return 0;
	}

	//devide
	create sequences S1,S2 each storing half of S
	for(i=1;i<=n/2;i++){
		S1.insert(S.remove(S.first()));
	}
	for(i=n/2+1;i<=n;i++){
		S1.insert(S.remove(S.first()));
	}

	//recursions
	//When we perform this the S1 and S2 should already be sorted!!
	inv1=countInversions(S1);
	inv2=countInversions(S2);

	//merge
	inv3=0;
	while(!S1.isEmpty() && !S2.isEmpty()){
		s1=S1.first();
		s2=S2.first();

		if(s1<=s2){ //not inversion
			S.insert(s1); 
			S1.remove(s1);
		}
		else{ //inversion
			S.insert(s2);
			//everything remaining in S1 is out of order with s1
			inv3=inv3+S1.size();//equal to S1.size()-i , bec i=0
			S2.remove(s2);
		}
	}
	return inv1+inv2+inv3;
}

//Time complexity: O(n log n)

e.g. S = (6, 9, 1, 14, 8, 12, 3, 2)
when we perform inv3 after inv1 and inv2, S1 and S2 are already sorted!!
>>> inv3: S1=[1,6,9,14],S2=[2,3,8,12]
s1=6 -> 3+3
s1=9 -> 2
s1=12 -> 1
>>> so inv3=9
inv1=2
inv2=5
>>> total solution = 16!!!FINISHED



//another solution which is better!
ANOTHER SOLUTION 
long merge(int[] arr, int[] left, int[] right) {
    int i = 0, j = 0, count = 0;
    while (i < left.length || j < right.length) {
    	//end of left half: insert all remaining j
        if (i == left.length) { 
            arr[i+j] = right[j];
            j++;
        } 
        //end of right half: insert all remaining i
        else if (j == right.length) { 
            arr[i+j] = left[i];
            i++;
        } 
        //no inversion: insert current i
        else if (left[i] <= right[j]) { 
            arr[i+j] = left[i];
            i++;                
        } 
        //inversion: insert current j
        //count+=all remaining elements in left half
        else {
            arr[i+j] = right[j];
            count += left.length-i;
            j++;
        }
    }
    return count;
}

long invCount(int[] arr) {
    if (arr.length < 2)
        return 0;

    int m = (arr.length + 1) / 2;
    int left[] = Arrays.copyOfRange(arr, 0, m);
    int right[] = Arrays.copyOfRange(arr, m, arr.length);

    return invCount(left) + invCount(right) + merge(arr, left, right);
}


///////////////////////////////////////
C_12_44 
Hint: modify the insert sort

Algorithm PrintInversion
Input: Sequence S with n elements
Output: print all the inversion in S
{
	int current=1; //the one to be inserted in the sorted part
	while(current<S.length()){
		currentElement=S[current]
		for(i=current-1;i>=0;i--){ // find the position of current element
			if(currentElement>S[i]){
				print(pair(S[i],currentElement);
				S[i+1]=S[i];
				S[i]=currentElement;
			}
		}
		current++;
	}
}

///////////////////////////////////////
C_12_46 PASSED
Compute A1 as a1=m-a : O(n)
Sort A1: O(n log n)
Sort B: O(n log n)
Compare if there are same elements in A1 and B using merging: O(2n)

Algorithm mergeComp(A1,B)
Input: sorted list A1 , B;
Output: whether there are same elements
{
	while(!A1.isEmpty() && !B.isEmpty()){
		if(A1.first()>B.first()){
			A1.remove(B.first());
		}
		else if(A1.first()<B1.first()){
			B.remove(B.first());
		}
		else{
			return True;
		}
	}
	return False;
}

///////////////////////////////////////
C_12_47 PASSED
Implement XOR
//Note that there is no same element in a set
Algorithm XOR(A,B)
Input: 2 sorted sets A,B;
Output: set S containing all elements of A XOR B
{
	Create empty set S;
	while(!A.isEmpty() && !B.isEmpty()){
		if(A.first()<B.first()){
			S.insert(A.remove(A.first()));
		}
		else if(A.first()>B.first()){
			S.insert(B.remove(B.first()));
		}
		else{
			A.remove(A.first());
			B.remove(B.first());
		}
	}
	while(!A.isEmpty()){
		S.insert(A.remove(A.first()));
	}
	while(!B.isEmpty()){
		S.insert(B.remove(B.first()));
	}
	return S;
}

///////////////////////////////////////
C_12_48 PASSED
find ceiling(log n) elements closest to median

Step 1: sort the set S and find the median M; O(n log n)
Step 2: devide S into S1 and S2 with M; O(n)
Step 3: reverse S1; O(n)
Step 4: compare S1 and S2 by |M-s1| and |M-s2|, then find elements; O(log n)

///////////////////////////////////////
C_12_49 PASSED
Based on randomly QuickSort:
Step 1: randomly pick a bolt A, partition nuts into larger AL and smaller AS
	and find the matching nut a;
Step 2: partition bolts by nut a-->larger aL,smaller aS;
Step 3: recursion: (AL,aL),(AS,aS)

//the time complexity should be O(n log n)
///////////////////////////////////////
C_12_51
inPlace QuickSelect
Do a revision about QuickSelect

///////////////////////////////////////

///////////////////////////////////////
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
***************************************
///////////////////////////////////////
Chapter 10 Maps, Hash Tables, and Skip Lists

R_10_1 PASSED
O(n^2) //compare if there are same keys
///////////////////////////////////////
R_10_4 PASSED

Separate Chaining: no
Linear Probing: yes, because almost all the space can be filled

///////////////////////////////////////
R_10_5 PASSED
Polynomial accumulation/ Cyclic shifting
break components into pieces

x0 + z ( x1 + z ( x2 + z ( x3 + z ( x4 )))) mod N

///////////////////////////////////////
R_10_6 PASSED
(12, 44, 13, 88, 23, 94, 11, 39, 20, 16, 5)
--> (3i+5) mod 11
use separate chaining 

R_10_7 PASSED
use linear probing 
///////////////////////////////////////
R_10_10 PASSED
Worst case: n^2, each insertion cause collision(O(n))
Best case: n, each insertion cost O(1)
///////////////////////////////////////
R_10_17 PASSED
Why hash map is unsuitable for sorted map
to handle collision, the order will be broken(separate chaining/open addressing)
///////////////////////////////////////
R_10_18 PASSED
n^2 because each find() operation costs O(n)
///////////////////////////////////////
R_10_23 PASSED
Do a revision about the insertion and deletion for skip list
///////////////////////////////////////
R_10_24 PASSED
Algorithm remove()
Input: skipList S, key K to be removed
Output: remove K from S 
{
	int l=sl; //the top level of S
	//find the top level containing K
	while(l>=0){
		if Sl.contains(K){
			break;
		}
		else{
			l--;
		}
	}
	delete K in Sl,Sl-1,...,S1,S0;
	if there are more than one empty levels, leave one and remove the others
}

///////////////////////////////////////

HOMEWORK Q1 PASSED
>>> Describe how to use a map to implement the dictionary ADT, assuming that the
user may attempt to insert entries with the same key.

define entry kk=(key,keyNumber), where key is the original key and 
keyNumber is the number key appears,
e.g. if the key K is inserted twice, the kk should be
kk1=(K,1),kk2=(K,2)

///////////////////////////////////////
HOMEWORK Q2 Still Have Some Questions
>>> Describe how to perform a removal from a hash table that
uses linear probing toresolve collisions where we do not use 
a special marker to represent deleted elements.
>>> That is we must rearrange the contents so that it appears 
that the removed entry was never inserted in the first place.

SOLUTION:
>>> we need to rearrange the hash table contents so that it seems 
the removed entry never existed

>>> This action can be done by simple incrementally stepping forward 
through the table (much as we do when there are collisions) 
and moving back one spot each key k for which f(k) equals
f(keyofremovedentry). 
>>> We continue walking through the table until we encounter the
first entry for which the f(k) value differs

///////////////////////////////////////
HOMEWORK Q3
>>> Given a dictionary, the method successor(k) returns all the entries with keys
greater than or equal to k. Describe how to implement successor(k) in an ordered
dictionary realized using an ordered search table. What is the running time?

SOLUTION:
>>> Binary search
>>> Step 1: find k, O(log n)
>>> Step 2: find those larger then k, O(m)
>>> time complexity: O(log n+m), m is the number of elements larger than k

///////////////////////////////////////
HOMEWORK Q4
>>> Repeat the previous exercise using a skip list.
 What is the expected running time? 

SOLUTION:
>>> find k: O(log n)
>>> scan forward to find successors: O(m)
>>> the time complexity is also O(log n+m)

///////////////////////////////////////
HOMEWORK Q5
>>> Describe an efficient dictionary structure for storing n entries 
whose r<n keys have distinct hash codes. 
>>> Your structure should perform operation findAll in O(s) expected time, 
where s is the number of entries returned, operation entries() in O(n)
time, and the remaining operations of the dictionary ADT in O(1) expected time.

SOLUTION: use a hashtable
n entries r keys--> handle the collisions;
find()-->O(1)-->findAll-->O(s);
entries()-->O(n)

///////////////////////////////////////

///////////////////////////////////////
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
***************************************
///////////////////////////////////////
Chapter 13 Text Proecssing

R_13_1 PASSED
R_13_2 PASSED
///////////////////////////////////////
R_13_3 PASSED
Brutal Force:
{
    int i=0;
    int j=0;
    while(i<n-m+1){
        if(P[j]==T[i]){
            if(j==m-1){
                return i-j;
            }
            else{
                i++;
                j++;
            }
        }
        else{
            j=0;
            i++;
        }
    }
    return -1;
}


R_13_4 PASSED Boyer-Moore
    l=L[T[i]];
    i+= m-min(j,l+1);
R_13_5 PASSED Knuth-Morris-Pratt
    j=F(j-1);

///////////////////////////////////////
R_13_6 PASSED
Algorithm LastOccuranceFunction
Input: pattern string P;
Output: a map represent the LOF of P;
{
    Map LOFmap = new HashMap();
    for(int i=0;i<P.length;i++){
        /* if P[i] has not appeared in the map, its position will be recored;
        * else: its position will be updated
        */ 
        LOFmap.put(Entry(i,P[i]));
    }
    return LOFmap;
}

///////////////////////////////////////
R_13_7 PASSED
Algorithm FailureFunction
Input: pattern string P;
Output: array F represent the LOF of P;
{
    int m = P.length;
    int[] F= new int[m];
    int i=0; //prefix
    int j=1; //surfix
    while(i<m){
        if(P[i]==P[j]){
            F[j]=i+1;
            i++;
            j++;
        }
        else if(i>0){
            i=F[i-1];
        }
        else{
            j++;
        }
    } 
    return F;
}
///////////////////////////////////////
R_13_8 PASSED Standard Trie 
R_13_9 PASSED Compressed Trie
R_13_10 PASSED Suffix Trie
///////////////////////////////////////
R_13_11 PASSED Huffman Encoding
removeMin()
removeMin()
merge
insert()
///////////////////////////////////////
R_13_14 PASSED
LCS{
	if(X[i]==Y[j]){
		LCS[i+1][j+1]=LCS[i][j]+1
	}
	else{
		LCS[i+1][j+1]=max(LCS[i+1][j],LCS[i][j+1])
	}
}

    s  k  u  l  l  a  n  d  b  o  n  e  s
 l  0  0  0  1  1  1  1  1  1  1  1  1  1
 u  0  0 [1] 1  1  1  1  1  1  1  1  1  1
 l  0  0  1 [2] 2  2  2  2  2  2  2  2  2
 l  0  0  1  2 [3] 3  3  3  3  3  3  3  3
 a  0  0  1  2  3 [4] 4  4  4  4  4  4  4
 b  0  0  1  2  3  4  4  4 [5] 5  5  5  5
 y  0  0  1  2  3  4  4  4  5  5  5  5  5
 b  0  0  1  2  3  4  4  4  5  5  5  5  5
 a  0  0  1  2  3  4  4  4  5  5  5  5  5
 b  0  0  1  2  3  4  4  4  5  5  5  5  5
 i  0  0  1  2  3  4  4  4  5  5  5  5  5
 e  0  0  1  2  3  4  4  4  5  5  5 [6] 6
 s  0  0  1  2  3  4  4  4  5  5  5  6 [7]

So the LCS should be "ullabes"

///////////////////////////////////////
C_13_15 PASSED

Solution: periodic, almost match but the last is not match
T="AAAAAAAAAAAAAAAAAAAAAAAAA"
P="AAAE"

///////////////////////////////////////
C_13_16 PASSED
BrutalForceFindLast:
{
    int i=0;
    int j=0;
    Stack result=new Stack();
    while(i<n-m+1){
        if(P[j]==T[i]){
            if(j==m-1){
                result.push(i-j);
            }
            else{
                i++;
                j++;
            }
        }
        else{
            j=0;
            i++;
        }
    }
    if(!result.isEmpty()){
        return result.pop();
    }
    else{
       return -1;
    }
}

C_3_18 PASSED
KMPFindLast:
{
	int i=0;
	int j=0;
	F=FailureFunction;
    Stack result =new Stack;

	while(i<n-m+1){
		if(T[i]==P[j]){
			if(j==m-1){
				Stack.push(i-j);
			}
			else{
				i++;
				j++;
			}
		}
		else{
			if(j>0){
				j=F(j-1);
			}
			else{//j==0
				i++;
			}
		}
	}
    if(!result.isEmpty()){
        return result.pop();
    }
    else{
	   return -1;
    }
}
///////////////////////////////////////
C_13_20 PASSED
Let T be a text of length n, and let P be a pattern of length m. Describe an O(n+m)-time method for finding the longest prefix of P that is a substring of T .

Hint: modify KMP, KMP is O(m+n)
Algorithm KMPLongestPrefix
Input: T/P;
Output: longest prefix of P
{
	int i=0;
	int j=0;
	F=FailureFunction;
	int longestPrefix=0;

	while(i<n-m+1){
		if(T[i]==P[j]){
			if(j==m-1){
				return P;//all match!
			}
			else{
				i++;
				j++;
			}
		}
		else{
			if(j>0){
				if(longestPrefix<j){
					longestPrefix=j;
				}
				j=F(j-1);
			}
			else{//j==0
				i++;
			}
		}
	}
	return P[0:longestPrefix+1];//the last position is P[longestPrefix]
}
///////////////////////////////////////
C_13_24 Still Have Some Questions
Let T be a text string of length n. Describe an O(n)-time method for finding the
longest prefix of T that is a substring of the reversal of T .

Hint: Prefix Trie

///////////////////////////////////////
C_13_25 Still Have Some Questions
Describe an efficient algorithm to find the longest palindrome that is a suffix of
a string T of length n. Recall that a palindrome is a string that is equal to its
reversal. What is the running time of your method?
///////////////////////////////////////
C_13_26 PASSED
Give an efficient algorithm for deleting a string from a standard trie and analyze its running time.
Algorithm stringDeletion(T,s)
Input: A standard trie T and a string s
Output: T without s
{
	Search for s;//locating the leaf
	if(not found){
		print "no match!";
		return 0;
	}
	else{//we find whole s at nod u 
		if(u is not external){
			print "partial match!";
			return 0;
		}
		//now we need to delete string s
		//we need to delete from u to the first ancestor with more than one child
		node c=u.getParent();
		while(c has only one child){
			delete u;
			u=c;
			c=u.getParent();
		}//f-u-c-k and f-a-c-e : delete u-c-k
		delete u;
		return 1;
	}
}
Time complexity: O(dm)

C_13_27 HOMEWORK PASSED
Give an efficient algorithm for deleting a string from a compressed trie and analyze its running time.

Algorithm stringDeletion(T, s)
Input: A compressed trie T and a string s
Output: T without s
// only one condition can perform delete 
{
	Search for s;
	if(not found){ //no match
		print "no match!";
		return 0;
	}
	else{ //find s at node u
		if(s is not the whole string ended at u||u has a child){
			//if not this substring contains too much
			//e.g. u is not the external: "sb"-"xyq"(child),"asshole"(child)
			//e.g. u contains more than s: "sbbbbb"
			print "partial match!";
			return 0;
		}
		//u do not have child and s contain u
		v=u.getParent();
		delete u;
		if(v has a child c){
			// p.string denotes the string stored at a node p
 			v.string=v.string+c.string;
 			delete node c; // merge v and c into a single node
 		}
 		return 1; // successful deletion
 	}
}


Time Complexity: O(dm)
///////////////////////////////////////
C_13_28 
Describe an algorithm for constructing the compact representation of a suffix trie,
given its noncompact representation, and analyze its running time.

Hint: Recall how you identify the branches of the suffix trie that can
be compressed

///////////////////////////////////////
C_13_29 - C_13_31 
Create a standard/compressed/suffix trie class
///////////////////////////////////////
C_13_32 Still Have Some Questions
Given a string X of length n and a string Y of length m, describe an O(n + m)-time algorithm for finding the longest prefix of X that is a suffix of Y .

Algorithm MatchPreSuf
Input: X(n), Y(m);
Output: the longestPrefix of X that is also a suffix of Y;
{
	Build a compressed tree of X; //O(n)
	Build a suffix tree of Y; //O(m)
	while(!Y.isEmpty()){
		find the longest suffix y in Y; //O(y.length)
		delete y from Y //O(y.length);
		search y in X;//O(y.length)
		if(y can be found in X){
			return y;
		}
	}//O(m)
	return -1;
}
///////////////////////////////////////
C_13_33 PASSED 
Greedy Method
Pick as much as 25;
Pick as much as 10;
Pick as much as 5;
Pick all the rest as 1s

C_13_35 & C_13_36 are also based on greedy method
///////////////////////////////////////

C_13_40 HOMEWORK PASSED
find the longest decreasing subsequence T of S
e.g. S=54312 , then T=5431
My thought is we can use something like LCS

LCS{
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			if(X[i]==Y[j]){
				L[i+1][j+1]=L[i][j]+1;
			}
			else{
				L[i+1][j+1]=max(L[i+1][j],L[i][j+1]);
			}
		}
	}
	return L;
}

SOLUTION{
	Compute the reverse of S: S1, note that the duplicates should be removed //e.g. S=544312, S1=54321
	Find the LCS of S1 and S;
	Then we can get T=LCS
}

Time complexity: 
	reverse: O(nlogn)
	LCS: O(n^2)

///////////////////////////////////////
C_13_42 PASSED
Get LCS of P and T, if LCS=P.length, then P is subsequence of T
Running time: O(mn)
///////////////////////////////////////
C_13_45 Still Have SOme Questions
Dynamic Programming
///////////////////////////////////////
C_13_46 PASSED
Hint: Brutal Force
Find all pairs(a,b) that a in A and b in B;//O(n^2)
Calculate k-a-b and sort as array D;//O(n^2 log n)
Sort C;//O(n log n)
Find if element in C is also in D, similar to merge;//O(n^2+n)
So the total time complexity should be O(n^2 log n)

C_13_47 Haojie Method


///////////////////////////////////////
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
***************************************
///////////////////////////////////////
Chapter 14 Graph

///////////////////////////////////////
R_14_1 PASSED
Simple Undirected Graph

Review the rule: sum(deg(v))=2m

///////////////////////////////////////
R_14_2 PASSED

For Undirected Graph, m<=n(n-1)/2
And there are 3 connected components, we can regard
this as a connected graph with 10 vertices and 2 single vertices
so the maximum of edges should be 45

///////////////////////////////////////
R_14_5 PASSED
Simple, Connected, Directed
DegIn+DegOut=2m

///////////////////////////////////////
R_14_6 PASSED
When performing insertVertex, we can just insert a vertex in the vertex list, so O(1)

When performing removeVertex, we should traversal the edge list to remove all the adjacent edges, so O(m)

///////////////////////////////////////
R_14_7 PASSED
Add x at location (u,v) and (v,u)

///////////////////////////////////////
R_14_11 PASSED

Choose suitable structure based on different condiitons

a. adjacency list:
    less space: adjacency matrix should be excluded (O(n^2))
    the average degree is 2: most operations of AL are based on deg
    there are a large number of total edges, so edge list should be excluded
b. AL, same to above
c. AM: areAdjacent(u,v) in O(1)

///////////////////////////////////////
R_14_13 Still Have Some Questions

///////////////////////////////////////
R_14_14 PASSED
DFS on Complete Graph

R_14_15 PASSED
BFS on Complete Graph
///////////////////////////////////////
R_14_16 PASSED
Perform DFS and BFS in a given graph
///////////////////////////////////////
R_14_17 PASSED
DFS in Directed Graph
or
Topological Sort

Solution:
LA15 LA22 LA16 LA141 LA127 LA31 LA32 LA126 LA169

///////////////////////////////////////
R_14_18 Topological Ordering

///////////////////////////////////////
R_14_19 Transitive Closure
May be we can use the Incidence Matrix

///////////////////////////////////////

R_14_20-R_14_22 Transitive Closure

///////////////////////////////////////

R_14_23 PASSED
Dijkastra

R_14_24 Still Have Some Questions
Dijkastra for directed graph

///////////////////////////////////////
R_14_25 PASSED
Prim 

R_14_26 PASSED
Kruskal

///////////////////////////////////////
R_14_27 PASSED
MST using Kruskal

///////////////////////////////////////





