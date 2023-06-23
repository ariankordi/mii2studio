meta:
  id: mii_data_wii
  title: Wii-format Mii data
  application: Wii
  file-extension:
    - rsd
    - rcd
  endian: le
seq:
  - id: unused_00
    type: b1
    doc: This bit is unused. It should be set to 0.
  - id: sex
    type: b1
    enum: sexes
    doc: The Mii's sex, male or female. 0 = male, 1 = female.
  - id: birthday_month
    type: b4
    enum: months
    doc: The month of the Mii's birthday, ranging from 0 to 12. 0 = no birthday set. Default: 0.
  - id: birthday_day
    type: b5
    doc: The day of the Mii's birthday, ranging from 0 to 31. 0 = no birthday set. Default: 0.
  - id: favorite_color
    type: b4
    doc: The Mii's favorite color, ranging from 0 to 11. The same order as it appears in-editor. Default: 0.
  - id: is_favorite
    type: b1
    enum: favorited
    doc: Determines if a Mii is considered a Favorite (gives normal Miis red pants). Favorite Miis appear in games more often. Up to 10 Favorites are allowed on Wii. 0 = not Favorited, 1 = is Favorited. Default: 0.
  - id: mii_name
    type: str
    size: 20
    encoding: utf-16be
    doc: The Mii's name (sometimes referred to as "nickname"). Up to 10 characters supported. Terminated by two 0x00 bytes in a row. (I would implement this in the Kaitai, but I don't know how to make it terminate by two bytes)
  - id: height
    type: u1
    doc: The Mii's height. Ranges from 0 to 127. Default: 64.
  - id: build
    type: u1
    doc: The Mii's build. Ranges from 0 to 127. Default: 64.
  - id: mii_id
    type: mii_id_contents
    doc: Four bytes (theoretically) unique to every Mii.
  - id: console_id
    size: 4
    doc: 4 bytes representing part of the MAC address of the device the Mii was created on, used as an identifier for the console. The first byte of the console ID is a Checksum8 of the first three bytes of the system's MAC address. The last three bytes of the console ID match the last three bytes of the system's MAC address.
  - id: head
    type: head_data
    doc: The information relating to the Mii's head and skin: face type, skin color, wrinkles, and makeup. Also includes some unused bits, the option for Mingling, and the Mii source type because I couldn't figure out how to make it work where some bits are part of these groups and others aren't lol
  - id: hair
    type: hair_data
    doc: The information relating to the Mii's hair: hair type, color, whether or not the hair is flipped, and five unused bits.
  - id: eyebrows
    type: eyebrow_data
    doc: The information relating to the Mii's eyebrows: eyebrow type, color, size, rotation, X, Y, and six unused bits.
  - id: eyes
    type: eye_data
    doc: The information relating to the Mii's eyes: eye type, color, size, rotation, X, Y, and five unused bits.
  - id: nose
    type: nose_data
    doc: The information relating to the Mii's nose: nose type, size, Y, and three unused bits.
  - id: mouth
    type: mouth_data
    doc: The information relating to the Mii's mouth: mouth type, color, size, and Y.
  - id: glasses
    type: glasses_data
    doc: The information relating to the Mii's glasses: glasses type, color, size, and Y.
  - id: facial_hair
    type: facial_hair_data
    doc: The information relating to the Mii's facial hair: mustache type, beard type, facial hair color, mustache size, and mustache Y.
  - id: mole
    type: mole_data
    doc: The information relating to the Mii's mole: mole type, size, X, Y, and an unused bit.
  - id: creator_name
    type: str
    size: 20
    encoding: utf-16be

types:
  mii_id_contents:
    seq:
      - id: mii_type
        type: b4
        enum: pants
        doc: Depending on this value, the Mii's type, along with the color of its pants, change. The Mii can be a Special Mii (golden pants), a non-local Mii meaning the Mii was received from another system and can't be edited (blue pants), or a normal Mii (gray pants). Also look at head_data.mingling if the Mii is Special.
      - id: creation_time
        type: b28
        doc: Creation time in seconds since January 1st, 2006, 00:00:00, multiplied by 4. Takes the system time of when the Mii was created.
  head_data:
    seq:
      - id: face_type
        type: b3
        doc: Face type. Ranges from 0 to 7. Same order as displayed in editor. Default: 0.
      - id: skin_tone
        type: b3
        doc: Skin tone. Ranges from 0 to 5. Same order as displayed in editor. Default: 0.
      - id: face_features
        type: b4
        doc: Face wrinkles and makeup (facial features). Ranges from 0 to 11. Same order as displayed in editor. Default: 0.
      - id: unused_01
        type: b2
        doc: These bits are unused. They should be set to 0.
      - id: not_mingling
        type: b1
        enum: mingle
        doc: Disables Mingling. Mingling allows the Mii to travel to others' systems via WiiConnect24. 0 = Mingling enabled, 1 = Mingling disabled. Default: 1. If the Mii is Special and this value is set to 0 (enabled), then the Mii will be considered invalid. Thus, all Special Miis must have Mingling disabled.
      - id: source_type
        type: b2
        enum: source
        doc: Determines the source of the Mii. For example, whether the Mii was made locally (on this current system), whether the Mii was downloaded through a service like the Check Mii Out Channel, etc. Currently, values 2 and 3 are unknown.
  hair_data:
    seq:
      - id: hair_type
        type: b7
        doc: Hair type. Ranges from 0 to 71. Not ordered the same as displayed in editor. Default depends on sex initally selected when creating the Mii.
      - id: hair_color
        type: b3
        doc: Hair color. Ranges from 0 to 7. Same order as displayed in editor. Default: 1.
      - id: hair_flip
        type: b1
        doc: Flip hair. 0 = no, 1 = yes. Default: 0.
      - id: unused_03
        type: b5
        doc: These bits are unused. They should be set to 0.
  eyebrow_data:
    seq:
      - id: eyebrow_type
        type: b5
        doc: Eyebrow type. Ranges from 0 to 23. Not ordered the same as displayed in editor. Default depends on sex initally selected when creating the Mii.
      - id: eyebrow_rotation
        type: b5
        doc: Eyebrow rotation. Ranges from 0 to 11, down to up. Default depends on eyebrow type.
      - id: unused_04
        type: b6
        doc: These bits are unused. They should be set to 0.
      - id: eyebrow_color
        type: b3
        doc: Eyebrow color. Ranges from 0 to 7. Same order as displayed in editor. Default: 1.
      - id: eyebrow_size
        type: b4
        doc: Eyebrow size. Ranges from 0 to 8, smallest to largest. Default: 4.
      - id: eyebrow_vertical
        type: b5
        doc: Eyebrow Y (vertical) position. Ranges from 3 to 18, high to low. Default: 10.
      - id: eyebrow_horizontal
        type: b4
        doc: Eyebrow X (horizontal) distance. Ranges from 0 to 12, close to far. Default: 2.
  eye_data:
    seq:
      - id: eye_type
        type: b6
        doc: Eye type. Ranges from 0 to 47. Not ordered the same as displayed in editor. Default depends on sex initally selected when creating the Mii.
      - id: eye_rotation
        type: b5
        doc: Eye rotation. Ranges from 0 to 7, down to up. Default depends on eye type.
      - id: eye_vertical
        type: b5
        doc: Eye Y (vertical) position. Ranges from 0 to 18, high to low. Default: 12.
      - id: eye_color
        type: b3
        doc: Eye color. Ranges from 0 to 5. Same order as displayed in editor. Default: 0.
      - id: eye_size
        type: b4
        doc: Eye size. Ranges from 0 to 7, smallest to largest. Default: 4.
      - id: eye_horizontal
        type: b4
        doc: Eye X (horizontal) distance. Ranges from 0 to 12, close to far. Default: 2.
      - id: unused_05
        type: b5
        doc: These bits are unused. They should be set to 0.
  nose_data:
    seq:
      - id: nose_type
        type: b4
        doc: Nose type. Ranges from 0 to 11. Not ordered the same as displayed in editor. Default: 1.
      - id: nose_size
        type: b4
        doc: Nose size. Ranges from 0 to 8, small to large. Default: 4.
      - id: nose_vertical
        type: b5
        doc: Nose Y (vertical) position. Ranges from 0 to 18, high to low. Default: 9.
      - id: unused_06
        type: b3
        doc: These bits are unused. They should be set to 0.
  mouth_data:
    seq:
      - id: mouth_type
        type: b5
        doc: Mouth type. Ranges from 0 to 23. Not ordered the same as displayed in editor. Default: 23.
      - id: mouth_color
        type: b2
        doc: Mouth (lipstick) color. Ranges from 0 to 2. Same order as displayed in editor. Default: 0.
      - id: mouth_size
        type: b4
        doc: Mouth size. Ranges from 0 to 8, small to large. Default: 4.
      - id: mouth_vertical
        type: b5
        doc: Mouth Y (vertical) position. Ranges from 0 to 18, high to low. Default: 13.
  glasses_data:
    seq:
      - id: glasses_type
        type: b4
        doc: Glasses type. Ranges from 0 to 8. Same order as displayed in editor. Default: 0.
      - id: glasses_color
        type: b3
        doc: Glasses color. Ranges from 0 to 5. Same order as displayed in editor. Default: 0.
      - id: glasses_size
        type: b4
        doc: Glasses size. Ranges from 0 to 7, small to large. Default: 4.
      - id: glasses_vertical
        type: b5
        doc: Glasses Y (vertical) position. Ranges from 0 to 20, high to low. Default: 10.
  facial_hair_data:
    seq:
      - id: facial_hair_mustache
        type: b2
        doc: Mustache type. Ranges from 0 to 3. Same order as displayed in editor. Default: 0.
      - id: facial_hair_beard
        type: b2
        doc: Beard type. Ranges from 0 to 3. Same order as displayed in editor. Default: 0.
      - id: facial_hair_color
        type: b3
        doc: Facial hair color (both beard and mustache). Ranges from 0 to 7. Same order as displayed in editor. Default: 0.
      - id: facial_hair_size
        type: b4
        doc: Mustache size. Ranges from 0 to 8, small to large. Default: 4.
      - id: facial_hair_vertical
        type: b5
        doc: Mustache Y (vertical) position. Ranges from 0 to 16, high to low. Default: 10.
  mole_data:
    seq:
      - id: mole_type
        type: b1
        doc: Enable the mole. 0 = disable mole, 1 = enable mole. Default: 0.
      - id: mole_size
        type: b4
        doc: Mole size. Ranges from 0 to 8, small to large. Default: 4.
      - id: mole_horizontal
        type: b5
        doc: Mole X (horizontal) position. Ranges from 0 to 16, left to right. Default: 2.
      - id: mole_vertical
        type: b5
        doc: Mole Y (vertical) position. Ranges from 0 to 30, high to low. Default: 20.
      - id: unused_07
        type: b1
        doc: This bit is unused. It should be set to 0.

enums:
  source:
    0: local
    1: downloaded
    2: unknown2
    3: unknown3
  pants:
    0: special0
    1: special1
    2: normal2
    3: normal3
    4: special4
    5: special5
    6: normal6
    7: normal7
    8: normal8
    9: normal9
    10: normal10
    11: normal11
    12: not_local12
    13: not_local13
    14: normal14
    15: normal15
  sexes:
    0: male
    1: female
  mingle:
    0: mingling_on
    1: mingling_off
  favorited:
    0: not_favorite
    1: favorite
  months:
    0: no_birthday
    1: january
    2: february
    3: march
    4: april
    5: may
    6: june
    7: july
    8: august
    9: september
    10: october
    11: november
    12: december
  fav_colors:
    0: red
    1: orange
    2: yellow
    3: lime_green
    4: forest_green
    5: royal_blue
    6: sky_blue
    7: pink
    8: purple
    9: brown
    10: white
    11: black
