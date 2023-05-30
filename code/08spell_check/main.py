from spell_check import SpellChecker

N_HINTS = 5

sc = SpellChecker()
try:
    while True:
        s = input("Type a word:").strip()
        hints = sc.get_hints(s,N_HINTS)
        print("Hints:")
        for h in hints:
            print(f"\t-> {h[0]} (distance = {h[1]})")
        hints = sc.get_hints(s,10)
except KeyboardInterrupt:
    print("\nClosing...")