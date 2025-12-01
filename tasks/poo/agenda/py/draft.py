class Agenda:
    def __init__(self, contacts: list[Contato]):
        self.contacts : list[Contato] = contacts


def addContato(self, name: str, fones: list[Fone]):
        self.contacts.append()














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
        fone = Fone(id, (number))
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
    contato = Contato()

    while True:
        line = input()
        args = line.split()
        print("$" + line)


        if args[0] == "init":
            contato = Contato(args[1])

        elif args[0] == "show":
            print(contato)

        elif args[0] == "add":
            contato.addFone(args[1],args[2])


        elif args[0] == "rm":
            contato.rmFone(int(args[1]))

        elif args[0] == "tfav":
            contato.toogleFavorited()


        elif args[0] == "end":
            break






main()