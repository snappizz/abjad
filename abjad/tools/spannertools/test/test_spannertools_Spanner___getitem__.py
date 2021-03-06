import abjad


def test_spannertools_Spanner___getitem___01():
    """
    Get at nonnegative index in spanner.
    """

    voice = abjad.Voice("{ c'8 d'8 } { e'8 f'8 } { g'8 a'8 }")
    leaves = abjad.select(voice).leaves()
    beam = abjad.Beam()
    abjad.attach(beam, leaves)

    assert format(voice) == abjad.String.normalize(
        r"""
        \new Voice
        {
            {
                c'8
                [
                d'8
            }
            {
                e'8
                f'8
            }
            {
                g'8
                a'8
                ]
            }
        }
        """
        )

    assert beam[0] is leaves[0]


def test_spannertools_Spanner___getitem___02():
    """
    Get at negative index in spanner.
    """

    voice = abjad.Voice("{ c'8 d'8 } { e'8 f'8 } { g'8 a'8 }")
    leaves = abjad.select(voice).leaves()
    beam = abjad.Beam()
    abjad.attach(beam, leaves)

    assert format(voice) == abjad.String.normalize(
        r"""
        \new Voice
        {
            {
                c'8
                [
                d'8
            }
            {
                e'8
                f'8
            }
            {
                g'8
                a'8
                ]
            }
        }
        """
        )

    assert beam[-1] is leaves[-1]


def test_spannertools_Spanner___getitem___03():
    """
    Get slice from spanner.
    """

    voice = abjad.Voice("{ c'8 d'8 } { e'8 f'8 } { g'8 a'8 }")
    leaves = abjad.select(voice).leaves()
    beam = abjad.Beam()
    abjad.attach(beam, leaves)

    assert format(voice) == abjad.String.normalize(
        r"""
        \new Voice
        {
            {
                c'8
                [
                d'8
            }
            {
                e'8
                f'8
            }
            {
                g'8
                a'8
                ]
            }
        }
        """
        )

    assert beam[-2:] == leaves[-2:]


def test_spannertools_Spanner___getitem___04():
    """
    Get all spanner components.
    """

    voice = abjad.Voice("{ c'8 d'8 } { e'8 f'8 } { g'8 a'8 }")
    leaves = abjad.select(voice).leaves()
    beam = abjad.Beam()
    abjad.attach(beam, leaves)

    assert format(voice) == abjad.String.normalize(
        r"""
        \new Voice
        {
            {
                c'8
                [
                d'8
            }
            {
                e'8
                f'8
            }
            {
                g'8
                a'8
                ]
            }
        }
        """
        )

    assert beam[:] == leaves[:]
