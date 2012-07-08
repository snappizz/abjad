from experimental.selectortools.CountRatioSelector import CountRatioSelector
from experimental.selectortools.SliceSelector import SliceSelector


class CountRatioSliceSelector(CountRatioSelector, SliceSelector):
    r'''.. versionadded:: 1.0

    Partition `reference` by `ratio` of counts. Then select zero or more contiguous parts.

        >>> from experimental import selectortools
        >>> from experimental import timespantools

    Select all background measures starting during segment ``'red'`` in ``'Voice 1'``.
    Then partition these measures ``1:1:1:1`` by their count.
    Then select the last two parts of this partition::

        >>> segment_selector = selectortools.SegmentSelector(index='red')
        >>> inequality = timespantools.expr_starts_during_timespan(timespan=segment_selector.timespan)
        >>> background_measure_selector = selectortools.BackgroundMeasureSliceSelector(inequality=inequality)

    ::

        >>> count_ratio_slice_selector = selectortools.CountRatioSliceSelector(
        ... background_measure_selector, (1, 1, 1, 1), start=-2)

    ::

        >>> z(count_ratio_slice_selector)
        selectortools.CountRatioSliceSelector(
            selectortools.BackgroundMeasureSliceSelector(
                inequality=timespantools.TimespanInequality(
                    timespantools.TimespanInequalityTemplate('t.start <= expr.start < t.stop'),
                    timespantools.Timespan(
                        selector=selectortools.SegmentSelector(
                            index='red'
                            )
                        )
                    )
                ),
            mathtools.Ratio(1, 1, 1, 1),
            start=-2
            )

    Count ratio slice selectors are immutable.
    '''

    ### INITIALIZER ###

    def __init__(self, reference, ratio, start=None, stop=None):
        CountRatioSelector.__init__(self, reference, ratio)
        SliceSelector.__init__(self, start=start, stop=stop)
