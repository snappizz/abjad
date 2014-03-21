# -*- encoding: utf-8 -*-
import os
from abjad import *
import scoremanager
configuration = scoremanager.core.ScoreManagerConfiguration()
score_manager = scoremanager.core.ScoreManager()


def test_DistributionDirectoryManager_add_to_repository_01():
    r'''Add two files to Git-managed distribution directory.
    Make sure Git recognizes the files as added.
    Then unadd the files and leave the distribution directory as found.
    '''

    manager = score_manager._find_up_to_date_versioned_manager(
        scoremanager.managers.DistributionDirectoryManager,
        configuration.abjad_score_packages_directory_path,
        infix='distribution',
        repository='git',
        )

    assert manager._test_add_to_repository()
    

def test_DistributionDirectoryManager_add_to_repository_02():
    r'''Add two files to Subversioned-managed score package.
    Make sure Subversion recognizes the files as added.
    Then unadd the file and leave the score package as found.
    '''

    manager = score_manager._find_up_to_date_versioned_manager(
        scoremanager.managers.DistributionDirectoryManager,
        configuration.user_score_packages_directory_path,
        infix='distribution',
        repository='svn',
        )
            
    if not manager:
        return

    assert manager._test_add_to_repository()