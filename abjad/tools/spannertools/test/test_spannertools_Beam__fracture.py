import abjad


def test_spannertools_Beam__fracture_01():
    """
    This test shows that fracturing beyond the first leaf
    effectively does nothing except to replace an existing
    spanner with an identical new spanner.
    """

    staff = abjad.Staff("c'8 d'8 e'8 f'8 g'8 a'8 b'8 c''8")
    beam = abjad.Beam()
    abjad.attach(beam, staff[:4])
    beam._fracture(0, direction=abjad.Left)

    assert format(staff) == abjad.String.normalize(
        r"""
        \new Staff
        {
            c'8
            [
            d'8
            e'8
            f'8
            ]
            g'8
            a'8
            b'8
            c''8
        }
        """
        )

    assert abjad.inspect(staff).is_well_formed()


def test_spannertools_Beam__fracture_02():

    staff = abjad.Staff("c'8 d'8 e'8 f'8 g'8 a'8 b'8 c''8")
    beam = abjad.Beam()
    abjad.attach(beam, staff[:4])
    beam._fracture(1, direction=abjad.Left)

    assert format(staff) == abjad.String.normalize(
        r"""
        \new Staff
        {
            c'8
            [
            ]
            d'8
            [
            e'8
            f'8
            ]
            g'8
            a'8
            b'8
            c''8
        }
        """
        )

    assert abjad.inspect(staff).is_well_formed()


def test_spannertools_Beam__fracture_03():
    """
    This test shows that fracurting beyond the last leaf
    effectively does nothing except to replace an existing
    spanner with an identical new spanner.
    """

    staff = abjad.Staff("c'8 d'8 e'8 f'8 g'8 a'8 b'8 c''8")
    beam = abjad.Beam()
    abjad.attach(beam, staff[:4])
    beam._fracture(-1, direction=abjad.Right)

    assert format(staff) == abjad.String.normalize(
        r"""
        \new Staff
        {
            c'8
            [
            d'8
            e'8
            f'8
            ]
            g'8
            a'8
            b'8
            c''8
        }
        """
        )

    assert abjad.inspect(staff).is_well_formed()


def test_spannertools_Beam__fracture_04():

    staff = abjad.Staff("c'8 d'8 e'8 f'8 g'8 a'8 b'8 c''8")
    beam = abjad.Beam()
    abjad.attach(beam, staff[:4])
    beam._fracture(1, direction=abjad.Right)

    assert format(staff) == abjad.String.normalize(
        r"""
        \new Staff
        {
            c'8
            [
            d'8
            ]
            e'8
            [
            f'8
            ]
            g'8
            a'8
            b'8
            c''8
        }
        """
        )

    assert abjad.inspect(staff).is_well_formed()


def test_spannertools_Beam__fracture_05():
    """
    Fracture both sides of leaf.
    """

    staff = abjad.Staff("c'8 cs'8 d'8 ef'8 e'8 f'8 fs'8 g'8")
    beam = abjad.Beam()
    abjad.attach(beam, staff[:5])
    beam._fracture(2, direction=None)

    assert format(staff) == abjad.String.normalize(
        r"""
        \new Staff
        {
            c'8
            [
            cs'8
            ]
            d'8
            [
            ]
            ef'8
            [
            e'8
            ]
            f'8
            fs'8
            g'8
        }
        """
        )

    assert abjad.inspect(staff).is_well_formed()


def test_spannertools_Beam__fracture_06():
    """
    Fracture both sides of first leaf in spanner.
    """

    staff = abjad.Staff("c'8 cs'8 d'8 ef'8 e'8 f'8 fs'8 g'8")
    beam = abjad.Beam()
    abjad.attach(beam, staff[:5])
    beam._fracture(0, direction=None)

    assert format(staff) == abjad.String.normalize(
        r"""
        \new Staff
        {
            c'8
            [
            ]
            cs'8
            [
            d'8
            ef'8
            e'8
            ]
            f'8
            fs'8
            g'8
        }
        """
        )

    assert abjad.inspect(staff).is_well_formed()


def test_spannertools_Beam__fracture_07():
    """
    Fracture both sides of last leaf in spanner.
    """

    staff = abjad.Staff("c'8 cs'8 d'8 ef'8 e'8 f'8 fs'8 g'8")
    beam = abjad.Beam()
    abjad.attach(beam, staff[:5])
    beam._fracture(4, direction=None)

    assert format(staff) == abjad.String.normalize(
        r"""
        \new Staff
        {
            c'8
            [
            cs'8
            d'8
            ef'8
            ]
            e'8
            [
            ]
            f'8
            fs'8
            g'8
        }
        """
        )

    assert abjad.inspect(staff).is_well_formed()


def test_spannertools_Beam__fracture_08():
    """
    Fracture both sides of leaf with negative index.
    """

    staff = abjad.Staff("c'8 cs'8 d'8 ef'8 e'8 f'8 fs'8 g'8")
    beam = abjad.Beam()
    abjad.attach(beam, staff[:5])
    beam._fracture(-1, direction=None)

    assert format(staff) == abjad.String.normalize(
        r"""
        \new Staff
        {
            c'8
            [
            cs'8
            d'8
            ef'8
            ]
            e'8
            [
            ]
            f'8
            fs'8
            g'8
        }
        """
        )

    assert abjad.inspect(staff).is_well_formed()


def test_spannertools_Beam__fracture_09():
    """
    Fracture container spanner to the right of index 1.
    """

    staff = abjad.Staff(
        r"""
        {
            c'8
            cs'8
            d'8
            ef'8
        }
        {
            e'8
            f'8
            fs'8
            g'8
        }
        {
            af'8
            a'8
            bf'8
            b'8
        }
        """
        )

    leaves = abjad.select(staff).leaves()
    beam = abjad.Beam()
    abjad.attach(beam, leaves)
    original, left, right = beam._fracture(7, direction=abjad.Right)

    assert len(original) == 12
    assert len(left) == 8
    assert len(right) == 4

    assert format(staff) == abjad.String.normalize(
        r"""
        \new Staff
        {
            {
                c'8
                [
                cs'8
                d'8
                ef'8
            }
            {
                e'8
                f'8
                fs'8
                g'8
                ]
            }
            {
                af'8
                [
                a'8
                bf'8
                b'8
                ]
            }
        }
        """
        )
