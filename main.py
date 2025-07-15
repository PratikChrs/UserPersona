import praw
import os
import re
from dotenv import load_dotenv

load_dotenv()

reddit=praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("USER_AGENT")
)
 
def extractName(url):
    match=re.search(r"reddit\.com/user/([^/]+)",url)
    if match:
      return match.group(1)
    else:
       return None

inp=input("Enter Reddit user profile url:").strip()
username=extractName(inp)

redditor=reddit.redditor(username)
comments=[]
posts=[]

for comment in redditor.comments.new(limit=50):
    comments.append({"text":comment.body,"url":f"https://reddit.com{comment.permalink}"})
for submission in redditor.submissions.new(limit=50):
    posts.append({"text":f"{submission.title}\n{submission.selftext}","url":f"https://reddit.com{submission.permalink}"})

import google.generativeai as genai
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
def generatePersona(username,posts,comments):
    combined=posts+comments
    formatted_input=[f"{i+1}.{item['text']}\n URL: {item['url']}" for i,item in enumerate(combined)]
    prompt=f"""You are a professional social behavior analyst. Based on the Reddit activity below, build a structured and insightful persona for the user u/{username}.

**IMPORTANT GUIDELINES**:
- Use bullet points or short paragraphs.
- For every characteristic, include a **direct quote** from the user.
- Always cite the **exact Reddit post or comment URL** that supports the claim.
- Avoid assumptions or generalizations not backed by text.
- Only use what's explicitly available in the input.

Use this format exactly:

---
**Age:**  
- Estimate: [e.g. 30–35]  
- Explanation: [Include quote with reasoning]  
- Quote: "..."  
- Source: [Reddit URL]

**Location:**  
- City or Country:  
- Quote: "..."  
- Source: [Reddit URL]

**Profession:**  
- Role: [Job title or area]  
- Quote: "..."  
- Source: [Reddit URL]

**Interests & Hobbies:**  
1. Interest: [e.g. Gaming – Strategy]  
   - Quote: "..."  
   - Source: [Reddit URL]  
2. Interest: [e.g. Anime – Edgerunners]  
   - Quote: "..."  
   - Source: [Reddit URL]  
(Include up to 5 interests max)

**Personality Traits:**  
- Trait: [e.g. Analytical]  
  - Explanation: [Reason with example]  
  - Quote: "..."  
  - Source: [Reddit URL]  
- Trait: [e.g. Curious]  
  - Quote: "..."  
  - Source: [Reddit URL]  
(Minimum 3 traits)

**Writing Style:**  
- Description: [Tone, complexity, humor, structure]  
- Example: "..."  
- Source: [Reddit URL]

**Mental/Emotional Cues:**  
- Cue: [e.g. Frustration about technology]  
  - Quote: "..."  
  - Source: [Reddit URL]  
- Cue: [e.g. Reflective or philosophical thoughts]  
  - Quote: "..."  
  - Source: [Reddit URL]  
(Minimum 2 emotional insights)

Reddit Activity (posts and comments):
{formatted_input[:12000]}
"""
    model=genai.GenerativeModel("gemini-1.5-flash")
    response=model.generate_content(prompt)
    return response.text

persona_profile=generatePersona(username, posts, comments)

import os
output_dir="output"
os.makedirs(output_dir,exist_ok=True)

def save_as_markdown(username, persona_text):
    md_path = f"output/persona_{username}.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(f"Persona Profile: u/{username}\n\n{persona_text}")
    print(f"Saved Markdown to: {md_path}")
    return md_path

import markdown

def convert_to_html(md_file):
    with open(md_file, "r", encoding="utf-8") as f:
        md_content = f.read()
    html_body = markdown.markdown(md_content, extensions=["tables", "fenced_code"])
    html_template = f"""
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            body {{
                background-color: white;
                color: black;
                font-family: Arial, sans-serif;
                line-height: 1.6;
                padding: 20px;
            }}
            h1, h2, h3 {{
                color: #333;
            }}
            code {{
                background-color: #f4f4f4;
                padding: 2px 4px;
                border-radius: 4px;
                font-size: 90%;
            }}
            a {{
                color: #0645ad;
            }}
        </style>
    </head>
    <body>
        {html_body}
    </body>
    </html>
    """
    html_path = md_file.replace(".md", ".html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_template)
    print(f"Saved HTML to : {html_path}")
    return html_path


md_file=save_as_markdown(username, persona_profile)
html=convert_to_html(md_file)