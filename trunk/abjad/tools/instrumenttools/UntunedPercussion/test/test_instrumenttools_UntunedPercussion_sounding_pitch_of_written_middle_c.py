# -*- encoding: utf-8 -*-
from abjad import *


def test_instrumenttools_UntunedPercussion_sounding_pitch_of_written_middle_c_01():

    percussion = instrumenttools.UntunedPercussion()

    assert percussion.sounding_pitch_of_written_middle_c == "c'"
