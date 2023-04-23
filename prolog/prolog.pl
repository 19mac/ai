female(pam).
female(liz).
female(ann).
female(pat).
male(tom).
male(bob).
male(jim).

parent(pam, bob).
parent(tom, bob).
parent(tom, liz).
parent(bob, ann).
parent(bob, pat).
parent(pat, jim).

mother(X,Y) :- parent(X,Y), female(X).
father(X,Y) :- parent(X,Y), male(X).
has_child(X) :- parent(X,_).
siblings(X,Y) :- parent(Z,X),parent(Z,Y),X\==Y.
sister(X,Y):- parent(Z,X),parent(Z,Y),female(X),X\==Y.
wife(X,Y) :- female(X),male(Y),parent(X,Z),parent(Y,Z).

aunt(X,Y) :- sister(X,Z),parent(Z,Y). 

grandparent(X,Y) :-parent(X,Z),parent(Z,Y).
grandmother(X,Y) :-parent(X,Z),parent(Z,Y),female(X).


predecessor(X, Z) :- parent(X, Z).
predecessor(X, Z) :- parent(X, Y),predecessor(Y, Z).