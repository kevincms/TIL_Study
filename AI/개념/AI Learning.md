# 머신러닝(Machine Learning)

## 개념
- 데이터를 바탕으로 학습하여 데이터의 입력(문제)과 출력(답)의 관계를 추측하는 방법
## 선형 회귀(Linear Regression)
### 선형 기저 함수 모델(Linear Basis Function Models)
- 지도학습 - 회귀(Regression)
- 기본 형태 : w<sub>0</sub>x+w<sub>1</sub>
- <img src="https://raw.githubusercontent.com/kevincms/image/main/%EC%9D%B4%EB%A1%A0/AI/Linear%20Regression.png" width="15%" height="15%"/>

- 기본 형태외에 다른 함수 : w<sub>0</sub>e<sup>w<sub>1</sub>a</sup>+w<sub>2</sub> 등
- - <img src="https://raw.githubusercontent.com/kevincms/image/main/%EC%9D%B4%EB%A1%A0/AI/Linear%20Basis%20Function%20Models.png" width="15%" height="15%"/>
- x(데이터의 입력)과 w(가중치)가 linear 한 함수 모델이면 모두 성립한다. [https://youtu.be/PyzBX93icz0?si=NMAcCM9WzjONxpg6&t=358]

- 데이터의 입력 x의 차원이 2차원 이상이면 행렬을 이용해 계산한다.


### 로지스틱 회귀
- 지도학습 - 분류(Classification)
- w<sub>0</sub>x+w<sub>1</sub> 를 시그모이드 혹은 소프트맥스 함수에 대입

## 딥러닝(Deep Learning)
- 신경망 이용한 머신러닝

