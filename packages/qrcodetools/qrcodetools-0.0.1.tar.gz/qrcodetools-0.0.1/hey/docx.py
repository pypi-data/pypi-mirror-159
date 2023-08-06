from win32com.client import constants, gencache
import os  # 目录的操作


def createpdf(wordPath, pdfPath):
    word = gencache.EnsureDispatch('Word.Application')
    doc = word.Documents.Open(wordPath, ReadOnly=1)
    # 转换方法
    doc.ExportAsFixedFormat(pdfPath, constants.wdExportFormatPDF)
    word.Quit()


# 单个文件转换
# createpdf('C:/Users/Administrator/PycharmProjects/Project3/info.docx','C:/Users/Administrator/PycharmProjects/Project3/info.pdf')

# 多个文件的转换:
# 自己指定路径，
# 为了适配wps不能转换doc的问题，这里限定：只能转换docx
def docx2pdf(path):
    print(os.listdir(path))  # 当前文件夹下的所有文件
    wordfiles = []
    for file in os.listdir('.'):
        if file.endswith(('.doc', '.docx')):  # 通过后缀找出所有的workd文件
            wordfiles.append(file)
    print(wordfiles)

    for file in wordfiles:
        # 获取文件路径
        filepath = os.path.abspath(file)
        index = filepath.rindex('.')
        # 通过截取获取pdfpath
        pdfpath = filepath[:index] + '.pdf'
        print(pdfpath)
        createpdf(filepath, pdfpath)
