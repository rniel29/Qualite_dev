# Rapport de scalabilité (forte)

## Données utilisées
Fichier source : resultat/resultats.csv (médianes sur 10 exécutions par point).

## Résumé par Ntot

### Ntot = 120000
| P | Temps médian (ns) | Speedup |
|---:|---:|---:|
| 1 | 8 651 450 | 1.00 |
| 2 | 10 417 050 | 0.83 |
| 4 | 11 029 600 | 0.78 |
| 8 | 9 169 050 | 0.94 |
| 12 | 7 640 450 | 1.13 |
| 24 | 7 523 800 | 1.15 |

**Observation :** pour un Ntot très faible, le coût fixe (overhead des threads/coordination) domine. Le speedup reste proche de 1.

### Ntot = 120000000
| P | Temps médian (ns) | Speedup |
|---:|---:|---:|
| 1 | 1 583 506 500 | 1.00 |
| 2 | 801 236 550 | 1.98 |
| 4 | 416 370 650 | 3.80 |
| 8 | 265 156 350 | 5.97 |
| 12 | 202 295 600 | 7.83 |
| 24 | 217 065 850 | 7.30 |

**Observation :** très bonne scalabilité jusqu’à 4–12 workers. À 24, le speedup diminue, suggérant saturation (coûts de synchro, contention, ou limites CPU).

### Ntot = 240000000
| P | Temps médian (ns) | Speedup |
|---:|---:|---:|
| 1 | 3 158 829 500 | 1.00 |
| 2 | 1 589 188 350 | 1.99 |
| 4 | 820 843 300 | 3.85 |
| 8 | 510 256 350 | 6.19 |
| 12 | 380 923 750 | 8.29 |
| 24 | 425 297 400 | 7.43 |

**Observation :** comportement similaire à Ntot=120000000, avec une bonne montée jusqu’à 12 workers, puis un plafond à 24.

## Conclusion
- **Faibles Ntot** : la parallélisation n’apporte pas de gain significatif (overhead dominant).
- **Ntot élevés** : scalabilité quasi-linéaire jusqu’à 4, puis encore bonne jusqu’à 12.
- **À 24 workers** : dégradation du speedup, indiquant une saturation des ressources ou des surcoûts de synchronisation.

## Recommandations
- Pour une **scalabilité forte**, fixer un **Ntot suffisant** (au moins 120 000 000 dans vos tests).
- Limiter le nombre de workers à **12** pour un bon compromis speedup/temps sur cette machine.
- Tester la **scalabilité faible** pour confirmer le comportement quand Ntot augmente avec P.
