from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque(maxlen=cacheSize)
    
    for city in cities:
        city = city.lower()
        # 들어오는 문자 소문자로 만들기
        # cache.append(city)
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:
            # if len(cache) ==3:
            #     cache.remove(city)
            cache.append(city)
            answer += 5
            
            
    
    return answer