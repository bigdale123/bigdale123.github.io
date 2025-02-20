import os
import re
import shutil
import sys
from datetime import datetime

def copy_vault_files(path_to_vault_folder):
    # Check that folder contains posts folder (validity check)
    if not os.path.isdir(path_to_vault_folder):
        raise IOError("Given path does not exist.")
    if not os.path.isdir(os.path.join(path_to_vault_folder, 'posts')):
        raise IOError("Given path does not contain a 'posts' folder.")

    # Recursively copy files over, maintaining the structure, including attachments
    shutil.copytree(path_to_vault_folder, os.path.join(os.getcwd(), "content"), dirs_exist_ok=True)

    # For every file that was copied over, replace obsidian formatted images with appropriate hugo image format
    for dirpath, _, filenames in os.walk("content"):
        for filename in filenames:
            if filename.endswith('.md'):
                file_path = os.path.join(dirpath, filename)
                # print(f"Markdown File: {file_path}")
                attachments_directory = os.path.join(dirpath, 'attachments')

                # Load file content and find all images matching format ![[]]
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()

                images = re.findall(r'\[\[([^]]+\.(?:png|jpg|jpeg|gif|bmp|svg|webp))\]\]', content)

                for image in images:
                    # Edge case: check that the image actually exists before replacing the markdown
                    # print(f"Found Image: {image}")
                    # check that attachments directory exists, only if file contains images
                    if not os.path.isdir(attachments_directory):
                        raise IOError(f"Attachments directory for file {file_path} does not exist")
                    image_path = os.path.join(attachments_directory, image)
                    if os.path.exists(image_path) and os.path.isfile(image_path):
                        # image exists, replace markdown and copy file to static/attachments
                        # copy file to static/attachments
                        new_image = os.path.join("static", "attachments", image)
                        os.makedirs(os.path.join("static", "attachments"), exist_ok=True)
                        shutil.copy2(image_path, new_image)
                        # replace markdown
                        new_markdown = f"![{image}](/attachments/{image.replace(' ', '%20')})"
                        # print(new_markdown)
                        content = content.replace(f"![[{image}]]", new_markdown)
                        print(f"Image Found in {file_path}:\n    Replacing ![[{image}]] with {new_markdown}")
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(content)    

def publish():
    os.system("hugo")
    commit_message = f"Automated Publish on {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}"
    os.system("git add *")
    os.system(f'git commit -am "{commit_message}"')
    os.system("git push")


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Usage: python3 obsidian_import.py <path>")
        quit()
    path_to_vault_folder = sys.argv[1]
    copy_vault_files(path_to_vault_folder)
    # choice = input("Do you want to go ahead and publish these changes? (yes/no): ").strip()

    # if choice in ("yes,", "y"):
    #     publish()
