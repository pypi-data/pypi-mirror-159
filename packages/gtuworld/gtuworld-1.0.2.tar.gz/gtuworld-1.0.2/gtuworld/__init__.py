import os, requests

def download(branch, subject_codes):
    # invalid branch
    if branch != "BE" and branch != "DI":
        print("Invalid branch. Please choose BE/DI.")
        return

    # create GTU folder
    dir = os.getcwd() + '/GTU'
    print(f"Creating GTU folder in {os.getcwd()}")
    try:
        os.mkdir(dir)
    except:
        pass
    
    for subject_code in subject_codes:
        print(f"\n\nStarting fetching {subject_code} papers")
        # get all paper links
        paper1 = f"https://www.gtu.ac.in/uploads/W2021/{branch}/{subject_code}.pdf"
        paper2 = f"https://www.gtu.ac.in/uploads/W2020/{branch}/{subject_code}.pdf"
        paper3 = f"https://www.gtu.ac.in/uploads/W2019/{branch}/{subject_code}.pdf"
        paper4 = f"https://www.gtu.ac.in/uploads/W2018/{branch}/{subject_code}.pdf"
        paper5 = f"https://www.gtu.ac.in/uploads/W2017/{branch}/{subject_code}.pdf"
        paper6 = f"https://www.gtu.ac.in/uploads/S2021/{branch}/{subject_code}.pdf"
        paper7 = f"https://www.gtu.ac.in/uploads/S2020/{branch}/{subject_code}.pdf"
        paper8 = f"https://www.gtu.ac.in/uploads/S2019/{branch}/{subject_code}.pdf"
        paper9 = f"https://www.gtu.ac.in/uploads/S2018/{branch}/{subject_code}.pdf"

        r1 = requests.get(paper1)
        r2 = requests.get(paper2)
        r3 = requests.get(paper3)
        r4 = requests.get(paper4)
        r5 = requests.get(paper5)
        r6 = requests.get(paper6)
        r7 = requests.get(paper7)
        r8 = requests.get(paper8)
        r9 = requests.get(paper9)

        # create subject code folders inside GTU folder
        print(f"Creating {subject_code} folder in /GTU")
        inner_dir = dir + '/' + str(subject_code)
        try:
            os.mkdir(inner_dir)
        except:
            pass

        print(f"Saving {subject_code} papers")
        # if status_code is 200 then save it into the directory 
        if r1.status_code == 200:
            with open(f'{inner_dir}/W2021.pdf', 'wb') as f:
                f.write(r1.content)

        if r2.status_code == 200:
            with open(f'{inner_dir}/W2020.pdf', 'wb') as f:
                f.write(r2.content)

        if r3.status_code == 200:
            with open(f'{inner_dir}/W2019.pdf', 'wb') as f:
                f.write(r3.content)

        if r4.status_code == 200:
            with open(f'{inner_dir}/W2018.pdf', 'wb') as f:
                f.write(r4.content)

        if r5.status_code == 200:
            with open(f'{inner_dir}/W2017.pdf', 'wb') as f:
                f.write(r5.content)

        if r6.status_code == 200:
            with open(f'{inner_dir}/S2021.pdf', 'wb') as f:
                f.write(r6.content)

        if r7.status_code == 200:
            with open(f'{inner_dir}/S2020.pdf', 'wb') as f:
                f.write(r7.content)

        if r8.status_code == 200:
            with open(f'{inner_dir}/S2019.pdf', 'wb') as f:
                f.write(r8.content)

        if r9.status_code == 200:
            with open(f'{inner_dir}/S2018.pdf', 'wb') as f:
                f.write(r9.content)

    # create txt file
    print("Please read instructions file in GTU folder :)")
    with open(f"{dir}/instructions.txt", 'w') as f:
        f.write(f"Welcome to GTU World!\n\nYou will find your {subject_codes} papers inside GTU directory.\nHope, you will found this module helpful.\n\nThanks & Regards,\nDhiraj Beri.")
