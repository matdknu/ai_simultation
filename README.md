# Gemelos digitales de encuestas longitudinales chilenas

Dos simulaciones basadas en agentes (ABM) calibradas con paneles reales. Cada una modela cómo **estructura social + contacto intergrupal** moldea actitudes en el tiempo.

```
ai_simulation/
├── ELSOC/          BarrioSim  — contacto migratorio → simpatía (ESOC 2016–2023)
└── ELRI/           WallmapuSim — conflicto mapuche–Estado (ELRI 2018–2023)
```

---

## La idea en una frase

No predecimos personas reales: **reproducimos la lógica estructural** del diseño muestral (vecindarios, composición étnica, olas panel) y proyectamos choques actitudinales sobre ese territorio.

---

## ELSOC — BarrioSim

**Pregunta:** ¿Cómo evoluciona la simpatía hacia migrantes cuando cambia la calidad del contacto?

| Capa | Fuente empírica |
|------|-----------------|
| Elasticidades contacto → simpatía | MLM panel ESOC (`r09`) |
| Trayectorias latentes | LCGA 4 clases (referencia venezolano) |
| Espacio | Barrio abstracto + hubs migrantes |

```bash
cd ELSOC
python app.py              # http://127.0.0.1:5050
python run.py integracion
```

**Escenarios:** línea base · integración · conflicto.

---

## ELRI — WallmapuSim

**Pregunta:** ¿Cómo justifican mapuche y no indígenas la fuerza estatal (`d3_1`) cuando el territorio es el del diseño muestral real?

| Capa | Fuente empírica |
|------|-----------------|
| Unidad espacial | **UMP/manzana** del diseño ELRI (`UMP.dta`) |
| Composición étnica | Empírica por manzana (`tipo_hogar`) |
| Fondo territorial | Censo 2017 (% indígena) + chilemapas |
| Actitudes | Panel 4 olas (`d3_1`, `d4_2`) |

```bash
cd ELRI

# 1. Territorio (censo + UMP + geometría)
Rscript analysis/censo_elri_abm.R

# 2. App visual — mapa Chile D3, estética estrategia moderna
python app_wallmapu.py     # http://127.0.0.1:5001

# 3. Consola
python run_wallmapu.py estallido mixtas
```

**Escenarios:** línea base · estallido 2021 · endurecimiento 2023.

**Filtros territoriales:** todo Chile · La Araucanía · RM · solo manzanas mixtas.

![WallmapuSim — mapa Chile, UMPs y agentes por ola](docs/wallmapusim-ui.png)

### Qué ves en la UI

- Mapa real de Chile con comunas coloreadas por **% indígena (censo 2017)**
- UMPs como círculos sobre el territorio (composición ELRI)
- Agentes animados por manzana (forma = clase latente, color = `d3_1`)
- Onda de shock en ola 3 (estallido)
- Timeline + sparkline longitudinal

---

## Metodología compartida

1. **Panel longitudinal** → medias y trayectorias por grupo
2. **Clases latentes (LCGA)** → heterogeneidad no observada en actitudes
3. **ABM espacial** → contacto intergrupal modulado por composición del parche
4. **Shocks de escenario** → contrafactuales (integración, estallido, endurecimiento)

### Por qué UMP y no geolocalización exacta

ELRI no publica coordenadas de hogar. La UMP es la unidad que el estudio usó para el muestreo: respeta privacidad y preserva **estructura de vecindario real**.

---

## Requisitos

- Python 3.11+ (`flask`, `numpy`)
- R 4.x + `chilemapas`, `sf`, `haven`, `jsonlite` (solo para generar territorio)

Los datos (`UMP.dta`, `BBDD_ELRI_LONG.RData`) y scripts de análisis `.R`/`.py` están en `.gitignore` — se generan localmente.

---

## Estado del proyecto

| Componente | ELSOC | ELRI |
|------------|-------|------|
| ABM + web UI | ✅ BarrioSim | ✅ WallmapuSim |
| LCGA integrado | ✅ | 🔜 |
| Mapa territorial real | — | ✅ D3 + GeoJSON |
| MLM coeficientes | ✅ | 🔜 |
