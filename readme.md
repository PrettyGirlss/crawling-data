# 🗺️3RD_PROJECT_3TEAM

<br>

## 💡**팀명 : **

<br>

✔️ 팀명 뜻 : 

✔️ 


<br>

---

## 🌟 팀원 소개

<br>

| 👩 김태연 | 👩 박지수 | 🧑 신승철 | 👩 이재은 | 👩 조해리 |
|---|---|---|---|---|
| <img src="img/taeyeon.jpg" width="150" height="190"/> | <img src="img/jisoo.png" width="150" height="190"/> | <img src="img/seungcheol.jpg" width="150" height="190"/> | <img src="img/jaeeun.png" width="150" height="190"/> | <img src="img/haeri2.png" width="150" height="190"/> |
|[@Taeyeon514](https://github.com/Taeyeon514)|[@0lipa](https://github.com/0lipa)|[@ssshinnpson](https://github.com/ssshinnpson)|[@JAEEUN0129](https://github.com/JAEEUN0129)|[@Haer111](https://github.com/Haer111)|

<br>

---

## 1. 프로젝트 개요

<br>

## **프로젝트 명 : 투어 가이드** 📚

<br>

### 1.1 프로젝트 소개
<br>

관광지 정보를 알려주고 코스를 짜주는 챗봇 개발

<br>

---

### 1.2 프로젝트 필요성

<br>

1. 관광지를 검색할 때, 놀러갈 곳을 검색할 때, 대부분 지도에 검색하거나 유튜브를 찾아보거나 블로그 or 인스타그램 검색.

→ 챗지피티를 잘 이용하지 않는다는 경험을 떠올림.

**이유: 챗지피티의 hallucination**

<예시 사진>

실제로 없는 장소인데 있는 장소인 것처럼 추천하는 경향이 있다.

실제로 있는 곳만 추출해달라고 해도 제대로 된 응답을 받기 쉽지 않음. 

1. 단순 검색 만으로는 이 관광지를 누구와 가면 좋을지, 어떤 관계에 있는 사람과(가족, 친구, 연인 등) 가면 좋을지 알기 어려움.

→ 실제로 이러한 부분 때문에 리뷰를 열심히 찾아보고 검색을 수없이 하는 경향이 있음.

1. 우리 나라 관광지에 대해 잘 모르는 경향이 있음. 실제로 관광 현황을 보면 해외여행으로 관광을 가고 싶다는 사람들이 많음(←자료필요) 그 이유 중 하나가 좋은 관광지를 잘 모르는 경우도 한몫함

⇒ 우리 나라 관광지에 대해 정확히 알려주고 코스도 추천해줄 수 있는 챗봇이 있다면 어떨까?

1. **관광지 검색 시간 감소 효과**
2. **관광 컨셉에 따른 관광지 및 코스 선정 용이**
3. **챗봇 이용률 높으면 국내 관광 현황에도 긍정적 영향 가능성**

<br>

---

### 1.3 프로젝트 목표

<br>

- 1차 목표 : hallucination이 없는 관광지 챗봇 구현
- 2차 목표 : 이에 기반해 코스를 짜주는 챗봇 구현
- 3차 목표 : 리뷰에 있는 내용들 잘 반영해 어떤 느낌을 느낄 수 있을지 얘기해주는 챗봇 구현

<br>

---



## 2.  **기술 스택 및 사용 모델** 🛠️

| **분류**         | **기술/도구**                                                                            |
|------------------|------------------------------------------------------------------------------------------|
| **Language**         | ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python)     |
| **Development**   | ![VS Code](https://img.shields.io/badge/VS%20Code-0078d7?style=for-the-badge&logo=visualstudiocode&logoColor=white) ![Colab](https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=googlecolab&color=525252)  ![RunPod](https://img.shields.io/badge/RunPod-5D29F0?style=for-the-badge&logo=runpod&logoColor=white)
| **Vector DB**	|![ChromaDB](https://img.shields.io/badge/ChromaDB-FF5CAA?style=for-the-badge&logo=chroma&logoColor=white)	|
| **Framework**	| ![LangChain](https://img.shields.io/badge/LangChain-00B8A9?style=for-the-badge&logo=langchain&logoColor=white)	|
| **Demo**	| ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)|
| **Collaboration Tool**      | ![GitHub](https://img.shields.io/badge/github-121011?style=for-the-badge&logo=github) ![Git](https://img.shields.io/badge/git-F05033?style=for-the-badge&logo=git) ![Discord](https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)|

<br>

## 사용 모델
| **분류**         | **사용 모델**                                                                             |
|------------------|-----------------------------------------------------------------------------------------|
|  **임베딩 모델**     |  SentenceTransformer (all-MiniLM-L6-v2)                              |
|  **LLM 모델**      |                  모델 이름                          |

---

## 3. 시스템 아키텍처 

### 이미지 사진 넣어야돼요

<img src="./img/WBS.png" width=700/>

<br>


---

## 4. WBS

		
<img width="964" height="409" alt="image" src="https://github.com/user-attachments/assets/ad3d9aa7-c324-4c11-9da6-90727d9254c2" />


---

## 5. 요구사항 명세서

---


## 6. 수집 데이터 및 전처리

### 6.1 수집한 데이터

- 도서관 이용에 대한 설문지를 바탕으로 이용자의 인구통계학적 정보, 이용 패턴 등을 포함하고 있는 데이터 셋 활용

<br>

**[🗨️ 서울특별시 서울시민의 도서관 이용실태 설문조사 데이터](https://www.data.go.kr/data/15051847/fileData.do#)**

<br>

| 항목 | 설명 |
| --- | --- |
| **데이터 명** | 서울특별시 서울시민의 도서관 이용실태|
| **데이터 출처** | 공공데이터포털 |
| **데이터 제공 기관** | 서울특별시 데이터전략과 |
| **데이터 설명** | 서울특별시민 도서관 이용실태 조사에 대한 데이터로 서울시민 대상(3,000명) 도서관 이용, 인식 조사 설문자료와 설문결과 데이터 |
| **주요 컬럼명** | 거주지역, 성별, 출생년도, 최종학력, 직업, 월평균 소득, 1년간 도서관 이용 경험 여부, 현재 도서관 이용 의향, 미래에 도서관 이용 의향 등 |

<br>

---

### 6.2 데이터 특징

<br>

**① 사용자 개인 특성 반영**
- 성별, 연령, 학력, 소득, 거주지역, 직업 등 인구통계학적 변수와 도서관 이용 여부 등 행동 패턴 변수를 모두 포함

**② 이탈 여부 파생 변수 생성**
- 설문 문항(미래 이용 의향 없음)을 바탕으로 ‘이탈 여부(Churn)’ 컬럼 직접 생성 가능

**③ 분류 모델 학습에 적합**
- 수치형 및 범주형 변수가 혼합된 형태로, 다양한 분류 알고리즘 실험 가능

**④ 현실적 적용 가능성**
- 실제 도서관 이용 패턴을 반영한 설문 기반 데이터로, 운영 개선에 바로 적용 가능

<br>

### 6.3 데이터 전처리 요약


---

## 7. DB 연동 구현 코드

🔗 링크

---

## 8. 테스트 계획 및 결과 보고서

### 8.1 테스트 계획
- `gender`, `age`, `education`, `income`, `experience`, `job`, `living_area`, `distance`, `future_use` 전부 결측치 없음.

  <img src="./img/결측치없음.png" width=300/> 


### 8.2 결과 보고서
- `income` : 99 → 모름/무응답 제거

  <img src="./img/income.png" width=800/>
---
## 9. 진행과정 중 프로그램 개선 노력

### 9.1 
서울시 25개 구를 경제·상권 특성으로 3개 군집화
- 기준: 거주지/소득과 도서관 이용률 간의 [상관관계](https://www.sisain.co.kr/news/articleView.html?idxno=47046)를 바탕으로
  - **Group_A**: 강남, 서초, 송파, 종로, 중구, 영등포, 용산
  - **Group_B**: 강동, 마포, 서대문, 성동, 광진, 동작, 양천
  - **Group_C**: 그 외 구

  <img src="./img/living_area_grouped.png" width=400/>

---
## 10.수행결과

###

**(1) 범주 병합**

- education (학력) 

  - 고등학교 졸업 + 대학교 중퇴 -> "고등학교 졸업"으로 변환
  - 대학교 졸업 + 전문대 졸업 + 4년제 졸업 -> "대학교 졸업"으로 변환

  <img src="./img/학력전처리.png"/> 

**(2) 이진화**

- experience (1년간 방문 경험)

  - 3 (도서관을 한 번도 이용한 경험이 없다) -> 제거
  
  - 1 (1년간 방문 경험 있다), 2 (1년간 방문 경험 없다) -> 0 (1년간 방문 경험 없다), 1 (1년간 방문 경험 있다)로 변환

    <img src="./img/1년이용전처리.png"/>
    
- gender (성별)
  - 1 (남자), 2 (여자) -> 0 (여자), 1(남자)로 변환
 
- distance (거주지와 도서관과의 인접 여부)

    - (현재 거주하는 자치구 내) + (도보 이용) => 도서관과 인접하다 (1)
    - 나머지 인접하지 않다 (0) 으로 판단

---

### 5.2. 최종 데이터 구조

#### **🔹주요 변수**

- `gender` : 성별
- `age` : 나이
- `education` : 학력 수준
- `income` : 소득 수준
- `experience` : 1년 이내 도서관 이용 여부
- `job` : 직업
- `living_area_grouped` : 거주 지역
- `distance` : 거주지와 도서관 인접 여부

#### **🔹분석 타겟 컬럼**

- `churn` : 도서관 이용자 이탈 여부 (0: 비이탈, 1: 이탈)

---

### 5.3 상관관계 분석

<img src="./img/상관관계분석.png" width=800/>

- experience(최근 1년간 도서관 이용 경험 유무), job(직업), age(나이) 순으로 상관관계가 높음 ⬆️
  
<br>

---

### 5.4 이탈률 분포

<img src="./img/이탈률experience.png" width=800/>

- 1년간 이용 경험이 있는 사람들은 이탈 확률 낮음 ⬇️, 1년간 이용 경험이 없는 사람들은 이탈 확률이 높음 ⬆️

<br>

<img src="./img/이탈률age.png" width=800/>

- 나이가 적을수록 이탈 확률 낮음 ⬇️, 나이가 많을수록 이탈 확률 높음 ⬆️


<br>

---

## 6. 머신러닝 파이프라인 🔧

### 6.1 사용 변수

- **Target**: `churn`
- **Features**: `gender`, `age`, `education`, `income`, `job`, `living_area_grouped`, `experience`, `distance`

<br>

### 6.2 Scaling & Encoding

| **변수 유형** | **변수명** | **전처리 방법** |
|---|---|---|
| 수치형 | `age` | StandardScaler |
| 명목형(순서X) | `gender`,`living_area_grouped`, `job`, `experience` | OneHotEncoder |
| 순서형 | `income`, `education` | Label Encoding |

- **파이프라인 구성**: ColumnTransformer + Pipeline

<br>

### 6.3 도서관 이탈 데이터 불균형 문제 

<img src="./img/churn_rate.png" width=300/>

- **원본 분포**: Churn 0 ≈ 89.4%, 1 ≈ 10.6%
- **적용 기법**: **SMOTEENN**

<br>

### 6.4 모델 성능 향상 전략 

#### 6.4.1 Base Model

**평가 지표** : precision / recall / F1 / accuracy

- **기본 features 구성**: 7개의 기본 features만 사용
  - `gender`, `living_area`, `job`, `age`, `education`, `income`, `child`, `experience`

  - model들을 돌렸을 때 Stacking 모델이 가장 높은 성능을 보임

<img src="./img/all_acc.png" width=500/>


  

<br>

#### 6.4.2 Updated Features

- **변수 제거**: 상관계수가 매우 낮아 상관관계가 없다고 판단된 변수 `child` 제거

- **새로운 파생변수 추가**: 
  - `living_area_grouped`: 거주지/소득과 도서관 이용률간의 상관관계가 존재한다는 [기사](https://www.sisain.co.kr/news/articleView.html?idxno=47046)를 바탕으로 지역 `living_area`를 경제·상권 특성으로 그룹화한 `living_area_grouped` 변수 추가
 
<br>

#### 6.4.3 Best Model: **Stacking Ensemble**

**Base Estimators:**
1. **RandomForestClassifier** 
2. **LightGBM** 
3. **XGBoost** 

**Final Estimator 후보:**
- logistic regression (기본)
- *RidgeClassifier
- SVC
- ElasticNet
- KNeighborsClassifier

<img src="./img/best_model.png" width=600/>




<br>

---

## 7. 하이퍼 파라미터 조정 모델 성능 결과 🖨️

**하이퍼파라미터 조정** : hyperopt를 통해 진행

<br>

#### 7.1.1 성능 비교


**하이퍼옵튜나 적용 전**

<img src="./img/best_model.png" width=500/>



**하이퍼옵튜나 적용 후**

<img src="./img/final_model.png" width=500/>


<br>

---

## 8. 인사이트 🔦

- 본 예측 모델을 활용하여 **인구통계학적 특성을 비롯한 최소한의 특성만으로** 따로 설문 조사를 진행하여 데이터를 수집할 필요 없이
  개별 및 단체 이용자의 이탈 확률을 예측 가능

### 8.1 개별 이용자 이탈 방지 전략

- **선별적 고객 관리**: 이탈 확률이 높은 고객에게만 집중적으로 개인 맞춤형 서비스(책 추천, 프로그램 소개, 개별 상담 등)를 제공

- **인력 및 예산 최적화**: 모든 이용자가 아닌 이탈 고위험 개별 사용자에게만 자원을 집중 투입하여 운영 효율성 극대화

<br>

### 8.2 단체 이용자 이탈 방지 전략

- **그룹별 고객 관리**: feature_importances가 높은 특성에 대해 그룹핑을 진행한 후 이탈 확률이 높은 그룹에게만 집중적으로 그룹 맞춤형 서비스(나이, 학력 등을 고려한 이탈방지 프로그램 진행, 지역 도서관 이벤트 등)를 제공

- **인력 및 예산 최적화**: 모든 이용자가 아닌 고위험 그룹에게만 자원을 집중 투입하여 운영 효율성 극대화

<br>

---

## 9. 한계점 🧩

### 9.1 불균형 데이터 처리
- SMOTEENN를 통한 균형 조정에도 불구하고 여전히 존재하는 test data set에서의 클래스 불균형 문제 → **낮은 precision**

<img src="./img/final_model.png" width=500/>
  


<br>

### 9.2 Train/Test Split 이전 SMOTE 적용

<img src="./img/smote_acc.png" width=600/>

실제 서비스를 운영할 환경(Production Environment)에서는 이러한 불균형이 존재할 가능성이 높음.

따라서 인위적인 데이터 비율 조정은 현실과 괴리된 평가 결과를 유발할 수 있다고 판단하여, 불균형 데이터셋을 그대로 유지한 채로 모델을 평가.

비록 모델 성능이 이상적으로 높지는 않았지만,실제 현업에 적용 가능한 신뢰 가능한 기준선(Baseline)을 확보하는 것이 더 중요하다고 판단.

<br>

- 데이터를 선택할 때, 클래스의 불균형까지 고려해서 선정할 필요성

<br>

### 9.3 개인특성 이외의 변수
- 현재 사용된 변수 외에 추가적인 파생 변수 생성 가능
  - `total reading time` : 총 독서 시간
  - `books per year` : 연간 독서량
- **제거 사유**: 총 독서시간과 연간 독서량은 처음 보는 사람의 개인 특성으로 보기에는 어려움이 있고, 또한 총 독서시간과 연간 독서량은 도서관을 이용하는 사람이면 당연히 높을 것으로 예상되는 특성이기에 제거

- 개인 특성에 해당하면서, 성능을 높일 수 있는 파생변수를 찾지 못한 것이 아쉬움
<br>



---

## 10. 수행 결과 페이지 📌

### 1️⃣ 개요

<img src="./img/page1.png" width=1000/>
   
### 2️⃣ 개인 이탈 예측

<img src="./img/page2-1.png" width=1000/>

<img src="./img/page2-2.png" width=1000/>

### 3️⃣ 단체 이탈 예측

<img src="./img/page3-1.png" width=1000/>

<img src="./img/page3-2.png" width=1000/>

### 4️⃣ 결과 분석

<img src="./img/page4.png" width=1000/>

<br>

<br>


 ### **팀원 한 줄 회고** 🧑‍💻
 
| **이름** | **회고 내용** |
|---|---|
| 양송이 |설문 기반의 패널 데이터를 이용하여 전처리하는 과정과, 모델 성능 향상을 위해 다양한 피처들의 중요도를 파악하며 여러 피처 조합을 시도하고, 이에 맞는 모델을 선정과 선정한 모델의 성능을 높히는 과정을 팀원들과 의견을 교류하며 프로젝트를 진행하였다. 이를 통하여 데이터 및 모델 성능에 대한 이해도가 높아졌다. 데이터에 따른 모델 선정 및 파라미터 조절, 팀원과 의사소통을 하며 협업하는 프로젝트가 모델 성능과 결과 해석에 얼마나 중요한지 체감할 수 있었다. |
| 박지수 | 저번 미니 프로젝트에서 신뢰 가능한 데이터를 찾지 못했다는 아쉬움이 있었습니다. 그래서 이번 2차 프로젝트에서는 이를 보완하기 위해 데이터 수집 과정에서 주제와 데이터 신뢰도, 컬럼의 다양성 등을 전반적으로 고려하였고, 좋은 데이터셋을 선정했다고 생각합니다. 가장 많은 고민을 했던 부분은 설문조사 데이터를 전처리하는 과정이었습니다. 어떤 질문의 어떤 답변을 데이터로 뽑아낼지, 6-7개로 나눠진 답변들을 어떤 기준으로 병합하면 좋을지 애매한 부분이 많았습니다. 특히 이탈의 기준을 무엇으로 잡을지에 대한 논의가 프로젝트 기간 내내 이어졌습니다. 이 과정에서 설문조사 데이터 전처리와 관련한 기법이나 규칙이 있는지 조사하고 공부해야겠다는 필요성을 느꼈습니다. 또, 인사이트라는 개념 자체가 와닿지 않아 방향성을 설정하기가 어려워 아쉬움이 많았습니다. 이후 인사이트가 무엇인지, 인사이트 도출을 어떤 데이터를 가지고 어떤 방향성으로 하는지 많이 접하고 공부해보아야겠다고 생각했습니다. 마지막으로 SMOTE 기법을 써서 성능을 올린 모델을 신뢰할 수 있을까 의문이 들어서, 보통은 어떤식으로 데이터 불균형을 해결하는지 조사해봐야겠다고 생각했습니다. |
| 조세희 |데이터에 따라 피처별로 스케일링 기법, 모델 선정, 파이프라인 구성 등 성능을 높이기 위하여 다양한 시도 하고, 프로젝트 목적에 맞는 학습 피처 선택과 우선으로 해야 할 성능지표 등 목적에 맞춰야 할 다양한 조건들을 생각하게 되는 계기가 되어 기분 좋은 프로젝트가 되었다. 아쉬웠던 점은 사용한 스태킹 모델에 원본 피처 데이터를 전달하는 passthrough=True옵션을 사용했다면 성능이 조금 더 나아지지 않았을까 생각이 든다. 모든 옵션을 사용해 보지 못한 것이 많이 아쉬웠다. 세세한 하이퍼파라미터 옵션 조절에 대하여 공부를 더 할 필요성을 느꼈다.|
| 김세한 | 모델 성능 특히 precision 값을 올리기 위해 다양한 방법을 사용한 것과 설문지 데이터를 정제하여 데이터프레임으로 만든 과정이 인상깊었습니다. |
| 양정민 |프로젝트를 진행하며, 이론적 근거 제시를 위한 논문 요약과 자료 조사 이에 따른 필요한 데이터 전처리를 하였으며 전처리를 통하여 정리한 데이터로 학습이 진행되어 가는 모습을 지켜보았다. 모델 학습에 직접적으로 가담하지는 않았지만 모델별 차이점과 파라미터 조절 등 성능을 올리는 방법을 배우게 되었다. 이번 프로젝트를 진행하며 모델성능 및 평가 부분에서 부족한 점을 알게되어 스스로 성장 후 다음 프로젝트의 발판이 되었으면 좋겠다. |
