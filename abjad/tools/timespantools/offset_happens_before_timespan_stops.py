def offset_happens_before_timespan_stops(
    timespan=None,
    offset=None,
    hold=False,
    ):
    """
    Makes time relation indicating that ``offset`` happens before ``timespan``
    stops.

    ..  container:: example

        >>> relation = abjad.timespantools.offset_happens_before_timespan_stops()
        >>> abjad.f(relation)
        abjad.timespantools.OffsetTimespanTimeRelation(
            inequality=abjad.timespantools.CompoundInequality(
                [
                    abjad.TimespanInequality('offset < timespan.stop'),
                    ],
                logical_operator='and',
                ),
            )

    Returns time relation or boolean.
    """
    from abjad.tools import timespantools

    inequality = timespantools.CompoundInequality([
        'offset < timespan.stop',
        ])

    time_relation = timespantools.OffsetTimespanTimeRelation(
        inequality,
        timespan=timespan,
        offset=offset)

    if time_relation.is_fully_loaded and not hold:
        return time_relation()
    else:
        return time_relation
