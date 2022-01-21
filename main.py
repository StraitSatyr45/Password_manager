'''
You can always find your passwords at vit.txt and
also you may ask for pull requests, it is upon me 
to chose tho, XD , also please checkout this soft
ware
Though I tried to save space, but it didn't work
so sorry, because of how huge the app is, (200 
bytes)
'''


#enter the password
password = input("Enter your password: ")
#enter the website name
website_name = input("Enter the website/app name: ")

#this string creates a string that will be used to write to the file for eq - password - website_name
array = '\n' + password + "-" + website_name
#this is the process where the file is created and writted to
vit = open("vit.txt", "a")
vit.write(array)
vit.close()