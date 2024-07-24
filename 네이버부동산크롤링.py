from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time

# 드라이버 설정
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # 시작 시 최대화
driver = webdriver.Chrome(options=options)

# 네이버 부동산 페이지 접속
driver.get("https://land.naver.com/")

# 매매 버튼 클릭
driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[2]/div/div[1]/div[1]/ul/div[2]/li[2]').click()

# 리스트 버튼 클릭
driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[2]/div/div[1]/div[1]/p').click()

# 서울시 선택
driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[2]/div/div[1]/div[3]/div[3]/div[1]/ul/li[1]').click()

# 서초구 선택
driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[2]/div/div[1]/div[3]/div[3]/div[2]/ul/li[15]').click()

# 반포동 선택 (명시적 대기 사용)
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[3]/div[2]/div/div[1]/div[3]/div[3]/div[3]/div/ul/li[2]')))
element.click()

# 확인매물 버튼 클릭
driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[2]/div/div[1]/div[3]/div[3]/div[4]/p[2]/a').click()

# 전체 화면 모드로 전환
driver.fullscreen_window()

# 단지 정보 탭으로 전환
driver.find_element(By.XPATH, '/html/body/div[2]/div/section/div[2]/div/div[1]/div/div/a/span[4]').click()

# 단지명을 저장할 리스트
complex_names = []

# 반복문 내에서 각 단지명을 추출하는 부분 수정
for i in range(1, 111):
    xpath = f'/html/body/div[2]/div/section/div[2]/div/div[1]/div/div/div/div[3]/ul/li[{i}]'

    # 요소가 존재하고 가시적일 때까지 대기
    complex_name_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, xpath))
    )

    complex_name = complex_name_element.text
    complex_names.append(complex_name)
    print(f"단지 {i}: {complex_name}")

# 드라이버 종료
driver.quit()

# 추출된 단지명 출력
for name in complex_names:
    print(name)