import abjad


def test_scoretools_NoteHead___init___01():
    """
    Initialize note-head by number.
    """

    notehead = abjad.NoteHead(6)
    assert notehead.written_pitch == abjad.NamedPitch(6)


def test_scoretools_NoteHead___init___02():
    """
    Initialize note-head by LilyPond-style pitch string.
    """

    notehead = abjad.NoteHead('cs,,,')
    assert notehead.written_pitch == abjad.NamedPitch('cs,,,')


def test_scoretools_NoteHead___init___03():
    """
    Initialize note-head by other note-head instance.
    """

    notehead = abjad.NoteHead(6)
    new = abjad.NoteHead(notehead)

    assert notehead is not new
    assert notehead.written_pitch == 6
    assert new.written_pitch == 6


def test_scoretools_NoteHead___init___04():
    """
    Initialize note-head with tweak pais.
    """

    note_head = abjad.NoteHead("cs''", tweaks=[('color', 'red')])

    assert format(note_head) == "\\tweak color #red\ncs''"
