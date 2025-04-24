print("Cambio de Divisas")
input("Presione una tecla para continuar...")

print("Bienvenido al programa de cambio de divisas")

# tasas de cambio
exchange_rates = {
    "USD_EUR": 0.85,
    "EUR_USD": 1.10,
    "DOP_USD": 1 / 62.50,
    "USD_DOP": 62.50,
    "EUR_DOP": 62.50 * 1.10,  
    "DOP_EUR": 1 / (62.50 * 1.10)  
}


def convert_currency(amount, rate):
    return amount * rate

# Menú de opciones
exchange_money = input(
    "Seleccione una opción:"
    "USD a EUR [1], EUR a USD [2], DOP a USD [3], USD a DOP [4], EUR a DOP [5], DOP a EUR [6]: "
)

if exchange_money == "1":
    print("Cambio de USD a EUR")
    usd = float(input("Ingrese la cantidad de USD a cambiar: "))
    eur = convert_currency(usd, exchange_rates["USD_EUR"])
    print(f"{usd} USD son {eur:.2f} EUR")

elif exchange_money == "2":
    print("Cambio de EUR a USD")
    eur = float(input("Ingrese la cantidad de EUR a cambiar: "))
    usd = convert_currency(eur, exchange_rates["EUR_USD"])
    print(f"{eur} EUR son {usd:.2f} USD")

elif exchange_money == "3":
    print("Cambio de DOP a USD")
    dop = float(input("Ingrese la cantidad de DOP a cambiar: "))
    usd = convert_currency(dop, exchange_rates["DOP_USD"])
    print(f"{dop} DOP son {usd:.2f} USD")

elif exchange_money == "4":
    print("Cambio de USD a DOP")
    usd = float(input("Ingrese la cantidad de USD a cambiar: "))
    dop = convert_currency(usd, exchange_rates["USD_DOP"])
    print(f"{usd} USD son {dop:.2f} DOP")

elif exchange_money == "5":
    print("Cambio de EUR a DOP")
    eur = float(input("Ingrese la cantidad de EUR a cambiar: "))
    dop = convert_currency(eur, exchange_rates["EUR_DOP"])
    print(f"{eur} EUR son {dop:.2f} DOP")

elif exchange_money == "6":
    print("Cambio de DOP a EUR")
    dop = float(input("Ingrese la cantidad de DOP a cambiar: "))
    eur = convert_currency(dop, exchange_rates["DOP_EUR"])
    print(f"{dop} DOP son {eur:.2f} EUR")

else:
    print("Opción no válida. Por favor, intente de nuevo.")