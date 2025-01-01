import requests
import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt

# Función para obtener datos históricos de precios de una criptomoneda desde la API de CoinGecko
def obtener_datos_historicos(criptomoneda, vs_moneda, dias):
    url = f'https://api.coingecko.com/api/v3/coins/{criptomoneda}/market_chart'
    parametros = {
        'vs_currency': vs_moneda,
        'days': dias
    }
    respuesta = requests.get(url, params=parametros) # Enviar solicitud GET a la API
    datos = respuesta.json() # Convertir la respuesta en un diccionario JSON
    precios = datos['prices'] # Extraer los precios (timestamp y precio) del JSON devuelto por la API
    df = pd.DataFrame(precios, columns=['timestamp', 'precio']) # Crear un DataFrame de Pandas a partir de los precios
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms') # Convertir la columna 'timestamp' a formato de fecha y hora
    df.set_index('timestamp', inplace=True) # Establecer 'timestamp' como el índice del DataFrame
    return df # Devolver el DataFrame resultante

# Obtener los datos históricos de Bitcoin en USD para los últimos 30 días
df = obtener_datos_historicos('bitcoin', 'usd', 30)

# Agrupar los datos en intervalos diarios y calcular valores OHLC (Open-High-Low-Close)
df_candlestick = df['precio'].resample('D').ohlc()


# Graficar las velas japonesas utilizando mplfinance
mpf.plot(
    df_candlestick,               
    type='candle',                
    style='charles',              
    title='Bitcoin - Velas Japonesas', 
    ylabel='Precio (USD)'         
)

# Mostrar estadísticas descriptivas del DataFrame original
print(df.describe())

# Graficar el precio de cierre de Bitcoin en los últimos 30 días
plt.figure(figsize=(14, 7))
plt.plot(df.index, df['precio'], label='Precio de Cierre')
plt.title('Precio de Cierre de Bitcoin')
plt.xlabel('Fecha')
plt.ylabel('Precio (USD)')
plt.legend()
plt.show()

# Calcular indicadores técnicos (media móvil de 20 días)
df['Media_Movil_20'] = df['precio'].rolling(window=20).mean()

# Graficar el precio de cierre junto con la media móvil de 20 días
plt.figure(figsize=(14, 7))
plt.plot(df.index, df['precio'], label='Precio de Cierre')
plt.plot(df.index, df['Media_Movil_20'], label='Media Móvil 20 días', color='orange')
plt.title('Precio de Cierre de Bitcoin con Media Móvil de 20 Días')
plt.xlabel('Fecha')
plt.ylabel('Precio (USD)')
plt.legend()
plt.show()



