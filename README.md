## Url Status Code Checker
This script runs fetches urls from the CSV file, checks and prints the HTTP status code for each url.

## Prerequistes

- Python 3.12.6
- CSV file
- VScode
- Internet connection is required.

## How to start the server

- Install the required packages by running `pip install requests` in your terminal.
- Run `python main.py` in VSCode terminal to excute the script.
- Result would be printed in the terminal.
  -"example - (200) http://sportv.globo.com/site/noticia/2011/11/em-casa-sao-jose-vence-colo-colo-e-e-campeao-da-libertadores-feminina.html "

## Technologies

- Python : the scripting environment contains inbuilt modules `time`, `contextlib` and `csv`
  - `time`: this module adds a 1 second delay between the requests.
  - `contextlib`: This provides the @contextmanager decorator for file management.
  - `csv`: This processes the CSV file.
- CSV file: This is where the urls are stored.

## How My Logic Works

I built the logic using a class `UrlStatusCheck` which has two static methods `getStatus` and `checkUrl`

- `getStatus`: This method uses `requests.get(url, timeout=10, allow_redirects=True)` to send a GET request to the url and uses 10 seconds limit for the request to complete. try-except block catches handles error `requests.RequestException`.
- `checkUrl`: This uses the `csvReader` to yield objects which provides an iteration over each row in the CSV using `for row in reader:`. Then checks `if not row or not row[0].strip():` to skip an empty row. Then it calls `self.getStatus(url)` method to get the status code and prints the result.
  Then, this logic is wrapped in a block to ensure that the scrrpt runs only when it is executed directly.
  `if __name__ == "__main__":
    checker = UrlStatusCheck()
    checker.checkUrl('Task 2 - Intern.csv')`

## Sample Output

- (200) http://www.periodicos.letras.ufmg.br/index.php/fulia/issue/view/677/showToc(200) http://www.saadec.com.br/noticiamostra.php?id=223
- (200) http://www.saopaulofc.net/spfcpedia/conquistas
- (403) http://www.wpsl.info/news/04_0121.html
- (200) https://agenciabrasil.ebc.com.br/esportes/noticia/2020-02/bia-zaneratto-chega-ao-palmeiras-em-momento-magico-do-futebol-feminino
