"""
generátor hesla, uživatel si může vybrat zda heslo
* délka (6-20)
* může mít čísla
* speciální znaky, kterými jsou pouze jsou pouze #!_-$@
* malá i velká písmena
ve výchozím stavu vygeneruje pouze heslo jen z malých písmen
"""

import random
import click

alphabet = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"
spe_chars = "#!_-$@"


@click.command()
@click.option("--length", "-l", required=True, prompt="Délka hesla (6-20)", type=click.IntRange(6, 20),
              help="délka hesla v rozmezí 6-20 znaků")
@click.option("--numbers", "-n", is_flag=True, prompt="Použít v hesle čísla?", help="použít i čísla")
@click.option("--special", "-s", is_flag=True, prompt=f"Použít speciální znaky ({spe_chars})?",
              help=f"použít speciální znaky ({spe_chars})")
@click.option("--lower_upper", "-i", is_flag=True, prompt="Použít i velka písmena?",
              help="použít malá i velká písmena")
@click.help_option("-h", "--help")
def main(length: int, numbers: bool, special: bool, lower_upper: bool):
    """
    Program k vygenerování jednoduchého (ne)bezpečného hesla
    """
    index = alphabet
    if numbers:
        index += num
    if special:
        index += spe_chars
    if lower_upper:
        index += alphabet.upper()

    index = list(index)
    random.shuffle(index)  # pro jistotu zamíchá list

    result = ""
    for i in range(length):
        result += random.choice(index)

    print(result)
    if click.confirm(click.style("Zkopírovat výsledek do clipboard?", fg="bright_green", bold=True), default=True):
        import pyperclip
        pyperclip.copy(result)
        print("Zkopírováno!")


if __name__ == '__main__':
    main()
