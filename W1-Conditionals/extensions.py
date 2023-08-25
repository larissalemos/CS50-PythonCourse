'''
This is a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends,
case-insensitively, in any of these suffixes:
.gif, .jpg, .jpeg, .png, .pdf, .txt, .zip
'''

filename = input("What is the name of the file? ").strip().casefold()
match filename:
    case str() as g if g.endswith(".gif"):
        print("image/gif")
    case str() as j if j.endswith(".jpg"):
        print("image/jpeg")
    case str() as k if k.endswith(".jpeg"):
        print("image/jpeg")
    case str() as p if p.endswith(".png"):
        print("image/png")
    case str() as r if r.endswith(".pdf"):
        print("application/pdf")
    case str() as t if t.endswith(".txt"):
        print("text/plain")
    case str() as z if z.endswith(".zip"):
        print("application/zip")
    case _:
        print("application/octet-stream")