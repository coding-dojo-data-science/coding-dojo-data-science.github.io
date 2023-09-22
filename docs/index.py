import os
print(os.path.abspath(os.curdir))

folder = "docs/Instructions"
output_file = "index-links.txt"

html_files = sorted(os.listdir(folder))
print(html_files)

txt_links = "<ol>\n"
for file in html_files:
	name = file.replace("_",' ').replace(".html","").title()
	full_fname = os.path.join("instructions/",file)
	new = f"<li><a href='{full_fname}'>{name}</a></li>\n"
	txt_links+=new
txt_links += "\n</ol>"

with open(output_file,'w') as f:
	f.write(txt_links)
	