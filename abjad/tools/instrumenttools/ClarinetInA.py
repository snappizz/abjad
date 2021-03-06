from .Instrument import Instrument


class ClarinetInA(Instrument):
    r"""
    Clarinet in A.

    ..  container:: example

        >>> staff = abjad.Staff("c'4 d'4 e'4 fs'4")
        >>> clarinet = abjad.ClarinetInA()
        >>> abjad.attach(clarinet, staff[0])
        >>> abjad.show(staff) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(staff)
            \new Staff
            {
                \set Staff.instrumentName = \markup { "Clarinet in A" }
                \set Staff.shortInstrumentName = \markup {
                    Cl.
                    A
                    \natural
                    }
                c'4
                d'4
                e'4
                fs'4
            }

    """

    ### CLASS VARIABLES ###

    __slots__ = ()

    ### INITIALIZER ###

    def __init__(
        self,
        *,
        name='clarinet in A',
        short_name=r'cl. A \natural',
        markup=None,
        short_markup=None,
        allowable_clefs=None,
        context=None,
        middle_c_sounding_pitch='A3',
        pitch_range='[Db3, A6]',
        hide=None,
        ):
        Instrument.__init__(
            self,
            name=name,
            short_name=short_name,
            markup=markup,
            short_markup=short_markup,
            allowable_clefs=allowable_clefs,
            context=context,
            middle_c_sounding_pitch=middle_c_sounding_pitch,
            pitch_range=pitch_range,
            hide=hide,
            )

    ### PUBLIC PROPERTIES ###

    @property
    def allowable_clefs(self):
        """
        Gets clarinet in A's allowable clefs.

        ..  container:: example

            >>> clarinet = abjad.ClarinetInA()
            >>> clarinet.allowable_clefs
            ('treble',)

        Returns clef list.
        """
        return Instrument.allowable_clefs.fget(self)

    @property
    def markup(self):
        """
        Gets clarinet in A's instrument name markup.

        ..  container:: example

            >>> clarinet = abjad.ClarinetInA()
            >>> clarinet.markup
            Markup(contents=['Clarinet in A'])

            >>> abjad.show(clarinet.markup) # doctest: +SKIP

        Returns markup.
        """
        return Instrument.markup.fget(self)

    @property
    def middle_c_sounding_pitch(self):
        """
        Gets sounding pitch of clarinet in A's written middle C.

        ..  container:: example

            >>> clarinet = abjad.ClarinetInA()
            >>> clarinet.middle_c_sounding_pitch
            NamedPitch('a')

            >>> abjad.show(clarinet.middle_c_sounding_pitch) # doctest: +SKIP

        Returns named pitch.
        """
        return Instrument.middle_c_sounding_pitch.fget(self)

    @property
    def name(self):
        """
        Gets clarinet in A's name.

        ..  container:: example

            >>> clarinet = abjad.ClarinetInA()
            >>> clarinet.name
            'clarinet in A'

        Returns string.
        """
        return Instrument.name.fget(self)

    @property
    def pitch_range(self):
        """
        Gets clarinet in A's range.

        ..  container:: example

            >>> clarinet = abjad.ClarinetInA()
            >>> clarinet.pitch_range
            PitchRange('[Db3, A6]')

            >>> abjad.show(clarinet.pitch_range) # doctest: +SKIP

        Returns pitch range.
        """
        return Instrument.pitch_range.fget(self)

    @property
    def short_markup(self):
        """
        Gets clarinet in A's short instrument name markup.

        ..  container:: example

            >>> clarinet = abjad.ClarinetInA()
            >>> clarinet.short_markup
            Markup(contents=['Cl.', 'A', MarkupCommand('natural')])

            >>> abjad.show(clarinet.short_markup) # doctest: +SKIP

        Returns markup.
        """
        return Instrument.short_markup.fget(self)

    @property
    def short_name(self):
        r"""
        Gets clarinet in A's short instrument name.

        ..  container:: example

            >>> clarinet = abjad.ClarinetInA()
            >>> clarinet.short_name
            'cl. A \\natural'

        Returns string.
        """
        return Instrument.short_name.fget(self)
