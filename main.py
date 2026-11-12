import json
import random
from pathlib import Path


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
    Quiz(
        "Python에서 값을 저장할 때 사용하는 것은?",
        ["반복문", "변수", "조건문", "클래스"],
        2
    ),
    Quiz(
        "Python에서 문자열을 나타내는 자료형은?",
        ["int", "bool", "str", "list"],
        3
    ),
    Quiz(
        "조건에 따라 다른 코드를 실행할 때 사용하는 것은?",
        ["if", "for", "while", "def"],
        1
    ),
    Quiz(
        "리스트의 항목을 하나씩 반복할 때 주로 사용하는 문법은?",
        ["if", "class", "return", "for"],
        4
    ),
    Quiz(
        "Python에서 함수를 정의할 때 사용하는 키워드는?",
        ["print", "input", "def", "import"],
        3
    )
]


class QuizGame:
    def __init__(self, quizzes):
        self.quizzes = quizzes
        self.best_score = 0
        self.data_file = Path(__file__).with_name("state.json")
        self.load_state()

    def save_state(self):
        data = {
            "quizzes": [
                {
                    "question": quiz.question,
                    "choices": quiz.choices,
                    "answer": quiz.answer
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score
        }

        try:
            with open(self.data_file, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        except OSError:
            print("파일 저장 중 오류가 발생했습니다.")


    def load_state(self):
        if not self.data_file.exists():
            return

        try:
            with open(self.data_file, "r", encoding="utf-8") as file:
                data = json.load(file)

            saved_quizzes = data["quizzes"]
            saved_score = data["best_score"]

            loaded_quizzes = []

            for item in saved_quizzes:
                question = item["question"]
                choices = item["choices"]
                answer = item["answer"]

                if (
                    not isinstance(question, str)
                    or not question.strip()
                    or not isinstance(choices, list)
                    or len(choices) != 4
                    or not all(isinstance(c, str) and c.strip() for c in choices)
                    or type(answer) is not int
                    or answer not in range(1, 5)
                ):
                    raise ValueError("잘못된 퀴즈 데이터")

                loaded_quizzes.append(Quiz(question, choices, answer))

            if type(saved_score) is not int or saved_score < 0:
                raise ValueError("잘못된 점수 데이터")

            self.quizzes = loaded_quizzes
            self.best_score = saved_score

        except (OSError, ValueError, KeyError, TypeError):
            print("저장 파일을 읽을 수 없어 기본 문제로 시작합니다.")


    def show_menu(self):
        print("\n===== 파이썬 퀴즈 게임 =====")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")


    def play_quiz(self):
        score = 0

        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return
        for i, quiz in enumerate(random.sample(self.quizzes, len(self.quizzes)), start=1):
            print(f"\n[{i}번문제]")
            quiz.show_question()
    

            while True:
                try:
                    user_input = input("정답 번호 (1~4): ").strip()

                    if not user_input:
                        print("정답 번호를 입력해주세요.")
                        continue

                    answer = int(user_input)

                    if answer not in range(1, 5):
                        print("1~4 사이의 숫자를 입력해주세요.")
                        continue

                    break

                except ValueError:
                    print("숫자를 입력해주세요.")

                except (KeyboardInterrupt, EOFError):
                    print("\n퀴즈를 중단합니다.")
                    return

            if quiz.check_answer(answer):
                print("정답입니다!")
                score += 1
            else:
                print("오답입니다!")

        print(f"최종 점수: {score}/{len(self.quizzes)}")

        if score > self.best_score:
            self.best_score = score
            self.save_state()


 
    def add_quiz(self):
        print("\n===== 퀴즈 추가 =====")

        try:
            while True:
                question = input("문제를 입력하세요: ").strip()

                if question:
                    break

                print("문제는 비워둘 수 없습니다.")

            choices = []

            for i in range(1, 5):
                while True:
                    choice = input(f"{i}번 선택지: ").strip()

                    if choice:
                        choices.append(choice)
                        break

                    print("선택지는 비워둘 수 없습니다.")

            while True:
                try:
                    user_input = input("정답 번호 (1~4): ").strip()

                    if not user_input:
                        print("정답 번호를 입력해주세요.")
                        continue

                    answer = int(user_input)

                    if answer not in range(1, 5):
                        print("정답은 1~4 중에서 선택해야 합니다.")
                        continue

                    break

                except ValueError:
                    print("정답은 숫자로 입력해야 합니다.")

        except (KeyboardInterrupt, EOFError):
            print("\n퀴즈 추가를 중단합니다.")
            return

        self.quizzes.append(Quiz(question, choices, answer))
        self.save_state()
        print("퀴즈가 추가되었습니다!")


    def list_quizzes(self):
        print("\n===== 퀴즈 목록 =====")

        for i, quiz in enumerate(self.quizzes, start=1):
            print(f"{i}. {quiz.question}")

        print(f"총 {len(self.quizzes)}개의 퀴즈가 등록되어 있습니다.")


    def run(self):
        while True:
            self.show_menu()

            try:
                choice = int(input("번호를 선택하세요: ").strip())
            except ValueError:
                print("숫자를 입력해주세요.")
                continue
            except (KeyboardInterrupt, EOFError):
                print("\n프로그램을 안전하게 종료합니다.")
                break

            if choice == 1:
                self.play_quiz()
            elif choice == 2:
                self.add_quiz()
            elif choice == 3:
                self.list_quizzes()
            elif choice == 4:
                print(f"최고 점수: {self.best_score}")
            elif choice == 5:
                print("게임을 종료합니다.")
                break
            else:
                print("1~5 사이의 숫자를 입력해주세요.")


game = QuizGame(quizzes)
game.run()