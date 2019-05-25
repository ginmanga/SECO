import os

directory = r'C:\Users\Panqiao\Documents\Research\SEC Online - 05042017\All'
#directory = r'C:\Users\Panqiao\Documents\Research\SEC Online - 05042017\Specs\10K'
#directory = r'C:\Users\Panqiao\Documents\Research\SEC Online - 05042017\ALLN'
#directory = r'C:\Users\Panqiao\Documents\Research\SEC Online - 05042017\single'
#directory = r'C:\Users\Panqiao\Documents\Research\SEC Online - 05042017\check'
path = os.path.abspath(directory)
#print(path)

start_docu = ["of", "DOCUMENTS"]

terms_old_1 = ["[*Summary]             COPYRIGHT 1988 SEC ONLINE, INC.",
             "[*Summary]             COPYRIGHT 1989 SEC ONLINE, INC.",
             "[*Summary]             COPYRIGHT 1990 SEC ONLINE, INC.",
             "[*Summary]             COPYRIGHT 1991 SEC ONLINE, INC.",
             "[*Summary]             COPYRIGHT 1992 SEC ONLINE, INC.",
             "[*Summary]             COPYRIGHT 1993 SEC ONLINE, INC.",
             "[*Summary]             COPYRIGHT 1994 SEC ONLINE, INC.",
             "[*Summary]             COPYRIGHT 1995 SEC ONLINE, INC.",
             ]
terms_old_2 = ["COPYRIGHT 1987 SEC ONLINE, INC.",
               "COPYRIGHT 1988 SEC ONLINE, INC.",
               "COPYRIGHT 1989 SEC ONLINE, INC.",
               "COPYRIGHT 1990 SEC ONLINE, INC.",
               "COPYRIGHT 1991 SEC ONLINE, INC.",
               "COPYRIGHT 1992 SEC ONLINE, INC.",
               "COPYRIGHT 1993 SEC ONLINE, INC.",
               "COPYRIGHT 1994 SEC ONLINE, INC.",
               "COPYRIGHT 1995 SEC ONLINE, INC."]

terms_old = terms_old_1 + terms_old_2
terms_new_1 = ["SEC Online Database"]

def folder_loop(path):
    """Loops through contents of a folder
    saves file path, keep only text files"""
    req_paths = []
    for path, dirs, files in os.walk(path):
        req_paths.extend([os.path.join(path, i) for i in files])
    req_paths_doc = [i for i in req_paths if os.path.splitext(i)[1] == ".doc" or os.path.splitext(i)[1] == ".DOC"]
    req_paths = [i for i in req_paths if os.path.splitext(i)[1] == ".txt" or os.path.splitext(i)[1] == ".TXT"]
    return req_paths, req_paths_doc


req_paths, req_paths_doc = folder_loop(path)
#print(req_paths)
print(req_paths_doc)

#for i in req_paths_doc:
    #print(i)

def det_file(file):
    """If called, it determines the file type and number of documents in the file"""
    #First, find the first line of the first document
    #Second, determine file type.
    #Return a list with file_name, file_type, number of docs and path
    #Find first instance of # of # DOCUMENTS
    #Make separate list with document name, number and line of each document
    doc_count = 0
    line_count = 0
    doc_type_known = False
    doc_type = ''
    fhand = open(file, encoding="utf8")
    #fhand = open(file)
    #return None
    #print(fhand)
    #print(file)
    #print(fhand)
    file_info = [file,'','']
    doc_info = [file,'','']
    doc_file_info = []
    #try:
    for i in fhand:
        #print("LINE")
        #print(i)
        #if all(f in i for f in start_docu) and len(set(i.split())-set(start_docu)) is 2 \
        #and all(s.isdigit for s in list(set(i.split())-set(start_docu))):
        #doc_count += 1
        #doc_info[1] = doc_count
        #doc_info[2] = line_count
        #doc_file_info.append([file,doc_count,line_count])
        #print(doc_count)
        #print(line_count)
        if doc_count == 1 and not doc_type_known:
            if terms_new_1[0].lower() in i.lower():
                doc_type_known = True
                file_info[1] = "SEC_NEW"
                doc_type = "SEC_NEW"
            if any(f.lower() in i.lower() for f in terms_old_2):
                file_info[1] = "SEC_OLD"
                doc_type = "SEC_OLD"
                doc_type_known = True
        if all(f in i for f in start_docu) and len(set(i.split())-set(start_docu)) is 2 \
                and all(s.isdigit for s in list(set(i.split())-set(start_docu))):
            doc_count += 1
            doc_info[1] = doc_count
            doc_info[2] = line_count
            doc_file_info.append([file, doc_type, str(doc_count), str(line_count)])
        file_info[2] = str(doc_count)
        try:
            doc_file_info[0][1] = doc_type
        except:
            None
        line_count += 1
#except:
    #print(doc_file_info)
        #print("Error while reading file")
    return file_info, doc_file_info



def getText(para, par_top, option = ""):
    """Function gathers text from text files for later parsing"""
    #Gather Text From Beginning of Document Until Table of Contents
    fullText = []
    aicpa_count = 29 #number of line to check at start of document
    if option is "check":
        aicpa_count = 10
    if option is 'seconline':
        aicpa_count = 40
    for i in par_top:
        newText = []
        for j in range(i, i+aicpa_count):
           (newText.append(para[j].text.strip()) if para[j].text.strip() != '' else None)
        fullText.append(newText)
    return fullText

def det_db(file):
    """Determines if files fro Sec Online Old or New"""
    #Gather Text From Beginning of Document Until Table of Contents
    #Old After # of # Docs always has:   [*Summary]             COPYRIGHT 1990 SEC ONLINE, INC.
    #New: after # of $ Docs always gas: SEC Online Database
    ttofind_1 = ["[*Summary]             COPYRIGHT 1988 SEC ONLINE, INC.",
                 "[*Summary]             COPYRIGHT 1989 SEC ONLINE, INC.",
                 "[*Summary]             COPYRIGHT 1990 SEC ONLINE, INC.",
                 "[*Summary]             COPYRIGHT 1991 SEC ONLINE, INC.",
                 "[*Summary]             COPYRIGHT 1992 SEC ONLINE, INC.",
                 "[*Summary]             COPYRIGHT 1993 SEC ONLINE, INC.",
                 "[*Summary]             COPYRIGHT 1994 SEC ONLINE, INC.",
                 "[*Summary]             COPYRIGHT 1995 SEC ONLINE, INC.",
                 ]
    ttofind_2 = ["COPYRIGHT 1988 SEC ONLINE, INC.",
                 "COPYRIGHT 1989 SEC ONLINE, INC.",
                 "COPYRIGHT 1990 SEC ONLINE, INC.",
                 "COPYRIGHT 1991 SEC ONLINE, INC.",
                 "COPYRIGHT 1992 SEC ONLINE, INC.",
                 "COPYRIGHT 1993 SEC ONLINE, INC.",
                 "COPYRIGHT 1994 SEC ONLINE, INC.",
                 "COPYRIGHT 1995 SEC ONLINE, INC.",
                 ]

    fhand = open(file)
    #print(fhand)
    for i in fhand:
        print("LINE")
        print(i)
    fullText = []
    #aicpa_count = 29 #number of line to check at start of document
    #if option is "check":
        #aicpa_count = 10
    #if option is 'seconline':
        #aicpa_count = 40
    #for i in par_top:
        #newText = []
        #for j in range(i, i+aicpa_count):
           #(newText.append(para[j].text.strip()) if para[j].text.strip() != '' else None)
        #fullText.append(newText)
    return fullText


def main(path):
    """Main Function"""
    # First determine file type New or Old Sec
    # Second, gather text for later parsing
    # Two determine filing type: 10K, AR, 10Q, Proxy
    # Three Collect Information Equal to All 4
    # Collect Specific informaiton
    path = os.path.abspath(path)
    print(path)
    #names = [['File_Path', 'File_Name', 'Doc_num', 'Doc_count',
              #'start_paragraph', 'Company Name','SIC', 'DATE', 'TICKER']]
    #names2 = [['File_Path', 'File_Name', 'Doc_num', 'Doc_count', 'start_paragraph',
               #'Document Type', 'Company Name', 'Filing Date','Document Date',
               #'TICKER', 'Exchange','Incorporation', 'CUSIP', 'SIC']]
    #names3 = [['File_Path', 'File_Name', 'Doc_num', 'Doc_count']]
    #names4 = [['File_Path', 'File_Name', 'Doc_num', 'Doc_count']]
    names = [['File_Path', 'File_Name', 'Doc_num', 'Doc_count', 'start_line', 'D_base']]
    names2 = [['Filing_type', 'Filing-date', 'Document-Date', 'Ticker', 'Exchange']]
    names_10K = [['Icorp', 'Cusip', 'DUNS', 'IRS', 'SIC', 'FYE']]
    names_10Q = [['Icorp', 'Cusip', 'DUNS', 'IRS', 'SIC', 'FYE']]
    names_AR = [['Icorp', 'Cusip', 'DUNS', 'IRS', 'SIC', 'FYE']]
    names_PX = [['Icorp', 'Cusip', 'DUNS', 'IRS', 'SIC', 'FYE']]
    all_file_info = []
    docfile_info = [] #line and doc number of each file
    req_paths = folder_loop(path)[0]
    print(req_paths)
    #path_s = [os.path.splitext(i)[1] for i in req_paths]
    #req_paths = [os.path.abspath(i) for i in req_paths]
    #print(req_paths)
    for i in req_paths:
        print(i)
        a, b = det_file(i)
        #print(b)
        #all_file_info.append(det_file(i)[0])
        all_file_info.append(a)
        docfile_info.extend(b)

        #print(i)
        #print(os.path.splitext(i))
    #print(all_file_info)
    #print(docfile_info)
    return all_file_info, docfile_info
    #for i in req_paths:

def write_file(path_file, data, options = 0):
    """Writes all data to file"""
    #If no GVKEY or document contains many files, then one CSV file per document
    #For files containing less
    #if we know the gvkey, write a single file with all the files data
    #if no gvkey, write one per file
    path_to_1 = os.path.join(path_file, 'file_data.txt')
    path_to_2 = os.path.join(path_file, 'doc_file_data.txt')
    #data_ss = open(os.path.join(path_file, 'sum.text'),'w')
    with open(path_to_1,'w') as file:
        file.writelines('\t'.join(i) + '\n' for i in data[0])
    file.close()
    with open(path_to_2,'w') as file:
        file.writelines('\t'.join(i) + '\n' for i in data[1])
    file.close()

#a, b = main(path)
#print(a)
#print(b)
#write_file(path,[a, b])



