# Which of the following strings is the longest?
# Use the len() function to find out.

longest_german_word = "Donaudampfschifffahrtsgesellschaftskapitänskajütentürschnalle"
longest_hungarian_word = "Megszentségteleníthetetlenségeskedéseitekért"
longest_finnish_word = "Lentokonesuihkuturbiinimoottoriapumekaanikkoaliupseerioppilas"
strong_password = "%8Ddb^ca<*'{9pur/Y(8n}^QPm3G?JJY}\(<bCGHv^FfM}.;)khpkSYTfMA@>N"

words = [longest_german_word, longest_hungarian_word, longest_finnish_word, strong_password]
maxlen = len(max(words))

longest_str = None
if len(longest_german_word) == maxlen:
    longest_str = longest_german_word
elif len(longest_hungarian_word) == maxlen:
    longest_str = longest_hungarian_word
elif len(longest_finnish_word) == maxlen:
    longest_str = longest_finnish_word
else:
    longest_str = strong_password

for i in words:
    print(len(i))

print(f'The longest word is: {longest_str}, with {maxlen} characters')