SETTINGS_FILE_PATH = 'settings.ini'

PLAYER = 0
COMPUTER = 1

SEA = 0
SHIP = 1
SUNK_SHIP = -1
HIT = 2
MISS = -2

PATROL_BOAT = 2
DESTROYER = 3
BATTLESHIP = 4
CARRIER = 5

COMPUTER_BOARD_REPRESENTATION = {SUNK_SHIP: '[]', SEA: ' ', SHIP: ' ', HIT: '!', MISS: 'X'}
PLAYER_BOARD_REPRESENTATION = {SUNK_SHIP: '[]', SEA: ' ', SHIP: 'S', HIT: '!', MISS: 'X'}
POSITIONING_REPRESENTATION = {SUNK_SHIP: ' ', SEA: ' ', SHIP: 'S', HIT: ' ', MISS: ' '}
LENGTH_OF_SHIPS = {CARRIER: 5, BATTLESHIP: 4, DESTROYER: 3, PATROL_BOAT: 2}
SHIP_NAMES = {CARRIER: "carrier", BATTLESHIP: "battleship", DESTROYER: "destroyer", PATROL_BOAT: "patrol boat"}
