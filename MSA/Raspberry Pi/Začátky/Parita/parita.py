from typing import List


class Parita:
    @staticmethod
    def spocitat(inp: List[int]) -> int:
        """
        Funkce na spočítání parity
        :param inp: list int jedniček a nul na spočítání parity
        :return: paritu zadaného listu
        """
        parita = inp[0] ^ inp[1]
        for bit in range(2, len(inp)):
            parita ^= inp[bit]
        return parita
