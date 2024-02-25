import os
import random
from colorama import Fore, Style, init

# Inicjalizacja colorama
init()

quiz_dict = {
    "Jak nazywa się najbliższa nam galaktyka?": "Andromeda",
    "Która planeta w Układzie Słonecznym jest największa?": "Jowisz",
    "Ile lat świetlnych wynosi odległość do najbliższej nam gwiazdy?": "4,24 lat świetlnych",
    "Jak nazywa się najjaśniejsza gwiazda na nocnym niebie?": "Syriusz",
    "Co to jest czarna dziura?": "Region przestrzeni, z którego nic nie może uciec, nawet światło",
    "Jakie są trzy typy galaktyk?": ["Spiralne", "Elipstyczne", "Nieregularne"],
    "Co to jest czerwony karzeł?": "Gwiazda o niskiej masie, która spala wodór",
    "Jak nazywa się nasza galaktyka?": "Droga Mleczna",
    "Co to jest Wielki Wybuch?": "Teoria opisująca powstanie Wszechświata",
    "Jakie są fazy Księżyca?": ["Nów", "Pierwsza kwadra", "Pełnia", "Ostatnia kwadra"],
    "Co to jest rok świetlny?": "Odległość, którą światło pokonuje w ciągu jednego roku",
    "Jakie są planety w Układzie Słonecznym?": ["Merkury", "Wenus", "Ziemia", "Mars", "Jowisz", "Saturn", "Uran", "Neptun"],
    "Co to jest zorza polarna?": "Zjawisko optyczne występujące w wyższych szerokościach geograficznych",
    "Co to jest ekliptyka?": "Ścieżka, po której porusza się Słońce na sferze niebieskiej",
    "Co to jest meteoryt?": "Fragment materii kosmicznej, który przetrwał przejście przez atmosferę Ziemi i uderzył w powierzchnię Ziemi"
}



# Dodajemy słownik do śledzenia błędnych odpowiedzi
wrong_answers = {question: 3 for question in quiz_dict.keys()}

def display_flashcard():
    # Wybieramy pytanie z największą liczbą błędnych odpowiedzi
    question = max(wrong_answers, key=wrong_answers.get)
    answer = quiz_dict[question]
    print(Fore.GREEN + f"Pytanie: {question}" + Style.RESET_ALL)
    input("Naciśnij enter, aby zobaczyć odpowiedź...")
    print(Fore.BLUE + f"Odpowiedź: {answer}" + Style.RESET_ALL)
    return question

def main():
    while True:
        # Czyszczenie konsoli
        os.system('cls' if os.name == 'nt' else 'clear')
        question = display_flashcard()
        user_input = input("Czy odpowiedziałeś poprawnie? (t/n): ")
        if user_input.lower() == 't':
            # Zmniejszamy licznik błędnych odpowiedzi, jeśli jest większy od zera
            if wrong_answers[question] > 0:
                wrong_answers[question] -= 1
        else:
            # Zwiększamy licznik błędnych odpowiedzi
            wrong_answers[question] += 1
        print(f"Liczba błędnych odpowiedzi na to pytanie: {wrong_answers[question]}")
        # Sprawdzamy, czy są jeszcze jakieś pytania z błędnymi odpowiedziami
        if max(wrong_answers.values()) == 0:
            print("Gratulacje! Odpowiedziałeś poprawnie na wszystkie pytania.")
            break

if __name__ == "__main__":
    main()
