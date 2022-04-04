def reorderLogFiles(logs):
    """
    :type logs: List[str]
    :rtype: List[str]
    """
    letters = []
    letter_indicators = []
    digits = []

    for log in logs:
        arrays = log.split()
        if arrays[1].isdigit():
            digits.append(log)
        else:
            letter_indicators.append(arrays[0])
            letters.append(log)

    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

    return letters + digits


case = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]
print(reorderLogFiles(case))