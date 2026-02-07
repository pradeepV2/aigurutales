#!/usr/bin/env python3
"""
AI Jungle Challenge - Chapter Generator
This script generates all 14 chapter HTML files from the markdown content.
"""

import re
import os

# Chapter configuration
CHAPTERS = [
    {
        'id': 'chapter-1',
        'file': 'chapter-1-eagle.html',
        'number': 'Chapter 1',
        'title': 'Eagle - The Vision Master',
        'subtitle': 'Learning How CNNs See the World',
        'emoji': '🦅',
        'next': 'chapter-2-snake.html',
        'prev': 'prologue.html'
    },
    {
        'id': 'chapter-2',
        'file': 'chapter-2-snake.html',
        'number': 'Chapter 2',
        'title': 'Snake - The Path Follower',
        'subtitle': 'Understanding Basic Sequential Memory (RNN)',
        'emoji': '🐍',
        'next': 'chapter-3-elephant.html',
        'prev': 'chapter-1-eagle.html'
    },
    {
        'id': 'chapter-3',
        'file': 'chapter-3-elephant.html',
        'number': 'Chapter 3',
        'title': 'Elephant - The Memory Keeper',
        'subtitle': 'The Three Magical Gates of LSTM',
        'emoji': '🐘',
        'next': 'chapter-4-lion.html',
        'prev': 'chapter-2-snake.html'
    },
    {
        'id': 'chapter-4',
        'file': 'chapter-4-lion.html',
        'number': 'Chapter 4',
        'title': 'Lion - The Attention King',
        'subtitle': 'The Revolutionary Transformer',
        'emoji': '🦁',
        'next': 'chapter-5-owl.html',
        'prev': 'chapter-3-elephant.html'
    },
    {
        'id': 'chapter-5',
        'file': 'chapter-5-owl.html',
        'number': 'Chapter 5',
        'title': 'Owl - The Understanding Master',
        'subtitle': 'BERT and Bidirectional Reading',
        'emoji': '🦉',
        'next': 'chapter-6-parrot.html',
        'prev': 'chapter-4-lion.html'
    },
    {
        'id': 'chapter-6',
        'file': 'chapter-6-parrot.html',
        'number': 'Chapter 6',
        'title': 'Parrot - The Story Weaver',
        'subtitle': 'GPT and Word-by-Word Creation',
        'emoji': '🦜',
        'next': 'chapter-7-giraffe.html',
        'prev': 'chapter-5-owl.html'
    },
    {
        'id': 'chapter-7',
        'file': 'chapter-7-giraffe.html',
        'number': 'Chapter 7',
        'title': 'Giraffe - The Efficient Helper',
        'subtitle': 'LLaMA and Open-Source AI',
        'emoji': '🦒',
        'next': 'chapter-8-zebra-twins.html',
        'prev': 'chapter-6-parrot.html'
    },
    {
        'id': 'chapter-8',
        'file': 'chapter-8-zebra-twins.html',
        'number': 'Chapter 8',
        'title': 'The Zebra Twins - Competitive Artists',
        'subtitle': 'GANs and Learning Through Competition',
        'emoji': '🦓',
        'next': 'chapter-9-chameleon.html',
        'prev': 'chapter-7-giraffe.html'
    },
    {
        'id': 'chapter-9',
        'file': 'chapter-9-chameleon.html',
        'number': 'Chapter 9',
        'title': 'Chameleon - The Shape Shifter',
        'subtitle': 'VAE and the Latent Space',
        'emoji': '🦎',
        'next': 'chapter-10-snail.html',
        'prev': 'chapter-8-zebra-twins.html'
    },
    {
        'id': 'chapter-10',
        'file': 'chapter-10-snail.html',
        'number': 'Chapter 10',
        'title': 'Snail - The Patient Perfectionist',
        'subtitle': 'Diffusion Models and 1000-Step Creation',
        'emoji': '🐌',
        'next': 'chapter-11-grand-assembly.html',
        'prev': 'chapter-9-chameleon.html'
    },
    {
        'id': 'chapter-11',
        'file': 'chapter-11-grand-assembly.html',
        'number': 'Chapter 11',
        'title': 'The Grand Assembly',
        'subtitle': 'All Powers United!',
        'emoji': '🌟',
        'next': 'chapter-12-ai-family-tree.html',
        'prev': 'chapter-10-snail.html'
    },
    {
        'id': 'chapter-12',
        'file': 'chapter-12-ai-family-tree.html',
        'number': 'Chapter 12',
        'title': 'The AI Family Tree',
        'subtitle': 'How All AI Models Are Related',
        'emoji': '🌳',
        'next': 'chapter-13-when-to-call.html',
        'prev': 'chapter-11-grand-assembly.html'
    },
    {
        'id': 'chapter-13',
        'file': 'chapter-13-when-to-call.html',
        'number': 'Chapter 13',
        'title': 'When to Call Each Animal',
        'subtitle': 'Practical Guide to Using AI',
        'emoji': '🎯',
        'next': 'epilogue.html',
        'prev': 'chapter-12-ai-family-tree.html'
    },
    {
        'id': 'epilogue',
        'file': 'epilogue.html',
        'number': 'Epilogue',
        'title': 'You Are Now AI-Literate!',
        'subtitle': 'Your Journey Continues',
        'emoji': '✨',
        'next': None,
        'prev': 'chapter-13-when-to-call.html'
    }
]


def markdown_to_html(text):
    """Convert markdown formatting to HTML"""
    
    # Handle code blocks first
    def replace_code_blocks(match):
        code = match.group(1)
        return f'<div class="code-block">{code}</div>'
    
    text = re.sub(r'```(.+?)```', replace_code_blocks, text, flags=re.DOTALL)
    
    # Headers
    text = re.sub(r'^#### (.+)$', r'<h4>\1</h4>', text, flags=re.MULTILINE)
    text = re.sub(r'^### (.+)$', r'<h3>\1</h3>', text, flags=re.MULTILINE)
    text = re.sub(r'^## (.+)$', r'<h2>\1</h2>', text, flags=re.MULTILINE)
    
    # Bold and italic
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    
    # Inline code
    text = re.sub(r'`(.+?)`', r'<code>\1</code>', text)
    
    # Process line by line for paragraphs and lists
    lines = text.split('\n')
    html_lines = []
    in_list = False
    in_special_box = None
    list_type = 'ul'
    
    for i, line in enumerate(lines):
        line = line.rstrip()
        
        # Skip if already processed as code block
        if '<div class="code-block">' in line or '</div>' in line and in_special_box != 'code':
            html_lines.append(line)
            continue
        
        # Handle special boxes
        if any(marker in line for marker in ['🔍 Pause & Think', 'Pause & Think', '⏸️ Pause & Think']):
            if in_list:
                html_lines.append(f'</{list_type}>')
                in_list = False
            html_lines.append('<div class="pause-think">')
            html_lines.append('<strong>⏸️ Pause & Think!</strong>')
            in_special_box = 'pause'
            continue
            
        if any(marker in line for marker in ['🎨 Try This', 'Try This Activity', 'Try This!']):
            if in_list:
                html_lines.append(f'</{list_type}>')
                in_list = False
            html_lines.append('<div class="try-activity">')
            html_lines.append('<strong>🎨 Try This Activity!</strong>')
            in_special_box = 'try'
            continue
        
        # Close special boxes
        if in_special_box and (line.startswith('##') or line == '---' or 
                               (i + 1 < len(lines) and lines[i+1].startswith('##'))):
            html_lines.append('</div>')
            in_special_box = None
        
        # Handle lists
        if line.strip().startswith(('- ', '* ')):
            if not in_list or list_type != 'ul':
                if in_list:
                    html_lines.append(f'</{list_type}>')
                html_lines.append('<ul>')
                in_list = True
                list_type = 'ul'
            content = line.strip()[2:]
            html_lines.append(f'<li>{content}</li>')
            
        elif re.match(r'^\d+\. ', line):
            if not in_list or list_type != 'ol':
                if in_list:
                    html_lines.append(f'</{list_type}>')
                html_lines.append('<ol>')
                in_list = True
                list_type = 'ol'
            content = re.sub(r'^\d+\. ', '', line)
            html_lines.append(f'<li>{content}</li>')
            
        # Regular paragraphs
        elif line.strip() and not line.startswith(('<', '---', '#')):
            if in_list:
                html_lines.append(f'</{list_type}>')
                in_list = False
            html_lines.append(f'<p>{line}</p>')
            
        elif line == '---':
            if in_list:
                html_lines.append(f'</{list_type}>')
                in_list = False
            html_lines.append('<hr>')
            
        elif line.startswith('<'):
            html_lines.append(line)
    
    if in_list:
        html_lines.append(f'</{list_type}>')
    if in_special_box:
        html_lines.append('</div>')
    
    return '\n'.join(html_lines)


def extract_chapter_content(chapter_id, full_content):
    """Extract content for a specific chapter from the markdown"""
    
    # Find content between chapter markers
    pattern = f'<a name="{chapter_id}"></a>(.+?)(?=<a name="|$)'
    match = re.search(pattern, full_content, re.DOTALL)
    
    if match:
        content = match.group(1).strip()
        # Remove the chapter title (## Chapter X: Title) as we add it in the template
        content = re.sub(r'^##\s+Chapter.+?\n', '', content, count=1, flags=re.MULTILINE)
        content = re.sub(r'^##\s+Prologue.+?\n', '', content, count=1, flags=re.MULTILINE)
        content = re.sub(r'^##\s+Epilogue.+?\n', '', content, count=1, flags=re.MULTILINE)
        return content.strip()
    
    return ""


def generate_chapter_html(chapter_info, content_html):
    """Generate complete HTML for a chapter"""
    
    prev_link = f'<a href="{chapter_info["prev"]}" class="nav-button">← Previous Chapter</a>' if chapter_info['prev'] else '<span class="nav-button disabled">← Previous</span>'
    next_link = f'<a href="{chapter_info["next"]}" class="nav-button">Next Chapter →</a>' if chapter_info['next'] else '<span class="nav-button disabled">Next →</span>'
    
    # Get next chapter title for the button
    next_title = ""
    if chapter_info['next']:
        next_chapter = next((c for c in CHAPTERS if c['file'] == chapter_info['next']), None)
        if next_chapter:
            next_title = f"Next: {next_chapter['title']}"
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{chapter_info['number']}: {chapter_info['title']} - AI Guru Tales</title>
    <meta name="description" content="{chapter_info['subtitle']} - Part of The Great Jungle Challenge interactive AI learning adventure.">
    <link rel="stylesheet" href="../post-styles.css">
    <link rel="stylesheet" href="chapter-styles.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=Work+Sans:wght@300;400;500&display=swap" rel="stylesheet">
</head>
<body>
    <!-- Reading Progress Bar -->
    <div class="reading-progress" id="progress-bar"></div>

    <!-- Chapter Navigation -->
    <nav class="chapter-nav">
        <div class="chapter-nav-container">
            {prev_link}
            <a href="../post-ai-jungle-complete.html" class="nav-button toc">
                📚 Table of Contents
            </a>
            {next_link}
        </div>
    </nav>

    <!-- Breadcrumb -->
    <div class="breadcrumb">
        <a href="../index.html">Home</a>
        <span>›</span>
        <a href="../post-ai-jungle-complete.html">The Great Jungle Challenge</a>
        <span>›</span>
        <span>{chapter_info['number']}</span>
    </div>

    <!-- Chapter Content -->
    <article class="chapter-content">
        <header class="chapter-header">
            <div class="chapter-number">{chapter_info['emoji']} {chapter_info['number']}</div>
            <h1 class="chapter-title">{chapter_info['title']}</h1>
            <p class="chapter-subtitle">{chapter_info['subtitle']}</p>
        </header>

        {content_html}
    </article>

    <!-- Bottom Navigation -->
    <nav class="chapter-bottom-nav">
        {prev_link}
        <a href="../post-ai-jungle-complete.html" class="nav-button toc">
            📚 Back to Contents
        </a>
        {next_link}
    </nav>

    <script>
        // Reading progress bar
        window.addEventListener('scroll', () => {{
            const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
            const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
            const scrolled = (winScroll / height) * 100;
            document.getElementById('progress-bar').style.width = scrolled + '%';
        }});

        // Smooth scrolling for anchor links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {{
            anchor.addEventListener('click', function (e) {{
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {{
                    target.scrollIntoView({{
                        behavior: 'smooth',
                        block: 'start'
                    }});
                }}
            }});
        }});
    </script>
</body>
</html>'''
    
    return html


def main():
    print("🚀 AI Jungle Challenge - Chapter Generator")
    print("=" * 60)
    
    # Read the markdown file
    markdown_file = 'ai-jungle-complete-expanded.md'
    if not os.path.exists(markdown_file):
        print(f"❌ Error: {markdown_file} not found!")
        print("Please make sure the file is in the same directory as this script.")
        return
    
    print(f"📖 Reading {markdown_file}...")
    with open(markdown_file, 'r', encoding='utf-8') as f:
        full_content = f.read()
    
    print(f"✅ Loaded {len(full_content)} characters")
    
    # Create output directory
    output_dir = 'jungle-challenge'
    os.makedirs(output_dir, exist_ok=True)
    print(f"📁 Output directory: {output_dir}/")
    
    # Generate chapters
    print(f"\n🔨 Generating {len(CHAPTERS)} chapter files...")
    print("-" * 60)
    
    for i, chapter in enumerate(CHAPTERS, 1):
        print(f"\n[{i}/{len(CHAPTERS)}] Generating {chapter['file']}...")
        
        # Extract content
        raw_content = extract_chapter_content(chapter['id'], full_content)
        if not raw_content:
            print(f"  ⚠️  Warning: No content found for {chapter['id']}")
            continue
        
        print(f"  📝 Extracted {len(raw_content)} characters")
        
        # Convert to HTML
        content_html = markdown_to_html(raw_content)
        print(f"  🎨 Converted to HTML ({len(content_html)} characters)")
        
        # Generate full HTML
        full_html = generate_chapter_html(chapter, content_html)
        
        # Write file
        output_path = os.path.join(output_dir, chapter['file'])
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(full_html)
        
        print(f"  ✅ Saved to {output_path}")
    
    print("\n" + "=" * 60)
    print("🎉 SUCCESS! All chapters generated!")
    print(f"\n📊 Summary:")
    print(f"  - Total chapters: {len(CHAPTERS)}")
    print(f"  - Output directory: {output_dir}/")
    print(f"  - Files created: {len([f for f in os.listdir(output_dir) if f.endswith('.html')])}")
    print(f"\n🚀 Next steps:")
    print(f"  1. Upload the entire 'jungle-challenge' folder to your website")
    print(f"  2. Make sure 'post-ai-jungle-complete.html' is in the root")
    print(f"  3. Deploy to Vercel!")
    print("\n✨ Happy storytelling!")


if __name__ == "__main__":
    main()
