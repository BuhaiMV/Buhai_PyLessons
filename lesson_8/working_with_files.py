file1 = open('files/a.txt', 'r')
lines_that_we_read = file1.readlines()
print(lines_that_we_read)
file1.close()

file2 = open('files/a.txt', 'w')
file2.write('We have written this line of text 2\n')
file2.writelines(['aadsfsfd\n', 'sdfsdfdsf\n'])
file2.close()

file3 = open('files/a.txt', 'a')
file3.write('aaaaa')
file3.close()

permanent_line = []
with open('files/a.txt', 'r') as file4:
    permanent_line = file4.readlines()

with open('files/a.txt', 'w') as file5:
    for i in range(len(permanent_line)):
        if len(permanent_line[i]) < 20:
            permanent_line[i] = 'we changed this\n'
    file5.writelines(permanent_line)

with open('files/a.txt', 'r') as file4:
    print(file4.readlines())
