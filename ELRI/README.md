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
├── wallmapu/          # Motor ABM
├── frontend_wallmapu/ # Interfaz web del simulador
└── README.md
```

## WallmapuSim (ABM)

Simulación de agentes calibrada con trayectorias latentes de actitud. Escenarios contrafactuales del estallido (más intenso, más suave, sin estallido). Territorio real del sur de Chile.

## Scripts legacy (confianza Módulo C)

Variables alternativas de confianza intergrupal (`c2`, `c5`, confianza ingroup/outgroup) — pipeline paralelo al módulo de conflicto.
