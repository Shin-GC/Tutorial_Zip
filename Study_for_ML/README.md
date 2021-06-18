# Study_for_ML

### 머신러닝을 위한 파이썬 공부를 모아놓는 곳 입니다.


* Numpy 

* edwith [Python]

* linear algebra [선형대수학]


## Site
### https://www.boostcourse.org/ai222/
### https://ko.khanacademy.org/math/linear-algebra/vectors-and-spaces

---

🔥  사이킷런은 입력 데이터에서 샘플이 행에 위치하고 특성이 옆에 놓여있다고 기대한다.

---

# 배경지식

---

인공지능 [ Artificial intelligence ]
: 사람처럼 학습하고 추론할 수 있는 지능을 가진 컴퓨터 시스템을 만드는 기술

---

- 인공 일반지능 [ Artificial general intelligence ] 및 강인공지눙 [Strong AI ] 이란?
: 사람과 구분하기 어려운 지능을 가진 컴퓨터 시스템

- 약 인공지능 [Week AI]
: 특정 분야에서 사람의 일을 도와주는 보조 역활을 하는 인공지능

---

머신러닝 [ Machine Learning ]
: 규칙을 프로그래밍 하지 않아도 자동으로 데이터에서 규칙을 학습하는 알고리즘을 연구하는 분야
[ 인공지능의 하위 분애 중에서 지능을 구현하기 위한 소프트웨어를 담당하는 핵심 분야 ]

- 대표적인 머신러닝 라이브러리 사이킷런 [ Scikit-learn ]

: Scikit-learn 은 Python API를 사용한다.

---

딥 러닝 [ Deep Learning ]
: 인공 신경망 [ Artificial neural network ]을 기반으로 한 방법들을 통칭한 것

- 대표적인 딥러닝 라이브러리 텐서플로 [ TensorFlow ] 와 파이토치 [ PyTorch ]

: TensorFlow와 PyTorch 둘다 인공 신경망 알고리즘을 전문으로 다루며, 파이썬 API를 제공한다.

---

입력 [ Input ]
: 데이터
타깃 [ Target ]
: 정답
이 둘을 합쳐서 훈련 데이터 **[ Training data ]** 라고 한다

---

지도 학습 [ Supervised Learning ]
: 지도학습은 훈련하기 위한 데이터와 정답이 필요
: 입력과 타깃을 전달하여 모델을 훈련시키며 새로운 데이터를 예측하는데 활용한다.
ex) K-최근접 알고리즘 [ K-Nearest Neighbor Algorithm]

비지도 학습 [ Unsupervised Learning ]
: 타깃데이터가 없다.
: 무엇을 예측할 때 보단 입력 데이터에서 어떤 특징을 찾는데 주로 활용한다.

---

훈련 세트 [ Training Set ]
: 모델을 훈련할 때 사용하는 데이터로, 훈련세트가 클 수록 좋다.
따라서, 테스트 세트를 제외한 모든 데이터를 훈련세트로 사용한다.

테스트 세트 [ Test Set ]
: 전체 데이터의 20~30%를 사용하는 경우가 많으며, 전체 데이터가 아주 크다면 1%로도 충분할 수 있다.

---

샘플링 편향 [ Sampling bias ]
: 훈련 세트와 테스트 샘플이 골고루 섞여 있지 않아 샘플링이 한쪽으로 치우친 상태
🔥훈련 세트와 테스트 세트가 잘 못 만들어져 전체 데이터를 대표하지 못하는 현상

---

* 표준점수 [ Standard Score ]
> 각 데이터가 원점에서 몇 표준편차만큼 떨어져 있는지를 나타내는 값
: 훈련 세트의 스케일을 바꾸는 대표적인 방법 중 하나로, 표준점수를 얻으려면 특성의 평균을 빼고 표준편차로 나눈다.
:* 🔥 반드시 훈련 세트의 평균과 표준편차로 테스트 세트를 바꿔야한다.

- 표준점수 구하기

    ```python
    # 평균 구하기
    mean = np.mean(train_input, axis=0)
    #표준편차 구하기
    std = np.std(train_input, axis=0)
    #표준점수 구하기 평균값을 뺀 후 표준편차로 나누기
    train_scaled = (train_input - mean) / std
    #Broadcasting으로 인해 모든 행에서 적용 된다.
    ```

---

> 브로드캐스팅 [ Broadcasting ]

: 크기가 다른 넘파이 배열에서 자동으로 사칙 연산을 모든 행이나 열로 확장하여 수행하는 기능

---

 분류 [ Classification ]
: 머신러닝에서 여러 개의 종류 [혹은 클래스(class)] 중 하나를 구별해 내는 문제를 classification 라고 부른다.

특성 [ Feature ]
: 머신러닝에서 feature 란 데이터를 표현하는 하나의 성질이다.

훈련 [ Training ]
: 머신러닝 알고리즘이 데이터에서 규칙을 찾는 과정을 말한다.
[  Scikit-learn 에서는 fit() 메서드가 하는 일. ]

모델 [ Model ] 이란?
: 머신러닝 알고리즘을 구현한 프로그램 또는 알고리즘을 구체화하여 표현한 것을 모델이라고 한다.

---

> 회귀 [ Regression ]

: 임의의 수치를 예측하는 문제로 타깃값도 임의의 수치가 된다.
[ 두 변수 사이의 상관관계를 분석하는 방법 ]

---

과대적합 [Over-fitting]
: 모델의 훈련 세트 점수가 테스트 세트 점수보다 훨씬 높은 경우를 의미

→ 훈련세트에만 잘 맞는 모델이라 나중에 실전 투입 시 새로운 삼플에 대한 예측이 잘 동작하지 않는 문제 발생

과소적합 [Under-fitting]
: 모델의 훈련 세트와 테스트 세트 점수가 모두 동일하게 낮거나 테스트 세트 성능의 오히려 더 높은 경우를 의미한다.

→ 모델이 너무 단순하여 훈련 세트에 적절히 훈련되지 않은 경우로 훈련 세트가 전체 데이터를 대표한다고 가정하기 때문에 훈련 세트를 잘 학습하는 것이 중요하다.

해결 방법
→ 과대적합 일 경우 모델을 덜 복잡하게 만들어야 하므로 K-최근접 이웃의 경우 K 값을 늘린다.
    과소적합 일 경우 모델을 더 복잡하게 만들어야 하므로 K-최근접 이웃의 경우 K 값을 줄인다.

---

회귀 [ Regression ] 에서는 정확한 숫자를 맞힌다는 것은 거의 불가능하기 때문에
정확도를 결정계수 [ Cofficient of determination ] 이라고 부르며 간단히 $R^2$ 라고 부른다.

---

> 결정 계수를 구하는 법

$$1-\frac {(타깃-예측)^2의합}{(타깃-평균)^2의 합} $$

타깃이 평균정도를 예측하는 수준이라면 $R^2$은 0에 가까워지고, 예측이 타깃에 아주 가까워지면 1에 가까운 값이 된다.

---
# 알고리즘

K-최근접 이웃 알고리즘 [ K-Nearest Neighbor ] : K-NN 
: 어떤 데이터에 대한 답을 구할 때, 주위의 다른 데이터를 보고 다수를 차지하는 것을 정답으로 사용.

# 핵심 패키지 및 함수

- Matplotlib
    - Scatter(x, y, c='색깔')
    : 산점도를 그리는 함수로서, 처음 2개의 매개변수로 x축 값과 y축 값을 전달해주며, 이 값은 파이썬 리스트 또는 넘파이 배열이며, c 매개변수로 색깔을 지정할 수 있다. [ Default : 10가지 기본 색으로 지정]
    - marker 매개변수로 마커 스타일을 지정해줄 수 있으며 기본 값은 o (Circle : 원) 이다.

---

- Scikit-learn
    - **KNeighborsClassifier()**
    : k-최근접 이웃 분류 모델을 만드는 Scikit-learn Class로 n_neighbors 매개변수로 이웃 개수를 지정할 수 있으며, p 매개변수로 거리를 재는 방식을 지정할 수 있는데 1은 맨해튼 거리, 2는 유클리디안 거리를 사용하며 Default 값은 2인 유클리디안 거리를 사용한다.

    ---

    - **fit()**
    : Scikit-learn model을 Training할때 사용하는 메서드로 처음 두 매개변수로 훈련에 사용할 특성과 정답 데이터를 전달한다.

    ---

    - **Predict()**
    : Scikit-learn model을 Training하고, predict [예측] 할때 사용하는 메서드로 특성데이터 하나만 매개변수로 받는다.

    ---

    - **Score()**
    : Training한 Scikit-learn model의 성능을 측정하는 메서드로 처음 두 매개변수로 특성과 정답 데이터를 전달하며, Predict() 메서드로 예측을 수행한 다음 분류 모델일 경우 정답과 비교하여 올바르게 예측한 개수의 비율을 반환한다.

    ---

    - **train_test_split()**
    : 훈련 데이터를 훈련 세트와 테스트 세트로 나누는 함수로, 여러개의 배열을 전달 할 수 있다
    : 테스트 세트로 나누는 비율은 test_size 매개변수로 지정할 수 있으며 기본값은 0.25이다.
    : Shuffle 매개변수로 훈련 세트와 테스트 세트로 나누기 전에 무작위로 섞을지 여부를 결정할 수 있으며                   
     기본값은 True이다.
    : stratify 매개변수에 클래스 레이블이 담긴 배열 (일반적으로 타깃 데이터)을 전달하면 클래스 비율에
      맞게 훈련 세트와 테스트 세트를 나눈다.
        - ex

            ```python
            from sklearn.model_selection import train_test_split

            train_input, test_input, train_target, test_target = train_test_split(fish_data, fish_target, stratify = fish_target, random_state=42)
            ```

    ---

    - **Kneighbors()
    : k-최근접 이웃 객체의 메서드로, 입력한 데이터에 가장 가까운 이웃을 찾아 거리와 이웃 샘플의 인덱스를 반환해준다.
    : 기본적으로 이웃의 개수는 클래스의 객체를 생성할 때 지정한 개수를 사용하며, n_neighbors 매개변수에서 따로 지정이 가능하다.
    : return_distance 매개변수를 False로 지정하면 이웃 샘플의 인덱스만 반환하고 거리는 반환하지 않는다.**
        - ex

            ```python
            distances, indexes = kn.kneighbors([[25,150]])
            ```

    ---

    - KNeighborsRegressor()
    : k-최근접 이웃 회귀 모델을 만드는 사이킷런 클래스로 n_neighbors 매개변수로 이웃의 개수를 지정해주며 default 값은 5이다.

        : 다른 매개변수들은 KNeighborsClassifier 클래스와 동일하다.

        - ex

            ```python
            from sklearn.neighbors import KNeighborsRegressor

            knr = KNeighborsRegressor() #객체 생성

            knr.fit(train_input, train_target) #훈련

            knr.score(test_input, test_target) #점수
            ```

    ---

    - mean_absolute_error()
    : 회귀 모델의 평균 절댓값 오차를 계산해주며 첫번째 매개변수로 target, 두번째 매개변수로 predict 값을 전달해준다.
    : 비슷한 함수로 평균 제곱 오차를 계산하는 mean_squared_error() 있으며 이 함수는 타깃과 예측을 뺀 값을 제곱한 다음 전체 샘플에 대해 평균한 값을 반환 해준다.
        - ex

            ```python
            test_prediction = knr.predict(test_input) #예측 값
            mae = mean_absolute_error(test_target, test_prediction)
            ```

---

- Numpy
    - array()

        배열 생성 : np.array([리스트])

        ```python
        input_arr = np.array(fish_data)
        ```

    - Shape():

        배열의 크기를 알려주는 속성

        ```python
        input_arr.shape
        ```

    - arange()

        : 일정 범위를 가진 배열을 생성하는 함수

        ```python
        	np.arange(1,11) # 1부터 10까지 1의 간격을 가진 배열 생성

        	np.arange(1,11,2) # 1부터 10까지 2의 간격을 가진 배열 생성
        ```

    - shuffle()

        : Numpy 의 random 패키지안에 있는 주어진 배열을 무작위로 섞는 함수
        🔥다차원 배열일 경우엔 첫 번째 축(행)에 대해서만 섞는다.

        ```python
        np.random.shuffle(index)
        ```

    - array indexing

        배열 인덱싱 [ array indexing ]은 1개의 인덱스가 아닌 여러개의 인덱스로 한 번에 여러 개의 원소를 선탁핼 수 있는 기능이다.

        ```python
        input_arr[[1,3]]
        ```

    - seed()

        Numpy에서 난수를 생성하기 위한 정수 초깃값을 지정하여 초깃값이 같을 시 동일한 난수를 뽑게 해주는 함수로, 랜덤 함수의 결과를 동일하게 재현하고 싶을 때 사용한다.

        ```python
        np.random.seed(정수값)
        ```

    - column_stack()

        : 전달 받은 리스트를 일렬로 세운 다음 차례대로 나란히 연결하는 함수

        ```python
        np.column.stack(([1,2,3],[4,5,6]))

        # array([[1,4],
        #				[2,5],
        #				[3,6]])
        ```
