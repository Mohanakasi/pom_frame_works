from openpyexcel import load_workbook, Workbook
from selenium.webdriver.common.by import By
path =r"C:\development\pom_frame_work\ajio_submission\page_home\utilities\test_data_fk.xlsx"
class Excel_test_data:
    pass

def locators_fetch_from_excel(path, shet_name):
    """reading only two coloumns in the excel to store like key and value pairs
    so whenver data adding add like key & value pairs in two coloumns only"""
    wb = load_workbook(path)
    ws = wb[shet_name]
    max_rows = ws.max_row
    max_cols = ws.max_column
    print(max_cols, max_rows)
    for row in range(2, max_rows+1):
        for col in range(1, max_cols+1):
            # print(ws['A' + str(row)].value, ws['B' + str(row)].value)
            setattr(Excel_test_data, ws['A' + str(row)].value, eval(ws['B' + str(row)].value))
