def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowel_indexes = [i for i in range(0, len(s)) if s[i].lower() in "aeiou"]

    reversed_vowel_indexes = vowel_indexes.copy()
    reversed_vowel_indexes.reverse()
    vowel_dict = {vowel_indexes[i] : reversed_vowel_indexes[i] for i in range(0, len(vowel_indexes))}

    result = ""
    for i in range(0, len(s)):
        result = result + s[vowel_dict[i]] if i in vowel_dict.keys() else result + s[i]
    return result