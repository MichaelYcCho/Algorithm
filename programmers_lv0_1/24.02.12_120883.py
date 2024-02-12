def solution(id_pw, db):
    for i in db:
        if id_pw[0] in i:
            if id_pw[1] == i[1]:
                return "login"
            else:
                return "wrong pw"
    return "fail"


# Ver2 Hash
# id를 key, pw를 value인 dict로 만듬
def solution(id_pw, db):
    db_dict = {i[0]: i[1] for i in db}
    # id 가 있는경우
    if id_pw[0] in db_dict:
        if id_pw[1] == db_dict[id_pw[0]]:
            return "login"
        else:
            return "wrong pw"
    # id가 없는 경우
    else:
        return "fail"