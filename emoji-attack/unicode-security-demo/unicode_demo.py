# Demonstration of hidden Unicode characters

# Normal word
normal = "admin"

# Word with hidden Zero Width Space
hidden = "a\u200bd\u200bm\u200bi\u200bn"

print("Normal:", normal)
print("Hidden:", hidden)

print("\nAre they equal?")
print(normal == hidden)

print("\nLength of normal string:", len(normal))
print("Length of hidden string:", len(hidden))

print("\nRaw representation:")
print(repr(hidden))
