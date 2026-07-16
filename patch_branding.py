import os

with open('src/branding.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
skip = False
for i, line in enumerate(lines):
    if line.startswith("def add_comment_box("):
        skip = True
        continue
    
    if skip:
        # Stop skipping when we find another top level def or if
        if line.startswith("def ") or line.startswith("if __name__"):
            skip = False
        else:
            continue
            
    if "if cfg.get(\"comment_box\"" in line:
        skip = True
        continue
        
    if skip and (line.startswith("    #") or line.startswith("    if cfg.get")):
        pass # this is inside the comment box calling block. Wait, this logic is flimsy.
