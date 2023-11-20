# PriorityQueue

## 1. PriorityQueue 란?

* 입력된 순서에 의해 pop되는 queue와 는 달리,

* 입력된 원소의 값중 `가장 작은값이 pop`되는 특성을 가지고 있다.

## 2. 선언 방법

```python
from queue import PriorityQueue

que = PriorityQueue()

que.put("abc")
que.put("_sss")
que.put("123")

# 123이 pop
que.get()

# _sss이 pop
que.get()

# abc가 pop
que.get()

que2 = PriorityQueue()
que2.put((1, "hello"))
que2.put((0, "world"))

# (0, "world") pop
que2.get()

# (1, "hello") pop
que2.get()
```