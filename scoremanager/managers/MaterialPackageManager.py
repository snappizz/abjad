# -*- encoding: utf-8 -*-
import copy
import os
import shutil
import traceback
from abjad.tools import datastructuretools
from abjad.tools import mathtools
from abjad.tools import stringtools
from abjad.tools import topleveltools
from scoremanager import wizards
from scoremanager.managers.PackageManager import PackageManager


class MaterialPackageManager(PackageManager):
    r'''Material package manager.


    ..  container:: example

        ::

            >>> import os
            >>> configuration = scoremanager.core.ScoreManagerConfiguration()
            >>> session = scoremanager.core.Session()
            >>> path = os.path.join(
            ...     configuration.abjad_material_packages_directory_path,
            ...     'example_numbers',
            ...     )
            >>> manager = scoremanager.managers.MaterialPackageManager(
            ...     path=path,
            ...     session=session,
            ...     )
            >>> manager
            MaterialPackageManager('.../materials/example_numbers')

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_output_module_import_statements',
        )

    ### INTIALIZER ###

    def __init__(self, path=None, session=None):
        if path is not None:
            assert os.path.sep in path
        PackageManager.__init__(
            self,
            path=path,
            session=session,
            )
        self._output_module_import_statements = [
            self._abjad_import_statement,
            ]

    ### PRIVATE PROPERTIES ###

    @property
    def _breadcrumb(self):
        if self._session.is_in_score:
            return self._space_delimited_lowercase_name
        name = self._space_delimited_lowercase_name
        configuration = self._configuration
        annotation = configuration._path_to_storehouse_annotation(self._path)
        string = '{} ({})'
        string = string.format(name, annotation)
        return string

    @property
    def _definition_module_manager(self):
        from scoremanager import managers
        return managers.FileManager(
            path=self._definition_module_path,
            session=self._session,
            )

    @property
    def _definition_module_path(self):
        return os.path.join(self._path, 'definition.py')

    @property
    def _illustrate_module_manager(self):
        from scoremanager import managers
        return managers.FileManager(
            path=self._illustrate_module_path,
            session=self._session,
            )

    @property
    def _illustrate_module_path(self):
        return os.path.join(self._path, '__illustrate__.py')

    @property
    def _illustration_ly_file_manager(self):
        from scoremanager import managers
        return managers.FileManager(
            path=self._illustration_ly_file_path,
            session=self._session,
            )

    @property
    def _illustration_ly_file_path(self):
        return os.path.join(self._path, 'illustration.ly')

    @property
    def _illustration_pdf_file_manager(self):
        from scoremanager import managers
        return managers.FileManager(
            path=self._illustration_pdf_file_path,
            session=self._session,
            )

    @property
    def _illustration_pdf_file_path(self):
        return os.path.join(self._path, 'illustration.pdf')

    @property
    def _material_package_name(self):
        return os.path.basename(self._path)

    @property
    def _output_module_manager(self):
        from scoremanager import managers
        return managers.FileManager(
            path=self._output_module_path,
            session=self._session,
            )

    @property
    def _output_module_path(self):
        return os.path.join(self._path, 'output.py')

    @property
    def _score_package_manager(self):
        from scoremanager import managers
        score_path = self._configuration._path_to_score_path(self._path)
        return managers.ScorePackageManager(
            path=score_path,
            session=self._session,
            )

    @property
    def _user_input_module_manager(self):
        from scoremanager import managers
        return managers.FileManager(
            path=self._user_input_module_path,
            session=self._session,
            )

    @property
    def _user_input_module_path(self):
        return os.path.join(self._path, 'user_input.py')

    @property
    def _user_input_to_action(self):
        superclass = super(MaterialPackageManager, self)
        result = superclass._user_input_to_action
        result = result.copy()
        result.update({
            'dme': self.edit_definition_module,
            'dmrm': self.remove_definition_module,
            'dms': self.write_definition_module_stub,
            'dmi': self.interpret_definition_module,
            'ime': self.edit_illustrate_module,
            'imei': self.edit_and_interpret_illustrate_module,
            'imrm': self.remove_illustrate_module,
            'ims': self.write_illustrate_module_stub,
            'imi': self.interpret_illustrate_module,
            'lyi': self.interpret_illustration_ly,
            'lyrm': self.remove_illustration_ly,
            'lyro': self.view_illustration_ly,
            'ma': self.autoedit_output_material,
            'mi': self.illustrate_material,
            'omw': self.write_output_material,
            'omrm': self.remove_output_module,
            'omro': self.view_output_module,
            'pca': self.configure_autoeditor,
            'pdfrm': self.remove_illustration_pdf,
            'pdfo': self.view_illustration_pdf,
            'pra': self.remove_autoeditor,
            'ren': self.rename,
            'uid': self.remove_user_input_module,
            'uis': self.display_user_input_demo_values,
            'uit': self.toggle_user_input_values_default_status,
            'uimro': self.view_user_input_module,
            })
        return result

    ### PRIVATE METHODS ###

    def _can_make_output_material(self):
        if os.path.isfile(self._definition_module_path):
            return True
        return False

    @staticmethod
    def _check_output_material(material):
        return True

    def _execute_output_module(self):
        attribute_names = (self._material_package_name,)
        result = self._output_module_manager._execute(
            attribute_names=attribute_names,
            )
        if result and len(result) == 1:
            output_material = result[0]
            return output_material

    def _has_output_material_editor(self):
        if not os.path.isfile(self._definition_module_path):
            if not os.path.isfile(self._user_input_module_path):
                True
        return False

    def _get_output_material_editor(self, target):
        if target is None:
            return
        from scoremanager import iotools
        prototype = (datastructuretools.TypedList, list)
        if isinstance(target, prototype):
            class_ = iotools.ListEditor
        else:
            class_ = iotools.Editor
        editor = class_(session=self._session, target=target)
        return editor

    def _get_storage_format(self, expr):
        if hasattr(expr, '_make_storage_format_with_overrides'):
            return expr._make_storage_format_with_overrides()
        elif hasattr(expr, '_storage_format_specification'):
            return format(expr, 'storage')
        return repr(expr)

    def _handle_main_menu_result(self, result):
        assert isinstance(result, str)
        if result in self._user_input_to_action:
            self._user_input_to_action[result]()
        elif result == 'user entered lone return':
            pass
        else:
            raise ValueError(result)

    def _interpret_definition_module(self):
        if not os.path.isfile(self._definition_module_path):
            return
        result = self._definition_module_manager._execute(
            attribute_names=(self._material_package_name,),
            )
        if result:
            assert len(result) == 1
            result = result[0]
            return result

    def _make_illustrate_module_menu_section(self, menu):
        commands = []
        if os.path.isfile(self._illustrate_module_path):
            is_hidden = False
            string = 'illustrate module - edit'
            commands.append((string, 'ime'))
            string = 'illustrate module - edit & interpret'
            commands.append((string, 'imei'))
            string = 'illustrate module - interpret'
            commands.append((string, 'imi'))
            string = 'illustrate module - remove'
            commands.append((string, 'imrm'))
            string = 'illustrate module - stub'
            commands.append((string, 'ims'))
        else:
            is_hidden = True
            string = 'illustrate module - stub'
            commands.append((string, 'ims'))
        menu.make_command_section(
            is_hidden=is_hidden,
            menu_entries=commands,
            name='illustrate module',
            )

    def _make_illustration_ly_menu_section(self, menu):
        if not os.path.isfile(self._illustration_ly_file_path):
            return
        commands = []
        commands.append(('illustration ly - interpret', 'lyi'))
        commands.append(('illustration ly - remove', 'lyrm'))
        commands.append(('illustration ly - read only', 'lyro'))
        menu.make_command_section(
            menu_entries=commands,
            name='illustration ly',
            )

    def _make_illustration_pdf_menu_section(self, menu):
        commands = []
        if os.path.isfile(self._illustration_pdf_file_path):
            commands.append(('illustration pdf - remove', 'pdfrm'))
            commands.append(('illustration pdf - open', 'pdfo'))
        if commands:
            section = menu.make_command_section(
                menu_entries=commands,
                name='illustration pdf',
                )

    def _make_main_menu(self, name='material manager'):
        superclass = super(MaterialPackageManager, self)
        menu = superclass._make_main_menu(name=name)
        self._make_directory_menu_section(menu)
        self._make_illustrate_module_menu_section(menu)
        self._make_illustration_ly_menu_section(menu)
        self._make_illustration_pdf_menu_section(menu)
        self._make_initializer_menu_section(menu)
        self._make_material_definition_menu_section(menu)
        self._make_autoeditor_summary_menu_section(menu)
        self._make_metadata_menu_section(menu)
        self._make_material_menu_section(menu)
        self._make_metadata_module_menu_section(menu)
        self._make_output_module_menu_section(menu)
        self._make_package_configuration_menu_section(menu)
        self._make_sibling_asset_tour_menu_section(menu)
        try:
            section = menu['material summary']
            menu.menu_sections.remove(section)
            menu.menu_sections.insert(0, section)
        except KeyError:
            pass
        return menu

    def _make_material_definition_menu_section(self, menu):
        name = 'definition module'
        commands = []
        if os.path.isfile(self._definition_module_path):
            commands.append(('definition module - edit', 'dme'))
            commands.append(('definition module - interpret', 'dmi'))
            commands.append(('definition module - remove', 'dmrm'))
        else:
            commands.append(('definition module - stub', 'dms'))
        if commands:
            use_autoeditor = self._get_metadatum('use_autoeditor')
            menu.make_command_section(
                is_hidden=use_autoeditor,
                menu_entries=commands,
                name='definition module',
                )

    def _make_material_menu_section(self, menu):
        commands = []         
        if os.path.isfile(self._output_module_path):
            commands.append(('material - autoedit', 'ma'))
        if os.path.isfile(self._output_module_path):
            commands.append(('material - illustrate', 'mi'))
        if commands:
            menu.make_command_section(
                menu_entries=commands,
                name='material',
                )

    def _make_autoeditor_summary_menu_section(self, menu):
        if not self._get_metadatum('use_autoeditor'):
            if os.path.isfile(self._definition_module_path):
                return
            if os.path.isfile(self._user_input_module_path):
                return
            if not os.path.isfile(self._output_module_path):
                return
        output_material = self._execute_output_module()
        editor = self._get_output_material_editor(target=output_material)
        if not editor:
            return
        lines = editor._get_target_summary_lines()
        lines = lines or ['(empty)']
        section = menu.make_material_summary_section(lines=lines)
        return section

    def _make_output_material(self):
        return

    def _make_output_material_triple(self):
        result = self._retrieve_import_statements_and_output_material()
        import_statements, output_material = result
        body_string = '{} = {}'
        output_material_name = self._material_package_name
        output_material = self._get_storage_format(output_material)
        body_string = body_string.format(
            output_material_name,
            output_material,
            )
        return (import_statements, body_string, output_material)

    def _make_output_module_body_lines(self, output_material):
        if hasattr(output_material, '_storage_format_specification'):
            lines = format(output_material, 'storage').splitlines()
        else:
            lines = [repr(output_material)]
        lines = list(lines)
        lines[0] = '{} = {}'.format(self._material_package_name, lines[0])
        lines = [line + '\n' for line in lines]
        return lines

    def _make_output_module_menu_section(self, menu):
        if not os.path.isfile(self._initializer_file_path):
            return
        commands = []
        if os.path.isfile(self._output_module_path):
            commands.append(('output module - remove', 'omrm'))
            commands.append(('output module - read only', 'omro'))
        if self._can_make_output_material():
            commands.append(('output module - write', 'omw'))
        if commands:
            menu.make_command_section(
                menu_entries=commands,
                name='output module',
                )

    def _make_package_configuration_menu_section(self, menu):
        commands = []
        use_autoeditor = self._get_metadatum('use_autoeditor')
        if use_autoeditor:
            commands.append(('package - remove autoeditor', 'pra'))
        else:
            commands.append(('package - configure autoeditor', 'pca'))
        if commands:
            path = self._definition_module_path
            has_definition_module = os.path.isfile(path)
            menu.make_command_section(
                is_hidden=has_definition_module,
                menu_entries=commands,
                name='package configuration',
                )

    def _make_temporary_illustrate_module_lines(self):
        lines = []
        lines.append(self._unicode_directive)
        lines.append('import os')
        lines.append(self._abjad_import_statement)
        line = 'from output import {}'
        line = line.format(self._material_package_name)
        lines.append(line)
        if os.path.isfile(self._illustrate_module_path):
            lines.append('from illustrate import __illustrate__')
        lines.append('')
        lines.append('')
        if os.path.isfile(self._illustrate_module_path):
            line = 'lilypond_file = __illustrate__({})'
        else:
            line = 'lilypond_file = {}.__illustrate__()'
        line = line.format(self._material_package_name)
        lines.append(line)
        lines.append('file_path = os.path.abspath(__file__)')
        lines.append('directory_path = os.path.dirname(file_path)')
        line = "file_path = os.path.join(directory_path, 'illustration.pdf')"
        lines.append(line)
        lines.append("persist(lilypond_file).as_pdf(file_path)")
        return lines

    @staticmethod
    def _replace_in_file(file_path, old, new):
        with file(file_path, 'r') as file_pointer:
            new_file_lines = []
            for line in file_pointer.readlines():
                line = line.replace(old, new)
                new_file_lines.append(line)
        with file(file_path, 'w') as file_pointer:
            file_pointer.write(''.join(new_file_lines))

    def _retrieve_import_statements_and_output_material(self):
        attribute_names = (
            'output_module_import_statements',
            self._material_package_name,
            )
        result = self._definition_module_manager._execute(
            attribute_names=attribute_names,
            )
        return result

    def _run_first_time(self):
        if self._session.pending_user_input:
            pending_user_input = 'ma ' + self._session.pending_user_input
            self._session._pending_user_input = pending_user_input
        else:
            self._session._pending_user_input = 'ma'
        self._run()

    def _write_definition_module_stub(self, prompt=True):
        self.write_definition_module_stub()
        message = 'stub material definition written to disk.'
        self._io_manager.proceed(message, prompt=prompt)

    ### PUBLIC METHODS ###

    def autoedit_output_material(self):
        r'''Autoedits output material.

        Returns none.
        '''
        output_material = self._execute_output_module()
        if (hasattr(self, '_make_output_material') and
            output_material is None and
            self._make_output_material() and
            isinstance(self._make_output_material(), wizards.Wizard)
            ):
            editor = self._make_output_material(target=output_material)
        else:
            editor = self._get_output_material_editor(target=output_material)
        if not editor:
            return
        editor._run()
        if self._should_backtrack():
            return
        output_module_import_statements = self._output_module_import_statements
        if hasattr(self, '_make_output_module_body_lines'):
            body_lines = self._make_output_module_body_lines(editor.target)
        else:
            line = '{} = {}'
            target_repr = self._get_storage_format(
                editor.target)
            line = line.format(
                self._material_package_name,
                target_repr,
                )
            body_lines = [line]
        self.write_output_material(
            import_statements=output_module_import_statements,
            body_lines=body_lines,
            output_material=editor.target,
            )

    def configure_autoeditor(self, prompt=True):
        r'''Configures autoeditor.

        Returns none.
        '''
        from scoremanager import iotools
        from scoremanager import managers
        selector = iotools.Selector(session=self._session)
        selector = selector.make_inventory_class_selector()
        class_ = selector._run()
        if not class_:
            return
        self._add_metadatum('use_autoeditor', True)
        self._add_metadatum('output_material_class_name', class_.__name__)
        empty_target = class_()
        if type(empty_target) is list:
            storage_format = repr(empty_target)
        else:
            storage_format = format(empty_target, 'storage')
        body_lines = '{} = {}'.format(
            self._package_name,
            storage_format,
            )
        body_lines = body_lines.split('\n')
        body_lines = [_ + '\n' for _ in body_lines]
        import_statements = [self._abjad_import_statement]
        if 'handlertools.' in storage_format:
            statement = 'from experimental.tools import handlertools'
            import_statements.append(statement)
        if ' makers.' in storage_format:
            statement = 'from scoremanager import makers'
            import_statements.append(statement)
        self.write_output_material(
            body_lines=body_lines,
            import_statements=import_statements,
            output_material=empty_target,
            prompt=False,
            )
        message = 'package configured for {} autoeditor.'
        message = message.format(class_.__name__)
        self._io_manager.proceed(message, prompt=prompt)

    def display_user_input_demo_values(self, prompt=True):
        r'''Displays user input demo values.

        Returns none.
        '''
        lines = []
        for i, (key, value) in enumerate(self.user_input_demo_values):
            line = '    {}: {!r}'.format(key.replace('_', ' '), value)
            lines.append(line)
        lines.append('')
        self._io_manager.display(lines)
        self._io_manager.proceed(prompt=prompt)

    def edit_and_interpret_illustrate_module(self):
        r'''Edits and then interprets illustrate module module.

        Returns none.
        '''
        self.edit_illustrate_module()
        self.interpret_illustrate_module()

    def edit_definition_module(self):
        r'''Edits material definition module.

        Returns none.
        '''
        file_path = self._definition_module_path
        self._io_manager.edit(file_path)

    def edit_illustrate_module(self):
        r'''Edits illustrate module module.

        Returns none.
        '''
        self._illustrate_module_manager.edit()

    def illustrate_material(self, prompt=True):
        r'''Illustrates material.

        Creates illustration.pdf and illustration.ly files.

        Returns none.
        '''
        from scoremanager import managers
        lines = self._make_temporary_illustrate_module_lines()
        contents = '\n'.join(lines)
        file_name = 'temporary_illustrate.py'
        path = os.path.join(self._path, file_name)
        manager = managers.FileManager(path=path, session=self._session)
        manager._write(contents)
        result = manager._interpret(prompt=False)
        manager._remove()
        if result:
            message = 'created illustration.pdf and illustration.ly files.'
            self._io_manager.proceed(message, prompt=prompt)

    def interpret_definition_module(self):
        r'''Runs Python on material definition module.

        Returns none.
        '''
        self._definition_module_manager._interpret()

    def interpret_illustrate_module(self, prompt=True):
        r'''Runs Python on illustrate module module.

        Returns none.
        '''
        self._illustrate_module_manager._interpret(prompt=prompt)

    def interpret_illustration_ly(self, prompt=True):
        r'''Calls LilyPond on illustration.ly file.

        Returns none.
        '''
        from scoremanager import managers
        path = self._illustration_ly_file_path
        if os.path.isfile(path):
            manager = managers.FileManager(path=path, session=self._session)
            manager.call_lilypond(prompt=prompt)
        else:
            message = 'illustration.ly file does not exist.'
            self._io_manager.proceed(message)

    def remove_autoeditor(self, prompt=True):
        r'''Removes autoeditor.

        Returns none.
        '''
        self._remove_metadatum('use_autoeditor')
        message = 'Removed autoeditor from package.'
        self._io_manager.proceed(message, prompt=prompt)

    def remove_definition_module(self, prompt=True):
        r'''Removes material definition module.

        Returns none.
        '''
        self._definition_module_manager.remove(prompt=prompt)
        self._session._is_backtracking_locally = False

    def remove_illustrate_module(self, prompt=True):
        r'''Removes illustrate module module.

        Returns none.
        '''
        self._illustrate_module_manager.remove(prompt=prompt)
        self._session._is_backtracking_locally = False

    def remove_illustration_ly(self, prompt=True):
        r'''Removes illustration ly.

        Returns none.
        '''
        self._illustration_ly_file_manager.remove(prompt=prompt)
        self._session._is_backtracking_locally = False

    def remove_illustration_pdf(self, prompt=True):
        r'''Removes illustration PDF.

        Returns none.
        '''
        self._illustration_pdf_file_manager.remove(prompt=prompt)
        self._session._is_backtracking_locally = False

    def remove_output_module(self, prompt=True):
        r'''Removes output module.

        Returns none.
        '''
        self._output_module_manager.remove(prompt=prompt)
        self._session._is_backtracking_locally = False

    def remove_user_input_module(self, prompt=True):
        r'''Removes user input module.

        Returns none.
        '''
        self._user_input_module_manager.remove(prompt=prompt)
        self._session._is_backtracking_locally = False

    def rename(self):
        r'''Renames material package.

        Returns none.
        '''
        base_name = os.path.basename(self._path)
        line = 'current name: {}'.format(base_name)
        self._io_manager.display(line)
        getter = self._io_manager.make_getter()
        getter.append_snake_case_package_name('new name')
        new_package_name = getter._run()
        if self._should_backtrack():
            return
        lines = []
        lines.append('current name: {}'.format(base_name))
        lines.append('new name:     {}'.format(new_package_name))
        lines.append('')
        self._io_manager.display(lines)
        if not self._io_manager.confirm():
            return
        old_directory_path = self._path
        new_directory_path = old_directory_path.replace(
            base_name,
            new_package_name,
            )
        is_in_git_repository, is_svn_versioned = False, False
        if self._is_in_git_repository():
            is_in_git_repository = True
            command = 'git mv {} {}'
        elif self._is_svn_versioned():
            is_svn_versioned = True
            command = 'svn mv {} {}'
        else:
            command = 'mv {} {}'
        command = command.format(self._path, new_directory_path)
        self._io_manager.spawn_subprocess(command)
        self._path = new_directory_path
        for directory_entry in os.listdir(new_directory_path):
            if directory_entry.endswith('.py'):
                file_path = os.path.join(new_directory_path, directory_entry)
                result = os.path.splitext(base_name)
                old_package_name, extension = result
                self._replace_in_file(
                    file_path,
                    old_package_name,
                    new_package_name,
                    )
        commit_message = 'Renamed material package.\n\n'
        commit_message += 'OLD: {!r}.\n\n'.format(old_package_name)
        commit_message += 'NEW: {!r}.'.format(new_package_name)
        if is_in_git_repository:
            command = 'git add -A {}'.format(new_directory_path)
            self._io_manager.spawn_subprocess(command)
            command = 'git commit -m "{}" {} {}'
            command = command.format(
                commit_message,
                new_directory_path,
                old_directory_path,
                )
            self._io_manager.spawn_subprocess(command)
        elif is_svn_versioned:
            parent_directory_path = os.path.dirname(self._path)
            command = 'svn commit -m "{}" {}'
            command = command.format(commit_message, parent_directory_path)
            self._io_manager.spawn_subprocess(command)
        self._session._is_backtracking_locally = True

    def toggle_user_input_values_default_status(self):
        r'''Toggles user input values default status.

        Returns none.
        '''
        self._session.toggle_user_input_values_default_status()

    def view_illustration_ly(self):
        r'''Views illustration LilyPond file.

        Returns none.
        '''
        self._illustration_ly_file_manager.view()

    def view_illustration_pdf(self):
        r'''Views illustration PDF.

        Returns none.
        '''
        self._illustration_pdf_file_manager.view()

    def view_output_module(self):
        r'''Views output module.

        Returns none.
        '''
        self._output_module_manager.view()

    def view_user_input_module(self):
        r'''Views user input module.

        Returns none.
        '''
        file_path = self._user_input_module_path
        self._io_manager.view(file_path)

    def write_definition_module_stub(self):
        r'''Writes stub material definition module.

        Returns none.
        '''
        lines = []
        lines.append(self._unicode_directive + '\n')
        lines.append(self._abjad_import_statement + '\n')
        lines.append('output_module_import_statements = []')
        lines.append('\n\n\n')
        line = '{} = None'.format(self._material_package_name)
        lines.append(line)
        lines = ''.join(lines)
        with file(self._definition_module_path, 'w') as file_pointer:
            file_pointer.write(lines)

    def write_illustrate_module_stub(self, prompt=True):
        r'''Writes stub illustrate module module.

        Returns none.
        '''
        material_package_name = self._package_name
        lines = []
        lines.append(self._abjad_import_statement + '\n')
        line = 'from {}.output import {}\n'
        line = line.format(material_package_path, material_package_name)
        lines.append(line)
        lines.append('\n')
        lines.append('\n')
        line = 'score, treble_staff, bass_staff ='
        line += ' scoretools.make_piano_score_from_leaves({})\n'
        line = line.format(material_package_name)
        lines.append(line)
        line = 'illustration = lilypondfiletools.'
        line += 'make_basic_lilypond_file(score)\n'
        lines.append(line)
        file_path = os.path.join(
            self._path,
            '__illustrate__.py',
            )
        with file(file_path, 'w') as file_pointer:
            file_pointer.write(''.join(lines))
        message = 'stub illustrate module written to disk.'
        self._io_manager.proceed(message, prompt=prompt)

    def write_output_material(
        self,
        import_statements=None,
        body_lines=None,
        output_material=None,
        prompt=True,
        ):
        r'''Writes output material.

        Returns none.
        '''
        if import_statements is None:
            assert body_lines is None
        else:
            assert isinstance(import_statements, list), repr(import_statements)
        if body_lines is None:
            assert import_statements is None
            assert output_material is None
        else:
            assert isinstance(body_lines, list), repr(body_lines)
            assert output_material is not None
        lines = []
        lines.append(self._unicode_directive + '\n')
        if body_lines is None:
            triple = self._make_output_material_triple()
            import_statements = triple[0]
            output_module_body_string = triple[1]
            output_material = triple[2]
            body_lines = [output_module_body_string]
        import_statements = import_statements or []
        if any('handlertools' in _ for _ in body_lines):
            statement = 'from experimental.tools import handlertools'
            import_statements.append(statement)
        if any(' makers.' in _ for _ in body_lines):
            statement = 'from scoremanager import makers'
            import_statements.append(statement)
        import_statements = [x + '\n' for x in import_statements]
        lines.extend(import_statements)
        lines.extend(['\n', '\n'])
        lines.extend(body_lines)
        contents = ''.join(lines)
        self._output_module_manager._write(contents)
        output_material_class_name = type(output_material).__name__
        self._add_metadatum('output_material_class_name', output_material_class_name)
        message = 'output module written to disk.'
        self._io_manager.proceed(message, prompt=prompt)