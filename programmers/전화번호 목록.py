def solution(phone_book): 
    # 이거 쓰기
    # answer = True
    # for i, word in enumerate(phone_book):
    #     for j in range(i+1, len(phone_book)):
    #         if phone_book[j].startswith(word):
    #             return False
    answer = True
    phone_dict = {}
    
    for number in phone_book:
        phone_dict[number] = True
    # print(phone_dict)
        
    for number in phone_book:
        prefix = ''
        # print(number)
        for digit in number:
            prefix += digit
            # print(prefix)
            # print(number)
            # print(phone_dict)
            if prefix in phone_dict and prefix != number:
                # 이곳이 이해가 안될수 있는데 119가 있으면 1195524421도 있으니까
                # 1195524421이 119로 시작하는지 확인하는 것이다.   
                # print(number)
                # print(prefix)
                answer = False
                break
        if not answer:
            break
            
    return answer

S = ["119", "97674223", "1195524421"]
per = 	{"119":True, '97674223': True, '1195524421': True}
if "119" in per:
    print('True')
else:
    print('False')