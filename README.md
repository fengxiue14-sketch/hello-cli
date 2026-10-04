# Hello CLI

Premier projet de la **Forteresse YUAN**.

## Objectif

Découvrir `argparse` (bibliothèque standard Python) pour créer des scripts en ligne de commande.

## Installation

Aucune dépendance externe (argparse est natif en Python 3.2+).

## Usage

```bash
python hello_cli.py --help
python hello_cli.py --name Fang
python hello_cli.py --name `Fang Yuan` --count 3
python hello_cli.py --name Delkrist --count 2 --verbose
```

## Options

| Option | Court | Description |
|--------|:-----:|-------------|
| `--name` | `-n` | Nom à saluer (défaut: Monde) |
| `--count` | `-c` | Nombre de répétitions (défaut: 1) |
| `--verbose` | `-v` | Mode bavard |
| `--help` | `-h` | Aide |

## Compétences acquises

- Utilisation de `argparse`
- Structure d'un script Python CLI
- Sortie standard vs erreur standard
- Fichiers Python typés (`#!/usr/bin/env python3`)

## Auteur

**FENG XIUE** — [GitHub](https://github.com/fengxiue14-sketch)

## Licence

MIT
