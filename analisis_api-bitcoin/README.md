# Análisis de Datos Históricos de Bitcoin

Este proyecto obtiene, procesa y visualiza datos históricos de precios de Bitcoin utilizando la API de [CoinGecko](https://www.coingecko.com/). Proporciona gráficos y análisis básicos para observar tendencias y patrones de precios.

---

## Características

1. **Obtención de datos históricos:**
   - Descarga datos de precios de Bitcoin en tiempo real desde la API de CoinGecko.
   - Los datos incluyen precios con marcas de tiempo para un período especificado.

2. **Transformación de datos:**
   - Procesa los datos para obtener valores OHLC (Open-High-Low-Close) necesarios para gráficos de velas japonesas.
   - Calcula indicadores técnicos, como una media móvil de 20 días.

3. **Visualización de datos:**
   - Gráfico de velas japonesas (Candlestick) para observar patrones diarios.
   - Gráfico de línea del precio de cierre.
   - Superposición de indicadores técnicos en los gráficos.

4. **Análisis descriptivo:**
   - Genera estadísticas básicas de los datos, como promedio, mínimos y máximos.

---

## Requisitos

Asegúrate de tener instalados los siguientes paquetes de Python:

- `requests`
- `pandas`
- `mplfinance`
- `matplotlib`


