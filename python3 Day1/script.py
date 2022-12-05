from typing import List

def prepare_list_input_file(path: str) -> List[List]:
    with open(path, 'r') as file:
        text = file.read().strip()
    text = text.split('\n\n')
    for i in range(len(text)):
        text[i] = text[i].split("\n")
        for j in range(len(text[i])):
            text[i][j] = int(text[i][j])
    return text

def calc_eachelf_sum(path:str) -> list:
    uncalculated_list = prepare_list_input_file(path)
    total_list = []
    for elf in uncalculated_list:
        elf = sum(elf)
        total_list.append(elf)
    return total_list

def find_most_kkal_elf(calculated_list: list) -> int:
    return max(calculated_list)
def find_trio_elfs(calculated_list: list) -> int:
    calculated_list.sort()
    calculated_list.reverse()
    return sum(calculated_list[:3])

def main():
    elf_list = calc_eachelf_sum('input.txt')
    kkalest_elf = find_most_kkal_elf(elf_list)
    kkalest_trio = find_trio_elfs(elf_list)
    print(kkalest_trio)
    print(kkalest_elf)
if __name__ == "__main__":
    main()
