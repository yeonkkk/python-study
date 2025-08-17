# 리스트 주의(깊은 복사, 얕은 복사)
marks1 = [['~'] * 5 for n in range(5)]
marks2 = [['~'] * 5] * 5

print(marks1)
print(marks2)

print()

# 수정
marks1[0][1] = 'X'
marks2[0][1] = 'X'

print(marks1)
print(marks2)

# 증명
print([id(i) for i in marks1])
print([id(i) for i in marks2])