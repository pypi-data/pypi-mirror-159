""".. versionadded:: 0.0.5

Control the macOS Voice Memos application using JXA-like syntax.
"""

from typing import List, Union

from PyXA import XABase
from PyXA import XABaseScriptable

class XAVoiceMemosApplication(XABase.XAApplication):
    """A class for managing and interacting with Voice Memos.app.

    .. seealso:: :class:`XATextEditWindow`, :class:`XATextEditDocument`

    .. versionadded:: 0.0.1
    """
    def __init__(self, properties):
        super().__init__(properties)

    def voice_memos(self):
        print(self.front_window())

class XAVoiceMemo(XABase.XAObject):
    def __init__(self, properties):
        super().__init__(properties)
