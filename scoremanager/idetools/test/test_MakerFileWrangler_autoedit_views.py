# -*- encoding: utf-8 -*-
import os
from abjad import *
import scoremanager
score_manager = scoremanager.idetools.AbjadIDE(is_test=False)
views_file = os.path.join(
    score_manager._configuration.wrangler_views_directory,
    '__MakerFileWrangler_views__.py',
    )
metadata_file = os.path.join(
    score_manager._configuration.wrangler_views_directory,
    '__metadata__.py',
    )


def test_MakerFileWrangler_autoedit_views_01():

    with systemtools.FilesystemState(keep=[views_file, metadata_file]):
        os.remove(views_file)
        os.remove(metadata_file)
        input_ = "K va add _test add 'RedExampleScoreRhythmMaker.py'~in~:ds:"
        input_ += " add 'RedExampleScoreTemplate.py'~in~:ds: done"
        input_ += " ren _test _new_test"
        input_ += " _new_test rm 'RedExampleScoreRhythmMaker.py' done"
        input_ += " rm _new_test done q"
        score_manager._run(input_=input_)
        transcript = score_manager._transcript

    lines = [
        'Abjad IDE - maker files - views - _test (EDIT)',
        '',
        '      elements - add (add)',
        '      editing - done (done)',
        '',
        ]
    assert any(_.lines == lines for _ in transcript)

    lines = [
        'Abjad IDE - maker files - views - _test (EDIT)',
        '',
        "   1: 'RedExampleScoreRhythmMaker.py' in :ds:",
        '',
        '      elements - add (add)',
        '      elements - remove (rm)',
        '      editing - done (done)',
        '',
        ]
    assert any(_.lines == lines for _ in transcript)

    lines = [
        'Abjad IDE - maker files - views - _test (EDIT)',
        '',
        "   1: 'RedExampleScoreRhythmMaker.py' in :ds:",
        "   2: 'RedExampleScoreTemplate.py' in :ds:",
        '',
        '      elements - add (add)',
        '      elements - move (mv)',
        '      elements - remove (rm)',
        '      editing - done (done)',
        '',
        ]
    assert any(_.lines == lines for _ in transcript)

    lines = [
        'Abjad IDE - maker files - views (EDIT)',
        '',
        "   1: _test: 'RedExampleScoreRhythmMaker.py' in :ds:, 'RedExampleScoreTemplate.py' in :ds:",
        '',
        '      elements - add (add)',
        '      elements - remove (rm)',
        '      elements - rename (ren)',
        '      editing - done (done)',
        '',
        ]
    assert any(_.lines == lines for _ in transcript)

    lines = [
        'Abjad IDE - maker files - views (EDIT)',
        '',
        "   1: _new_test: 'RedExampleScoreRhythmMaker.py' in :ds:, 'RedExampleScoreTemplate.py' in :ds:",
        '',
        '      elements - add (add)',
        '      elements - remove (rm)',
        '      elements - rename (ren)',
        '      editing - done (done)',
        '',
        ]
    assert any(_.lines == lines for _ in transcript)

    lines = [
        'Abjad IDE - maker files - views - _new_test (EDIT)',
        '',
        "   1: 'RedExampleScoreRhythmMaker.py' in :ds:",
        "   2: 'RedExampleScoreTemplate.py' in :ds:",
        '',
        '      elements - add (add)',
        '      elements - move (mv)',
        '      elements - remove (rm)',
        '      editing - done (done)',
        '',
        ]
    assert any(_.lines == lines for _ in transcript)

    lines = [
        'Abjad IDE - maker files - views - _new_test (EDIT)',
        '',
        "   1: 'RedExampleScoreTemplate.py' in :ds:",
        '',
        '      elements - add (add)',
        '      elements - remove (rm)',
        '      editing - done (done)',
        '',
        ]
    assert any(_.lines == lines for _ in transcript)

    lines = [
        'Abjad IDE - maker files - views (EDIT)',
        '',
        "   1: _new_test: 'RedExampleScoreTemplate.py' in :ds:",
        '',
        '      elements - add (add)',
        '      elements - remove (rm)',
        '      elements - rename (ren)',
        '      editing - done (done)',
        '',
        ]
    assert any(_.lines == lines for _ in transcript)

    lines = [
        'Abjad IDE - maker files - views (EDIT)',
        '',
        '      elements - add (add)',
        '      editing - done (done)',
        '',
        ]
    assert any(_.lines == lines for _ in transcript)