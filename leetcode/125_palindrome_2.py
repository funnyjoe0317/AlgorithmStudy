def ispalindrome(self, s:str)->bool:
    #자료형데크 선언
    s = s.lower()

    s = re.sub('[^a-z0-9]', '',s)

    return s ==s[::-1] #슬라이싱