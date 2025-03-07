def task_A():
    for S in range(1, 110):
        if S + 1 >= 110 or 2 * S >= 110:
            continue
        petya_moves = [S + 1, 2 * S]
        valid = True
        for x in petya_moves:
            if not ((x + 1 >= 110) or (2 * x >= 110)):
                valid = False
                break
        if valid:
            return S
    return None


def task_B():
    results = []
    for S in range(1, 55):
        if (S + 1 >= 110) or (2 * S >= 110):
            continue
        petya_can_force = False
        for m in [S + 1, 2 * S]:
            forced = True
            for v in [m + 1, 2 * m]:
                if v >= 110:
                    forced = False
                    break
                else:
                    if not ((v + 1 >= 110) or (2 * v >= 110)):
                        forced = False
                        break
            if forced:
                petya_can_force = True
                break
        if petya_can_force:
            results.append(S)
            if len(results) == 2:
                break
    return results


def task_C():
    for S in range(1, 55):
        if (S + 1 >= 110) or (2 * S >= 110):
            continue
        all_petya_moves_work = True

        immediate_win_available_for_all = True
        for p in [S + 1, 2 * S]:
            vanya_has_winning_response = False
            immediate_win_for_this_p = False
            for v in [p + 1, 2 * p]:
                if v >= 110:
                    vanya_has_winning_response = True
                    immediate_win_for_this_p = True
                    break
                else:
                    can_win_after_v = True
                    for w in [v + 1, 2 * v]:
                        if not ((w + 1 >= 110) or (2 * w >= 110)):
                            can_win_after_v = False
                            break
                    if can_win_after_v:
                        vanya_has_winning_response = True
            if not vanya_has_winning_response:
                all_petya_moves_work = False
                break
            if not immediate_win_for_this_p:
                immediate_win_available_for_all = False

        if all_petya_moves_work and (not immediate_win_available_for_all):
            return S
    return None


print("Task A answer:", task_A())
print("Task B answers:", task_B())
print("Task C answer:", task_C())
