import abjad


def test_spannertools_MeasuredComplexBeam___eq___01():
    """
    Spanner is strict comparator.
    """

    spanner_1 = abjad.MeasuredComplexBeam()
    spanner_2 = abjad.MeasuredComplexBeam()

    assert not spanner_1 == spanner_2
