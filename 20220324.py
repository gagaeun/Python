# 1번
# letters = 'python'
# print(letters[0])
# print(letters[2])

# 2번
# string = "PYTHON"
# a = ''
# for i in string:
#     a = i + a
# print(a) 

# 3번
# url = input('주소를 입력하세요 : ')
# domain = url.find('kr')
# print(domain)
# print(url[domain])

# # 4번
# file_name = "보고서.xlsx"
# a = ".xlsx"
# print(file_name.endswith(a))

# 5번
# file_name = "2020_보고서.xlsx"
# a = "2020"
# print(file_name.startswith(a))

# 6번
# score = int(input('점수를 입력하세요 : '))
# if 100 >= score and score >= 81: 
#     print('A')
# if 80>= score and score >= 61: 
#     print('B')
# if 60 >= score and score >= 41: 
#     print('C')
# if 40 >= score and score >= 21: 
#     print('D')
# if 20 >= score and score >= 0: 
#     print('E')

# 7번
# cook = ["피자","김밥","만두","양념치킨","족발","피자","김치만두","쫄면","소시지","라면","팥빙수","김치전"]
# cnt = 0
# for a in cook:
#     cnt += 1
# print(cnt)

# 8번
# warn_investment_list = ["Microsoft", "Google","Naver","Kakao","SAMAUNG","LG"]
# investment = input("종목명을 입력하세요 : ")
# for i in warn_investment_list:
#     a = i.find(investment)
# if a >= 0:
#     print('투자 경고 종목입니다')
# else : 
#     print('투자 경고 종목이 아닙니다')

# 9번
# list = [100,200,300]
# a = []
# for i in list:
#     a.append(i+10)
# print(a)

#10번
# list = ["SK하이닉스", "삼성전자","LG전자"]
# for i in list:
#     print(len(i))