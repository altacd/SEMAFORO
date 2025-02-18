import yfinance as yf
import time
import threading

semaforo = threading.Semaphore(2)  # Permite solo 2 hilos a la vez

def obtener_precio(accion):
    while True:
        with semaforo:  # Accede al recurso controlado
            stock = yf.Ticker(accion)
            precio = stock.history(period='1d').iloc[-1]['Close']
            print(f"{accion}: ${precio:.2f}")
        time.sleep(10)  # Espera 10 segundos antes de actualizar

if __name__ == "__main__":
    lista_acciones = ["AAPL", "GOOGL", "MSFT", "AMZN"]  # Lista de símbolos de acciones
    hilos = [threading.Thread(target=obtener_precio, args=(accion,)) for accion in lista_acciones]

    for hilo in hilos:
        hilo.start()

    for hilo in hilos:
        hilo.join()
