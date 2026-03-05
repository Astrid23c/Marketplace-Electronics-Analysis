# Análisis de Mercado: Electrónica en Facebook Marketplace
Pipeline ETL y Dashboard de análisis de precios para el mercado de electrónica en Facebook Marketplace usando Python (Selenium) y Power BI

## Descripción
Este proyecto automatiza la extracción y clasificación de productos tecnológicos en Lima para identificar oportunidades de compra.

## Tecnologías utilizadas
* **Python**: Web Scraping con Selenium.
* **Pandas**: Limpieza y normalización de datos.
* **Power BI**: Modelado de datos (Star Schema) y visualización.

## Proceso (ETL)
1. **Extracción**: Scraper desarrollado en Selenium para navegar por Marketplace.
2. **Transformación**: Diccionario lógico en Python para clasificar marcas y modelos a partir de texto no estructurado.
3. **Carga**: Exportación a CSV y conexión con Power BI.

## Insights
1. Se detectó que la mayoría de los vendedores en Marketplace no especifican la marca en los campos estructurados, lo que resultó en un 52% de publicaciones clasificadas como "Otro/Genérico" (350 de 679 publicaciones).
2. La mayor oferta de dispositivos electrónicos se concentra en distritos específicos como La Victoria y Santiago de Surco, lo que indica los nodos principales de comercio de segunda mano en la ciudad.
3. Más del 90% de las publicaciones corresponden a artículos usados, confirmando que el Marketplace de Facebook es primordialmente un mercado de reventa y economía circular en el sector tecnológico.

## Nota de uso
El script incluye una pausa de 15 segundos (time.sleep(15)) al inicio para permitir que el usuario realice el inicio de sesión de forma manual en la ventana del navegador antes de comenzar la extracción. Esto garantiza la seguridad de las credenciales del usuario.
