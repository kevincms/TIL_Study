import reflex as rx

# GUI 기능 동작 클래스
class TextAreaControlled(rx.State):
    text: str = ""

    # 입력된 text를 클래스 변수로 바꾸는 함수
    def set_text(self,text): # on_chage의 경우 인자로 input을 반환한다.
        self.text=text


# GUI 구성 함수
def controlled_example():
    return rx.vstack(
        rx.text_area(
            # 아무것도 없을 때 기본 text 설정
            placeholder="텍스트를 입력하세요.",
            # text 변수 (GUI에 입력된 text가 바로 변수에 적용되니 않는다. onchange로 결정해야 한다.)
            value=TextAreaControlled.text,
            # text의 변화가 있을 때 원하는 함수 실행
            on_change=TextAreaControlled.set_text,
        ),
        rx.input(
            value="Edit Text: " + TextAreaControlled.text,
        ),
    )