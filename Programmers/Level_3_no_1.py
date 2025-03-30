def solution(n, bans):
    # Convert banned spells to set
    banned = set(bans)
    
    # First, find the length of the nth spell
    target_length = 0
    spell_count = 0
    
    for length in range(1, 12):  # Max length is 11
        # Total possible spells of this length
        total_of_length = 26 ** length
        # Number of banned spells of this length
        banned_of_length = sum(1 for s in banned if len(s) == length)
        # Valid spells of this length
        valid_of_length = total_of_length - banned_of_length
        
        if spell_count + valid_of_length >= n:
            target_length = length
            n -= spell_count  # Convert n to position within spells of target_length
            break
        
        spell_count += valid_of_length
    
    # Pre-process banned spells of target length for faster lookup
    banned_of_target_length = [b for b in banned if len(b) == target_length]
    
    # Build a prefix tree (trie) of banned spells to optimize prefix checking
    banned_prefixes = {}
    for spell in banned_of_target_length:
        for i in range(1, len(spell) + 1):
            prefix = spell[:i]
            if prefix not in banned_prefixes:
                banned_prefixes[prefix] = 0
            banned_prefixes[prefix] += 1
    
    # Now, build the spell character by character
    result = ""
    
    for position in range(target_length):
        for char in "abcdefghijklmnopqrstuvwxyz":
            candidate = result + char
            
            # If this is a complete word, check if it's banned
            if len(candidate) == target_length:
                if candidate not in banned:
                    n -= 1
                    if n == 0:
                        return candidate
            else:
                # Calculate how many valid spells start with this prefix
                remaining_positions = target_length - len(candidate)
                total_possible = 26 ** remaining_positions
                
                # Use the prefix tree to find banned spells with this prefix
                banned_with_prefix = banned_prefixes.get(candidate, 0)
                
                valid_with_prefix = total_possible - banned_with_prefix
                
                if n <= valid_with_prefix:
                    result = candidate
                    break
                else:
                    n -= valid_with_prefix
    
    return result