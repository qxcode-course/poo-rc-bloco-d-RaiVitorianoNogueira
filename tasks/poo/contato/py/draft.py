class Contato:
    def __init__(self, name: str=""):
        self.__nome : str  = name
        self.__favorited : bool = False
        self.__fones : list[Fone] = []




    def __str__(self):
        lista = ", ".join([str(fone) for fone  in self.__fones])
        return f"- {self.__nome} [{lista}]"
    

    def addFone(self, id: str, number : str): 
        fone = Fone(id, (number))
        self.__fones.append(fone)

    def rmFone(self, index: int):
        self.__fones.pop(index)
            




    def isFavorited(self):
        return self.__favorited
    
    def toogleFavorited(self):
        self.__favorited = not self.isFavorited()

















class Fone:

    def __init__(self, id: str, number: str):
        self.id: str = id
        self.number : str = number



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