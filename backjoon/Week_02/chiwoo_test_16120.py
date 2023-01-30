import sys
input= sys.stdin.readline

N=list(input().strip())

stack=[]

i=0
temp=""
while 1:
    if not stack:
        temp=str(N.pop())
        stack.append(temp)
    else:
        while 1:
            if stack:
                if len(stack)>=4 and temp=="P":
                    #print(stack[-1],stack[-2],stack[-3],stack[-4] )
                    if stack[-1]=="P"and stack[-2]=="P" and stack[-3]=="A"and stack[-4]=="P" :
                        cnt=0
                        while cnt<3:
                            stack.pop()
                            cnt+=1
            if len(stack)==1 and stack[0]=="P" and N==[]:
                print("PPAP")
                exit(0)
            elif stack and N==[]:
                print("NP")
                exit(0)
            temp=str(N.pop())
            stack.append(temp)