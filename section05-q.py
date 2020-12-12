# Section05-3
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈(정답은 영상)

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
for k,v in q1.items():
    if k == '가을':
        print(v)


# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
for k,v in q2.items():
    if k=='사과' or v =='사과':
        print(k,v)
        break
else:
    print('사과 없음')



# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점
q3=80
if q3>80 and q3<=100:
    print("A학점")
elif q3>60 and q3<=80:
    print("B학점")
elif q3>40 and q3<=60:
    print("C학점")
elif q3>20 and q3<=40:
    print("D학점")
else :
    print("E학점")



# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18
q4=[12,6,18]
tempQ4=0
for k in q4:
    if(k>tempQ4):
        tempQ4=k
    
print(tempQ4)



# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)
name='891022-2473837'
index=name.index('-')+1


if name[index]=='1' or name[index]=='3':
    print("남자")
elif name[index]=='2' or name[index]=='4' :
    print("여자")

# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정"]
for k in q3:
    if k == '정':
        continue
    print(k, end='')

print()

q5=[x for x in q3 if x != '정' ]
print(q5)

# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.
for k in range(1,101):
    if(k%2!=0):
        print(k,end=' ')
    

print()

q6=[x for x in range(1,101) if x % 2 !=0]
print(q6)

# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]
for k in q4:
    if len(k)>=5:
        print(k, end=' ')

print()
# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]
for k in q5:
    if k.islower():
        print(k, end=' ')

print()

# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]

for k in q6:
    if k.isupper():
        print(k.lower(),end=' ')
    else:
        print(k.upper(),end=' ')

print()



#일반적 방법
numbers = []

for n in range(1,101):
    numbers.append(n)
print(numbers)

# 리스트 컴프리헨션
numbers2 = [x for x in range(1,101)]
print(numbers2)

#x = [y for  y in range(1,100) if y%2!=0]
#print(x)