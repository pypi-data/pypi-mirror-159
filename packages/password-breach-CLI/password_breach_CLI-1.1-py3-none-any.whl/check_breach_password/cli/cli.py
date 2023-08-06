import click
import os

command_files_location = os.path.join(os.path.dirname(__file__), "commands")
command_files = os.listdir(command_files_location)


# main class. should have 2 methods.
class CLI(click.MultiCommand):
    def list_commands(self, ctx):
        """
        Obtain the list of all the available commands
        :param ctx: Click context
        :return:List of commands
        """

        available_commands = []

        for command_file in command_files:
            # avoiding init and pycache
            if command_file.startswith("__init__") or not command_file.endswith(".py"):
                continue

            available_commands.append(command_file.split(".")[0])
        return sorted(available_commands)

    def get_command(self, ctx, name):
        """
           Get information for a specific command
           :param ctx: Click Context
           :param name: Command name
           :return: Information about the command
        """
        if name != "check":
            return

        ns = {}
        command_file_location = os.path.join(command_files_location, name + ".py")

        # creates a code object, evaluates it and add it to dictionary.
        with open(command_file_location) as f:
            code = compile(f.read(), command_file_location, "exec")
            eval(code, ns, ns)

        return ns["cli"]  # executes cli function of the module command_file_location


# entry point of the cli application. runs when you run without arguments
@click.command(cls=CLI)
def cli():
    """Commands to help manage the project"""
    pass
