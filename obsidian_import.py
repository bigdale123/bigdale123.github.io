#!/usr/bin/env python3

import os
import re
import shutil
import sys
import subprocess
from datetime import datetime


def copy_vault_files(path_to_vault_folder):
    """
    Copies an Obsidian vault's posts/ folder into a Hugo project, preserving
    whatever directory structure exists.

    The posts/ tree is mirrored under content/posts/, and any images found in
    a post's attachments/ subfolder are copied to static/attachments/ under the
    same relative path as the post directory.

    Example:
        Vault:
            posts/2025/My Post/My Post.md
            posts/2025/My Post/attachments/image.png
            posts/misc/Notes.md

        Hugo output:
            content/posts/2025/My Post/My Post.md
            static/attachments/2025/My Post/image.png
            content/posts/misc/Notes.md
    """
    if not os.path.isdir(path_to_vault_folder):
        raise IOError(f"Given path does not exist: {path_to_vault_folder}")

    posts_src = os.path.join(path_to_vault_folder, "posts")
    if not os.path.isdir(posts_src):
        raise IOError("Given vault path does not contain a 'posts' folder.")

    posts_dst = os.path.join(os.getcwd(), "content", "posts")
    print(f"Copying posts from: {posts_src}")
    shutil.copytree(posts_src, posts_dst, dirs_exist_ok=True)

    # Walk every markdown file and rewrite image embeds
    for dirpath, _, filenames in os.walk(posts_dst):
        for filename in filenames:
            if not filename.endswith(".md"):
                continue
            file_path = os.path.join(dirpath, filename)
            # Relative path of this file's directory inside content/posts/
            # e.g. "2025/My Post" or "misc"
            rel_dir = os.path.relpath(dirpath, posts_dst)
            _process_markdown(file_path, rel_dir)


def _process_markdown(file_path, rel_dir):
    """
    Rewrites Obsidian-style image embeds (![[image.png]]) in a markdown file
    to standard Hugo markdown, and copies the images to the mirrored location
    under static/attachments/<rel_dir>/.
    """
    image_pattern = re.compile(
        r'!\[\[([^\]]+\.(?:png|jpg|jpeg|gif|bmp|svg|webp))\]\]',
        re.IGNORECASE,
    )

    with open(file_path, "r", encoding="utf-8") as fh:
        content = fh.read()

    images = image_pattern.findall(content)
    if not images:
        return

    attachments_src = os.path.join(os.path.dirname(file_path), "attachments")
    if not os.path.isdir(attachments_src):
        raise IOError(
            f"'{file_path}' contains image embeds but has no attachments/ "
            f"directory at: {attachments_src}"
        )

    # Mirror the post's relative path under static/attachments/,
    # nested one level deeper under the markdown file's own name.
    post_title = os.path.splitext(os.path.basename(file_path))[0]
    attachments_dst = os.path.join(os.getcwd(), "static", "attachments", rel_dir, post_title)

    modified = False
    for image in images:
        # Use only the basename for the source lookup
        image_filename = os.path.basename(image)
        image_src = os.path.join(attachments_src, image_filename)

        if not os.path.isfile(image_src):
            print(f"  WARNING: image not found, skipping: {image}")
            print(f"      Article: {post_title}")
            continue

        os.makedirs(attachments_dst, exist_ok=True)
        shutil.copy2(image_src, os.path.join(attachments_dst, image_filename))

        parts = [p for p in rel_dir.replace("\\", "/").split("/") if p != "."]
        url_path = "/".join(
            ["/attachments"] + parts + [post_title.replace(" ", "%20"), image_filename.replace(" ", "%20")]
        )
        new_md = f"![{image_filename}]({url_path})"
        old_md = f"![[{image}]]"  # old_md still uses full original match to replace correctly

        content = content.replace(old_md, new_md)
        modified = True

    if modified:
        with open(file_path, "w", encoding="utf-8") as fh:
            fh.write(content)


def publish(commit_message):
    os.system("hugo")
    os.system("git add .")
    os.system(f'git commit -am "{commit_message}"')
    os.system("git push")


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Usage: python3 obsidian_import.py <path-to-vault>")
        sys.exit(1)

    path_to_vault_folder = sys.argv[1]
    copy_vault_files(path_to_vault_folder)

    choice = input("\nPublish these changes? (yes/no): ").strip().lower()
    if "y" in choice:
        commit_message = (
            f"Automated Publish on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )
        if "y" in input("Write a custom commit message? (yes/no): ").strip().lower():
            commit_message = input("Commit message: ").strip()
        publish(commit_message)
    else:
        if "y" in input("Preview with `hugo serve`? (yes/no): ").strip().lower():
            subprocess.run(["hugo", "serve", "--disableFastRender"])