


PROTOCOLO = input("De que protocolo quieres consultar su distancia administrativa? ")

if PROTOCOLO == "ospf":
    print("La distancia administrativa de OSPF es de 110 ")
elif PROTOCOLO == "rip":
    print("La distancia administrativa de RIP es de 120 ")
elif PROTOCOLO == "eigrp":
    print("La distancia administrativa de EIGRP es de 90 ")       
elif PROTOCOLO == "bgp":
    print("La distancia administrativa de BGP es de 20 ")
else:
    print("este protocolo no está disponible")  
          