import os

export_dir = "./frontend"
# export_dir = "./.web/_static"

def replace_absolute_to_relative(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith((".html", ".js", ".css")):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                updated_content = (
                    content.replace('="/', '="./')
                        .replace(" url(/", " url(./")
                )
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(updated_content)

replace_absolute_to_relative(export_dir)
print("Rutas absolutas convertidas a relativas.")