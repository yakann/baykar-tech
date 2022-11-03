from enumfields import Enum


class ProductType(Enum):
    flying = 'flying'
    armor = 'armor'
    sniper = 'sniper'
    airdefence = 'airdefence'
    pistol = 'pistol'
    interphone = 'interphone'


class AttributeType(Enum):
    infantry = 'infantry'
    seaman = 'seaman'