def drop_firtst_last(grades):
    first,*middle,last=grades
    return avg(middle)

record=('Dave','jflksaj','19927672430','19927672430')
name,email,*phone_number=record

def compare_trailing(sales_record):
    ×trailing_qtrs,current_qtr=sales_record
    trailing_avg=sum(trailing_qtrs)/len(trailing_qtrs)
    return avg_comparison(trailing_avg,current_qtr)