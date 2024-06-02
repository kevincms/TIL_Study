# Tailwind css
- 기본적인 css는 tag, class, id을 바탕으로 아래 코드와 같이 스타일을 지정할 수 있다.
- Tailwind css는 미리 만들어둔 라이브러리를 가져다가 쓰는 느낌이다.

```javascript
p {
  color: red;
}
```


# Tailwind css in Reflex
- Reflex에서는 아래와 같이 class_name 속성을 추가하여 tailwind css를 사용할 수 있다.

```python
rx.box(
    "Hello World",
    class_name="text-4xl text-center text-blue-500",
)
```

- https://reflex.dev/docs/styling/overview/
