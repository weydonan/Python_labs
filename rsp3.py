import os
from typing import List, Dict, Optional

class Gesture:
    def get_name(self) -> str:
        return "жест"

    def compare(self, other: 'Gesture') -> int:
        return 0


class Rock(Gesture):
    def get_name(self) -> str:
        return "камень"

    def compare(self, other: Gesture) -> int:
        if isinstance(other, Rock):
            return 0
        elif isinstance(other, Scissors):
            return 1
        elif isinstance(other, Paper):
            return -1
        return 0


class Scissors(Gesture):
    def get_name(self) -> str:
        return "ножницы"

    def compare(self, other: Gesture) -> int:
        if isinstance(other, Scissors):
            return 0
        elif isinstance(other, Paper):
            return 1
        elif isinstance(other, Rock):
            return -1
        return 0


class Paper(Gesture):
    def get_name(self) -> str:
        return "бумага"

    def compare(self, other: Gesture) -> int:
        if isinstance(other, Paper):
            return 0
        elif isinstance(other, Rock):
            return 1
        elif isinstance(other, Scissors):
            return -1
        return 0

class Player:
    def __init__(self, name: str, player_id: int):
        self.name = name
        self.id = player_id
        self.score = 0
        self.current_gesture: Optional[Gesture] = None

    def make_choice(self) -> Gesture:
        gesture_map = {
            '1': Rock(),
            '2': Scissors(),
            '3': Paper()
        }

        while True:
            print(f"\n{self.name}, ваш выбор:")
            print("1. Камень")
            print("2. Ножницы")
            print("3. Бумага")
            choice = input("Введите номер (1-3): ").strip()

            if choice in gesture_map:
                self.current_gesture = gesture_map[choice]
                return self.current_gesture
            print("Неверный ввод. Попробуйте снова.")

    def add_score(self, points: int = 1):
        self.score += points

    def reset_score(self):
        self.score = 0

    def __str__(self):
        return f"{self.name} - {self.score} очков"


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')



class Game:
    def __init__(self):
        self.players: List[Player] = []
        self.rounds_total = 0
        self.current_round = 0
        self.choices_history: List[Dict[int, str]] = []

    def setup_players(self):
        print("НАСТРОЙКА ИГРЫ")
        print("=" * 60)

        while True:
            try:
                num_players = int(input("Введите количество игроков (2-10): "))
                if 2 <= num_players <= 10:
                    break
                print("В игре должно быть минимум 2 игрока, максимум 10.")
            except ValueError:
                print("Неверный ввод. Введите целое число.")

        for i in range(1, num_players + 1):
            name = input(f"\nВведите имя для игрока {i}: ").strip()
            if not name:
                name = f"Игрок {i}"
            self.players.append(Player(name, i))

        while True:
            try:
                self.rounds_total = int(input("\nВведите количество раундов: "))
                if self.rounds_total > 0:
                    break
                print("Количество раундов должно быть больше 0.")
            except ValueError:
                print("Неверный ввод. Введите целое число.")


    def play_round(self):
        self.current_round += 1
        round_gestures = {}
        for player in self.players:
            print("\n" + "=" * 60)
            print(f"РАУНД {self.current_round} из {self.rounds_total}")
            print(f"ХОДИТ: {player.name}")
            print("=" * 60)
            gesture = player.make_choice()
            round_gestures[player.id] = gesture
            if player != self.players[-1]:
                clear_screen()

        print("\n" + "=" * 60)
        print(f"РЕЗУЛЬТАТЫ РАУНДА {self.current_round}")
        print("=" * 60)

        print("\nВЫБОРЫ ВСЕХ ИГРОКОВ:")
        for player in self.players:
            gesture = round_gestures[player.id]
            print(f"  {player.name}: {gesture.get_name()}")

        history_entry = {}
        for player in self.players:
            history_entry[player.id] = round_gestures[player.id].get_name()
        self.choices_history.append(history_entry)

        print("\n" + "-" * 40)
        print("РЕЗУЛЬТАТЫ ПАР:")
        print("-" * 40)

        round_wins = {}
        for player in self.players:
            round_wins[player.id] = 0

        for i in range(len(self.players)):
            for j in range(i + 1, len(self.players)):
                player1 = self.players[i]
                player2 = self.players[j]

                gesture1 = round_gestures[player1.id]
                gesture2 = round_gestures[player2.id]

                result = gesture1.compare(gesture2)

                if result == 1:
                    round_wins[player1.id] += 1
                    print(f"[+] {player1.name} победил {player2.name}")
                elif result == -1:
                    round_wins[player2.id] += 1
                    print(f"[+] {player2.name} победил {player1.name}")
                else:
                    print(f"[=] Ничья между {player1.name} и {player2.name}")

        print("\n" + "-" * 40)
        print("ОЧКИ ЗА РАУНД:")
        for player in self.players:
            wins = round_wins[player.id]
            if wins > 0:
                player.add_score(wins)
                print(f"  {player.name}: +{wins} очков")
            else:
                print(f"  {player.name}: 0 очков")

    def show_current_scores(self):
        print("\n" + "=" * 60)
        print("ТЕКУЩИЙ СЧЁТ:")
        print("=" * 60)

        sorted_players = sorted(self.players, key=lambda p: p.score, reverse=True)
        for i, player in enumerate(sorted_players, 1):
            print(f"{i}. {player}")

    def show_final_results(self):
        clear_screen()
        print("\n" + "=" * 60)
        print("ИГРА ЗАВЕРШЕНА!")
        print("=" * 60)
        print("\nФИНАЛЬНЫЙ СЧЁТ:")
        sorted_players = sorted(self.players, key=lambda p: p.score, reverse=True)

        for i, player in enumerate(sorted_players, 1):
            print(f"{i}. {player}")

        if sorted_players[0].score > sorted_players[1].score:
            print(f"\nПОБЕДИТЕЛЬ: {sorted_players[0].name}!")
        else:
            max_score = sorted_players[0].score
            winners = [p for p in sorted_players if p.score == max_score]
            if len(winners) > 1:
                print(f"\nНИЧЬЯ между {', '.join([w.name for w in winners])}!")
            else:
                print(f"\nПОБЕДИТЕЛЬ: {sorted_players[0].name}!")

        print("\n" + "=" * 60)
        print("ПОЛНАЯ СТАТИСТИКА ПО РАУНДАМ:")
        print("=" * 60)

        for round_num, choices in enumerate(self.choices_history, 1):
            print(f"\nРаунд {round_num}:")
            for player in self.players:
                choice = choices.get(player.id, "?")
                print(f"  {player.name}: {choice}")

    def play(self):
        print("\n" + "=" * 60)
        print("ДОБРО ПОЖАЛОВАТЬ В МУЛЬТИПЛЕЕРНУЮ ИГРУ")
        print("КАМЕНЬ, НОЖНИЦЫ, БУМАГА")

        self.setup_players()

        print(f"\nИгра началась! {len(self.players)} игроков, {self.rounds_total} раундов.")
        print("Важно: ходы других игроков не будут видны до конца раунда.")
        input("\nНажмите Enter, чтобы начать первый раунд...")

        for _ in range(self.rounds_total):
            self.play_round()
            self.show_current_scores()

            if self.current_round < self.rounds_total:
                input("\nНажмите Enter для следующего раунда...")

        self.show_final_results()
        print("\nСпасибо за игру!")


def main():
    game = Game()
    game.play()


if __name__ == "__main__":
    main()