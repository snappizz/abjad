import sys


def run_abjad():
    """
    Runs Abjad.

    Returns none.
    """
    from abjad.tools import systemtools

    try:
        file_name = sys.argv[1]
    except IndexError:
        file_name = ''

    commands = (
        "import abjad;",
        "from abjad import *;",
        "print(abjad_configuration.get_abjad_startup_string());",
        )
    commands = ' '.join(commands)

    command = r'''python -i {} -c "{}"'''
    command = command.format(file_name, commands)
    systemtools.IOManager.spawn_subprocess(command)
