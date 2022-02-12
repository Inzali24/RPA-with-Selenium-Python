#必要なモジュールのインポート
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl
from selenium.webdriver.common.keys import Keys

def spaceFunction(j):
    switcher = {
        5: "{}\n"
    }
    return switcher.get(j, " ")

#Excelファイルをwbという変数に読み込む
wb = openpyxl.load_workbook("D:\excelFilePython.xlsx")

#Excelファイルのシート名「Sheet1」をwsという変数に読み込む
ws = wb["Sheet1"]

#ブラウザを起動し、Google検索ページを開く。念のため待機処理を入れる
#このコードでバージョンの問題から生じるエラーを回避できている
driver = webdriver.Chrome(ChromeDriverManager().install())#Chromeを起動
driver.get("http://localhost:3000/")#Google検索ページを開く
WebDriverWait(driver, 15).until(EC.visibility_of_all_elements_located)#待機処理

#奈良、京都、大阪、滋賀とそれぞれ入力するため、for文で繰り返し処理
for i in range(1,10):#range(3,7)は3,4,5,6（ExcelのB3,B4,B5,B6セルに対応）
    for j in range(1,6):
     element = driver.find_element_by_class_name("input_inputData__3gK-e")#検索窓要素を取得。name以外にもid、css_selectorなど
     keyword = ws.cell(row=i, column=j).value#ExcelのセルBiの値をkeywordという変数に入力。rowは行、columnは列
     if j == 5:
         element.send_keys("{}\n".format(keyword))#.send_keys()で検索窓にkeywordを入力
     else:
         element.send_keys("{} ".format(keyword))  # .send_keys()で検索窓にkeywordを入力


driver.find_element_by_class_name("input_sendData__3_CCV").send_keys(Keys.ENTER)
print("sample test case sucessfully completed")