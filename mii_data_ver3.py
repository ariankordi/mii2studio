# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class MiiDataVer3(KaitaiStruct):

    class RegionText(Enum):
        jpn_usa_pal_aus = 0
        chn = 1
        kor = 2
        twn = 3

    class Sexes(Enum):
        male = 0
        female = 1

    class CreationDevice(Enum):
        wii = 1
        ds = 2
        n3ds = 3
        wiiu_switch = 4

    class Region(Enum):
        no_lock = 0
        jpn = 1
        usa = 2
        pal_aus = 3

    class Months(Enum):
        no_birthday = 0
        january = 1
        february = 2
        march = 3
        april = 4
        may = 5
        june = 6
        july = 7
        august = 8
        september = 9
        october = 10
        november = 11
        december = 12

    class FavColors(Enum):
        red = 0
        orange = 1
        yellow = 2
        lime_green = 3
        forest_green = 4
        royal_blue = 5
        sky_blue = 6
        pink = 7
        purple = 8
        brown = 9
        white = 10
        black = 11
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.format_version = self._io.read_u1()
        self.copying = self._io.read_bits_int_le(1) != 0
        self.profanity = self._io.read_bits_int_le(1) != 0
        self.region_lock = KaitaiStream.resolve_enum(MiiDataVer3.Region, self._io.read_bits_int_le(2))
        self.font_region = KaitaiStream.resolve_enum(MiiDataVer3.RegionText, self._io.read_bits_int_le(2))
        self.unused_00 = self._io.read_bits_int_le(2)
        self.position_page = self._io.read_bits_int_le(4)
        self.position_slot = self._io.read_bits_int_le(4)
        self.unknown_0 = self._io.read_bits_int_le(4)
        self.birth_platform = KaitaiStream.resolve_enum(MiiDataVer3.CreationDevice, self._io.read_bits_int_le(3))
        self.unused_01 = self._io.read_bits_int_le(1) != 0
        self._io.align_to_byte()
        self.console_id = self._io.read_u8le()
        self.mii_id = MiiDataVer3.MiiIdContents(self._io, self, self._root)
        self.console_mac = self._io.read_bytes(6)
        self.unused_02 = self._io.read_u2le()
        self.sex = KaitaiStream.resolve_enum(MiiDataVer3.Sexes, self._io.read_bits_int_le(1))
        self.birthday_month = KaitaiStream.resolve_enum(MiiDataVer3.Months, self._io.read_bits_int_le(4))
        self.birthday_day = self._io.read_bits_int_le(5)
        self.favorite_color = KaitaiStream.resolve_enum(MiiDataVer3.FavColors, self._io.read_bits_int_le(4))
        self.is_favorite = self._io.read_bits_int_le(1) != 0
        self.unknown_2 = self._io.read_bits_int_le(1) != 0
        self._io.align_to_byte()
        self.mii_name = (self._io.read_bytes(20)).decode(u"utf-16le")
        self.height = self._io.read_u1()
        self.build = self._io.read_u1()
        self.head = MiiDataVer3.HeadData(self._io, self, self._root)
        self.hair = MiiDataVer3.HairData(self._io, self, self._root)
        self.eyes = MiiDataVer3.EyeData(self._io, self, self._root)
        self.eyebrows = MiiDataVer3.EyebrowData(self._io, self, self._root)
        self.nose = MiiDataVer3.NoseData(self._io, self, self._root)
        self.mouth = MiiDataVer3.MouthData(self._io, self, self._root)
        self.facial_hair = MiiDataVer3.FacialHairData(self._io, self, self._root)
        self.glasses = MiiDataVer3.GlassesData(self._io, self, self._root)
        self.mole = MiiDataVer3.MoleData(self._io, self, self._root)
        self.creator_name = (self._io.read_bytes(20)).decode(u"utf-16le")
        self.unused_12 = self._io.read_u2le()
        self.checksum = self._io.read_u2le()

    class NoseData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.nose_type = self._io.read_bits_int_le(5)
            self.nose_size = self._io.read_bits_int_le(4)
            self.nose_vertical = self._io.read_bits_int_le(5)
            self.unused_08 = self._io.read_bits_int_le(2)


    class HeadData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.not_sharing = self._io.read_bits_int_le(1) != 0
            self.face_type = self._io.read_bits_int_le(4)
            self.skin_tone = self._io.read_bits_int_le(3)
            self.face_wrinkles = self._io.read_bits_int_le(4)
            self.face_makeup = self._io.read_bits_int_le(4)


    class FacialHairData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.facial_hair_mustache = self._io.read_bits_int_le(5)
            self.unused_09 = self._io.read_bits_int_le(6)
            self.facial_hair_beard = self._io.read_bits_int_le(3)
            self.facial_hair_color = self._io.read_bits_int_le(3)
            self.facial_hair_size = self._io.read_bits_int_le(4)
            self.facial_hair_vertical = self._io.read_bits_int_le(5)
            self.unused_10 = self._io.read_bits_int_le(1) != 0


    class HairData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.hair_type = self._io.read_u1()
            self.hair_color = self._io.read_bits_int_le(3)
            self.hair_flip = self._io.read_bits_int_le(1) != 0
            self.unused_03 = self._io.read_bits_int_le(4)


    class MoleData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.mole_type = self._io.read_bits_int_le(1) != 0
            self.mole_size = self._io.read_bits_int_le(4)
            self.mole_horizontal = self._io.read_bits_int_le(5)
            self.mole_vertical = self._io.read_bits_int_le(5)
            self.unused_11 = self._io.read_bits_int_le(1) != 0


    class MiiIdContents(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.is_normal = self._io.read_bits_int_be(1) != 0
            self.is_ds = self._io.read_bits_int_be(1) != 0
            self.is_developer_mii = self._io.read_bits_int_be(1) != 0
            self.is_valid = self._io.read_bits_int_be(1) != 0
            self.creation_time = self._io.read_bits_int_be(28)


    class EyebrowData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.eyebrow_type = self._io.read_bits_int_le(5)
            self.eyebrow_color = self._io.read_bits_int_le(3)
            self.eyebrow_size = self._io.read_bits_int_le(4)
            self.eyebrow_stretch = self._io.read_bits_int_le(3)
            self.unused_05 = self._io.read_bits_int_le(1) != 0
            self.eyebrow_rotation = self._io.read_bits_int_le(4)
            self.unused_06 = self._io.read_bits_int_le(1) != 0
            self.eyebrow_horizontal = self._io.read_bits_int_le(4)
            self.eyebrow_vertical = self._io.read_bits_int_le(5)
            self.unused_07 = self._io.read_bits_int_le(2)


    class MouthData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.mouth_type = self._io.read_bits_int_le(6)
            self.mouth_color = self._io.read_bits_int_le(3)
            self.mouth_size = self._io.read_bits_int_le(4)
            self.mouth_stretch = self._io.read_bits_int_le(3)
            self.mouth_vertical = self._io.read_bits_int_le(5)


    class GlassesData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.glasses_type = self._io.read_bits_int_le(4)
            self.glasses_color = self._io.read_bits_int_le(3)
            self.glasses_size = self._io.read_bits_int_le(4)
            self.glasses_vertical = self._io.read_bits_int_le(5)


    class EyeData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.eye_type = self._io.read_bits_int_le(6)
            self.eye_color = self._io.read_bits_int_le(3)
            self.eye_size = self._io.read_bits_int_le(4)
            self.eye_stretch = self._io.read_bits_int_le(3)
            self.eye_rotation = self._io.read_bits_int_le(5)
            self.eye_horizontal = self._io.read_bits_int_le(4)
            self.eye_vertical = self._io.read_bits_int_le(5)
            self.unused_04 = self._io.read_bits_int_le(2)



