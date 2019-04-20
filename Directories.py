import os

directory = r'C:\Users\Panqiao\Documents\Research\SEC Online - 05042017\All'
path = os.path.abspath(directory)
print(os.listdir(path))

def folder_loop(path):
    """Loops through contents of a folder
    saves file path"""
    req_paths = []
    for path, dirs, files in os.walk(path):
        ps = [os.path.join(path, i) for i in files]
        req_paths.extend(ps)
    return req_paths


req_paths = folder_loop(path)
for i in req_paths:
    print(i)

def fipath(gvkey, path, ptofile = 0):
    """Function delivers path to files to open"""
    # call fsstotal, getText and parseText
    path = os.path.abspath(path)
    names = [['File_Path', 'File_Name', 'Doc_num', 'Doc_count',
              'start_paragraph', 'Company Name','SIC', 'DATE', 'TICKER']]
    names2 = [['File_Path', 'File_Name', 'Doc_num', 'Doc_count', 'start_paragraph',
               'Document Type', 'Company Name', 'Filing Date','Document Date',
               'TICKER', 'Exchange','Incorporation', 'CUSIP', 'SIC']]
    names3 = [['File_Path', 'File_Name', 'Doc_num', 'Doc_count']]
    names4 = [['File_Path', 'File_Name', 'Doc_num', 'Doc_count']]



#fipath(0, directory, 0)
