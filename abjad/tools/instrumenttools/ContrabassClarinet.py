from .Instrument import Instrument


class ContrabassClarinet(Instrument):
    r"""
    Contrassbass clarinet.

    ..  container:: example

        >>> staff = abjad.Staff("c'4 d'4 e'4 fs'4")
        >>> contrabass_clarinet = abjad.ContrabassClarinet()
        >>> abjad.attach(contrabass_clarinet, staff[0])
        >>> abjad.show(staff) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(staff)
            \new Staff
            {
                \set Staff.instrumentName = \markup { "Contrabass clarinet" }
                \set Staff.shortInstrumentName = \markup { "Cbass. cl." }
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
        name='contrabass clarinet',
        short_name='cbass. cl.',
        markup=None,
        short_markup=None,
        allowable_clefs=('treble', 'bass'),
        context=None,
        middle_c_sounding_pitch='Bb1',
        pitch_range='[Bb0, G4]',
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
        Gets contrabass clarinet's allowable clefs.

        ..  container:: example

            >>> contrabass_clarinet = abjad.ContrabassClarinet()
            >>> contrabass_clarinet.allowable_clefs
            ('treble', 'bass')

        Returns clef list.
        """
        return Instrument.allowable_clefs.fget(self)

    @property
    def markup(self):
        """
        Gets contrabass clarinet's instrument name markup.

        ..  container:: example

            >>> contrabass_clarinet = abjad.ContrabassClarinet()
            >>> contrabass_clarinet.markup
            Markup(contents=['Contrabass clarinet'])

            >>> abjad.show(contrabass_clarinet.markup) # doctest: +SKIP

        Returns markup.
        """
        return Instrument.markup.fget(self)

    @property
    def middle_c_sounding_pitch(self):
        """
        Gets sounding pitch of contrabass_clarinet's written middle C.

        ..  container:: example

            >>> contrabass_clarinet = abjad.ContrabassClarinet()
            >>> contrabass_clarinet.middle_c_sounding_pitch
            NamedPitch('bf,,')

            >>> abjad.show(contrabass_clarinet.middle_c_sounding_pitch) # doctest: +SKIP

        Returns named pitch.
        """
        return Instrument.middle_c_sounding_pitch.fget(self)

    @property
    def name(self):
        """
        Gets contrabass clarinet's name.

        ..  container:: example

            >>> contrabass_clarinet = abjad.ContrabassClarinet()
            >>> contrabass_clarinet.name
            'contrabass clarinet'

        Returns string.
        """
        return Instrument.name.fget(self)

    @property
    def pitch_range(self):
        """
        Gets contrabass clarinet's range.

        ..  container:: example

            >>> contrabass_clarinet = abjad.ContrabassClarinet()
            >>> contrabass_clarinet.pitch_range
            PitchRange('[Bb0, G4]')

            >>> abjad.show(contrabass_clarinet.pitch_range) # doctest: +SKIP

        Returns pitch range.
        """
        return Instrument.pitch_range.fget(self)

    @property
    def short_markup(self):
        """
        Gets contrabass clarinet's short instrument name markup.

        ..  container:: example

            >>> contrabass_clarinet = abjad.ContrabassClarinet()
            >>> contrabass_clarinet.short_markup
            Markup(contents=['Cbass. cl.'])

            >>> abjad.show(contrabass_clarinet.short_markup) # doctest: +SKIP

        Returns markup.
        """
        return Instrument.short_markup.fget(self)

    @property
    def short_name(self):
        """
        Gets contrabass clarinet's short instrument name.

        ..  container:: example

            >>> contrabass_clarinet = abjad.ContrabassClarinet()
            >>> contrabass_clarinet.short_name
            'cbass. cl.'

        Returns string.
        """
        return Instrument.short_name.fget(self)
