cards= [7, 11, 10, 7, 7,7,7,7,7, 3, 1]
# cards=[]
query=7

# def locate_card(cards,query):
#     position=0
#     if len(cards)>0:
#         for card in cards:
#             if cards[position]==query:
#                 return position
#             position+=1
#     return -1
# cd=locate_card(cards,query)
# print(cd)
def locate_Cards(cards,query):
    l,r=0,len(cards)-1
    while l<=r:
        mid=(l+r)//2
        if cards[l]==query:
            return l
        elif cards[r]==query:   
            return r
        elif cards[mid]==query:
            return mid
        elif cards[mid]<query:
            r=mid-1
        else:
            l=mid+1
    return -1
cd=locate_Cards(cards,query)
print(cd)
