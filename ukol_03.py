import json
with open('person.json', encoding='utf-8') as vstupni_soubor:
    person = json.load(vstupni_soubor)
# print(person)

for body in person:
    # print(person[body])
    if (person[body]) >= 60:
        # print(f"{body}: {person[body]}, Prospěch: Pass")
            person[body] = "Pass"
    else:
        # print(f"{body}: {person[body]}, Prospěch: Fail")
            person[body] = "Fail"
with open("person_prospech", mode="w", encoding="utf-8") as vystupni_soubor:
    json.dump(person, vystupni_soubor, ensure_ascii=False, indent=4)

