# BarrioSim 🏘️

**Simulación de agentes generativos en una comunidad latinoamericana.**

Inspirado en *"Generative Agents: Interactive Simulacra of Human Behavior"*
(Park et al., 2023, Stanford), pero adaptado a escenarios sociológicos de un
barrio de LATAM. Los vecinos son agentes con personalidad y memoria que
deliberan, se influyen entre sí y toman decisiones colectivas usando un LLM
(Claude) como "cerebro".

---

## ¿Qué hace?

Pone a cinco vecinos arquetípicos de un barrio a enfrentar un conflicto
social. Cada uno razona con su propia personalidad, recuerda lo vivido y
reacciona a lo que dicen los demás. Al final votan, y el sistema entrega una
**lectura sociológica** del desenlace.

### Los 4 escenarios

| Escenario | Marco sociológico |
|---|---|
| 🏗️ **La constructora y el parque** | Activismo y movimientos sociales: dilema represión-movilización, free-riders (Olson), oportunidad política (Tarrow) |
| 💧 **Tres días sin agua** | Bienes comunes: tragedia de los comunes (Hardin) vs. gobernanza comunitaria (Ostrom), "guerras del agua" |
| 🗳️ **Elecciones de la junta vecinal** | Polarización afectiva, sesgo in-group/out-group |
| 📱 **El WiFi gratis del municipio** | Brecha digital, difusión de noticias falsas, dependencia de pantallas |

### Métricas que calcula en vivo

Cohesión, polarización, movilización, tensión y confianza institucional —
actualizadas ronda a ronda.

---

## Instalación (3 pasos)

```bash
# 1. Entra a la carpeta
cd barrio_sim

# 2. (Recomendado) crea un entorno virtual
python3 -m venv venv
source venv/bin/activate        # En Windows: venv\Scripts\activate

# 3. Instala dependencias
pip install -r requirements.txt
```

---

## Uso

### Opción A — Modo OFFLINE (sin API key, gratis)

Ideal para probar la mecánica sin gastar nada. Las respuestas son simuladas.
Ya viene activado por defecto.

```bash
# En el navegador:
python app.py
# Abre http://127.0.0.1:5000

# O en la consola:
python run.py parque      # o: agua / junta / wifi
```

### Opción B — Modo API real (con Claude)

Aquí los agentes **piensan de verdad** y el debate es rico y emergente.

```bash
# 1. Consigue tu API key en https://console.anthropic.com
# 2. Configúrala como variable de entorno:
export ANTHROPIC_API_KEY="sk-ant-..."     # Windows: setx ANTHROPIC_API_KEY "sk-ant-..."

# 3. Desactiva el modo offline:
export BARRIO_OFFLINE=false                # Windows: setx BARRIO_OFFLINE "false"

# 4. Corre igual que antes:
python app.py
```

---

## Estructura del proyecto

```
barrio_sim/
├── config.py            # API key, modelo, modo offline/online
├── app.py               # Servidor web (Flask + streaming en vivo)
├── run.py               # Runner de consola
├── requirements.txt
├── barrio/
│   ├── llm.py           # Conexión al modelo (Claude) + modo offline
│   ├── memory.py        # Flujo de memoria (recencia + importancia + relevancia)
│   ├── agent.py         # El agente: persona + memoria + atributos sociales
│   ├── scenarios.py     # Los 4 escenarios + reparto de vecinos
│   └── engine.py        # Motor: rondas, eventos, métricas, votación
└── frontend/
    └── index.html       # Interfaz web
```

---

## Cómo extenderlo

**Agregar un vecino nuevo:** añade un diccionario a la lista `VECINOS` en
`barrio/scenarios.py`. Define su `persona`, atributos y `memorias_iniciales`.

**Agregar un escenario:** añade una entrada a `ESCENARIOS` con su `marco`,
`opciones`, `rondas` y `eventos_dinamicos` (eventos que se inyectan en rondas
específicas para alterar la dinámica).

**Cambiar el modelo de memoria:** en `barrio/memory.py`, la relevancia usa
similitud de palabras (Jaccard). Puedes reemplazarla por embeddings reales
para mayor fidelidad, como en el paper original.

**Red social:** en `VECINOS`, el campo `red` define con qué vecinos tiene
vínculo cada agente. El motor usa esa red para el contagio de posturas
(`_aplicar_contagio_social` en `engine.py`).

---

## Notas

- En modo API, cada simulación completa cuesta unos pocos centavos de dólar
  (depende del modelo y la cantidad de rondas).
- El modo offline NO razona: solo prueba que la mecánica, el streaming y las
  métricas funcionen. Para ver comportamiento emergente real, usa la API.
- Inspirado académicamente en CS222 (Stanford) y el paper de Generative Agents.

---

*Hecho para explorar cómo las comunidades latinoamericanas enfrentan sus
conflictos — con todas sus tensiones, solidaridades y contradicciones.*
