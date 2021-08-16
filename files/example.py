# must be created before
file = open('hello.txt', 'r')
content = file.read()
print(content)
file.close()

# must be created before
output_file = open('output.txt', 'w')
output_file.write(content)
output_file.close()

output_file = open('output.txt', 'w')
output_file.write('Bye-bye!')
output_file.close()

output_file = open('output.txt', 'a')
output_file.write('Bye-bye!')
output_file.close()