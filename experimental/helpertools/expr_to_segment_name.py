def expr_to_segment_name(expr):
    r'''.. versionadded:: 1.0
    
    Change segment specification to segment name::

        >>> from experimental import *

    ::

        >>> template = scoretemplatetools.GroupedRhythmicStavesScoreTemplate(staff_count=1)
        >>> red_segment = specificationtools.SegmentSpecification(template, 'red')

    ::

        >>> red_segment
        SegmentSpecification('red')

    ::

        >>> helpertools.expr_to_segment_name(red_segment)
        'red'

    Leave string unchanged::

        >>> helpertools.expr_to_segment_name('red')
        'red'

    Raise exception on nonsegment, nonstring input.

    Return string.
    '''
    from experimental import specificationtools
    if isinstance(expr, specificationtools.SegmentSpecification):
        return expr.segment_name
    elif isinstance(expr, str):
        return expr
    else:
        raise Exception('{!r} is neither segment nor string.'.format(expr))
