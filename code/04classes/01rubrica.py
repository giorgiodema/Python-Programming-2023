from typing import List
# Implementare una rubrica che mi permette di creare nuovi contatti, 
# aggiornare il numero di un contatto
# esistente e visualizzare il numero di un contatto

class Contatto:
    def __init__(self, nome:str, numero:str):
        self.nome = nome
        self.numero = numero

    def __eq__(self,c):
        return self.nome == c.nome
    

if __name__=="__main__":
    rubrica = []

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
                rubrica.append(Contatto(nome,numero))
            else:
                continue
        