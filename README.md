# binary-leds

Reprezentarea cu ajutorul ledurilor a unui numar binar pe 8 biti.

HARDWARE

Se vor utiliza 8 leduri, cate 1 led pentru fiecare bit, 8 rezistori de 220 ohmi, 1 breadboard, 9 fire mama-tata si o placa de dezvoltare Raspberry Pi 3 model B.

SOFTWARE

Python v3 (inclus in sistemul de operare Raspbian)

CIRCUIT

Se utilizeaza pinii 12,16,18,22,24,26,32,36 ca surse de tensiune pentru leduri. Se utilizeaza pinul 6 ca pin de impamantare.
Schema circuitului este prezentata in pozele Circuit.png si P1.jpg.

UTILIZARE

La introducerea unui numar intreg si pozitiv de la tastatura, el va fi convertit in binar si reprezentat pe 8 biti cu ajutorul ledurilor.
De exemplu, pentru n=239, reprezentarea sa in binar pe 8 biti este 11101111 si reprezentarea cu ajutorul ledurilor in imaginea P3.jpg. Folosind doar 8 biti, cel mai mare numar care poate fi reprezentat este 255.




Alexandru Romanet - Universitatea Petrol-Gaze din Ploiesti
