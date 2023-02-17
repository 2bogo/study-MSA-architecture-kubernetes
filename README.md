# study-MSA-architecture-kubernetes

- LIKELION kakaoenterprise [도커/쿠버네티스 온라인 부트캠프] 1기 수업

## MSA (MicroService Architecture)
> application logic을 각각의 작은 component로 구현하고 이를 조합하는 framework

### 프로젝트 내용
- 주어진 소스(html로만 구성된 영화 예제 사이트)를 사용해 MSA 아키텍처로 구성하고 kubernetes에 배포하는 실습을 수행

### MSA 구성
- UI의 틀을 구성하는 container
- 영화 정보데이터가 있는 REST API

### 실행

```sh
kubectl apply -f kubernetes/
```
