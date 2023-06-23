# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class MiiDataWii(KaitaiStruct):

    class Source(Enum):
        local = 0
        downloaded = 1
        unknown2 = 2
        unknown3 = 3

    class Pants(Enum):
        special0 = 0
        special1 = 1
        normal2 = 2
        normal3 = 3
        special4 = 4
        special5 = 5
        normal6 = 6
        normal7 = 7
        normal8 = 8
        normal9 = 9
        normal10 = 10
        normal11 = 11
        not_local12 = 12
        not_local13 = 13
        normal14 = 14
        normal15 = 15

    class Favorited(Enum):
        not_favorite = 0
        favorite = 1

    class Mingle(Enum):
        mingling_on = 0
        mingling_off = 1

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
        self.unused_00 = self._io.read_bits_int_be(1) != 0
        self.sex = self._io.read_bits_int_be(1)
        self.birthday_month = KaitaiStream.resolve_enum(MiiDataWii.Months, self._io.read_bits_int_be(4))
        self.birthday_day = self._io.read_bits_int_be(5)
        self.favorite_color = self._io.read_bits_int_be(4)
        self.is_favorite = KaitaiStream.resolve_enum(MiiDataWii.Favorited, self._io.read_bits_int_be(1))
        self._io.align_to_byte()
        self.mii_name = (self._io.read_bytes(20)).decode(u"utf-16be")
        self.height = self._io.read_u1()
        self.build = self._io.read_u1()
        self.mii_id = MiiDataWii.MiiIdContents(self._io, self, self._root)
        self.console_id = self._io.read_bytes(4)
        self.head = MiiDataWii.HeadData(self._io, self, self._root)
        self.hair = MiiDataWii.HairData(self._io, self, self._root)
        self.eyebrows = MiiDataWii.EyebrowData(self._io, self, self._root)
        self.eyes = MiiDataWii.EyeData(self._io, self, self._root)
        self.nose = MiiDataWii.NoseData(self._io, self, self._root)
        self.mouth = MiiDataWii.MouthData(self._io, self, self._root)
        self.glasses = MiiDataWii.GlassesData(self._io, self, self._root)
        self.facial_hair = MiiDataWii.FacialHairData(self._io, self, self._root)
        self.mole = MiiDataWii.MoleData(self._io, self, self._root)
        self.creator_name = (self._io.read_bytes(20)).decode(u"utf-16be")

    class NoseData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.nose_type = self._io.read_bits_int_be(4)
            self.nose_size = self._io.read_bits_int_be(4)
            self.nose_vertical = self._io.read_bits_int_be(5)
            self.unused_06 = self._io.read_bits_int_be(3)


    class HeadData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.face_type = self._io.read_bits_int_be(3)
            self.skin_tone = self._io.read_bits_int_be(3)
            self.face_features = self._io.read_bits_int_be(4)
            self.unused_01 = self._io.read_bits_int_be(2)
            self.not_mingling = KaitaiStream.resolve_enum(MiiDataWii.Mingle, self._io.read_bits_int_be(1))
            self.source_type = KaitaiStream.resolve_enum(MiiDataWii.Source, self._io.read_bits_int_be(2))


    class FacialHairData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.facial_hair_mustache = self._io.read_bits_int_be(2)
            self.facial_hair_beard = self._io.read_bits_int_be(2)
            self.facial_hair_color = self._io.read_bits_int_be(3)
            self.facial_hair_size = self._io.read_bits_int_be(4)
            self.facial_hair_vertical = self._io.read_bits_int_be(5)


    class HairData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.hair_type = self._io.read_bits_int_be(7)
            self.hair_color = self._io.read_bits_int_be(3)
            self.hair_flip = self._io.read_bits_int_be(1) != 0
            self.unused_03 = self._io.read_bits_int_be(5)


    class MoleData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.mole_type = self._io.read_bits_int_be(1) != 0
            self.mole_size = self._io.read_bits_int_be(4)
            self.mole_horizontal = self._io.read_bits_int_be(5)
            self.mole_vertical = self._io.read_bits_int_be(5)
            self.unused_07 = self._io.read_bits_int_be(1) != 0


    class MiiIdContents(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.mii_type = KaitaiStream.resolve_enum(MiiDataWii.Pants, self._io.read_bits_int_be(4))
            self.creation_time = self._io.read_bits_int_be(28)


    class EyebrowData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.eyebrow_type = self._io.read_bits_int_be(5)
            self.eyebrow_rotation = self._io.read_bits_int_be(5)
            self.unused_04 = self._io.read_bits_int_be(6)
            self.eyebrow_color = self._io.read_bits_int_be(3)
            self.eyebrow_size = self._io.read_bits_int_be(4)
            self.eyebrow_vertical = self._io.read_bits_int_be(5)
            self.eyebrow_horizontal = self._io.read_bits_int_be(4)


    class MouthData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.mouth_type = self._io.read_bits_int_be(5)
            self.mouth_color = self._io.read_bits_int_be(2)
            self.mouth_size = self._io.read_bits_int_be(4)
            self.mouth_vertical = self._io.read_bits_int_be(5)


    class GlassesData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.glasses_type = self._io.read_bits_int_be(4)
            self.glasses_color = self._io.read_bits_int_be(3)
            self.glasses_size = self._io.read_bits_int_be(4)
            self.glasses_vertical = self._io.read_bits_int_be(5)


    class EyeData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.eye_type = self._io.read_bits_int_be(6)
            self.eye_rotation = self._io.read_bits_int_be(5)
            self.eye_vertical = self._io.read_bits_int_be(5)
            self.eye_color = self._io.read_bits_int_be(3)
            self.eye_size = self._io.read_bits_int_be(4)
            self.eye_horizontal = self._io.read_bits_int_be(4)
            self.unused_05 = self._io.read_bits_int_be(5)



