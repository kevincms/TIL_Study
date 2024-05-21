import reflex as rx

class SelectControlled(rx.State):
    type: list[str] = ["apple", "grape", "pear"]

    value: str = "apple"

    def set_type(self,value):
        self.value=value


def select_example3():
    return rx.vstack(
        rx.select(
            SelectControlled.type,
            value=SelectControlled.value,
            on_change=SelectControlled.set_type,
        ),
    )