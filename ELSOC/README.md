# BarrioSim — Contacto migratorio y simpatía (ESOC Chile)

ABM calibrado con el panel longitudinal **ESOC**: cómo el contacto con migrantes
(conocidos, amigos, frecuencia, calidad positiva/negativa) afecta la simpatía
intergrupal (`r09`), estimado con un **modelo multinivel** y simulado en 3 olas.

## Escenarios

| Escenario | Qué modela |
|---|---|
| **Línea base** | Contacto fluctúa al azar; contrafactual |
| **Integración** | Sube red, frecuencia y calidad positiva del contacto |
| **Conflicto** | Suben malas experiencias; baja calidad del contacto |

## Estructura

```
ELSOC/
├── analysis/     # Modelo multinivel y exportación de coeficientes (local)
├── data/         # Panel ESOC (local)
├── barrio/       # Motor ABM
├── frontend/     # Interfaz web del simulador
└── README.md
```

## Hallazgos empíricos (MLM, panel 3 olas)

- **Contacto positivo** (+0.32): predictor más fuerte de simpatía
- **Frecuencia** (+0.13) y **amigos migrantes** (+0.12): efectos positivos
- **Contacto negativo** (−0.11): erosiona actitudes
- Variación entre personas (intercepto aleatorio σ ≈ 0.43)

Datos: [Harvard Dataverse — ESOC Chile](https://dataverse.harvard.edu/api/access/datafile/10735184)
