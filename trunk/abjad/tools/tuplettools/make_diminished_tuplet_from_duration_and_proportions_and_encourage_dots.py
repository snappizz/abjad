def make_diminished_tuplet_from_duration_and_proportions_and_encourage_dots(
    duration, proportions, big_endian=True):
    r'''.. versionadded:: 2.0

    .. note:: Deprecate. Use ``tuplettools.make_tuplet_from_duration_and_proportions()`` instead.

    Make diminished tuplet from `duration` and `proportions` and encourage dots::

        >>> tuplettools.make_diminished_tuplet_from_duration_and_proportions_and_encourage_dots(
        ... Fraction(3, 16), [1, 1, 1, -1, -1])
        FixedDurationTuplet(3/16, [c'32., c'32., c'32., r32., r32.])

    Interpret nonassignable `proportions` according to `direction`::

        >>> tuplettools.make_diminished_tuplet_from_duration_and_proportions_and_encourage_dots(
        ... Fraction(3, 16), [5, -1, 5], big_endian=False)
        FixedDurationTuplet(3/16, [c'16..., r64., c'16...])

    Reduce `proportions` relative to each other.

    Interpret negative `proportions` as rests.

    Return fixed-duration tuplet.

    .. versionchanged:: 2.0
        renamed ``divide.duration_into_arbitrary_diminution_dotted()`` to
        ``tuplettools.make_diminished_tuplet_from_duration_and_proportions_and_encourage_dots()``.
    '''
    from abjad.tools.tuplettools._make_tuplet_from_duration_with_proportions_and_encourage_dots import \
        _make_tuplet_from_duration_with_proportions_and_encourage_dots

    return _make_tuplet_from_duration_with_proportions_and_encourage_dots(
        duration, proportions, 'diminution', big_endian=big_endian)
