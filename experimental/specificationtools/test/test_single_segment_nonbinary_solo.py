from abjad.tools import *
from experimental.specificationtools import helpers
from experimental.specificationtools import library
from experimental.specificationtools import ScoreSpecification


def test_single_segment_nonbinary_solo_01():
    '''Nonbinary division.
    '''

    specification = ScoreSpecification(scoretemplatetools.GroupedRhythmicStavesScoreTemplate(n=1))

    segment = specification.append_segment()
    segment.set_time_signatures(segment, [(4, 8), (3, 8)])
    segment.set_divisions(segment.v1, [(1, 5)])
    segment.set_rhythm(segment, library.tuplet_monads)

    score = specification.interpret()

    current_function_name = introspectiontools.get_current_function_name()
    helpers.write_test_output(score, __file__, current_function_name)

    assert score.format == helpers.read_test_output(__file__, current_function_name)
