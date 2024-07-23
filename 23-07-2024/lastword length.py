def length_of_last_word(s: str) -> int:
    words = s.strip().split()
    return len(words[-1]) if words else 0
s = "Hello World"
print(length_of_last_word(s))  
