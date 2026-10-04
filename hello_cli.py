#!/usr/bin/env python3
"""
Hello CLI - Premier projet de la Forteresse.
Un script simple qui prend des arguments en ligne de commande.
"""

import argparse
import sys
from datetime import datetime


def parse_args():
    """Parse les arguments de la ligne de commande."""
    parser = argparse.ArgumentParser(
        description="Affiche un message personnalisé. Premier projet de la Forteresse YUAN.",
        epilog="Exemple: python hello_cli.py --name Fang --count 3 --verbose"
    )
    
    parser.add_argument(
        "--name", "-n",
        type=str,
        default="Monde",
        help="Le nom à saluer (défaut: Monde)"
    )
    
    parser.add_argument(
        "--count", "-c",
        type=int,
        default=1,
        help="Nombre de fois à répéter le message (défaut: 1)"
    )
    
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Affiche plus d'informations (mode bavard)"
    )
    
    return parser.parse_args()


def greet(name, verbose=False):
    """Génère le message de salutation."""
    message = f"Bonjour, {name} !"
    
    if verbose:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message += f" [Généré le {now}]"
    
    return message


def main():
    """Point d'entrée principal."""
    args = parse_args()
    
    if args.verbose:
        print(f"[INFO] Nom : {args.name}", file=sys.stderr)
        print(f"[INFO] Répétitions : {args.count}", file=sys.stderr)
        print(f"[INFO] Mode verbose : activé", file=sys.stderr)
        print("-" * 40, file=sys.stderr)
    
    message = greet(args.name, args.verbose)
    
    for i in range(args.count):
        print(f"{i+1}. {message}")
    
    if args.verbose:
        print("-" * 40, file=sys.stderr)
        print(f"[INFO] Terminé avec succès", file=sys.stderr)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
