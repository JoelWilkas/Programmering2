class Elev:
    def __init__(self, namn, ålder, godkänd):
        self.namn = namn
        self.ålder = ålder
        self.godkänd = godkänd
        self.glad = None
    def humör(person):
        if(person.godkänd):
            person.glad = "Glad"
        else:
            person.glad = "Inte Glad"


elev1 = Elev("Test", 18, True)

elev1.humör()
print(elev1.glad)
