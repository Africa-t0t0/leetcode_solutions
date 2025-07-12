def solution(strs_ls: list) -> str:
    minimum = 999999
    current_min_lenght = min([len(element) if len(element) < minimum else minimum for element in strs_ls])

    if "" in strs_ls: return ""

    common_prefix = ""

    for i in range(current_min_lenght):
        current_column_ls = [element[i] for element in strs_ls]

        is_valid = all([element == current_column_ls[0] for element in current_column_ls])

        if not is_valid:
            break
        else:
            common_prefix += current_column_ls[0]
    return common_prefix

print(solution(["flower", "flol", "fly"]))


def optimal_solution(strs) -> str:
    if not strs:  # Caso vacío
        return ""

    # Encontrar la cadena más corta para limitar las comparaciones
    shortest_str = min(strs, key=len)

    for i, char in enumerate(shortest_str):
        for string in strs:
            if string[i] != char:
                return shortest_str[:i]

    return shortest_str