from abjad import *


def test_scoretools_Chord_lilypond_format_01():
    r'''Format chord with one note head.
    '''

    chord = Chord("<cqs'>4")

    assert str(chord) == "<cqs'>4"
    assert chord.lilypond_format == "<cqs'>4"
    assert len(chord.note_heads) == 1
    assert len(chord.written_pitches) == 1


def test_scoretools_Chord_lilypond_format_02():
    r'''Format chord with LilyPond command mark.
    '''

    chord = Chord("<d' ef' e'>4")
    command = marktools.LilyPondCommandMark('glissando', 'right')
    attach(command, chord)

    assert chord.lilypond_format == "<d' ef' e'>4 \\glissando"


def test_scoretools_Chord_lilypond_format_03():
    r'''Format tweaked chord with LilyPond command mark.
    '''

    chord = Chord("<d' ef' e'>4")
    chord.note_heads[0].tweak.color = 'red'
    command = marktools.LilyPondCommandMark('glissando', 'right')
    attach(command, chord)

    assert testtools.compare(
        chord,
        r'''
        <
            \tweak #'color #red
            d'
            ef'
            e'
        >4 \glissando
        '''
        )

    assert inspect(chord).is_well_formed()
