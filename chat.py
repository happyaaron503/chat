# 讀取input file

def read_file(filename):
    data = []
    with open(filename, 'r', encoding = 'utf-8-sig') as file:
        for line in file:
            data.append(line.strip())
        return data
def convert(data):
    new = []
    person = None
    for line in data:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        if person:
            new.append(person + ': ' + line)
    return new

def write_file(filename, data):
    with open(filename, 'w') as file:
        for line in data:
            file.write(line + '\n')

def main():
    data = read_file('input.txt')
    data = convert(data)
    write_file('output.txt', data)

main()