import abjad


def test_spannertools_ComplexBeam___eq___01():
    """
    Spanner is strict comparator.
    """

    spanner_1 = abjad.ComplexBeam()
    spanner_2 = abjad.ComplexBeam()

    assert not spanner_1 == spanner_2
