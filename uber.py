#programa sencillo uber
def agencia_viajes():
    destino = "acapulco:"
    costo_pasajero = 420

    print("AGENCIA DE VIAJES")
    print("destino",destino)
    pasajeros = int(input("ingresa el numero de pasjeros: "))

    total_pagar = pasajeros + costo_pasajero

    print("\nRESUMEN DEL VIAJE")
    print("destino:",destino)
    print("pasajeros",pasajeros)
    print("costo por pasajero: $",costo_pasajero)
    print("total a pagar",total_pagar)

    agencia_viajes()
    print("total a pagar:$",total_pagar)

if __name__ =='__main__':
    app.run(debug=True)