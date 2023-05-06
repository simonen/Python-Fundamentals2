string = input().split("\\")

name, ext = string[-1].split(".")
print(f"File name: {name}\n"
      f"File extension: {ext}")

