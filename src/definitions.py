from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent

KEYS_TO_ORDINAL = {
        30000: 0,
        65030: 1,
        65000: 2,
        80000: 3,
        74000: 4,
        70000: 5,
        70032: 6,
        88000: 7,
        86000: 8,
        99000: 9,
        90000: 10,
        93000: 11
    }

KEYS_TO_LITHOLOGY = {30000: 'Sandstone',
                     65030: 'Sandstone/Shale',
                     65000: 'Shale',
                     80000: 'Marl',
                     74000: 'Dolomite',
                     70000: 'Limestone',
                     70032: 'Chalk',
                     88000: 'Halite',
                     86000: 'Anhydrite',
                     99000: 'Tuff',
                     90000: 'Coal',
                     93000: 'Basement'}

ORDINAL_TO_KEYS = {value: key for key, value in  KEYS_TO_ORDINAL.items()}

ORDINAL_TO_LITHOLOGY = {}
for ordinal_key, key in ORDINAL_TO_KEYS.items():
    ORDINAL_TO_LITHOLOGY[ordinal_key] = KEYS_TO_LITHOLOGY[key]