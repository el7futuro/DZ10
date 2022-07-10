import json

def load_candidates(): #которая загрузит данные из файла
    with open("candidates.json", encoding='utf-8') as file:
        json_list = file.read()
        candidates_list = list(json.loads(json_list))
    return candidates_list


def get_all(candidates_list): #которая покажет всех кандидатов
    candidates_name="<pre>"
    for i in candidates_list:
        candidates_name += f"{i['name']}\n{i['position']}\n{i['skills']}\n\n"
    candidates_name +="</pre>"
    return candidates_name


def get_by_pk(uid): #которая вернет кандидата по pk
    candidates_list = load_candidates()
    candidate = ""
    for i in candidates_list:

        if uid == i["pk"]:
            candidate += f"<img src='({i['picture']})'>"
            candidate += "<pre>"
            candidate += f"{i['name']}\n{i['position']}\n{i['skills']}\n\n"
            break
        else:
            continue
    candidate +="</pre>"
    return candidate


def get_by_skill(skill_name): #которая вернет кандидатов по навыку
    candidates_list = load_candidates()
    candidates_by_skill = "<pre>"
    for i in candidates_list:
        if skill_name in i["skills"]:
            candidates_by_skill += f"{i['name']}\n{i['position']}\n{i['skills']}\n\n"

    candidates_by_skill += "</pre>"
    return candidates_by_skill





