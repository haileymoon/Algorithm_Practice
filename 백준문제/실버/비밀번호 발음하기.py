#모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
#모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
#같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.
vowels = ["a","e","i","o","u"]

def continuous_check(pwd):
    vowel_count = 0
    consonant_count = 0
    past_letter = ""
    exclude = ["e", "o"]
    global vowel_exist
    pwd_list = list(pwd)
    while pwd_list:
        letter = pwd_list.pop()

        if letter in vowels:
            consonant_count = 0
            vowel_count += 1
            vowel_exist = True
        else:
            vowel_count = 0
            consonant_count += 1

        if past_letter == letter and past_letter not in exclude:
            #print("연속적 글자")
            return True
        past_letter = letter
        if vowel_count >= 3 or consonant_count >= 3:
            #print("3이상")
            return True
    return False

answer = ""
while True:
    vowel_exist = False
    pwd = input()
    if pwd == "end":
        break
    if continuous_check(pwd):
        answer = "not acceptable."
    elif vowel_exist == False:
        answer = "not acceptable."
    else:
        answer = "acceptable"
    print(f"<{pwd}> is "+answer)


