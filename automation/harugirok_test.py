import time
from selenium import webdriver
from selenium.webdriver.common.by import By

passed = 0
failed = 0

driver = webdriver.Chrome()
driver.get("https://guswns17.github.io/harugirok/")
time.sleep(2)

driver.execute_script("document.documentElement.style.scrollBehavior = 'auto'")

driver.find_element(By.CSS_SELECTOR, '[data-testid="nav-records"]').click()
time.sleep(1)
title = driver.find_element(By.CSS_SELECTOR, ".page-title").text
if title == "기록":
    print("통과: 기록 메뉴")
    passed = passed + 1
else:
    print("실패: 기록 메뉴 (화면 제목:", title, ")")
    failed = failed + 1

driver.find_element(By.CSS_SELECTOR, '[data-testid="nav-stats"]').click()
time.sleep(1)
title = driver.find_element(By.CSS_SELECTOR, ".page-title").text
if title == "통계":
    print("통과: 통계 메뉴")
    passed = passed + 1
else:
    print("실패: 통계 메뉴 (화면 제목:", title, ")")
    failed = failed + 1

driver.find_element(By.CSS_SELECTOR, '[data-testid="nav-settings"]').click()
time.sleep(1)
title = driver.find_element(By.CSS_SELECTOR, ".page-title").text
if title == "설정":
    print("통과: 설정 메뉴")
    passed = passed + 1
else:
    print("실패: 설정 메뉴 (화면 제목:", title, ")")
    failed = failed + 1

driver.find_element(By.CSS_SELECTOR, '[data-testid="nav-write"]').click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '[data-testid="title-input"]').send_keys("첫 자동화 글")
driver.find_element(By.CSS_SELECTOR, '[data-testid="content-input"]').send_keys("내가 직접 코드로 쓴 글이야.")
driver.find_element(By.CSS_SELECTOR, '[data-testid="save-btn"]').click()
time.sleep(1)

saved_title = driver.find_element(By.CSS_SELECTOR, '[data-testid="detail-title"]').text
if saved_title == "첫 자동화 글":
    print("통과: 글 작성")
    passed = passed + 1
else:
    print("실패: 글 작성 (저장된 제목:", saved_title, ")")
    failed = failed + 1

print("----------------------------")
print("통과", passed, "개 / 실패", failed, "개")

time.sleep(3)
driver.quit()
