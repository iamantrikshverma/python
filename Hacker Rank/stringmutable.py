def mutate_string(string, position, character): 
    """
    This function takes a string, a position, and a character as input. It returns a new
    string where the character at the specified position in the original string is replaced
    with the new character.
    """
    # Convert the string to a list of characters to make it mutable
    string_list = list(string)
    # Replace the character at the specified position with the new character
    string_list[position] = character
    # Convert the list of characters back to a string
    return ''.join(string_list)

    
    return

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)