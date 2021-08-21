def solution(N,number):
    dp_table = [[]] # 인덱스가 N을 몇 번 사용했는지 나타냄
    for i in range(1,8+1): # N 조건이자 사용 횟수 조건(8보다 크면 -1 리턴)
        case = []
        for j in range(1,i):
            for k in dp_table[j]: # j번 사용한 경우의 수 원소
                for l in dp_table[i -j]:
                    case.append(k + l)
                    if k - l >= 0:
                        case.append(k - l)
                    case.append(k * l)
                    if l != 0 and k != 0:
                        case.append(k // l)
        case.append(int(str(N) * i)) # 숫자를 i 번 이어 붙인 경우 ex) 55, 555

        if number in case:
            return i
        dp_table.append(list(set(case)))
    return -1 



result = solution(5, 31168)
print(result)