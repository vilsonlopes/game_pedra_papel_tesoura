import random
import time

pedra = 1
papel = 2
tesoura = 3

names = {pedra: "Pedra", papel: "Papel", tesoura: "Tesoura"}
rules = {pedra: tesoura, papel: pedra, tesoura: papel}

player_score = 0
computer_score = 0

def start():
    print("Vamos jogar Pedra, Papel, Tesoura?")
    while game():
        pass
    scores()


def game():
    player = move()
    computer = random.randint(1, 3)
    result(player, computer)
    return play_again()


def move():
    while True:
        print()
        player = input("Pedra = 1\nPapel = 2\nTesoura = 3\nQual escolhe: ")
        try:
            player = int(player)
            if player in (1, 2, 3):
                return player
        except ValueError:
            pass
        print("Oops! Não entendo sua jogada. Por favor digite 1, 2 ou 3.")


def result(player, computer):
    print("1...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("3!")
    time.sleep(0.5)
    print(f"O computador jogou {names[computer]}")
    global player_score, computer_score
    if player == computer:
        print("Empatou!")
    else:
        if rules[player] == computer:
            print("Você ganhou, parabéns!")
            player_score += 1
        else:
            print("O computador ri da sua cara quando te vence.")
            computer_score += 1

def play_again():
    answer = input("Gostaria de jogar novamente? y/n: ")
    if answer in ("y", "Y", "Yes", "s", "S", "Sim", "sim", "SIM", "YES"):
        return answer
    else:
        print("Obrigado por jogar, te vejo na próxima.")


def scores():
    global player_score, computer_score
    print("MAIORES SCORES")
    print("Player: ", player_score)
    print("Computer: ", computer_score)

if __name__ == '__main__':
    start()
