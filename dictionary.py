pr = {"apple": 100, "khiar": 500, "narengi": 18 }


print(pr["apple"])


price = {"apple":150.6 , "banana": 65 , "khiar": 11.300}

rate = {"jadi": {"math": 18 , "fizik": 14 , "sport": 20} , "ahmad": {"math": 13 , "fizik": 15 , "sport": 2}}

print(rate.items())

print(price.get("halal" , -1))

chap = f"i want to buy a few khiar how much it cost ?\n it cost is {price.get('apple')}"
print(chap)


nomre = {"list1": [1,2,3,4,5,6,7] , "list2":[7,8,9,0]}
kelasha = {1: ["jadi","saeed","ali","sahar"], 2:["melissa","melina","susan","mike"]}

print(kelasha.get(1))

