def conversor(montoacambiar,moneda):
    cotdiaria = float(input(f'¿En cuanto cotiza el {moneda} el día de hoy para compra?\n'))
    cambio = montoacambiar/cotdiaria
    print(f"Puedes comprar {round(cambio,2)} dolares ahora mismo, antes de que cambie la cotización")


conversor(float(input('¿Cuantos deseas cambiar?\n')),input('¿A que moneda necesitas cambiar?\n'))