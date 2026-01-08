import numpy as np

leads = np.array([
    # s  m    t  w   th
    [12, 18, 10, 15, 5],   # facebook
    [20, 25, 22, 18, 8],   # insta
    [18, 30, 25, 22, 10],  # youtube
    [25, 28, 30, 26, 12],  # refferal
    [30, 35, 28, 32, 15],  # walkin
    [40, 45, 38, 40, 20],  # reddit
    [35, 50, 42, 45, 25]   # camp
    
])

#1. total leads generated each day

total_leads_eachday = np.sum(leads,axis=0)
print(total_leads_eachday)

#2. total leads from each source in 7 days
total_leads_eachsource = np.sum(leads,axis=1)
print(total_leads_eachsource)

#3. Highest lead each day
print(np.max(leads,axis=0))

#4. Highest lead day
day_wise_total = np.sum(leads,axis=0)
#max_total = np.max(day_wise_total)
print(np.argmax(day_wise_total))

#5. Average leads per source
print(np.average(leads,axis=1))

#6. Average leads per day
print(np.average(leads,axis=0))

#7. Highest lead source
source_wise_total = np.sum(leads,axis=1)
print(source_wise_total)
print(np.argmax(source_wise_total))