#!/usr/bin/env python3 

##################################################
## Job Logic 
##################################################
## A simple script to show a rudimentary "job" 
## acquisition logic sequence 
##################################################
## Author: Charles F Port 
## Copyright: Copyright 2021 
## License: MIT (Most Permissive) 
## Version: 1.0.0
## Email: cport@rawbw.com
##################################################

job = 0 
interview = 0 

def got_interview():
    interview_0 = input("#" * 15 + "\n" + "Did your resume generate interest enough to get interview? True or False?")
    if(interview_0=="True"):
        i_bool = True
    else:
        i_bool = False
    return(i_bool)

def job_offer():
    job_0 = input("#" * 15 + "\n" + "Did your job interview generate a job offer? True or False?")
    if(job_0=="True"):
        j_bool = True
    else:
        j_bool = False
    return(j_bool)

while job < 1 and interview < 10:
    print("#" * 15 + "\n" + "Write/Re-write Resume")
    print("#" * 15 + "\n" + "Show Skills")
    print("#" * 15 + "\n" + "Send Resume")
    print("#" * 15 + "\n" + "Get Interviewed")
    status = got_interview() 
    if status:
        print("Congratulations")
        offer_status = job_offer()
        if offer_status:
            print("Great! Whew!")
            break
        else:
            continue 
    interview = interview + 1
    if interview == 9:
        print("\n" + "#" * 50 + "\n" + "Sorry!!!!!! Looks like you might stay unemployed." + "\n" + "#" * 50 + "\n")
