import importlib
import inspect
import pathlib
from uqbar.cli import CLI, CLIAggregator


class AbjDevScript(CLIAggregator):
    '''
    Entry-point to the Abjad developer scripts catalog.

    Can be accessed on the commandline via `abj-dev` or `ajv`:

    ..  shell::

        ajv --help

    `ajv` supports subcommands similar to `svn`:

    ..  shell::

        ajv api --help

    '''

    ### CLASS VARIABLES ###

    config_name = '.abjadrc'
    short_description = 'Entry-point to Abjad developer scripts catalog.'

    ### SPECIAL METHODS ###

    @property
    def cli_classes(self):
        """
        Lists CLI classes for aggregation.
        """
        def scan_module(module):
            classes = []
            for name in dir(module):
                obj = getattr(module, name)
                if not isinstance(obj, type):
                    continue
                elif not issubclass(obj, CLI):
                    continue
                elif issubclass(obj, type(self)):
                    continue
                elif inspect.isabstract(obj):
                    continue
                classes.append(obj)
            return classes
        import abjad.cli
        classes = scan_module(abjad.cli)
        try:
            import abjadext  # type: ignore
            for abjadext_path in abjadext.__path__:
                abjadext_path = pathlib.Path(abjadext_path)
                for extension_path in abjadext_path.iterdir():
                    if (
                        extension_path.name.startswith(('.', '_')) or
                        not extension_path.is_dir() or
                        not (extension_path / '__init__.py').exists()
                    ):
                        continue
                    module_name = 'abjadext.{}'.format(extension_path.name)
                    module = importlib.import_module(module_name)
                    classes.extend(scan_module(module))
        except ImportError:
            pass
        classes.sort(key=lambda x: x.__name__)
        return classes
