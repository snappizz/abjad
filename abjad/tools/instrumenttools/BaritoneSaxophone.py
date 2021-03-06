from .Instrument import Instrument


class BaritoneSaxophone(Instrument):
    r"""
    Baritone saxophone.

    ..  container:: example

        >>> staff = abjad.Staff("c'4 d'4 e'4 fs'4")
        >>> baritone_saxophone = abjad.BaritoneSaxophone()
        >>> abjad.attach(baritone_saxophone, staff[0])
        >>> abjad.show(staff) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(staff)
            \new Staff
            {
                \set Staff.instrumentName = \markup { "Baritone saxophone" }
                \set Staff.shortInstrumentName = \markup { "Bar. sax." }
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
        name='baritone saxophone',
        short_name='bar. sax.',
        markup=None,
        short_markup=None,
        allowable_clefs=None,
        context=None,
        middle_c_sounding_pitch='Eb2',
        pitch_range='[C2, Ab4]',
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
        Gets baritone saxophone's allowable clefs.

        ..  container:: example

            >>> baritone_saxophone = abjad.BaritoneSaxophone()
            >>> baritone_saxophone.allowable_clefs
            ('treble',)

        Returns clef list.
        """
        return Instrument.allowable_clefs.fget(self)

    @property
    def markup(self):
        """
        Gets baritone saxophone's instrument name markup.

        ..  container:: example

            >>> baritone_saxophone = abjad.BaritoneSaxophone()
            >>> baritone_saxophone.markup
            Markup(contents=['Baritone saxophone'])

            >>> abjad.show(baritone_saxophone.markup) # doctest: +SKIP

        Returns markup.
        """
        return Instrument.markup.fget(self)

    @property
    def middle_c_sounding_pitch(self):
        """
        Gets sounding pitch of baritone saxophone's written middle C.

        ..  container:: example

            >>> baritone_saxophone = abjad.BaritoneSaxophone()
            >>> baritone_saxophone.middle_c_sounding_pitch
            NamedPitch('ef,')

            >>> abjad.show(baritone_saxophone.middle_c_sounding_pitch) # doctest: +SKIP

        Returns named pitch.
        """
        return Instrument.middle_c_sounding_pitch.fget(self)

    @property
    def name(self):
        """
        Gets baritone saxophone's name.

        ..  container:: example

            >>> baritone_saxophone = abjad.BaritoneSaxophone()
            >>> baritone_saxophone.name
            'baritone saxophone'

        Returns string.
        """
        return Instrument.name.fget(self)

    @property
    def pitch_range(self):
        """
        Gets baritone saxophone's range.

        ..  container:: example

            >>> baritone_saxophone = abjad.BaritoneSaxophone()
            >>> baritone_saxophone.pitch_range
            PitchRange('[C2, Ab4]')

            >>> abjad.show(baritone_saxophone.pitch_range) # doctest: +SKIP

        Returns pitch range.
        """
        return Instrument.pitch_range.fget(self)

    @property
    def short_markup(self):
        """
        Gets baritone saxophone's short instrument name markup.

        ..  container:: example

            >>> baritone_saxophone = abjad.BaritoneSaxophone()
            >>> baritone_saxophone.short_markup
            Markup(contents=['Bar. sax.'])

            >>> abjad.show(baritone_saxophone.short_markup) # doctest: +SKIP

        Returns markup.
        """
        return Instrument.short_markup.fget(self)

    @property
    def short_name(self):
        """
        Gets baritone saxophone's short instrument name.

        ..  container:: example

            >>> baritone_saxophone = abjad.BaritoneSaxophone()
            >>> baritone_saxophone.short_name
            'bar. sax.'

        Returns string.
        """
        return Instrument.short_name.fget(self)
