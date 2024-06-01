import reflex as rx

# GUI 기능 동작 클래스 - 기본적으로 input, textarea와 동일
class SelectControlled(rx.State):
    type: list[str] = ["apple", "grape", "pear"]

    value: str = "apple"

    # 입력된 선택지를 클래스 변수로 바꾸는 함수
    def set_type(self,value): # on_change에 함수를 지정하면 input값을 해당 함수의 인자로 반환한다. input은 값이 변화할 때(text에 글을 쓰거나 지울 때)마다 반환된다.
        self.value=value


def select_example():
    return rx.vstack(
        rx.select(
            # list의 value로 선택지 구성.
            SelectControlled.type,
            # 기본 선택지 설정
            default_value=SelectControlled.type[0],
            # 선택지를 저장하는 변수 (input, textarea와 마찬가지로 달라진 값이 적용되지 않는다. onchange로 결정해야 한다.)
            value=SelectControlled.value,
            # 선택지의 변화가 있을 때 원하는 함수 실행
            on_change=SelectControlled.set_type,
        ),
    )