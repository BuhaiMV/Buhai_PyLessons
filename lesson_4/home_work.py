note = []
answer = ''
while answer != 'exit':
    answer = input('Що будемо робити? ')
    if answer == 'add':
        note.append(input('Введіть нотатку: '))
        continue
    elif answer == 'earliest':
        for element in note:
            print(element)
        continue
    elif answer == 'latest':
        for i in range(len(note)):
            print(note[len(note) - (i + 1)])
        continue
    elif answer == 'longest':
        temporary_note = note.copy()
        longest_note = []
        for i in range(len(temporary_note)):
            longest_note.append(max(temporary_note, key=len))
            index = temporary_note.index(longest_note[len(longest_note) - 1])
            temporary_note.pop(index)
        for i in range(len(longest_note)):
            print(longest_note[i])
        continue
    elif answer == 'shortest':
        temporary_note = note.copy()
        shortest_note = []
        for i in range(len(temporary_note)):
            shortest_note.append(min(temporary_note, key=len))
            index = temporary_note.index(shortest_note[len(shortest_note) - 1])
            temporary_note.pop(index)
        for i in range(len(shortest_note)):
            print(shortest_note[i])
        continue
    elif answer == 'Exit':
        break
