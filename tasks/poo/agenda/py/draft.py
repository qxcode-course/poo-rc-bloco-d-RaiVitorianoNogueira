class Agenda:
    def __init__(self):
        self.contacts: list[Contato] = []


#pesquisar os contatos
    def findPosByName(self, name: str):
        for i, contato in enumerate(self.contacts):
            if contato.getNome() == name:
                return i
            return -1

    def __str__(self):
        return "\n".join(str(c) for in c in self.contacts)



    def addContact(self, name: str, fones: list[Fone]):
        p = self.findPosByName(name)
        if p != -1:
            cont = self.contacts[p]
            for f in fones:
                cont.addFone(f.getId(), f.getNumber())
            return
        novo = Contato(name)
        for f in fones:
            novo.addFone(f.getId(), f.getNumber())
        
        self.contacts.append(novo)
        self.contacts.sort(key=lambda c: c.getNome())

    def getContact(self, name: str):
        p =  self.findPosByName(name)
        if p == -1:
            return None
        return self.contacts[p]
    
    def rmContact(self, name: str):
        p = self.findPosByName(name)
        if p != -1:
            self.contacts.pop(p)








   




        














class Contato:
    
    def __init__(self, name: str=""):
        self.__nome : str  = name
        self.__favorited : bool = False
        self.__fones : list[Fone] = []

    def getNome(self):
        return self.__nome
    
    def setNome(self, nome: str):
        self.__nome = nome


    def getFavorited(self):
        return self.__favorited
    
    def setFavorited(self, value: bool):
        self.__favorited = value

    def getFones(self):
        return self.__fones


    def __str__(self):
        favorito = "@ " if self.__favorited else "- "
        lista = ", ".join([str(fone) for fone  in self.__fones])
        return f"{favorito}{self.__nome} [{lista}]"
    

    def addFone(self, id: str, number : str): 
        fone = Fone(id, number)
        if not fone.isValid():
            print("fail: invalid number")
            return 
        self.__fones.append(fone)
        


    def rmFone(self, index: int):
        if 0 <= index < len(self.__fones):
            self.__fones.pop(index)
        else:
            print("fail: invalid index")







    def isFavorited(self):
        return self.__favorited
    
    def toogleFavorited(self):
        self.__favorited = not self.isFavorited()

















class Fone:

    def __init__(self, id: str, number: str):
        self.id: str = id
        self.number : str = number

    def getId(self):
        return self.id
    
    def setId(self, value: str):
        self.id = value

    def getNumber(self):
        return self.number
    
    def setNumber(self, value: str):
        self.number = value

    def __str__(self):
        return f"{self.id}:{self.number}"

    
    def isValid(self):
        numeros = "0123456789()."
        for i in self.number:
                if i not in numeros:
                    return False

        return True
    

            



def main():
    agenda  = Agenda()

    while True:
        line = input()
        args = line.split()
        print("$" + line)



        if args[0] == "end":
            break

        elif args[0] == "add":
            name = args[1]
            fones = []
            for fn in args[2:]:
                id, num = fn.split(":")
                fones.append(Fone(id,num))
            agenda.addContact(name, fones)

        elif args[0] == "show":
            print(agenda)

        elif args[0] == "rm":
            agenda.rmContact(args[1])

        elif args[0] == "rmFone":






        






main()