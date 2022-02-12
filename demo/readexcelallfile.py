import glob
from selenium.webdriver.common.keys import Keys
import openpyxl
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


path = "D:\Text2"
col_list = ["Question Id", "Total Blanks", "Correct Answers", "Submissions"]
# read all the files with extension .xlsx i.e. excel
filenames = glob.glob(path + "\*.csv")
print('File names:', filenames)
li = []
# for loop to iterate all excel files
for file in filenames:
    # reading excel files
    print("Reading file = ", file)
    df = pd.read_csv(file, usecols=col_list)
    li.append(df)
frame = pd.concat(li, axis=0, ignore_index=True)
sum = frame.groupby('Question Id').sum()
sum['Correct Rate'] = sum['Correct Answers'] / sum['Total Blanks'] * 100
result = sum.drop(columns=["Total Blanks", "Correct Answers"])
# result.to_excel("D:\output.xlsx")
print(result.shape)

wb = openpyxl.load_workbook("D:\output.xlsx")

# Excelファイルのシート名「Sheet1」をwsという変数に読み込む
ws = wb["Sheet1"]

# ブラウザを起動し、Google検索ページを開く。念のため待機処理を入れる
# このコードでバージョンの問題から生じるエラーを回避できている
driver = webdriver.Chrome(ChromeDriverManager().install())  # Chromeを起動
driver.get("http://localhost:3000/")  # Google検索ページを開く
WebDriverWait(driver, 15).until(EC.visibility_of_all_elements_located)  # 待機処理

# 奈良、京都、大阪、滋賀とそれぞれ入力するため、for文で繰り返し処理
for i in range(2, 30):  # range(3,7)は3,4,5,6（ExcelのB3,B4,B5,B6セルに対応）28
    for j in range(1, 4):  # 4
        element = driver.find_element_by_id("filled-multiline-static")  # 検索窓要素を取得。name以外にもid、css_selectorなど
        keyword = ws.cell(row=i, column=j).value  # ExcelのセルBiの値をkeywordという変数に入力。rowは行、columnは列
        if(j==3 and i!=29):
            element.send_keys("{}\n".format(keyword))  # .send_keys()で検索窓にkeywordを入力
        else:
            element.send_keys("{} ".format(keyword))  # .send_keys()で検索窓にkeywordを入力

driver.find_element_by_class_name("MuiButton-contained").send_keys(Keys.ENTER)
print("sample test case sucessfully completed")
