import matplotlib.pyplot as plt

# 축 범위 지정하기
# matplotlib.pyplot 모듈의 xlim(), ylim(), axis() 함수를 사용하면 그래프의 X, Y축이 표시되는 범위를 지정할 수 있다.

# 기본 사용 - xlim(), ylim()
plt.plot([1, 2, 3, 4], [2, 3, 5, 10])
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.xlim([0, 5])      # X축의 범위: [xmin, xmax]
plt.ylim([0, 20])     # Y축의 범위: [ymin, ymax]

plt.show()


# 기본 사용 - axis()
# axis() 함수에 입력한 리스트 (또는 튜플)는 반드시 네 개의 값 (xmin, xmax, ymin, ymax)가 있어야 한다.
# 입력값이 없으면 데이터에 맞게 자동으로 범위를 지정한다.
plt.plot([1, 2, 3, 4], [2, 3, 5, 10])
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.axis([0, 5, 0, 20])  # X, Y축의 범위: [xmin, xmax, ymin, ymax]

plt.show()


# 옵션 지정하기
# 'on' | 'off' | 'equal' | 'scaled' | 'tight' | 'auto' | 'normal' | 'image' | 'square'
plt.plot([1, 2, 3, 4], [2, 3, 5, 10])
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
# plt.axis('square')
plt.axis('scaled')

plt.show()


# 축 범위 지정하기
plt.plot([1, 2, 3, 4], [2, 3, 5, 10])
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

# 그래프 영역에 표시되는 X축, Y축의 범위를 각각 반환한다.
x_range, y_range = plt.xlim(), plt.ylim()
print(x_range, y_range)

# axis 함수는 그래프 영역에 표시되는 X, Y축의 범위를 반환한다.
axis_range = plt.axis('scaled')
print(axis_range)

plt.show()