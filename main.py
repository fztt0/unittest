import unittest
import re
import time

def is_palindrome(s):
	rev = ''.join(reversed(s))
	if (s == rev):
		return True
	return False

frase = input("Qual a palavra? ").upper()
frase = re.sub(r'[!’./;,\s]','', frase)
if frase == frase[::-1]:
    print(f"Verdadeiro, "+ frase +" é um palíndromo")
else:
    print("Falso, "+ frase +" não é um palíndromo")

print("\nIniciando etapa de testes...")

time.sleep(2)

class TestPalindromes(unittest.TestCase):

    def test_is_palindrome(self):
        assert is_palindrome("Rotator".upper()) is True

    def test_is_palindrome2(self):
        assert is_palindrome('bob') is True

    def test_is_palindrome3(self):
        assert is_palindrome('madam') is True
    
    def test_is_palindrome4(self):
        assert is_palindrome('mAlAyAlam'.lower()) is True

    def test_is_palindrome5(self):
        assert is_palindrome('1') is True

    def test_is_palindrome6(self):
        assert is_palindrome('Able was I, ere I saw Elba'.upper().replace(" ", "").replace(",", "")) is True

    def test_is_palindrome7(self):
        assert is_palindrome('Madam I’m Adam'.upper().replace("’", "").replace(" ", "")) is True

    def test_is_palindrome8(self):
        assert is_palindrome('Step on no pets.'.upper().replace(".", "").replace(" ", "")) is True

    def test_is_palindrome9(self):
        assert is_palindrome('Top spot!'.upper().replace("!", "").replace(" ", "")) is True      

    def test_is_palindrome10(self):
        assert is_palindrome('02/02/2020'.replace("/", "")) is True

    def test_is_palindrome11(self):
        assert is_palindrome('xyz') is False

    def test_is_palindrome12(self):
        assert is_palindrome('elephant') is False

    def test_is_palindrome13(self):
        assert is_palindrome('Country'.lower()) is False

    def test_is_palindrome14(self):
        assert is_palindrome('Top . post!'.upper().replace(" ", "").replace(".", "").replace("!", "")) is False

    def test_is_palindrome15(self):
        assert is_palindrome('Wonderful-fool'.upper().replace("-", "")) is False

    def test_is_palindrome16(self):
        assert is_palindrome('Wild imagination!'.upper().replace("!", "")) is False

if __name__ == '__main__':
    unittest.main()

