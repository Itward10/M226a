from productInstock import ProductInStock

class Stock:                        
    products = []                       #= [] Als Liste auf listen

    def add(self, pis:ProductInStock):  #Methode Add
        isAlreadyInStock = False 
        for p in self.products: # for .... durch alle self.products durchloopen
            if(pis.product.number == p.product.number ): #übprüft ob das Produkt schon in der Liste ist. pis neue Produkt p produkte in der liste
                isAlreadyInStock = True

        if  (isAlreadyInStock == False):
            self.products.append(pis)  #Produkt wird der Liste hinzugefügt
        else:
            print("It exist already")


    def getProducts(self):  #Methode anzeigen   
        return self.products #zeigt alle Produkte an


