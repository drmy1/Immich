# MK1:
Verze MK1 generuje posloupnost/hash, která není vůbec na nicčem závislá. Jedná se o šestiznakovou posloupnost, která se skládá z malých písmen a čísel (jak čísla, tak znaky se mohou opakovat). Posloupnost, kterou generátor vyplivne se dá použít na zcela všechno, protože je i kryptograficky bezpečná. Pokud jsem to vypočítal správně, tak by mělo existovat 36^6 kombinací.

- pár příkladů:
    - vrwft0
    - 59c3e8
    - c2v641
    - 0aylcn
    - 3gdkcm
    - myk61i

# MK2:
Verze MK2 generuje šestiznakovou posloupnost/hash, která se skládá ze samohlásek a souhlásek (posloupnost vždy začíná samohláskou), které se střídají a samohláska/souhláska se ve výsledku může vyskytnout pouze jednou. Pokud jsem to správně vypočítal, tak by mělo existovat 6x20x5x19x4x18=820800 kombinací. Zde se to dá případně ještě upravit, tak, aby se mohly samohlásky i souhlásky opakovat.

- pár příkladů:
    - ecyriq
    - onekut
    - uxetim
    - yfidon
    - igupaw
    - imekul