male(john).
male(david).
male(raj).

female(mary).
female(sita).
female(rita).

parent(john, david).   % John is a parent of David
parent(mary, david).   % Mary is a parent of David
parent(john, rita).    % John is a parent of Rita
parent(mary, rita).    % Mary is a parent of Rita
parent(david, raj).    % David is a parent of Raj
parent(sita, raj).     % Sita is a parent of Raj

father(X, Y) :- male(X), parent(X, Y).
mother(X, Y) :- female(X), parent(X, Y).

sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.

grandparent(X, Y) :- parent(X, Z), parent(Z, Y).