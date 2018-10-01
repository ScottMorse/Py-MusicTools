from musictools.modules import _music_lib
import re

class _Note:

    def __init__(self,name,octave=None,rhythm=None,dots=None,triplet=None):
        name = name.strip().capitalize()
        if not re.match(_music_lib.NOTE_REGEX,name):
            raise ValueError("Invalid Note name.")
        self._name = name
        if octave:
            if not isinstance(octave,int):
                raise ValueError("Octave value must be None or int.")
        self._octave = octave
        if rhythm:
            if not isinstance(rhythm,str):
                raise ValueError("Rhythm value should be given as a string of flags.")
            if not re.match(_music_lib.RHYTHM_REGEX,rhythm):
                raise ValueError("Invalid rhythm flags. (0-10 followed by dots ('..') and/or t for triplet)")
        self._rhythm = rhythm

class _Interval:

    def __init__(self,flags,displace=0):
        flags = flags.strip()
        if not isinstance(flags, str):
            raise ValueError("Interval flags (first argument) should be a string.")
        if not re.match(_music_lib.INT_FLAG_REGEX,flags):
            raise ValueError("Invalid interval flags.  (see documentation)")
        if not isinstance(displace,int):
            raise ValueError("Displacement value should be a positive integer or 0(default).")
        if displace < 0:
            raise ValueError("Displacement value should be a positive integer or 0(default).")
        self._flags = flags
        self._displace = displace
