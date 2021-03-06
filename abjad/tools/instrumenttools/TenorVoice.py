from .Instrument import Instrument


class TenorVoice(Instrument):
    r"""
    Tenor voice.

    ..  container:: example

        >>> staff = abjad.Staff("c'4 d'4 e'4 fs'4")
        >>> tenor = abjad.TenorVoice()
        >>> abjad.attach(tenor, staff[0])
        >>> abjad.show(staff) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(staff)
            \new Staff
            {
                \set Staff.instrumentName = \markup { Tenor }
                \set Staff.shortInstrumentName = \markup { Ten. }
                c'4
                d'4
                e'4
                fs'4
            }

    """

    ### CLASS VARIABLES ###

    __slots__ = ()

    performer_abbreviation = 'ten.'

    ### INITIALIZER ###

    def __init__(
        self,
        *,
        name='tenor',
        short_name='ten.',
        markup=None,
        short_markup=None,
        allowable_clefs=None,
        context=None,
        middle_c_sounding_pitch=None,
        pitch_range='[C3, D5]',
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
        self._is_primary_instrument = True

    ### PUBLIC PROPERTIES ###

    @property
    def allowable_clefs(self):
        """
        Gets tenor's allowable clefs.

        ..  container:: example

            >>> tenor = abjad.TenorVoice()
            >>> tenor.allowable_clefs
            ('treble',)

        Returns clef list.
        """
        return Instrument.allowable_clefs.fget(self)

    @property
    def markup(self):
        """
        Gets tenor's instrument name markup.

        ..  container:: example

            >>> tenor = abjad.TenorVoice()
            >>> tenor.markup
            Markup(contents=['Tenor'])

            >>> abjad.show(tenor.markup) # doctest: +SKIP

        Returns markup.
        """
        return Instrument.markup.fget(self)

    @property
    def middle_c_sounding_pitch(self):
        """
        Gets sounding pitch of tenor's written middle C.

        ..  container:: example

            >>> tenor = abjad.TenorVoice()
            >>> tenor.middle_c_sounding_pitch
            NamedPitch("c'")

            >>> abjad.show(tenor.middle_c_sounding_pitch) # doctest: +SKIP

        Returns named pitch.
        """
        return Instrument.middle_c_sounding_pitch.fget(self)

    @property
    def name(self):
        """
        Gets tenor's name.

        ..  container:: example

            >>> tenor = abjad.TenorVoice()
            >>> tenor.name
            'tenor'

        Returns string.
        """
        return Instrument.name.fget(self)

    @property
    def pitch_range(self):
        """
        Gets tenor's range.

        ..  container:: example

            >>> tenor = abjad.TenorVoice()
            >>> tenor.pitch_range
            PitchRange('[C3, D5]')

            >>> abjad.show(tenor.pitch_range) # doctest: +SKIP

        Returns pitch range.
        """
        return Instrument.pitch_range.fget(self)

    @property
    def short_markup(self):
        """
        Gets tenor's short instrument name markup.

        ..  container:: example

            >>> tenor = abjad.TenorVoice()
            >>> tenor.short_markup
            Markup(contents=['Ten.'])

            >>> abjad.show(tenor.short_markup) # doctest: +SKIP

        Returns markup.
        """
        return Instrument.short_markup.fget(self)

    @property
    def short_name(self):
        """
        Gets tenor's short instrument name.

        ..  container:: example

            >>> tenor = abjad.TenorVoice()
            >>> tenor.short_name
            'ten.'

        Returns string.
        """
        return Instrument.short_name.fget(self)
