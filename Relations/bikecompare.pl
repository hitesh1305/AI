bike(ktm, 200000).
bike(royal_enfield, 250000).
bike(honda, 150000).
bike(hero, 100000).
bike(bajaj, 120000).
bike(tvs,100000).
cheaper_than(B1, B2) :-
    bike(B1, P1),
    bike(B2, P2),
    P1 < P2.

same_price(B1,B2) :-
    bike(B1,P1),
	bike(B2,P2),
	P1=:=P2.

costlier_than(B1,B2) :-
    bike(B1,P1),
    bike(B2,P2),
    P1>P2.

