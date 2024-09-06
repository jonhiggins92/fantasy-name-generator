import random

beginnings = ['An', 'Lo', 'Is', 'Tar', 'Ur', 'Jen', 'Mor', 'Al', 'Sen']
middles = ['dre', 'fal', 'gor', 'las', 'net', 'rak', 'sav', 'vin', 'zul']
ends = ['dar', 'ius', 'moth', 'wen', 'thor', 'ion', 'on', 'an', 'el']

def generate_name():
    # Randomly decide how many syllables the name will have
    syllables_count = random.randint(1, 3)  # 1, 2, or 3 syllables

    # Build the name based on the number of syllables
    if syllables_count == 1:
        return random.choice(beginnings)
    elif syllables_count == 2:
        return random.choice(beginnings) + random.choice(ends)
    else:
        return random.choice(beginnings) + random.choice(middles) + random.choice(ends)

print(generate_name())