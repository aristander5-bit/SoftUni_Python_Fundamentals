title_input = input()
article = input()

print(f"<h1>\n    {title_input}\n</h1>")
print(f"<article>\n    {article}\n</article>")

while True:
    comment_input = input()
    if comment_input == "end of comments":
        break

    print(f"<div>\n    {comment_input}\n</div>")