import webbrowser
import time

country = "Italy"

html_content = f"<html><head></head><h1>{country}</h1>"

with open("index.html","w") as html_file:
    html_file.write(html_content)
    print("SUCCESSFUL")
