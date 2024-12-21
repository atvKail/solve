from itertools import combinations


BOARD_SIZE, k = map(int, input().split())
all_cells = [(x, y) for x in range(BOARD_SIZE) for y in range(BOARD_SIZE)]


def is_attacked(king_pos, rooks):
    kx, ky = king_pos
    for rx, ry in rooks:
        if kx == rx or ky == ry:
            return True
    return False


def is_pat(king_pos, rooks):
    if is_attacked(king_pos, rooks):
        return False

    for dx, dy in [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]:
        nx, ny = king_pos[0] + dx, king_pos[1] + dy
        if 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE:
            if not is_attacked((nx, ny), rooks):
                return False
    return True


pat_positions_k_rooks = set()
for king_pos in all_cells:
    for rooks in combinations(all_cells, k):
        if king_pos not in rooks:
            if is_pat(king_pos, rooks):
                pat_positions_k_rooks.add(tuple(sorted((king_pos, *rooks))))

print(len(pat_positions_k_rooks))
