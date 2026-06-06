"""
run.py
======
Corre BarrioSim directamente en la consola, sin navegador.

Uso:
    python run.py parque
    python run.py agua
    python run.py junta
    python run.py wifi

Si no pasas escenario, corre 'parque' por defecto.
"""

import sys

from barrio.engine import Simulacion
from barrio.scenarios import ESCENARIOS


def main():
    clave = sys.argv[1] if len(sys.argv) > 1 else "parque"
    if clave not in ESCENARIOS:
        print(f"Escenario '{clave}' no existe.")
        print("Opciones:", ", ".join(ESCENARIOS.keys()))
        sys.exit(1)

    sim = Simulacion(clave)
    for ev in sim.correr():
        t = ev["tipo"]
        if t == "sistema":
            print(f"\n=== {ev['texto']} ===")
        elif t == "marco":
            print(f"\n[MARCO SOCIOLOGICO]\n{ev['texto']}\n")
        elif t == "ronda":
            print(f"\n----- {ev['texto']} -----")
        elif t == "evento":
            print(f"\n  >> EVENTO: {ev['texto']}\n")
        elif t == "intervencion":
            print(f"  {ev['nombre']} ({ev['emocion']}, postura {ev['postura']:+.2f}):")
            print(f"     \"{ev['accion']}\"")
            if ev.get("pensamiento"):
                print(f"     [piensa: {ev['pensamiento']}]")
        elif t == "metricas":
            print(f"\n  METRICAS -> cohesion {ev['cohesion']} | "
                  f"polarizacion {ev['polarizacion']} | "
                  f"mobilizacion {ev['mobilizacion']} | tension {ev['tension']}")
        elif t == "voto":
            print(f"  VOTO {ev['nombre']}: {ev['voto']}  ({ev['razon']})")
        elif t == "resultado":
            print("\n" + "=" * 50)
            print("RESULTADO FINAL")
            print("=" * 50)
            for op, n in ev["conteo"].items():
                print(f"  {n} voto(s) -> {op}")
            print(f"\n  GANADORA: {ev['ganadora']}")
            print(f"\n  INTERPRETACION:\n  {ev['interpretacion']}")


if __name__ == "__main__":
    main()
