# ELRI — Conflicto e ideología (2018–2023)

Análisis del panel **ELRI** sobre justificación de violencia en el conflicto entre el Estado chileno y pueblos originarios.

## Variables dependientes (Módulo D)

| Código | Nombre | Pregunta (resumida) | Escala |
|--------|--------|---------------------|--------|
| **`d3_1`** | Control estatal | ¿Se justifica fuerza de Carabineros vs protestas indígenas? | 1=Nunca … 5=Siempre |
| **`d4_2`** | Resguardo indígena | ¿Se justifica toma de terrenos por grupos indígenas? | 1=Nunca … 5=Siempre |

Códigos missing → NA: 88, 99, 8888, 9999.

## Muestra analítica

| Criterio | Detalle |
|----------|---------|
| **Identidad (`a1`, ola 1)** | 1 = Mapuche · 12 = No indígena |
| **Panel** | Participación en las **4 olas** (1, 2, 3, 4) |

## Geografía — UMP y manzana

El diseño muestral usa **UMP** (Unidad de Muestreo Primaria) como parche espacial del ABM: composición étnica empírica por manzana, cuatro olas, estallido social 2019 como shock contrafactual.

| Variable | Origen |
|----------|--------|
| `ump` | Cluster de muestreo |
| `manzana` | Subdivisión dentro de la UMP |
| `id_geo` | Identificador comuna–manzana–ump |

## Estructura del proyecto

```
ELRI/
├── analysis/          # Pipeline empírico (local)
├── data/              # Panel ELRI + UMP (local)
├── output/            # Tablas y figuras (local)
├── wallmapu/          # Motor ABM (Cross the Wall)
├── frontend_wallmapu/ # Interfaz web Cross the Wall
└── README.md
```

## Cross the Wall (ABM)

Simulación de agentes calibrada con trayectorias latentes de actitud. Escenarios contrafactuales del estallido (más intenso, más suave, sin estallido). Territorio real del sur de Chile.

## Modelo empírico — composición territorial y justificación de violencia

**Pregunta:** ¿Vivir en una UMP mixta, de mayoría mapuche o de mayoría no indígena se asocia con mayor justificación de violencia estatal (`d3_1`) o de resguardo indígena (`d4_2`)? ¿Eso depende de la identidad del encuestado?

### Composición del territorio (UMP)

A partir de `UMP.dta`, cada UMP se clasifica por proporción de hogares indígenas en el diseño muestral:

| Categoría | Criterio (`pct_mapuche` en la UMP) |
|-----------|-------------------------------------|
| Mayoría mapuche | ≥ 80 % |
| Mixta (contacto) | 20–80 % |
| Mayoría no indígena | < 20 % |

La variable es **time-invariant** (mismo `folio` → misma UMP en las 4 olas).

### Especificaciones en R

| Modelo | Idea | Cuándo usarlo |
|--------|------|----------------|
| **MLM — intercepto aleatorio por persona** | `y ~ composicion * grupo + ola + (1\|folio)` | Efecto fijo de territorio y grupo; correlación intra-persona |
| **MLM — clustering en UMP** | `y ~ composicion * grupo + ola + (1\|ump)` | Incertidumbre a nivel de parche espacial (diseño muestral) |
| **MLM — cruzado** | `y ~ … + (1\|folio) + (1\|ump)` | Ambos niveles de anidamiento |
| **Efectos fijos de ola** | `y ~ composicion * grupo + factor(ola)` | Tendencia común; no estima cambio individual |
| **TWFE (folio)** | `y ~ factor(ola) \| folio` | Solo evolución temporal; **no** identifica composición ni grupo (ambos invariantes en el tiempo) |

`d3_1` y `d4_2` se modelan por separado (violencia estatal vs. resguardo indígena). La interacción `composicion × grupo` permite contrastar si el territorio opera distinto para mapuche y no indígena.

**Nota metodológica:** composición y grupo son invariantes en el panel → no usar TWFE de persona para estimar esos efectos. El MLM con `(1|folio)` o `(1|ump)` es la vía principal; opcionalmente `ordinal::clmm` si se prefiere tratar la escala 1–5 como ordinal.

### Script

```bash
cd ELRI
Rscript analysis/07_mlm_composicion_conflicto.R
```

Requiere `02_muestra_conflicto.R` y `04_pegar_ump.R`. Escribe tablas y coeficientes en `output/`.

### Mapas descriptivos — manzanas por grupo

```bash
Rscript analysis/08_mapa_manzanas_grupo.R
```

Dos mapas horizontales — **solo UMP mixtas** (muestra espejo, 20–80 % hogares indígenas), mapuche vs. no indígena:

| Archivo | Muestra |
|---------|---------|
| `mapa_manzanas_grupo_4olas_horizontal.png` | Panel 4 olas · mixtas |
| `mapa_manzanas_grupo_ola1_horizontal.png` | Ola 1 · mixtas (sin exigir 4 olas) |
| `mapa_manzanas_grupo_comparado_horizontal.png` | Ambos lado a lado |

**Limitación:** en la muestra analítica casi todos los folios caen en UMP **mixtas** (diseño ELRI estratificado hacia territorio mapuche). Las celdas mayoría mapuche / mayoría no indígena son muy pequeñas → algunas interacciones quedan no identificadas (matriz de efectos fijos rank-deficient). Conviene reportar contrastes con `emmeans` y, si hace falta, colapsar mixtas en una sola categoría vs. homogénea.

## Scripts legacy (confianza Módulo C)

Variables alternativas de confianza intergrupal (`c2`, `c5`, confianza ingroup/outgroup) — pipeline paralelo al módulo de conflicto.
