# Gasto catastrófico en México 

## Cómo reproducir el proyecto 

### 1. Clonar el repositorio 

```bash 
git clone https://github.com/anapparedesr/Gasto-catastrofico-en-Mexico
cd Gasto-catastrofico-en-Mexico 
```

### 2. Instalar el entorno con uv 

Para que tengamos las mismas versiones 

```bash
uv sync
```

### 3. Descarga de datos 

Utilizaremos la ENIGH 2024, especialmente los microdatos: "Principales variables por hogar" 

Es un resumen con información a nivel hogar, contiene las características de los hogares, los gastos e ingresos registrados trimestralmente. 

```bash
uv run python src/descargar_datos.py
```

### Estructura del repositorio

```
data/       # microdatos (ignorada por Git, cada quien la genera)
src/        # scripts del pipeline
outputs/    # tablas y figuras resultantes
docs/       # diccionario de variables y documentación relevante
notebooks/  # notebooks 
```