# -*- encoding: utf-8 -*-
import os
from abjad.tools.systemtools.AbjadConfiguration import AbjadConfiguration


class ScoreManagerConfiguration(AbjadConfiguration):
    r'''Score Manager configuration.

    ..  container:: example

        ::

            >>> score_manager = scoremanager.core.ScoreManager(is_test=True)
            >>> configuration = score_manager._configuration
            >>> configuration
            ScoreManagerConfiguration()

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_cache_file_path',
        )

    ### INITIALIZER ###

    def __init__(self):
        AbjadConfiguration.__init__(self)
        self._make_missing_directories()

    ### PRIVATE PROPERTIES ###

    @property
    def _initial_comment(self):
        return [
            '-*- coding: utf-8 -*-',
            '',
            'Score Manager tools configuration file created on {}.'.format(
                self._current_time),
            'This file is interpreted by ConfigObj'
            ' and should follow ini syntax.',
        ]

    def _get_option_definitions(self):
        #parent_options = AbjadConfiguration._get_option_definitions(self)
        options = {
            'score_manager_library': {
                'comment': [
                    '',
                    'Set to the directory where you'
                    ' house your score manager library.',
                    'Defaults to $HOME/score_manager_library/.',
                ],
                'spec': 'string(default={!r})'.format(
                    os.path.join(
                        self.home_directory,
                        'score_manager_library',
                        )
                    ),
            },
            'scores_directory': {
                'comment': [
                    '',
                    'Set to the directory where you house your scores.',
                    'Defaults to $HOME/scores/.'
                ],
                'spec': 'string(default={!r})'.format(
                    os.path.join(
                        self.home_directory,
                        'scores',
                        )
                    ),
            },
            'composer_full_name': {
                'comment': [
                    '',
                    'Set to full name of composer.',
                ],
                'spec': "string(default='Full Name')",
            },
            'composer_last_name': {
                'comment': [
                    '',
                    'Set to last name of composer.',
                ],
                'spec': "string(default='Name')",
            },
        }
        #parent_options.update(options)
        #return parent_options
        return options

    @property
    def _user_library_directory_name(self):
        directory = self.user_library_directory
        directory_name = os.path.split(directory)[-1]
        return directory_name

    ### PRIVATE METHODS ###

    def _make_missing_directories(self):
        directories = (
            self.user_library_directory,
            self.user_library_material_packages_directory,
            self.user_library_makers_directory,
            )
        for directory in directories:
            if not os.path.exists(directory):
                os.makedirs(directory)
                file_path = os.path.join(directory, '__init__.py')
                with open(file_path, 'w') as file_pointer:
                    file_pointer.write('')
        directories = (
            self.user_score_packages_directory,
            self.user_library_stylesheets_directory,
            self.transcripts_directory,
            )
        for directory in directories:
            if not os.path.exists(directory):
                os.makedirs(directory)

    def _path_to_score_path(self, path):
        if path.startswith(self.user_score_packages_directory):
            prefix_length = len(self.user_score_packages_directory)
        elif path.startswith(self.example_score_packages_directory):
            prefix_length = len(self.example_score_packages_directory)
        else:
            return
        path_prefix = path[:prefix_length]
        path_suffix = path[prefix_length+1:]
        score_name = path_suffix.split(os.path.sep)[0]
        score_path = os.path.join(path_prefix, score_name)
        return score_path

    def _path_to_storehouse(self, path):
        is_in_score = False
        if path.startswith(self.user_score_packages_directory):
            is_in_score = True
            prefix_length = len(self.user_score_packages_directory)
        elif path.startswith(self.example_score_packages_directory):
            is_in_score = True
            prefix_length = len(self.example_score_packages_directory)
        elif path.startswith(self.user_library_directory):
            prefix_length = len(self.user_library_directory)
        elif path.startswith(self.abjad_stylesheets_directory):
            return self.abjad_stylesheets_directory
        else:
            message = 'unidentifiable path: {!r}.'
            message = message.format(path)
            raise Exception(message)
        path_prefix = path[:prefix_length]
        remainder = path[prefix_length+1:]
        path_parts = remainder.split(os.path.sep)
        assert 1 <= len(path_parts)
        if is_in_score:
            path_parts = path_parts[:2]
        else:
            assert 1 <= len(path_parts)
            path_parts = path_parts[:1]
        storehouse_path = os.path.join(path_prefix, *path_parts)
        return storehouse_path

    def _path_to_storehouse_annotation(self, path):
        import scoremanager
        score_path = self._path_to_score_path(path)
        if score_path:
            session = scoremanager.core.Session
            manager = scoremanager.managers.ScorePackageManager(
                path=score_path,
                session=session,
                )
            title = manager._get_title()
            return title
        elif path.startswith(self.user_library_directory):
            return self.composer_last_name
        elif path.startswith(self.abjad_root_directory):
            return 'Abjad'
        else:
            message = 'path in unknown storehouse: {!r}.'
            message = message.format(path)
            raise ValueError(path)

    ### PUBLIC PROPERTIES ###

    @property
    def abjad_makers_directory(self):
        r'''Gets Abjad makers directory.

        ..  container:: example

            ::

                >>> configuration.abjad_makers_directory
                '.../scoremanager/makers'

        Returns string.
        '''
        path = os.path.join(
            self.score_manager_directory,
            'makers',
            )
        return path

    @property
    def abjad_material_packages_directory(self):
        r'''Gets Abjad material packages directory.

        ..  container:: example

            ::

                >>> configuration.abjad_material_packages_directory
                '.../scoremanager/materials'

        Returns string.
        '''
        path = os.path.join(
            self.score_manager_directory,
            'materials',
            )
        return path

    @property
    def abjad_score_package_names(self):
        r'''Gets Abjad score package names.

        ..  container:: example

            ::

                >>> for x in configuration.abjad_score_package_names:
                ...     x
                'blue_example_score'
                'etude_example_score'
                'red_example_score'

        Returns tuple of strings.
        '''
        return (
            'blue_example_score',
            'etude_example_score',
            'red_example_score',
            )

    @property
    def abjad_stylesheets_directory(self):
        r'''Gets Abjad stylesheets directory.

        ..  container:: example

            ::

                >>> configuration.abjad_stylesheets_directory
                '.../abjad/stylesheets'

        Returns string.
        '''
        path = os.path.join(
            self.abjad_directory,
            'stylesheets',
            )
        return path

    @property
    def boilerplate_directory(self):
        r'''Gets boilerplate directory.

        ..  container:: example

            >>> configuration.boilerplate_directory
            '.../scoremanager/boilerplate'

        Returns string.
        '''
        path = os.path.join(
            self.score_manager_directory,
            'boilerplate',
            )
        return path

    @property
    def cache_file_path(self):
        r'''Gets cache file path.

        ..  container:: example

            ::

                >>> configuration.cache_file_path
                '.../.score_manager/cache.py'

        Returns string.
        '''
        file_path = self._cache_file_path = os.path.join(
            self.configuration_directory,
            'cache.py',
            )
        return file_path

    @property
    def composer_full_name(self):
        r'''Gets composer full name.

        ..  container:: example

            ::

                >>> configuration.composer_full_name
                '...'

        Aliases `composer` setting in score manager configuration
        file.

        Returns string.
        '''
        return self._settings['composer_full_name']

    @property
    def composer_last_name(self):
        r'''Gets composer last name.

        ..  container:: example

            ::

                >>> configuration.composer_last_name
                '...'

        Aliases `composer` setting in score manager configuration
        file.

        Returns string.
        '''
        return self._settings['composer_last_name']

    @property
    def configuration_directory(self):
        r'''Gets configuration directory.

        ..  container:: example

            ::

                >>> configuration.configuration_directory
                '.../.score_manager'

        Defaults to path of hidden ``.score_manager`` directory.

        Returns string.
        '''
        return os.path.join(self.home_directory, '.score_manager')

    @property
    def configuration_file_name(self):
        r'''Gets configuration file name.

        ..  container:: example

            ::

                >>> configuration.configuration_file_name
                'score_manager.cfg'

        Returns string.
        '''
        return 'score_manager.cfg'

    @property
    def configuration_file_path(self):
        r'''Gets configuration file path.

        ..  container:: example

            ::

                >>> configuration.configuration_file_path
                '.../.score_manager/score_manager.cfg'

        Returns string.
        '''
        #superclass = super(ScoreManagerConfiguration, self)
        #return superclass.configuration_file_path
        return os.path.join(
            self.configuration_directory,
            self.configuration_file_name,
            )

    @property
    def example_score_packages_directory(self):
        r'''Gets Abjad score packages directory.

        ..  container:: example

            ::

                >>> configuration.example_score_packages_directory
                '.../scoremanager/scores'

        Returns string.
        '''
        path = os.path.join(
            self.score_manager_directory,
            'scores',
            )
        return path

    @property
    def handler_tools_directory(self):
        r'''Gets handler tools directory.

        ..  container:: example

            ::

                >>> configuration.handler_tools_directory
                '.../experimental/tools/handlertools'

        Returns string.
        '''
        path = os.path.join(
            self.abjad_experimental_directory,
            'tools',
            'handlertools',
            )
        return path

    @property
    def home_directory(self):
        r'''Gets home directory.

        ..  container:: example

            ::

                >>> configuration.home_directory
                '...'

        Returns string.
        '''
        superclass = super(ScoreManagerConfiguration, self)
        return superclass.home_directory

    @property
    def transcripts_directory(self):
        r'''Gets score manager transcripts directory.

        ..  container:: example

            ::

                >>> configuration.transcripts_directory
                '.../.score_manager/transcripts'

        Returns string.
        '''
        path = os.path.join(
            self.configuration_directory,
            'transcripts',
            )
        return path

    @property
    def unicode_directive(self):
        r'''Gets Unicode directive.

        ..  container:: example

            ::

                >>> configuration.unicode_directive
                '# -*- encoding: utf-8 -*-'

        Returns string.
        '''
        return '# -*- encoding: utf-8 -*-'

    @property
    def user_library_directory(self):
        r'''Gets user library directory.

        ..  container:: example

            ::

                >>> configuration.user_library_directory
                '...'

        Aliases `score_manager_library` setting in score manager configuration
        file.

        Returns string.
        '''
        path = self._settings['score_manager_library']
        path = os.path.expanduser(path)
        path = os.path.normpath(path)
        return path

    @property
    def user_library_makers_directory(self):
        r'''Gets user library makers path.

        ..  container:: example

            ::

                >>> configuration.user_library_makers_directory
                '.../makers'

        Returns string.
        '''
        path = os.path.join(
            self.user_library_directory,
            'makers',
            )
        return path

    @property
    def user_library_material_packages_directory(self):
        r'''Gets user library material packages directory.

        ..  container:: example

            ::

                >>> configuration.user_library_material_packages_directory
                '.../materials'

        Returns string.
        '''
        path = os.path.join(
            self.user_library_directory,
            'materials',
            )
        return path

    @property
    def user_library_stylesheets_directory(self):
        r'''Gets user library stylesheets directory.

        ..  container:: example

            ::

                >>> configuration.user_library_stylesheets_directory
                '.../stylesheets'

        Returns string.
        '''
        path = os.path.join(
            self.user_library_directory,
            'stylesheets',
            )
        return path

    @property
    def user_score_packages_directory(self):
        r'''Gets user score packages directory.

        ..  container:: example

            ::

                >>> configuration.user_score_packages_directory
                '...'

        Aliases `scores_directory` setting in score manager configuration file.

        Returns string.
        '''
        path = self._settings['scores_directory']
        path = os.path.expanduser(path)
        path = os.path.normpath(path)
        return path

    @property
    def wrangler_views_directory(self):
        r'''Gets wrangler views directory.

        ..  container::

            >>> configuration.wrangler_views_directory
            '.../views'

        Defined equal to views/ subdirectory of score manager directory.

        Returns string.
        '''
        return os.path.join(self.configuration_directory, 'views')

    ### PUBLIC METHODS ###

    def list_score_directorys(
        self,
        abjad=False,
        user=False,
        ):
        r'''Lists score directorys.

        ..  container:: example

            Lists Abjad score directorys:

            ::

                >>> for x in configuration.list_score_directorys(
                ...     abjad=True,
                ...     ):
                ...     x
                '.../scoremanager/scores/blue_example_score'
                '.../scoremanager/scores/etude_example_score'
                '.../scoremanager/scores/red_example_score'

        Returns list.
        '''
        result = []
        if abjad:
            scores_directory = self.example_score_packages_directory
            directory_entries = sorted(os.listdir(scores_directory))
            for directory_entry in directory_entries:
                if directory_entry[0].isalpha():
                    directory = os.path.join(
                        scores_directory,
                        directory_entry,
                        )
                    package_path = self.path_to_package_path(
                        directory,
                        )
                    path = os.path.join(
                        self.example_score_packages_directory,
                        directory_entry,
                        )
                    result.append(path)
        if user:
            scores_directory = self.user_score_packages_directory
            directory_entries = sorted(os.listdir(scores_directory))
            for directory_entry in directory_entries:
                if directory_entry[0].isalpha():
                    package_path = directory_entry
                    path = os.path.join(
                        self.user_score_packages_directory,
                        directory_entry,
                        )
                    result.append(path)
        return result

    def path_to_package_path(self, path):
        r'''Changes `path` to package path.

        Returns string.
        '''
        if path is None:
            return
        assert isinstance(path, str), repr(path)
        path = os.path.normpath(path)
        if path.endswith('.py'):
            path = path[:-3]
        if path.startswith(
            self.example_score_packages_directory):
            prefix_length = len(self.example_score_packages_directory) + 1
        elif path.startswith(
            self.user_library_material_packages_directory):
            prefix_length = \
                len(self.user_library_material_packages_directory) + 1
            remainder = path[prefix_length:]
            if remainder:
                remainder = remainder.replace(os.path.sep, '.')
                result = '{}.{}'.format(
                    self._user_library_directory_name,
                    'material_packages',
                    remainder,
                    )
            else:
                result = '.'.join([
                    self._user_library_directory_name,
                    'material_packages',
                    ])
            return result
        elif path.startswith(
            self.abjad_material_packages_directory):
            prefix_length = len(self.abjad_root_directory) + 1
        elif path.startswith(self.score_manager_directory):
            prefix_length = \
                len(os.path.dirname(self.score_manager_directory)) + 1
        elif path.startswith(
            self.user_score_packages_directory):
            prefix_length = len(self.user_score_packages_directory) + 1
        elif path.startswith(
            self.user_library_stylesheets_directory):
            prefix_length = \
                len(os.path.dirname(
                self.user_library_stylesheets_directory)) + 1
        elif path.startswith(self.abjad_stylesheets_directory):
            prefix_length = len(self.abjad_root_directory) + 1
        else:
            message = 'can not change path to package path: {!r}.'
            raise Exception(message.format(path))
        package_path = path[prefix_length:]
        package_path = package_path.replace(os.path.sep, '.')
        return package_path
