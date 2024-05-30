from pandas import read_excel


def convert_xls_to_xlsx(path: str) -> str:
    df = read_excel(path, engine='xlrd')
    new_path: str = path.replace(".xls", ".xlsx")
    df.to_excel(new_path, index=False, engine='openpyxl')
    # df.close()
    return new_path


convert_xls_to_xlsx(r"C:\Users\1234x\PycharmProjects\biolog\examples\Пример ввода_AZB1_1_1.xls")