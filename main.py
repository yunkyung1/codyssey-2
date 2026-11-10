class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def show_question(self):
        print(self.question)

        for i, choice in enumerate(self.choices, start=1):
            print(f"{i}. {choice}")

    def check_answer(self, user_answer):
        return self.answer == user_answer


quizzes = [
    Quiz("피카츄의 타입은?", ["물", "불꽃", "전기", "풀"], 3),
    Quiz("파이리의 타입은?", ["풀", "불꽃", "물", "전기"], 2),
    Quiz("꼬부기의 타입은?", ["물", "풀", "불꽃", "얼음"], 1),
    Quiz("이상해씨의 타입 조합은?", ["풀/독", "물/독", "불꽃/독", "풀/전기"], 1),
    Quiz("이브이가 진화할 수 있는 포켓몬은?", ["피카츄", "잠만보", "샤미드", "뮤"], 3)
]

while True:
    print("\n===== 포켓몬 퀴즈 게임 =====")
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")

    try:
        choice = int(input("번호를 선택하세요: ").strip())
    except ValueError:
        print("숫자를 입력해주세요.")
        continue
    except (KeyboardInterrupt, EOFError):
        print("\n프로그램을 안전하게 종료합니다.")
        break

   

    if choice == 1:
        score = 0

        for quiz in quizzes:
            quiz.show_question()

            try:
                user_answer = int(input("정답 번호 (1~4): ").strip())
            except ValueError:
                print("숫자가 아니므로 오답 처리합니다.")
                continue
            except (KeyboardInterrupt, EOFError):
                print("\n퀴즈를 중단합니다.")
                break

            if quiz.check_answer(user_answer):
                print("정답입니다!")
                score += 1
            else:
                print("오답입니다!")

        print(f"최종 점수: {score}/{len(quizzes)}")


    elif choice == 2:
        print("퀴즈 추가 준비 중")
    elif choice == 3:
        print("퀴즈 목록 준비 중")
    elif choice == 4:
        print("점수 확인 준비 중")
    elif choice == 5:
        print("게임을 종료합니다.")
        break
    else:
        print("1~5 사이의 숫자를 입력해주세요.")
