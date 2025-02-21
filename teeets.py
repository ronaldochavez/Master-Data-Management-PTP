import markdown

# Read the Markdown file
with open(r"C:\Users\Chaver19\OneDrive - Heineken International\Desktop\PYTHON\notas\SOP_PTP_MDM_ANALYST_004.md", "r", encoding="utf-8") as f:
    md_content = f.read()

# Convert to HTML
html_content = markdown.markdown(md_content)

# Save as an HTML file
with open(r"C:\Users\Chaver19\OneDrive - Heineken International\Desktop\PYTHON\notas\html.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Markdown converted to HTML successfully!")