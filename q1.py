def anagram(n):
    anagram_bank = set()
    for i in range(n):
        given_str = input()
        given_str = given_str.lower().replace(" ", "")
        final = sorted(given_str)
        result = "".join(final)
        anagram_bank.add(result)
    print(len(anagram_bank))
    print(anagram_bank)


def main():
    n = int(input())
    anagram(n)


if __name__ == '__main__':
    main()
