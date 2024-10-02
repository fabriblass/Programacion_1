""" En una ferretería se quiere implementar un sistema que permita a los usuarios saber cuánto deberán
 pagar por la compra de lámparas de bajo consumo. Se tiene en cuenta que todas las lámparas cuestan $800.

A partir de la cantidad y marca de las lámparas compradas (solo se puede comprar una marca por vez)
se aplicará el siguiente descuento:

Si compra 6 o más  lámparas bajo consumo tiene un descuento del 50%. 

Si compra 5  lámparas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y
si es de otra marca el descuento es del 30%.

Si compra 4  lámparas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y
si es de otra marca el descuento es del 20%.

Si compra 3  lámparas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%,
si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.

Por otro lado, si el importe final con descuento suma más de $4000
se obtiene un descuento adicional de 5%.
Mostrar por pantalla: 
Marca, cantidad de lámparas, total a pagar sin descuento, el descuento obtenido si corresponde,
el descuento adicional (si corresponde) y el total a pagar con descuento. """

marca = " "
lamparas= 800
cantidad= 0
descuento_extra= 0
descuento= 0


cantidad=int(input("Ingrese la cantidad de lampareas "))
marca=input("Ingrese la marca de la lampara ( Argentinaluz, felipelamparas, otro) ").lower()
if cantidad>= 6:
    descuento = 0.5
elif cantidad== 5:
    if marca == "argentinaluz":
        descuento = 0.40
    else:
        descuento = 0.30
elif cantidad == 4:
    if marca == "argentinaluz" or marca == "felipelamparas":
        descuento=0.25
    else:
        descuento= 0.20
elif cantidad==3:
    if marca =="argentinaluz":
        descuento= 0.15
    elif marca== "felipelamparas":
        descuento= 0.10
    else:
        descuento=0.05
total= cantidad * lamparas
total_descuento= total *  (1- descuento)

if total>= 4000:
    descuento_extra= 0.5
    total_descuento *= (1 - descuento_extra)





print("La cantidad de lamparas compradas es de:" , cantidad )
print("La marca es:") + marca
print("Total a pagar sin descuento es:" , total)
print("El descuento es de la compra es de:" , descuento)
print("El descuneto extra es de: " , descuento_extra)
print("Descuento es:" , total_descuento )

    










