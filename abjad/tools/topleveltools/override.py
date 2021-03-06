def override(argument):
    r"""
    Makes LilyPond grob name manager.

    ..  container:: example

        Overrides staff symbol color:

        >>> staff = abjad.Staff("c'4 e'4 d'4 f'4")
        >>> abjad.override(staff).staff_symbol.color = 'red'
        >>> abjad.show(staff) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(staff)
            \new Staff
            \with
            {
                \override StaffSymbol.color = #red
            }
            {
                c'4
                e'4
                d'4
                f'4
            }

    ..  container:: example

        Specify grob context like this:

        >>> staff = abjad.Staff("c'4 e'4 d'4 f'4")
        >>> abjad.override(staff[0]).staff.staff_symbol.color = 'blue'
        >>> abjad.show(staff) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(staff)
            \new Staff
            {
                \once \override Staff.StaffSymbol.color = #blue
                c'4
                e'4
                d'4
                f'4
            }

    ..  container:: example

        Returns LilyPond grob name manager:

        >>> staff = abjad.Staff("c'4 e' d' f'")
        >>> abjad.override(staff)
        LilyPondGrobNameManager()

    """
    from abjad.tools import lilypondnametools
    if getattr(argument, '_lilypond_grob_name_manager', None) is None:
        manager = lilypondnametools.LilyPondGrobNameManager()
        argument._lilypond_grob_name_manager = manager
    return argument._lilypond_grob_name_manager
