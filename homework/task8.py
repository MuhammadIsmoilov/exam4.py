rubl1 = int(input())
rubl2 = int(input())
rubl3 = int(input())
rubl4 = int(input())
change1 = rubl1 * 100 + rubl2
change2 = rubl3 * 100 + rubl4
change3 = change2 - change1
print(int(change3/100),(change3%100))