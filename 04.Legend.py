import matplotlib.pyplot as plt

# 범례(Legend) 표시하기
# 범례는 그래프에 데이터의 종류를 표시하기 위한 텍스트이다.
# Keywork: plt.legend(), label, loc, ncol, fontsize, frameon, shadow, 범례

# 기본 사용
plt.plot([1, 2, 3, 4], [2, 3, 5, 10], label='Price ($)')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.legend()

plt.show()

# 위치 지정하기
plt.plot([1, 2, 3, 4], [2, 3, 5, 10], label='Price ($)')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
# plt.legend(loc=(0.0, 0.0))
# plt.legend(loc=(0.5, 0.5))
# plt.legend(loc=(1.0, 1.0))

# lower, upper, left, right, center
plt.legend(loc='lower right')
plt.show()


# 열 개수 지정하기
# ncol 파라미터는 범례에 표시될 열의 개수를 지정한다.
plt.plot([1, 2, 3, 4], [2, 3, 5, 10], label='Price ($)')
plt.plot([1, 2, 3, 4], [3, 5, 9, 7], label='Demand (#)')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.legend(loc='best')          # ncol = 1
#plt.legend(loc='best', ncol=2)    # ncol = 2

plt.show()


# 폰트 크기 지정하기
plt.plot([1, 2, 3, 4], [2, 3, 5, 10], label='Price ($)')
plt.plot([1, 2, 3, 4], [3, 5, 9, 7], label='Demand (#)')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
# plt.legend(loc='best')
plt.legend(loc='best', ncol=2, fontsize=14)

plt.show()


# 범례 테두리 꾸미기
plt.plot([1, 2, 3, 4], [2, 3, 5, 10], label='Price ($)')
plt.plot([1, 2, 3, 4], [3, 5, 9, 7], label='Demand (#)')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
# plt.legend(loc='best')

# frameon : 범레 텍스트 상자의 테두리를 표시할지 여부를 지정한다.
# shadow : 텍스트 상자에 그림자를 표시할 수 있다.
# 이 외에도 legend() 함수에는 facecolor, edgecolor, borderpad, labelspacing과 같은 다양한 파라미터가 있다.
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html
plt.legend(loc='best', ncol=2, fontsize=14, frameon=True, shadow=True)

plt.show()