#Ex2 swap 2 number
def swap(S1,S2):
    S3=S1
    S4=S2
    S2=S3
    S1=S4
    return (S1,S2)

(S1_change, S2_change)=swap(1,2)
print('a =', S1_change, ' b =', S2_change, sep=' ')