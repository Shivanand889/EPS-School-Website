import os

x =1

for i in os.listdir("images"):
    os.rename(f"images/{i}", f"images/img{x}.jpg")
    x+=1