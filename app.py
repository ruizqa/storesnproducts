from Store import Store
from Product import Product

Tienda = Store("Tienda")
Galletas = Product("Galletas",1000,"Comestibles")
Pan = Product("Pan", 2000, "Comestibles" )
Papel = Product("Papel", 3000, "Utileria")


Galletas.print_info()
Pan.print_info()
Papel.print_info()


Tienda.add_product(Galletas).add_product(Pan).add_product(Papel)
Tienda.inflation(15)
Galletas.print_info()
Tienda.sell_product(Galletas.id)
print(f"En la tienda ahora hay {len(Tienda.products)} productos")

