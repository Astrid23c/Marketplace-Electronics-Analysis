import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS
import os
from diccionarioTech2 import jerarquia_total, diccionario_estados

# ==========================================
# 1. MOTORES DE PROCESAMIENTO
# ==========================================

def preparar_mapeo_maestro(arbol):
    """Aplana el diccionario jerárquico para búsquedas rápidas"""
    mapeo = []
    for cat, marcas in arbol.items():
        for marca, productos in marcas.items():
            for producto, modelos in productos.items():
                for nombre_modelo, tokens in modelos.items():
                    for t in tokens:
                        mapeo.append({
                            'token': t.lower(),
                            'categoria': cat, 'marca': marca, 
                            'producto': producto, 'modelo': nombre_modelo
                        })
    return sorted(mapeo, key=lambda x: len(x['token']), reverse=True)

BASE_MAESTRA = preparar_mapeo_maestro(jerarquia_total)

def clasificar_item(titulo):
    """Extrae jerarquía y estado de un título de Marketplace"""
    titulo = str(titulo).lower()
    res = {
        'Categoria': 'Otros', 'Marca': 'Otro/Genérico', 
        'Producto': 'Genérico', 'Modelo': 'No identificado',
        'Estado': 'Usado (No especificado)'
    }
    
    # 1. Detectar Estado
    for estado, keys in diccionario_estados.items():
        if any(k in titulo for k in keys):
            res['Estado'] = estado
            break
            
    # 2. Detectar Jerarquía (Greedy Match)
    for item in BASE_MAESTRA:
        if item['token'] in titulo:
            res.update({
                'Categoria': item['categoria'],
                'Marca': item['marca'],
                'Producto': item['producto'],
                'Modelo': item['modelo']
            })
            break
    return pd.Series(res)

def limpiar_precio(precio_str):
    """Limpia 'S/ 1,200' -> 1200"""
    try:
        p = str(precio_str).upper().replace('S/', '').replace(' ', '')
        num = re.sub(r'[^\d]', '', p)
        return int(num) if num else 0
    except: return 0

df = pd.read_csv("tech_lima_raw.csv")

# Limpieza 

df['Titulo'] = df['Titulo'].fillna('').astype(str).str.lower().str.strip()
df['Ubicacion'] = df['Ubicacion'].fillna('no especificada').astype(str).str.lower()
df['Titulo_Limpio'] = df['Titulo'].fillna('').str.lower().str.strip()
df['Precio_Num'] = df['Precio'].apply(limpiar_precio)

# Aplicar Clasificación Jerárquica (4 niveles + Estado)
print("🧠 Aplicando inteligencia de jerarquía...")
df_clasificado = df['Titulo_Limpio'].apply(clasificar_item)
df = pd.concat([df, df_clasificado], axis=1)


palabras_no_electronicas = [
    'twice', 'photobook', 'card', 'coleccionable', 'poster', 'kpop', 'bts',
    'plano', 'unifilar', 'construccion', 'obra', 'terreno', 'indeco',
    'servicio', 'reparacion', 'mantenimiento', 'clases', 'ropa', 'zapatilla', 
    'mueble', 'silla', 'escritorio', 'tubo', 'pvc', 'perfil', 'fierro', 
    'microscopio', 'twitters', 'automotriz', 'electricista', 'timbre',
    'calibre', 'npt', '3x6', '3x2', '4x4', '6mm', 'rollo', 'taza', 'jesus',
    's/', 'remate', 'compro', 'internet', 'tps', 'ecografo', 'ecógrafo', 
    'mindray', 'bioquimico', 'schneider', 'industrial', 'medico', 'bioquímico',
    'analizador', 'balanzas', '$', 'ventanilla', 'lima', 'broca', 'contador',
    'módulo', 'antiasalto', 'chapa', 'santiago', 'tintas', 'internet', 'corriente',
    'alquiler', 'reparación', 'carcasa', 'viaje', 'toner', 'monedero', 'kit', 'wifi',
    'cables', 'bulla', 'utp', 'parante', 'rubro', 'tinta', 'twitter', 'trípode', 
    'parante', 'disco', 'lente', 'funda', 'dragon', 'flotador', 'trípode', 'windows'  
]


df = df[~df['Titulo'].apply(lambda x: any(p in str(x) for p in palabras_no_electronicas))].copy()


    
    # Segmentación Tier
df['Segmento'] = df['Precio_Num'].apply(
        lambda x: 'Premium' if x > 3500 else ('Estándar' if x > 800 else 'Económico')
    )
    
    # Filtro de Calidad (Elimina basura de precios S/ 1 o estafas)
df_final = df[(df['Precio_Num'] > 50) & (df['Precio_Num'] < 25000)].copy()
    
def limpiar_distrito_inteligente(loc):
    loc = str(loc).lower().strip()
    if loc == 'no especificada' or loc == '':
        return 'Lima (Global)'
    
    # Separamos por la coma (Lima, Lm -> tomamos "Lima")
    partes = loc.split(',')
    distrito = partes[0].strip()
    
    # Limpieza de ruido común sin borrar el nombre del distrito
    ruido = ['peru', 'perú', 'provincia', 'distrito', 'departamento']
    for r in ruido:
        distrito = distrito.replace(r, '')
    
    # Si después de limpiar quedó vacío o es muy corto (ej. "Lm"), ponemos Lima
    distrito = distrito.strip().title()
    if len(distrito) <= 2 or distrito.lower() == 'lima':
        return 'Lima Centro'
        
    return distrito

df['Ubicacion'] = df['Ubicacion'].fillna('no especificada')

df['Distrito_Limpio'] = df['Ubicacion'].apply(limpiar_distrito_inteligente)

df_final['Distrito_Limpio'] = df_final['Ubicacion'].apply(limpiar_distrito_inteligente)    


# ==========================================
# ANÁLISIS ESTRATÉGICO DE PRECIOS
# ==========================================

# A. Filtrar solo Smartphones para la comparativa Apple vs Samsung
df_smartphones = df_final[df_final['Producto'] == 'Smartphone'].copy()

# B. Crear el reporte de Precio Promedio por Marca
reporte_marcas = df_smartphones.groupby('Marca')['Precio_Num'].agg(['mean', 'median', 'count']).reset_index()
reporte_marcas.columns = ['Marca', 'Precio_Promedio', 'Precio_Mediana', 'Total_Publicaciones']

# C. Crear el reporte detallado por Modelo (para comparar iPhone 13 vs Galaxy S23, etc.)
reporte_modelos = df_smartphones.groupby(['Marca', 'Modelo'])['Precio_Num'].mean().reset_index()
reporte_modelos = reporte_modelos.sort_values(by='Precio_Num', ascending=False)

# D. Guardar los reportes para usarlos en el Dashboard
reporte_marcas.to_csv("analisis_precios_marcas.csv", index=False, encoding='utf-8-sig')
reporte_modelos.to_csv("analisis_precios_modelos.csv", index=False, encoding='utf-8-sig')

print("✅ Reportes de precios generados exitosamente.")
    
# Exportación General        
  
df_final.to_csv("dataset_mkpfacebook_electronica_v2.csv", index=False, encoding='utf-8-sig')
print(f"📊 Registros finales procesados: {len(df_final)}")