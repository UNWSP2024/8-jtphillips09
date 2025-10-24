def word_separator(sentence):

    new_sentence = ""
    #    Add your logic here
    for i, char in enumerate(sentence):
        if char.isupper() and i != 0:
            new_sentence += " " + char.lower()
        else:
            new_sentence += char

    # Make sure the first letter of the sentence is capitalized
    new_sentence = new_sentence[0].upper() + new_sentence[1:]

    return new_sentence.strip()

# Example usage

sentence = "StopAndSmellTheRoses"

new_sentence = word_separator(sentence)

print(new_sentence)
