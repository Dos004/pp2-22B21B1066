with open('source.txt', 'r') as source_file:
    file_contents = source_file.read()

with open('destination.txt', 'w') as destination_file:
    destination_file.write(file_contents)
