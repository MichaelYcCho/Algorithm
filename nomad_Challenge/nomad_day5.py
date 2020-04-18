import os
import requests
from bs4 import BeautifulSoup

os.system("clear")
url = "https://www.iban.com/currency-codes"


# 1. 위 사이트에서 countries와 currencies를 가져오기
# 2. array 안에 Alpha-3 code와 country 이름을 저장하기
# Alpha-3 code: ISO 3166-1에서 정한 알파벳 세 글자의 국가 코드 (KOR: 대한민국)
# 3. 사용자의 입력을 확인, list에있는 country에 있는 숫자만 받는다.
# 4. country가 선택되었을 때 name과 currency code를 출력한다.


def request_iban():
  get_request = requests.get(url)
  html_parse = BeautifulSoup(get_request.text, "html.parser")
  table = html_parse.find("table", {"class": "table"})

  # table > thead > tr > th
  table_header = table.find("thead").find_all("th")
  heads = []
  for table_head in table_header:
    head = table_head.text
    heads.append(head)

  # tbody > tr > td
  countries = table.find("tbody").find_all("tr")

  # IBAN 만들기
  ibans = []
  for country in countries:
    country = country.find_all("td")
    print(country[3])
    if country[3].text == '':
      continue

    iban = {}
    for i in range(4):
      iban[heads[i]] = country[i].text

    # iban List
    ibans.append(iban)
  
  return ibans

# 사용자 입력
def user_answer(len_iban):
  # 숫자 외에 입력 시 다시 입력
  try:
    answer = int(input("#: ").strip())
    if answer > len_iban:
      print("Choose a number from the last.")
      user_answer(len_iban)
    else:
      return answer
  except ValueError:
    print("That's wasn't a number.")
    user_answer(len_iban)

# 프로그램 실행 함수
def main():

  isbns = request_iban()
  
  # 화면 출력
  for idx, isbn in enumerate(isbns, start=1):
    print(f"# {idx} {isbn['Country']}")
  
  # 숫자 입력 시 country name, currency 출력
  iban_num = user_answer(len(isbns))
  
  # 검색 루프
  for idx, isbn in enumerate(isbns, start=1):
    if idx == iban_num:
      print(f" You choose {isbn['Country']}")
      print(f" The Currency Code is {isbn['Code']}")

# 프로그램 실행
main()