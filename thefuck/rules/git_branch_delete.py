from thefuck import utils
from thefuck.utils import replace_argument
from thefuck.specific.git import git_support


@git_support
def match(command, settings):
    return ('branch -d' in command.script
            and 'If you are sure you want to delete it' in command.stderr)


@git_support
def get_new_command(command, settings):
    return replace_argument(command.script, '-d', '-D')
