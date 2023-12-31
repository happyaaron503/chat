def read_file(filename):
    data = []
    with open(filename, 'r', encoding = 'utf-8-sig') as file:
        for line in file:
            data.append(line.strip())
        return data

def convert(data):
    new = []
    person = None
    aaron_word_count = 0
    kaun_word_count = 0
    aaron_sticker_count = 0
    kaun_sticker_count = 0
    aaron_image_count = 0
    kaun_image_count = 0
    for line in data:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        chat = s[2:]
        if name == 'Aaron':
            if s[2] == '貼圖':
                aaron_sticker_count += 1
            elif s[2] == '圖片':
                aaron_image_count += 1
            else:
                for m in s[2:]:
                    aaron_word_count += len(m)
        elif name == '林寬宇':
            if s[2] == '貼圖':
                kaun_sticker_count += 1
            elif s[2] == '圖片':
                kaun_image_count += 1
            else:
                for m in s[2:]:
                    kaun_word_count += len(m)
    print(aaron_word_count)
    print(kaun_word_count)
    print(aaron_sticker_count)
    print(kaun_sticker_count)
    print(aaron_image_count)
    print(kaun_image_count)

def write_file(filename, data):
    with open(filename, 'w') as file:
        for line in data:
            file.write(line + '\n')

def main():
    data = read_file('[Line]Kaun.txt')
    data = convert(data)
    # write_file('output.txt', data)

main()