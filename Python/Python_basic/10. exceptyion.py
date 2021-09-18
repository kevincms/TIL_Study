class zeor_error(Exception):
    def __init__(self):
        print("0 말고 다른 숫자를 입력해주세요.")
    def __str__(self):
        return "zeor_error"

try: # 오류가 발생되면 except으로 오류가 발생하지 않으면 정상적으로 실행된다.
    num=int(input("숫자를 입력해 주세요\n"))
    if num==0:
        raise zeor_error # raise를 이용해 오류를 일으킬 수 있다.
    print("입력한 숫자는 %d입니다"%num)
except ValueError: # ValueError 가 발생할 경우 
    print("숫자가 아닙니다.")
except Exception as err: # 앞의 모든 except error를 제외한 모든 에러가 발생한 경우 (Exception as err 생략가능)
    print("에러가 발생하였습니다.")
    print(err)
finally: # 오류와 관계없이 마지막에 실행된다.
    print("프로그램이 종료되었습니다.")