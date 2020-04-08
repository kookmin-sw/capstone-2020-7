f = open('text.txt', 'rt', encoding="UTF8")

while True:
    # 파일의 끝까지 한 문장씩 읽는다.
    line = f.readline()
    if not line: break

    print(line)

f.close()