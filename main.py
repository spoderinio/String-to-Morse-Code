alphabet = {
    "a": ". -",
    "b": "- . . .",
    "c": "- . - .",
    "d": "- . .",
    "e": ".",
    "f": ". . - .",
    "g": "- - .",
    "h": ". . . .",
    "i": ". .",
    "j": ". - - -",
    "k": "- . -",
    "l": ". - . .",
    "m": "- -",
    "n": "- .",
    "o": "- - . -",
    "p": ". - - .",
    "r": ". - .",
    "s": ". . .",
    "t": "-",
    "u": ". . -",
    "v": ". . -",
    "w": ". - -",
    "x": "- . . -",
    "y": "- . - -",
    "z": "- - . .",
    "1": ". - - - -",
    "2": ". . - - -",
    "3": ". . . - -",
    "4": ". . . . -",
    "5": ". . . . .",
    "6": "- . . . .",
    "7": "- - . . .",
    "8": "- - - . .",
    "9": "- - - - .",
    "0": "- - - - -",
    " ": "/"
}


def generate_morse():
    usr_input = list(input("Enter a word to be converted: ").lower())

    try:
        output_list = [alphabet[letter] for letter in usr_input]
    except KeyError:
        print("Sorry only letters from the English alphabet and arabic numbers please.")
        generate_morse()
    else:
        print(output_list)


generate_morse()
