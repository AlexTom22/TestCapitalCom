from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import datetime
from pages.country_and_licence import coutry_list
# from country_and_licence import licence_list


def parsing_page(dr, page_url, location):
    print()
    if location == "en":
        location = ""
    page_url += location
    print(f"{datetime.datetime.now()} - Start page with url {page_url}")
    dr.get(page_url)

    list_href = list()
    list_href.append(page_url)
    css_loc = "[href^='" + page_url + "']"

    # Сделали выборку всех элементов, имеющих ссылки, начинающиеся на capital.com/loc
    elements = dr.find_elements(By.CSS_SELECTOR, css_loc)
    for element in elements:
        href = element.get_attribute("href")
        level_list = href.split("/")
        href_loc = level_list[-1]
        if href == "bg":
            break
        if "?license=" in href:
            continue
        elif ".png" in href:
            continue
        elif ".json" in href:
            continue
        elif ".css" in href:
            continue
        elif href_loc in coutry_list:
            continue
        elif href_loc == location:
            list_href.append(href)
        elif href == page_url:
            list_href.append(href)
        else:
            list_href.append(href)

    print(f"Длинна листа ссылок= {len(list_href)}")
    set_link = set(list_href)
    print(f"Длинна сета уникальных ссылок= {len(set_link)}")
    return set_link


try:
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    options.headless = True
    browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )
    print(f"{datetime.datetime.now()} - Начало работы скрипта")

    # для всех стран, указанных в списке стран формируем отдельные файлы со ссылками
    for country in coutry_list:
        print(f"\n!!! обрабатываем страну {country}")
        set_total = set()
        link = "https://capital.com/"
        loc = country
        set_link_start = sorted(parsing_page(browser, link, loc))
        set_total.update(set_link_start)

        # input("? ==>")

        i = 1
        for link in set_link_start:
            print(f"\n{i}  из  {len(set_link_start)}  ", end="")
            set_link_page = parsing_page(browser, link, "")
            set_total.update(set_link_page)
            print(f"Длинна общего сета уникальных ссылок = {len(set_total)}")
            i += 1

        set_resume = sorted(set_total)
        print(
            f"Длинна финального сета уникальных ссылок для страны {country} = "
            f"{len(set_resume)}"
        )

        # Записываем финальный отсортированный сет уникальных ссылок в файл
        dt_finish = datetime.datetime.now()
        name_file = (
            "txt/"
            + str(dt_finish.date())
            + "/"
            + loc
            + "/"
            + str(dt_finish.date())
            + " "
            + loc
            + " "
            + "link_of_capital_com.txt"
        )
        f = open(name_file, "w")
        for line in set_resume:
            f.write(line + "\n")

        f.close()

finally:
    browser.quit()
