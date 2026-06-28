# Cross the Wall

*Cruzar el muro. Cruzar el Wall.*

![Cross the Wall — simulación ELRI](docs/wallmapusim-ui.png)

---

Un modelo de agentes calibrado con el panel ELRI (2016–2023) sobre actitudes
intergrupales en el conflicto mapuche–Estado. Mapuche y no indígena, cuatro
olas, un estallido en el medio, territorio real.

El nombre tiene dos lecturas a propósito. Cruzar el muro: lo que pasa
— o no pasa — entre grupos que comparten el mismo espacio pero no siempre
el mismo mundo. El Wall de Wallmapu: el territorio donde ocurre todo esto
no es abstracto. Es el sur de Chile. Está en el mapa.

![UMP del diseño muestral ELRI — norte (izq.) → sur (der.)](docs/mapa_ump_puntos_horizontal.png)

**Cross the Wall** no predice personas. Reproduce la lógica estructural del
diseño muestral ELRI — manzanas reales, composición étnica empírica,
trayectorias latentes de actitud calibradas con los datos — y proyecta
qué habría pasado si el estallido social de 2019 hubiera sido más intenso,
más suave, o nunca hubiera ocurrido.

## Jugar

[![Muestra del juego — Cross the Wall](https://img.youtube.com/vi/NarVrjophkg/maxresdefault.jpg)](https://youtu.be/NarVrjophkg)

*Demo en video — [ver en YouTube](https://youtu.be/NarVrjophkg)*

```bash
cd crossthewall
pip install -r requirements.txt   # pygame, numpy
python main.py
```

Juego 2D vectorial: zona rural (mapuche) ↔ muro ↔ zona urbana (no indígena).
Elige tu grupo, camina con **WASD**, habla con NPCs con **E**, ajusta el shock
del estallido con **Tab** (panel ABM). Cuatro olas, ~30 s cada una.

| Tecla | Acción |
|-------|--------|
| WASD / flechas | Mover |
| E | Interactuar con NPC cercano |
| Tab | Panel parámetros ABM |
| P | Pausar |
