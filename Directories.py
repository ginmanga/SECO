import os

directory = r'C:\Users\Panqiao\Documents\Research\SEC Online - 05042017\All'
path = os.path.abspath(directory)
print(os.listdir(path))

def folder_loop(path):
    """Loops through contents of a folder
    saves file path"""
    req_paths = []
    for path, dirs, files in os.walk(path):
       # print(path)
        #print(dirs)
        #print(files)
        if files != []:
            for i in files:
                file_path = os.path.join(path,i)
                print(i)
                print(file_path)
                req_paths.append(file_path)
    print(req_paths)
    return req_paths

    #for file in [f for f in os.listdir(path)]:
        # Loops through files and folders in path
        # calls fsttotal function
        #file_path_a = os.path.join(path, file)
        #print(file_path_a)
folder_loop(path)

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
