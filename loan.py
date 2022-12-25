def cal_loan(acct_num,sal,acct_bal,loan_type,loan_expt,emi_expt):
    eligible_loan_amt= 0
    bank_emi_expet=0
    f=0
    if(acct_num>999 and acct_num<2000):
        if acct_bal>99999:
            if loan_type=="CAR"and sal>25000:
                if emi_expt<=36 and loan_expt<=500000:
                    eligible_loan_amt=500000
                    bank_emi_expet=36
                    f=1
                else:
                    print("The customer is not eligible for the loan")
            elif loan_type=="HOUSE"and sal>50000:
                if emi_expt<=60 and loan_expt<=600000:
                    eligible_loan_amt=600000
                    bank_emi_expet=60
                    f=1
                else:
                    print("The customer is not eligible to the loan")
            elif loan_type=="BUSINESS" and sal>75000:
                if emi_expt<=84 and loan_expt<=7500000:
                    eligible_loan_amt=7500000
                    bank_emi_expet=84
                    f=1
                else:
                    print("The customer is not eligible to the loan")
            else:
                print("invalid loan type or salary")
        else:
            print("Insufficient account balance")
    else:
        print("Invalid account number")
    if f==1:
        print("Account number:",acct_num)
        print("The custmoer can avail the amount of Rs:",eligible_loan_amt)
        print("Eligible EMIs:",bank_emi_expet)
        print("Requsted loan amount:",bank_emi_expet)
cal_loan(1001,40000,250000,"CAR",300000,30)