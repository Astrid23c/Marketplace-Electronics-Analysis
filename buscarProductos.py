from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import StaleElementReferenceException # Importamos la excepción
import pandas as pd
import time
import random

def extraer_tecnologia_robusto():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    url = "https://www.facebook.com/marketplace/category/electronics"
    driver.get(url)
    
    print("Inicia sesión si es necesario. Esperando 15 segundos...")
    time.sleep(15)

    datos = []
    enlaces_vistos = set()

    for i in range(200): # Haremos 40 scrolls
        try:
            driver.execute_script("window.scrollBy(0, 1000);")
            time.sleep(random.uniform(3, 5))
            
            # Buscamos los contenedores de productos
            elementos = driver.find_elements(By.TAG_NAME, "a")
            
            for el in elementos:
                try:
                    # Intentamos obtener el enlace
                    href = el.get_attribute('href')
                    
                    if href and '/marketplace/item/' in href:
                        enlace_limpio = href.split('?')[0]
                        
                        if enlace_limpio not in enlaces_vistos:
                            texto = el.text
                            if texto and '\n' in texto:
                                lineas = texto.split('\n')
                                if len(lineas) >= 2:
                                    datos.append({
                                        "Precio": lineas[0],
                                        "Titulo": lineas[1],
                                        "Ubicacion": lineas[2] if len(lineas) > 2 else "N/A",
                                        "Enlace": enlace_limpio
                                    })
                                    enlaces_vistos.add(enlace_limpio)
                
                # SI EL ELEMENTO SE PIERDE, PASAMOS AL SIGUIENTE SIN MORIR
                except StaleElementReferenceException:
                    continue 
                except Exception:
                    continue

            print(f"Vuelta {i+1}: {len(datos)} productos encontrados...")

        except Exception as e:
            print(f"Error en el scroll: {e}")
            continue

    driver.quit()
    return pd.DataFrame(datos)

# Ejecución
df_tech = extraer_tecnologia_robusto()
if not df_tech.empty:
    df_tech.to_csv("tech_lima_raw.csv", index=False, encoding='utf-8-sig')
    print("✅ ¡Éxito! Datos guardados en tech_lima_raw.csv")
else:
    print("❌ No se recolectaron datos.")