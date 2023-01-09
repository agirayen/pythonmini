# pip install resume-parser
def scan_resume(resume):
    from resume_parser import resumeparse
    data= resumeparse.read_file(resume)
    for i,j in data.items():
        print(f"{i}:>>{j}")
scan_resume("Agnita-Resume-2022.pdf")        
        
