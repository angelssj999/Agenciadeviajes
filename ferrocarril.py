#programa sencillo de ferrocarril
def agencia_viajes():
    destino = "Acapulco"
    costo_pasajero = 320

    print("AGENCIA DE VIAJES")
    print("Destino",destino)
    pasajeros = int(input("Ingresa el numero de pasajeros: "))

    total_pagar = pasajeros + costo_pasajero

    print("\nRESUMEN DEL VIAJE")
    print("Destino:",destino)
    print("Pasajeros:",pasajeros)
    print("Costo por pasajero: $",costo_pasajero)
    print("Total a pagar: $",total_pagar)

agencia_viajes()