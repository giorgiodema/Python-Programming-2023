from typing import List
import os
# Implementare una rubrica che mi permette di creare nuovi contatti, 
# aggiornare il numero di un contatto
# esistente e visualizzare il numero di un contatto

class Contatto:
    def __init__(self, nome:str, numero:str):
        self.nome = nome
        self.numero = numero

    def read_line(self,s:str):
        s = s.strip()
        l = s.split(",")
        self.nome = l[0]
        self.numero = l[1]

    def write_line(self,f):
        s = f"{self.nome},{self.numero}\n"
        f.write(s)

    def __eq__(self,c):
        return self.nome == c.nome
    

if __name__=="__main__":
    rubrica = []
    if os.path.exists(os.path.join(".","rubrica.csv")):
        f = open(os.path.join(".","rubrica.csv"),"r",encoding="utf-8")
        for line in f:
            c = Contatto("","")
            c.read_line(line)
            rubrica.append(c)
        f.close()

    f = open(os.path.join(".","rubrica.csv"),"a",encoding="utf-8")

    try:
        while True:
            nome = input("Inserisci nome:")
            # se il contatto è presente, visualizza
            # il numero e chiedi all'utente se 
            # intende modificarlo
            if Contatto(nome,"") in rubrica:
                i = rubrica.index(Contatto(nome,""))
                print(f"numero:{rubrica[i].numero}")
            
            # altrimenti chiedi all'utente se vuole
            # aggiungere un nuovo contatto e in caso
            # affermativo chiedi il numero
            else:
                print("contatto non trovato")
                prompt=input("inserirlo[S/N]")
                while prompt != "S" and prompt != "N":
                    prompt=input("inserirlo[S/N]")
                if prompt == "S":
                    numero=input("inserisci numero:")
                    c = Contatto(nome,numero)
                    rubrica.append(c)
                    c.write_line(f)
                else:
                    continue
    except KeyboardInterrupt:
        print("Closing")
        f.close()
        