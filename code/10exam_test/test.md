1. Dato il seguente frammento di codice, scegliere una tra le seguenti l'opzione corretta:
    ```python
    s = "hello world"
    s[5] = ""
    print(s)
    ```
    A. il programma stampa `helloworld`  
    B. il programma stampa `hello orld`  
    C. la seconda riga lancia un'eccezione    
    D. la terza riga lancia un'eccezione  

2. Dato l'albero in figura
    ```
             A
            / \
           /   \
          /     \
         B       C
        / \       \
       /   \       \
      F     G       I
     /     / \       \
    N     O   K       L
    ```
    specificare l'ordine di visita dei nodi in una visita dfs (depth first search) in __post-order__

    A. N -> F -> B -> O -> G -> K -> A -> C -> I -> L    
    B. A -> B -> F -> N -> G -> O -> K -> C -> I -> L  
    C. N -> F -> O -> K -> G -> B -> L -> I -> C -> A  
    D. A -> B -> C -> F -> G -> I -> N -> O -> K -> L  

3. Qual'è il costo, usando la notazione O, dell'accesso ad un elemento di un dizionario tramite chiave, se il dizionario contiene n chiavi? (Ignora le collisioni)
    
    .  
    .  
    .  
    .  

4. Indicare il costo della seguente funzione (rispetto alla dimensione dell'input) usando la notazione asintotica
    ```python
    def foo(l1:List,l2:List):
        if len(l1)!=len(l2):
            raise ValueError
        o = 0
        for i in range(len(l1)):
            o += l1[i]*l2[i]
        return o
    ```

    .  
    .  
    .  
    .  

5. Cosa stampa il seguente programma? 
    ```python
    def foo(a):
        a = a+1
        return a

    a = 0
    for i in range(10):
        foo(a)
    print(a)
    ```

    A. 9  
    B. 0  
    C. 10  
    D. Nessuna delle precedenti  

6. Dato il seguente programma, scegliere una tra le seguenti opzioni

    ```python
    for i in range(10):
        if i%2 == 0:
            k = i

    print(k)
    ```

    A. il programma termina lanciando un'eccezione  
    B. il programma stampa 8  
    C. nessuna delle precedenti  

7. Dato il seguente programma, scegliere una tra le seguenti opzioni

    ```python
    l1 = [1,2,3]

    def foo(l:List):
        l1 = l
        del l1[0]
        del l1[-1]


    l = [4,5,6]
    foo(l)

    print(l1)
    print(l)
    ```

    A. stampa `[1,2,3]` e `[5]`  
    B. stampa `[1,2,3]` e `[4,5,6]`  
    C. stampa `[5]` e `[5]`  
    D. termina lanciando un'eccezione  

8. Dato il seguente programma, scegliere una tra le seguenti opzioni

    ```python
    class A:
        def __init__(self,a,b):
            self.a = a
            self.b = b

        def foo(self):
            print(f"Sum:{self.sum()},Sub:{self.sub()}")
        
        def sum(self):
            return self.a+self.b
        
        def sub(self):
            return self.a-self.b
        
    class B(A):
        def __init__(self,a,b,c):
            super().__init__(a,b)
            self.c = c

        def sum(self):
            return super().sum() + self.c

        def foo(self):
            print(f"Sum:{self.sum()},Sub:{self.sub()}")
        
    o = B(1,2,3)
    o.foo()
    ```

    A. Stampa `Sum:3,Sub:-1`    
    B. Stampa `Sum:6,Sub:-1`  
    C. Lancia la seguente eccezione: `AttributeError:'B' object has no attribute 'sub'`  


9. What is the time complexity of the recursive function below:
    ```python
    def ispalindrome(s):
        if len(s) <= 1:
            return True
        
        if s[0] != s[-1]:
            return False
        
        else:
            return ispalindrome(s[1:-1])
    ```

    .  
    .  
    .  
    .  

10. Cosa stampa il seguente programma?
    ```python
    class Vec2D:
        def __init__(self,x,y):
            self.x = x
            self.y = y

        def len(self):
            return math.sqrt(self.x**2 + self.y**2)
        
        def __str__(self) -> str:
            return f"({self.x},{self.y})"

    l = [Vec2D(5,3),Vec2D(-10,1),Vec2D(1,2)]
    l.sort(key=lambda x:x.len())
    for x in l:
        print(x,end=";")
    ```

    .  
    .  
    .  
    .  

11. Given the following program, chose one of the following options:
    ```python 
    import math

    class Person:

        def __init__(self,nome) -> None:
            self.nome = nome


    p1 = Person("Mario")
    p2 = Person("Andrea")

    if p1 < p2:
        print(f"{p1.nome},{p2.nome}")
    elif p1 > p2:
        print(f"{p2.nome},{p1.nome}")
    else:
        print("Same")
    ```

    A. stampa `Andrea,Mario`  
    B. stampa `Mario,Andrea`  
    C. stampa in modo arbitrario `Andrea,Mario` o `Mario,Andrea`  
    D. lancia l'eccezione `TypeError:'<' not supported between instances of 'Person' and 'Person'`  

12. Dato il seguente programma, qual'è loutput corretto?

    ``` python
    class MutableTuple:
        def __init__(self,a,b) -> None:
            self.a = a
            self.b = b

        def __setitem__(self,i,value):
            if i==0:
                self.a = value
            elif i ==1:
                self.b = value
            else:
                raise ValueError
            
        def __str__(self):
            return f"({self.a},{self.b})"
        
    a = MutableTuple(1,2)
    b = MutableTuple(1,4)

    print(a==b,end=" ")
    b[1] = 2
    print(b,end=" ")
    print(a==b)
    ```

    A. stampa `False (1,2) False`  
    B. stampa `False (1,2) True`  
    C. lancia l'eccezione `TypeError: 'MutableTuple' object does not support item assignment`  



14. Qual'è l'output del seguente programma?

    ```python
    def gen(l:List):
        for x in l:
            yield x%5


    l = [1,2,3,4,5,6,7,8,9,10]
    for x in gen(l):
        print(x,end=" ")
    ```

    A. stampa `1 2 3 4 0 1 2 3 4`  
    B. stampa `None`  
    C. lancia l'eccezione `TypeError:'NoneType' object is not iterable`  


15. Dato il seguente programma, quali tra le seguenti opzioni è corretta?

    ```python
    from typing import List

    class StrLenIterator:

        def __init__(self,l:List[str]):
            self.data = l
            self.id = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.id < len(self.data):
                r = (self.data[self.id], len(self.data[self.id]))
                self.id += 1
                return r
            

    l = ["in","bocca","al","lupo"]
    it = StrLenIterator(l)
    for x in it:
        print(x,end=" ")
    ```

    A. stampa `('in', 2) ('bocca', 5) ('al', 2) ('lupo', 4)`  
    B. lancia l'eccezione `TypeError:'StrLenIterator' object is not iterable`  
    C. il programma non termina  


