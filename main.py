
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
        print("퀴즈 풀기 준비 중")
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
