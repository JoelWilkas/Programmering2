text = input("")

index = len(text)
nyText = ""

for i in text:
    nyText += text[index - 1]
    index -= 1
print(nyText)
