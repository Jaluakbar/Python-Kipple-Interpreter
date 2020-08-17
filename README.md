
# Kipple Language Python Interpreter
Kipple is een simpele esoteric programming language (esolang) met operators, stacks and een control structuur. De taal heeft stacks die genoemd worden als het alfabet, van 'a' tot en met 'z' en  een extra stack '@'. De taal heeft 5 operators en een control structuur, de loop. De stacks zijn Last In First Out (LIFO).

| Operator | Functionaliteit |
|--|--|
| + | Zet de som van de rechte en linke waarde in de linke stack |
| - | Zet de minus van de rechte en linke waarde in de linke stack |
| > | Pakt de waarde van linker kant en zet hem in de rechte stack  |
| < | Pakt de waarde van rechter kant en zet hem in de linke stack |
| ? | Als de laatste waarde van stack voor deze operator 0 is, wordt de stack leeg gemaakt |


# Hoe werkt het

De Kipple programma moet geschreven worden in een *txt* file. Deze *txt* file naam moet je meegeven als parameter aan de interpret(filename) functie. 

De interpreter maakt een stack aan waar waardes worden bewaard. Daarna worden de character uit de file gelezen en geconverteerd naar Tokens. Deze tokens worden daarna gegeven aan de operator functie, deze gaat over alle tokens heen en opereert alle operators die hij vindt. Als er input stack wordt gebruikt dan wordt het op het start van de programma gevraagd. Als laatste print hij de Output Stack.


# Hoe gebruikt je het

- Invoegen

`
1>a
b<2
a>b
`

Dit resulteer in stack b met de waarde [2,1] en a leeg [].

- Vrij

`
2>b
1>b
0>b
b?
`

Omdat de laatste waarde in b 0 is, is b nu leeg [].

- Toevoegen

```
10>a
123>b
a+b
```

Dit resulteert in a = [133] en b is leeg [].

- Aftrekken

```
1>c
2>d
c-d
```
Dit resulteert in c = [-1] en d is leeg [].
- Lus

```
10>a
(a-1 b+1)
```

- Input

`
i>o
`

Als er input stack is gebruikt, moet die geassigned worden aan een andere stack. Er zal aan het start van de programma gevraagd worden voor input. Let op : Dit kan alleen een keer in gebruikt worden.

De lus blijft door gaan tot dat de waarde na de open haakje '(' nul is. Hier gaat de lus over a, dit resulteert in stack 'a' leeg/nul wordt [] en 'b' = [10]

# Voorbeelden

 - Hello World
 
`33>o 100>o 108>o 114>o 111>o 87>o 32>o 111>o 108>o 108>o 101>o 72>o`

- Nummers printen van 0 tot het aantal gegeven in de input

```
  i>n
  (n-1 n<n>@ @>o)
```
-  Rekenen en printen van nummers

```
15>a
12213>b
a+b 
a>@
(@>o)
```

- Lussen om te vermenigvuldigen

```
20>a
(a-1 b<3 (b-1 c+1))
c>@
(@>o)
```
