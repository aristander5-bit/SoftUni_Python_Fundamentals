morse_to_english = {
    ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E",
    "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J",
    "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O",
    ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
    "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y",
    "--..": "Z"
}
morse_words = input().split(" | ")
translated_sentence = []

for morse_word in morse_words:
    current_word = ""
    morse_symbols = morse_word.split()

    for morse_symbol in morse_symbols:
        if morse_symbol in morse_to_english:
            current_word += morse_to_english[morse_symbol]

    translated_sentence.append(current_word)

print(" ".join(translated_sentence))