
import click
from check_breach_password.check_breach import main


# tells click that the function will be a click command
@click.command()
@click.argument('passwords', nargs=-1)  # arguments to be supplied
def cli(passwords):
    """
    Reports how many times your password was leaked in a data breach.
    You can pass as many passwords as you want.\n
    Example: \n
    Command: breach facebook.com xvasafygvx \n
    facebook.com was found breached x times. You should consider changing your password.\n
    Congratulations! Your password xvasafygvx was not breached in any data leaks.

    :param passwords: Passwords to check for leakage in data breach
    :return: Subprocess call result
    """

    if len(passwords) == 0:
        print("Please pass at least one argument. Run breach check --help for more information")
        return

    print("Password is being Checked. Please wait.\n")
    main(list(passwords))


