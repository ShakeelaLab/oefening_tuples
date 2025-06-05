# puzzel = ["paraplu", "citroen", "banaan", "goudvis"]
# coordinaten = [(1,2), (0,0), (2,2), (3,1), (1,5), (2,3), (3,6)]
#
# woord = ""
# for i, j in coordinaten:
#     woord += puzzel[i][j]
#
# print(woord)
#
#
# puzzel = ["komkommer", "citroen", "paprika", "olijven"]
# coordinaten = [(1,0), (0,1), (2,2), (3,1), (0,5), (2,0), (1,5)]
#
# woord = ""
# for i, j in coordinaten:
#     woord += puzzel[i][j]
#
# print(woord)

puzzel = ["Albatros", "poncho", "vlinder", "glitter"]
coordinaten = [(0,0),(2,0),(0,-2),(1,3),(0,3),(2,4),(1,-1)]

letters[]

for woord, letters in puzzel:
    letters.append(puzzel[woord][letters])

antwoord = "".join(letters)
print(antwoord)