import matplotlib.pyplot as plt
import numpy as np

plt.plot([1, 2, 3, 4])
plt.show()

plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.show()

# 스타일 지정
# x, y값 인자에 대해 선의 색상과 형태를 지정하는 포맷 문자열(Format String)을 세번째 인자에 입력할 수 있다.
# 'ro' 는 빨간색 원형 마커
# 'b-' 는 파란색의 실선을 의미한다.
# matplotlib.pyplot 모듈의 axis() 함수를 이용해서 축의 범위 [xmin, xmax, ymin, ymax]를 지정했다.
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()


# 여러 개의 그래프 그리기
# 200ms 간격으로 균일하게 샘플된 시간 (0, 0.2, 0.4, 0.6 ..... 4.8, 5.0)
# Matplotlib에서는 일반적으로 NumPy 어레이를 이용하게 되는데,
# 사실 NumPy 어레이를 사용하지 않더라도 모든 시퀀스는 내부적으로 NumPy 어레이로 변환된다.
t = np.arange(0., 5., 0.2)

# 빨간 실선, 파란 사각형, 녹색 삼각형
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()