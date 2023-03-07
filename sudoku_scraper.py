from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def get_puzzle(url: str) -> list:
    puzzle = []

    try:
        driver = webdriver.Chrome()

        driver.get(url)
        sleep(5)

        board = driver.find_element(by=By.CLASS_NAME, value="su-board")
        cells = board.find_elements(by=By.CLASS_NAME, value="su-cell")

        if len(cells) != 81:
            raise Exception("Error in fetching the puzzle!!")

        for i in range(9):
            row = []
            for k in range(i*9, (i+1)*9):
                val = cells[k].get_attribute('aria-label')
                if val == "empty":
                    val = 0
                else:
                    val = int(val)
                row.append(val)
            puzzle.append(row)

    except Exception as e:
        print("an error occured!")
        print(e)
    finally:
        driver.close()
        return puzzle
