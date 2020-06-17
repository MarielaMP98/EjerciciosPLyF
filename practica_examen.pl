% Desarrollo una gramatica bnf (como la del video) para validar una 
% direccion ipv4 asi como una mascara de red.
% https://es.wikipedia.org/wiki/M%C3%A1scara_de_red#Tabla_de_m%C3%A1scaras_de_red
% Realice la implementacion de dicha gramatica en prolog donde
% se pueda validar la cadena donde esta esa ip o mascara ejemplo

%ip("192.168.1.1").
%true.
%ip("256.168.1.1").
%false.
%maskR("255.255.255.0").
%true.
%maskR("255.255.255.1").
%false.

latom_lstring([],[]).
latom_lstring([F|C],R) :- latom_lstring(C,S), atom_string(F,SF), append([SF],S,R).

preparar_string(Term,LS) :-
    atom(Term),
    atom_string(Term,Str),
    preparar_string(Str,LS).

preparar_string(Str,LS) :-
    string(Str),
    string_chars(Str,LAC),
    latom_lstring(LAC,LS).


r5(R):- R == "0"; R == "1"; R == "2"; R == "4"; R == "5"; R == "8".

digito(N) :-
   N == "0"; N == "1"; N == "2"; N == "3"; N == "4";
   N == "5"; N == "6"; N == "7"; N == "8"; N == "9".



%ip
ip(IP) :- split_string(IP,".",",",LIST), envIP(LIST).

envIP([F|[]]) :- valIP(F).
envIP([F|C])  :- valIP(F), envIP(C).

valIP(DIR) :- string_length(DIR,3),preparar_string(DIR,SEP), op1(SEP);
                   string_length(DIR,2),preparar_string(DIR,SEP), op2(SEP);
                   string_length(DIR,1),preparar_string(DIR,SEP), op2(SEP).

op1([F|C]) :- F == "2", octeto([F|C]); F == "1", op2([F|C]).
op2([F|[]]) :- digito(F).
op2([F|C])  :- digito(F), op2(C).

octeto([F|[]]) :- r5(F).
octeto([F|C])  :- r5(F), octeto(C).


%MaskR
maskR(MASCARA) :- split_string(MASCARA,".",",",MR), valMaskR(MR).

envMask([F|[]])  :- valMaskR(F).
envMask([F|C])  :- valMaskR(F), envMask(C).

valMaskR([F|[]]) :- string_length(F,3),prim_op(F);
                      string_length(F,1),seg_op(F).

valMaskR([F|C]) :- string_length(F,3),prim_op(F),valMaskR(C);
                     string_length(F,1),seg_op(F),envMask(C).


prim_op(N):- N == "128"; N == "192"; N == "224"; N == "240";
          N == "248"; N == "252"; N == "254"; N == "255".
seg_op(MC):- MC == "0".