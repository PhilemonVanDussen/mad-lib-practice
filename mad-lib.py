noun = input("Enter a noun: ")
noun2 = input("Enter a noun: ")
noun3 = input("Enter a noun: ")
noun4 = input("Enter a noun: ")
noun5 = input("Enter a noun: ")
verb = input("Enter a verb: ")
verb2 = input("Enter a verb: ")
verb3 = input("Enter a verb: ")
verb4 = input("Enter a verb: ")

txt = noun.upper()
txt2 = verb.lower()

madlibs = f"Hello there, Do you want a {txt} and {txt2}? It's like doing {verb3} with {noun4}. You don't do like doing that? Don't worry you can have {noun2}. You can also use {noun3} so you can do {verb3}. But also did you know that you save 15% more on {noun5} by doing {verb4} "

print(madlibs)