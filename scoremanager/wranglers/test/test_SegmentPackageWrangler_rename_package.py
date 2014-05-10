# -*- encoding: utf-8 -*-
import os
from abjad import *
import scoremanager
score_manager = scoremanager.core.ScoreManager(is_test=True)


def test_SegmentPackageWrangler_rename_package_01():
    r'''Creates package. Renames package.
    '''

    path = os.path.join(
        score_manager._configuration.example_score_packages_directory_path,
        'red_example_score',
        'segments',
        'segment_04',
        )
    new_path = os.path.join(
        score_manager._configuration.example_score_packages_directory_path,
        'red_example_score',
        'segments',
        'renamed_segment_04',
        )

    with systemtools.FilesystemState(remove=[path, new_path]):
        input_ = 'red~example~score g new segment~04 q'
        score_manager._run(pending_input=input_)
        assert os.path.exists(path)
        input_ = 'red~example~score g ren segment~04 renamed_segment_04 y q'
        score_manager._run(pending_input=input_)
        assert not os.path.exists(path)
        assert os.path.exists(new_path)