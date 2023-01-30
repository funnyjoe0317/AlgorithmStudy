# word = input()
# # word = str(word)
# word_list = word.split(" ")

# a=word_list.count('')
# if a >=1:
#     delete=word_list.index('')
#     del word_list[delete]

# print(len(word_list))
# 내가 시도하고 맞앗는데 백준 틀렸다고 한 답

word = input().split()
print(len(word)) 
# 그냥 스플릿 하면 알아서 공백은 사라짐;;;;





# for i in range(len(word_list)):
#     if word_list[i-1] == '':
#         delete=word_list.index('')
#         del delete[0]
# if word_list == '':
#     delete=word_list.index('')
#     del delete[0]

# for i in range(len(word_list)):
#     if word_list[i]=='':
#         del word_list[i]


# for i in range(len(word_list)):
#     if word_list[i] == '':
#         delete=word_list.index('')
#         del word_list[delete]