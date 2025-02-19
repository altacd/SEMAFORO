Monitor de Precios de Acciones con Semáforo en Python
📌 Descripción
Este proyecto es un script en Python que monitorea los precios de acciones en tiempo real utilizando la API de Yahoo Finance (yfinance). Para gestionar las solicitudes de datos de manera concurrente y evitar sobrecargas, se implementa el patrón de diseño de semáforo, lo que permite controlar cuántos hilos pueden acceder simultáneamente a la API.

🚀 Características
Obtiene precios de acciones en tiempo real.
Utiliza hilos (threading) para realizar múltiples consultas simultáneamente.
Implementa un semáforo (threading.Semaphore) para limitar el número de consultas concurrentes.
Se actualiza automáticamente cada 10 segundos.
