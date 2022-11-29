def solution(new_id):
    # 1,2 단계
    index = 0
    while index < len(new_id):
        if 65 <= ord(new_id[index]) <= 90:
            new_id = new_id.replace(new_id[index], chr(ord(new_id[index])+32))
            index += 1
            continue
        if new_id[index] == '.' or new_id[index] =='-' or new_id[index] == '_' or 97 <= ord(new_id[index]) <= 122 or 48 <= ord(new_id[index]) <= 57:
            index += 1
            continue
        new_id = new_id.replace(new_id[index], '')

    # 3 단계
    while '..' in new_id:
        new_id = new_id.replace('..', '.')

    # 4 단계
    if len(new_id) != 0 and new_id[0] == '.':
        new_id = new_id[1:]
    if len(new_id) != 0 and new_id[-1] == '.':
        new_id = new_id[:-1]

    # 5 단계
    if new_id == '':
        new_id = 'a'

    # 6 단계
    new_id = new_id[:15]
    if new_id[-1] == '.':
        new_id = new_id[:-1]

    # 7 단계
    while len(new_id) < 3:
        new_id += new_id[-1]

    answer = new_id
    
    return answer