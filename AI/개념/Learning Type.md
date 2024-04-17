# 지도학습
## 개념
- 머신러닝(구몬 학습지 답지 있음)
## 회귀(Regression)
- 구체적인 답(데이터 입력의 출력)을 찾는 것
- MSE(Mean squared error) : 찾은 답과 실제 답을 비교한 오차 제곱의 평균
- MSE가 낮은 쪽으로 경사하강법을 사용

## 분류(Classification)
- 특정 분류가 맞는지 확률로 표현하는 것 
- 분류는 회귀의 일부 : 회귀의 줄력을 시그모이드(Sigmoid) 혹은 소프트맥스(Softmax) 함수에 입력시켜 확률로 표현
- Cross Entropy Loss : 회귀의 줄력이 활성화함수를 거졌기 때문에 MSE가 적합하지 않음.
- Cross Entropy Loss 가 낮은 쪽으로 경사하강법을 사용

## <img src="https://raw.githubusercontent.com/kevincms/image/main/%EC%9D%B4%EB%A1%A0/AI/MSE.png" width="15%" height="15%"/>

# 비지도학습
## 개념
- 머신러닝(구몬 학습지 답지 없음)
## 군집화
- 분류와 유사
## 차원축소(dimensionality reduction)

# 강화학습
- 학습지 없이 자기주도학습