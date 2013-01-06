from abjad.tools import rhythmmakertools
from experimental.tools.requesttools.PayloadCallbackMixin import PayloadCallbackMixin


class RhythmMakerRequest(PayloadCallbackMixin):
    r'''Rhythm-maker request.

    Create behind-the-scenes at setting-time.
    '''

    ### INTIAILIZER ###

    def __init__(self, payload, payload_callbacks=None):
        assert isinstance(payload, rhythmmakertools.RhythmMaker), repr(payload)
        PayloadCallbackMixin.__init__(self, payload_callbacks=payload_callbacks)
        self._payload = payload

    ### PRIVATE METHODS ###

    def _get_payload(self, score_specification=None, voice_name=None):
        raise NotImplementedError

    ### READ-ONLY PUBLIC PROPERTIES ###

    @property
    def payload(self):
        return self._payload
