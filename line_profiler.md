
CPU 병목원인을 찾아주는 도구로 한줄씩 프로파일링 해주는 `line_profiler`를 사용해 보겠습니다.

- 프로파일링(profiling): 프로그램의 시간 복잡도 및 공간(메모리) 등 분석
- 병목(bottleneck): 전체 시스템의 성능이나 용량이 하나의 구성 요소로 인해 제한을 받는 현상

고성능 파이썬 책을 읽고 따라해보고 고찰한 것입니다. <br>
쥘리아집합 예제를 사용할 것입니다.
- 쥘리아 집합: 복작합 그림을 생성하는 프렉탈

자세한 건 저도 잘 모르고, CPU와 RAM사용량을 측정하기에 좋은 예제라고 합니다. [자세한 설명](https://ko.wikipedia.org/wiki/%EC%A5%98%EB%A6%AC%EC%95%84_%EC%A7%91%ED%95%A9)은 링크를 참조해주세요.

---

# 시작
#### 일단 설치
<pre><code>pip install line_profiler</code></pre>

[코드]()


kernprof -l -v  julia_example.py

`-l`은 결과를 한줄씩 출력
`-v`는 lprof파일 반환이 아니라 출력

## 결과
![image](https://user-images.githubusercontent.com/37397737/76531560-badc9600-64b8-11ea-952d-4d82d45d90e2.png)
![image](https://user-images.githubusercontent.com/37397737/76531722-fd9e6e00-64b8-11ea-919b-0502b10d2f11.png)
![image](https://user-images.githubusercontent.com/37397737/76531802-1444c500-64b9-11ea-96b2-fb71c3e909ff.png)

- https://ko.wikipedia.org/wiki/%EC%A5%98%EB%A6%AC%EC%95%84_%EC%A7%91%ED%95%A9
- 고성능 파이썬 책
- https://github.com/scari/high_performance_python/