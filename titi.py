from tinydb import TinyDB
from toto import Boat, Sailor

dock = list()

barque = Boat('Giga Barque')
barque.size = 'XXL'
bernard = Sailor('Bernard', 'Minet')
justine = Sailor('justine', 'Malo')
barque.add_sailor(bernard)
barque.add_sailor(justine)

kayak = Boat('KAYAK')
kayak.size = 'XS'

dock.append(barque)
dock.append(kayak)

db = TinyDB('tiny_lol.json')
boat_table = db.table('boat')
boat_table.truncate()

for boat in dock:
    boat_table.insert(boat.serialize())
    
"""for d in boat_table:
    dock.append(Boat.deserialize(d))"""

"""for boat in dock:
    print(boat.serialize())"""