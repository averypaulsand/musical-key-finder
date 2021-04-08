# Input must be Uppercase for natural notes and lowercase for sharps
# Currently only handles sharps - needs additional attention to parse flats/sharps correctley
# Would like to add Chord options if < 4 notes
# Would like to build out web interface

class MusicalKeys:
    def __init__(self, key_name, notes):
        self.key_name = key_name
        self.notes = notes


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
        print("No Matches")
    for key in matches:
        print(key.key_name, key.notes, sep=' ')


def run():
  # Complete listing of keys
    keys = [MusicalKeys("C Major", "CDEFGA"), MusicalKeys("A Major", "ABcDEfg")]
    # Temporary input for testing
    search = "CDEF"
    matches = search_keys(search, keys)
    print_matches(matches)


if __name__ == '__main__':
    run()
