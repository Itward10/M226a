from ProductInCart import ProductInCart

class ShoppingCart:     #Klasse ShoppingCart
    products = []       #Liste = []

    def add(self, prc:ProductInCart): #add Methoden 

        isAlreadyInCart = False
        for p in self.products:     # Geht die Produktliste durch
            if(prc.product.number == p.product.number):     #Vergleicht die Produkte mit dem neuen
                p.amount = p.amount + prc.amount            #Wenn das Produkt schon exestiert, dann wird die Anzahl erhöht
                isAlreadyInCart = True


        if (isAlreadyInCart == False):  #Wenn es nicht exestiert
            self.products.append(prc)   #wird das Produkt hinzugefügt


    def getProducts(self):
        return self.products            #Produkte anzeigen
