from abjad.tools import contexttools
from abjad.tools import durationtools
from experimental import quantizationtools


def test_BeatwiseQSchema___getitem___01():

    schema = quantizationtools.BeatwiseQSchema()

    assert schema[0] == schema[1] == schema[2] == {
        'beatspan': durationtools.Duration(1, 4),
        'search_tree': quantizationtools.SearchTree(),
        'tempo': contexttools.TempoMark((1, 4), 60),
    }


def test_BeatwiseQSchema___getitem___02():

    item_a = quantizationtools.BeatwiseQSchemaItem(search_tree={2: None})
    item_b = quantizationtools.BeatwiseQSchemaItem(tempo=((1, 4), 76))
    item_c = quantizationtools.BeatwiseQSchemaItem(beatspan=(1, 8), search_tree={5: None})

    schema = quantizationtools.BeatwiseQSchema(
        {2: item_a, 4: item_b, 7: item_c},
        beatspan=durationtools.Duration(1, 32),
        search_tree={3: None},
        tempo=contexttools.TempoMark((1, 16), 36)
        )

    assert schema[0] == schema[1] == {
        'beatspan': durationtools.Duration(1, 32),
        'search_tree': quantizationtools.SearchTree({3: None}),
        'tempo': contexttools.TempoMark((1, 16), 36),
    }

    assert schema[2] == schema[3] == {
        'beatspan': durationtools.Duration(1, 32),
        'search_tree': quantizationtools.SearchTree({2: None}),
        'tempo': contexttools.TempoMark((1, 16), 36),
    }

    assert schema[4] == schema[5] == schema[6] == {
        'beatspan': durationtools.Duration(1, 32),
        'search_tree': quantizationtools.SearchTree({2: None}),
        'tempo': contexttools.TempoMark((1, 4), 76),
    }

    assert schema[7] == schema[8] == schema[1000] == {
        'beatspan': durationtools.Duration(1, 8),
        'search_tree': quantizationtools.SearchTree({5: None}),
        'tempo': contexttools.TempoMark((1, 4), 76),
    }
