import math
import datetime
import requests

# ====== Glicko-1 Algorithm ======
class Player:
    """
    Glicko-1 рейтинг: хранит rating (R), rating deviation (RD) и историю.
    """
    def __init__(self, rating: float = 1500.0, rd: float = 350.0, last_date: datetime.date = None):
        self.rating = rating
        self.rd = rd
        self.last_date = last_date or datetime.date.today()
        self.history = [(self.last_date.isoformat(), self.rating, self.rd)]

    @staticmethod
    def _g(rd: float) -> float:
        q = math.log(10) / 400
        return 1 / math.sqrt(1 + (3 * q**2 * rd**2) / (math.pi**2))

    @staticmethod
    def _E(r: float, r_j: float, rd_j: float) -> float:
        return 1 / (1 + 10 ** (-Player._g(rd_j) * (r - r_j) / 400))

    def _decay_rd(self) -> None:
        """
        Увеличивает RD за время без активности.
        """
        days = (datetime.date.today() - self.last_date).days
        if days > 0:
            c = 50.0
            rd_max = 350.0
            self.rd = min(math.sqrt(self.rd**2 + c**2 * days), rd_max)
            self.last_date = datetime.date.today()
            self.history.append((self.last_date.isoformat() + ' (decay)', self.rating, self.rd))

    def update(self, opponents: list, results: list) -> None:
        """
        Обновляет рейтинг на основе списка opponents и results.
        opponents: [(rating, rd), ...]
        results: [score, ...] где score ∈ {1,0.5,0}.
        """
        if not opponents:
            print("Нет игр для обновления рейтинга.")
            return

        # 1) Учитываем бездействие
        self._decay_rd()

        q = math.log(10) / 400
        # 2) Вычисляем d2
        denom = 0.0
        for (r_j, rd_j), s_j in zip(opponents, results):
            E_j = self._E(self.rating, r_j, rd_j)
            g_j = self._g(rd_j)
            denom += (g_j**2) * E_j * (1 - E_j)
        if denom <= 0:
            print("Недостаточно данных для расчёта d2.")
            return
        d2 = 1 / (q**2 * denom)

        # 3) Вычисляем дельту
        delta = 0.0
        for (r_j, rd_j), s_j in zip(opponents, results):
            E_j = self._E(self.rating, r_j, rd_j)
            g_j = self._g(rd_j)
            delta += g_j * (s_j - E_j)

        # 4) Обновляем rating и rd
        pre = (self.rating, self.rd)
        self.rating = max(0.0, self.rating + (q / (1/self.rd**2 + 1/d2)) * delta)
        self.rd = math.sqrt(1 / (1/self.rd**2 + 1/d2))
        today = datetime.date.today().isoformat()
        self.history.append((today + ' (pre)', pre[0], pre[1]))
        self.history.append((today + ' (post)', self.rating, self.rd))


# ====== Chess.com API Interaction ======
HEADERS = {"User-Agent": "GlickoApp/1.0 (+https://yourdomain.com)"}


def fetch_stats(username: str, category: str = 'blitz') -> tuple:
    """
    Возвращает (rating, rd) для категории: bullet, blitz, rapid, daily.
    """
    key_map = {
        'bullet': 'chess_bullet',
        'blitz': 'chess_blitz',
        'rapid': 'chess_rapid',
        'daily': 'chess_daily'
    }
    key = key_map.get(category)
    if not key:
        raise ValueError(f"Неверная категория '{category}'")

    url = f"https://api.chess.com/pub/player/{username.lower()}/stats"
    resp = requests.get(url, headers=HEADERS)
    resp.raise_for_status()
    data = resp.json()

    stat = data.get(key)
    if not stat or 'last' not in stat:
        raise KeyError(f"В категории '{category}' нет данных о рейтинге.")

    last = stat['last']
    return last['rating'], last['rd']


def fetch_latest_games(username: str) -> list:
    """
    Возвращает список всех игр за текущий месяц.
    """
    url = f"https://api.chess.com/pub/player/{username.lower()}/games/archives"
    resp = requests.get(url, headers=HEADERS)
    resp.raise_for_status()
    archives = resp.json().get('archives', [])
    if not archives:
        return []
    last_url = archives[-1]
    resp2 = requests.get(last_url, headers=HEADERS)
    resp2.raise_for_status()
    return resp2.json().get('games', [])


def parse_opponent(game: dict, username: str) -> tuple:
    """
    Возвращает ((rating_opponent, rd_opponent), score) для заданного username.
    """
    usr = username.lower()
    white = game.get('white', {})
    black = game.get('black', {})
    if white.get('username', '').lower() == usr:
        opp, result = black, white.get('result', '')
    else:
        opp, result = white, black.get('result', '')
    score = 1.0 if result == 'win' else 0.5 if result == 'draw' else 0.0
    return (opp.get('rating', 0), opp.get('rd', 350)), score


# ====== Main Script ======
if __name__ == '__main__':
    user = input("Chess.com username: ")
    category = input("Category (bullet/blitz/rapid/daily): ").strip().lower()
    try:
        rating, rd = fetch_stats(user, category)
    except Exception as e:
        print(f"Ошибка при получении stats: {e}\nВведите rating и rd вручную.")
        rating = float(input("Рейтинг: "))
        rd = float(input("RD: "))

    player = Player(rating, rd)
    print(f"Current: R={rating}, RD={rd}\n")

    games = fetch_latest_games(user)
    print(f"Fetched {len(games)} games in latest archive.")

    opponents, results = [], []
    for g in games:
        try:
            op, sc = parse_opponent(g, user)
            opponents.append(op)
            results.append(sc)
        except:
            continue

    player.update(opponents, results)
    print(f"\nNew rating: {player.rating:.2f}, RD: {player.rd:.2f}")
    print("History (date, rating, RD):")
    for rec in player.history:
        print(rec)
