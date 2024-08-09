def improve_grammar(text):
    if not text:
        raise ValueError("No grammar in empty string.")
    
    first_character = text[0]
    last_character = text[-1]
    special_character = {"!", "%", "?", ".", "/"}
    
    if first_character.isupper() and last_character in special_character:
        return True
    elif first_character.isupper() and last_character not in special_character:
        return False
    elif last_character in special_character and first_character.islower():
        return False
    else:
        return False