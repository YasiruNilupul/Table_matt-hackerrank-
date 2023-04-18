height_and_length=list(map(int,input().split()))
rows='-'
mid_rows='.|.'
n=0
k=(height_and_length[0]-1)//2+1
for i in range((height_and_length[0]-1)//2):
    rows='-'*(height_and_length[1]-(3*k)) +mid_rows*(2*n+1)+'-'*(height_and_length[1]-3*k)
    print(rows)
    n+=1
    k+=1
k=(height_and_length[0]-1)
n=(height_and_length[0]-1)//2-1
print('-'*((height_and_length[1]//2)-3)+'WELCOME'+'-'*((height_and_length[1]//2)-3))
for i in range((height_and_length[0]-1)//2):
    rows='-'*(height_and_length[1]-(3*k)) +mid_rows*(2*n+1)+'-'*(height_and_length[1]-3*k)
    print(rows)
    n-=1
    k-=1
