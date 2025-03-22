from contextlib import contextmanager
import csv
import requests
import time

@contextmanager
def csvReader(csv_path: str):
    file = open(csv_path, 'r', encoding='utf-8')
    try:
        yield csv.reader(file)
    finally:
        file.close()

class UrlStatusCheck:
    @staticmethod
    def getStatus(url: str) -> int | None:
        try:
            return requests.get(url, timeout=10, allow_redirects=True).status_code
        except requests.RequestException:
            return None

    def checkUrl(self, csv_path: str) -> None:
        try:
            with csvReader(csv_path) as reader:
                for row in reader:
                    if not row or not row[0].strip():
                        continue
                    url = row[0].strip()
                    status = self.getStatus(url)
                    print(f"({'Error' if status is None else status}) {url}")
                    time.sleep(1)
        except FileNotFoundError:
            print(f"Error: File '{csv_path}' not found")
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    checker = UrlStatusCheck()
    checker.checkUrl('Task 2 - Intern.csv')