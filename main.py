# Input Only Accepts Sharps, Add Flat Functionality
# Would like to add Chord options if < 4 notes
# Would like to build out web interface

class MusicalKeys:
    def __init__(self, key_name, notes, print_format):
        self.key_name = key_name
        self.notes = notes
        self.print_format = print_format


# Reformat input notes, changing sharps to single-digit representation
# C# = 1, D# = 2, F# = 3, G# = 4, A# = 5
def reformat_input(notes):
    converted_notes = []
    skip = False
    # Traverse in reverse
    for index, note in reversed(list(enumerate(notes))):
        if skip:
            skip = False
            continue
        elif note == "#":
            converted_notes.append(convert_accidentals(notes[index - 1]))
            skip = True
        else:
            converted_notes.append(note)
    return converted_notes


# Assign single-digit moniker for later string matching
# C# = 1, D# = 2, F# = 3, G# = 4, A# = 5
def convert_accidentals(note):
    converted_note = ""
    if note == "C":
        converted_note = "1"
    elif note == "D":
        converted_note = "2"
    elif note == "F":
        converted_note = "3"
    elif note == "G":
        converted_note = "4"
    elif note == "A":
        converted_note = "5"
    else:
        converted_note = "ERROR CONVERTING"
    return converted_note


def search_keys(notes, keys):
    matches = []
    for key in keys:
        if contains_notes(notes, key.notes):
            matches.append(key)

    return matches


def contains_notes(notes, key):
    for note in notes:
        if note not in key:
            return False
    return True


def print_matches(matches):
    if len(matches) == 0:
        print("No Matching Keys")
    for key in matches:
        print(key.key_name, key.print_format, sep=' ')


def run():
    # Complete listing of keys
    keys = [MusicalKeys("C Major:", "CDEFGA", "C, D, E, F, G, A"),
            MusicalKeys("C# Major:", "12F34C", "C#, D#, F, G♭, A♭, C"),
            MusicalKeys("D Major:", "DE3GAB1", "D, E, F#, G, A, B, C#"),
            MusicalKeys("D# Major:", "2FG45CD", "D#, F, G, A♭, B♭, C, D"),
            MusicalKeys("E Major:", "E34AB12", "E, F#, G#, A, B, C#, D#"),
            MusicalKeys("F Major:", "FGA5CDE", "F, G, A, B♭, C, D, E"),
            MusicalKeys("F# Major:", "345B12F", "F#, G#, A#, B, C#, D#, F"),
            MusicalKeys("G Major:", "GABCDE3", "G, A, B, C, D, E, F#"),
            MusicalKeys("G# Major:", "45C12FG", "G#, A#, C, D♭, E♭, F, G"),
            MusicalKeys("A Major:", "AB1DE34", "A, B, C#, D, E, F#, G#"),
            MusicalKeys("A# Major:", "A5CD2FG", "A, B♭, C, D, E♭, F, G"),
            MusicalKeys("B Major:", "B12E345", "B, C#, D#, E, F#, G#, A#"),
            ]
    # Temporary input for testing
    search = input("Enter notes: ")
    search = reformat_input(search)
    matches = search_keys(search, keys)
    print_matches(matches)


if __name__ == '__main__':
    run()
