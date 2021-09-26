import matplotlib.pyplot as plt

# xlabel(), ylabel() 함수를 사용하면 x, y 축에 대한 레이블을 표시할 수 있다.
# Keyword: plt.xlabel(), plt.ylabel(), plt.axis(), labelpad, fontdict, loc

# 기본 사용
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.xlabel('X-Label')
plt.ylabel('Y-Label')
plt.show()

# 여백 지정하기
# labelpad는 그래프와 label 간의 여백을 지정한다.
plt.plot([1, 2, 3, 4], [2, 3, 5, 10])
plt.xlabel('X-Axis', labelpad=15)
plt.ylabel('Y-Axis', labelpad=20)
plt.show()

# 폰트 설정하기
# fontdict로 축 레이블의 폰트 스타일을 설정할 수 있다.
plt.plot([1, 2, 3, 4], [2, 3, 5, 10])
plt.xlabel('X-Axis', labelpad=15, fontdict={'family': 'serif', 'color': 'b', 'weight': 'bold', 'size': 14})
plt.ylabel('Y-Axis', labelpad=20, fontdict={'family': 'fantasy', 'color': 'deeppink', 'weight': 'normal', 'size': 'xx-large'})
plt.show()

font1 = {'family': 'serif',
         'color': 'b',
         'weight': 'bold',
         'size': 14
         }

font2 = {'family': 'fantasy',
         'color': 'deeppink',
         'weight': 'normal',
         'size': 'xx-large'
         }

plt.plot([1, 2, 3, 4], [2, 3, 5, 10])
plt.xlabel('X-Axis', labelpad=15, fontdict=font1)
plt.ylabel('Y-Axis', labelpad=20, fontdict=font2)
plt.show()

# 레이블 위치 지정하기
# xlabel() 함수의 loc 파라미터는 X축 레이블의 위치를 지정한다. ({‘left’, ‘center’, ‘right’})
# ylabel() 함수의 loc 파라미터는 Y축 레이블의 위치를 지정한다. ({‘bottom’, ‘center’, ‘top’})
plt.plot([1, 2, 3, 4], [2, 3, 5, 10])
plt.xlabel('X-Axis', loc='right')
plt.ylabel('Y-Axis', loc='top')
plt.show()