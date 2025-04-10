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
    def getStatus(url: str) -> tuple[int | str, str]:
        try:
            response = requests.get(url, timeout=10, allow_redirects=True)
            return response.status_code, "Success"
        except requests.Timeout:
            return "Timeout", "Request timed out after 10 seconds"
        except requests.ConnectionError:
            return "ConnectionError", "Failed to Connect to url"
        except requests.RequestException as e:
            return "Error", f"Unknown request error: {str(e)}"
        except Exception as e:
            return "Error", f"Unexpected error: {str(e)}"

    def checkUrl(self, csv_path: str) -> None:
        try:
            with csvReader(csv_path) as reader:
                # Thissi to skip the header row (url)
                next(reader, None)
                
                for row in reader:
                    if not row or not row[0].strip():
                        continue
                    url = row[0].strip()
                    status, message = self.getStatus(url)
                    if status == "Success":
                        print(f"({status}) {url}")
                    else:
                        print(f"({status}) {url} - {message}")
                    time.sleep(1)
        except FileNotFoundError:
            print(f"Error: File '{csv_path}' not found")
        except Exception as e:
            print(f"Error: {str(e)}")
        
if __name__ == "__main__":
    checker = UrlStatusCheck()
    checker.checkUrl('Task 2 - Intern.csv')