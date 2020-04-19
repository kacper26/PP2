# PP2
## Etap 1 - analiza struktury opinii w serwisie [Ceneo.pl](https://www.ceneo.pl/)
|Składowa                |Selektor                                 |Nazwa zmiennej|
|------------------------|-----------------------------------------|--------------|
|opinia                  |li.js_product-review                     |              |
|identyfikator opinii    |["data-entry-id"]                        |              |
|autor                   |div.reviewer-name-line                   |              |
|rekomendacja            |div.product-review-summary > em          |              |
|ocena                   |span.review-source-count                 |              |
|treść opinii            |p.product-review-body                    |              |
|lista wad               |div.cons-cell > ul                       |              |
|lista zalet             |div.prons-cell > ul                      |              |
|przydatna               |button.vote-yes > span                   |              |
|nieprzydatna            |button.vote-no > span                    |              |
|data wystawienia opinii |span.review-time:first-child["datetime"] |              |
|data zakupu             |span.review-time:nth-child(2)["datetime"]|              |

## Etap 2 - pobranie składniowych pojedynczej opinii
- pobranie kodu jednej strony z opiniami o konkretnym produkcie
- wyciągnięcie z kodu strony fragmentów odpowiadających poszczególnym opiniom
- zapisanie do pojedynczych zmiennych wartości poszczególnych składowych opinii
## Etap 3 - pobranie wszystkich opinii o pojedynczym produkcie
-zapisanie do złożonej struktury danych składowych wszystkich opinii z pojedynczej strony
-przechodzenie po kolejnych stronach z opiniami
-zapis wszystkich opinii o pojedynczym produkcie
## Etap 4
-transformacja i wyczyszczenie danych
-refaktoring kodu
-parametryzacja
## Etap 5 (Pandas, Matplotlib)
- wczytanie opinii do ramki danych 
- policzenie podstawowych statystyk
- narysowanie wykresów funkcji 
## Etap 6 interfejs webowy dla scrapera (Flask)

