import os
import re

# 1. config.yaml
with open('config.yaml', 'r', encoding='utf-8') as f:
    config = f.read()
# Regex to match "  comment_box:" and all indented lines underneath
config = re.sub(r'  comment_box:\n(    .*?\n)*', '', config)
with open('config.yaml', 'w', encoding='utf-8') as f:
    f.write(config)
    
# 2. src/branding.py
with open('src/branding.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
skip = False
for line in lines:
    if line.startswith('def add_comment_box(') or 'if cfg.get("comment_box"' in line:
        skip = True
        
    if skip and (line.startswith('def ') and not line.startswith('def add_comment_box(')):
        skip = False
    elif skip and 'if cfg.get("comment_box"' not in line and (line.startswith('    #') or line.startswith('    if cfg')):
        # Check if we exited the comment_box block in branding.py main logic
        # The block in branding.py is:
        #     # Comment Box
        #     if cfg.get("comment_box", {}).get("enabled", False):
        #         out = brand_dir / "with_comment.mp4"
        #         current = add_comment_box(current, out)
        pass

# Actually simpler to just use regex for branding.py too
with open('src/branding.py', 'r', encoding='utf-8') as f:
    content = f.read()
    
# Remove def add_comment_box and its body
content = re.sub(r'def add_comment_box.*?return output_path\n', '', content, flags=re.DOTALL)
content = re.sub(r'    # Comment Box\n    if cfg.get\("comment_box".*?current = add_comment_box\(current, out\)\n', '', content, flags=re.DOTALL)

with open('src/branding.py', 'w', encoding='utf-8') as f:
    f.write(content)
