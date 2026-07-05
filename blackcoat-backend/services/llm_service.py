import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# Initialize the Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def build_prompt(query: str, contexts: list[dict]) -> str:
    context_text = ""
    for i, c in enumerate(contexts, 1):
        context_text += f"""
--- Source {i} ---
Title: {c['title']}
Article/Section: {c.get('article_section', 'N/A')}
Law Text: {c['verbatim']}
Simple Explanation: {c['simplified']}
Landmark Case 1: {c['case_1']} ({c['case_1_year']}) — {c['case_1_holding']}
Landmark Case 2: {c['case_2']} ({c['case_2_year']}) — {c['case_2_holding']}
Current Status: {c['status']}
"""

    return f"""You are a sharp, experienced Indian legal advocate helping a common citizen understand their legal position.

The person has described their situation. Your job is to build a structured legal argument for them using ONLY the provided legal context below.

STRICT RULES:
- Use ONLY the laws and cases provided in the context. Do not invent any case or law.
- Write in simple English a 10th standard student can understand.
- If a legal term is used, explain it in simple words in brackets right after.
- Be direct, clear, and structured. No vague language.
- Every argument point must be backed by a specific Article, Section, or Case from the context.
- If the context does not cover the situation at all, say: "The specific situation you described is not covered in my current database. Please consult a qualified advocate."

PERSON'S SITUATION:
{query}

LEGAL CONTEXT FROM DATABASE:
{context_text}

Respond in EXACTLY this structure — use these exact headings:

⚖️ LEGAL POSITION
[One powerful sentence stating what right has been violated OR what legal claim they have]

📜 APPLICABLE LAWS
[List each relevant Article/Section. For each: name it, state what it says in simple words, and explain exactly how it applies to this person's situation]

🗣️ THE ARGUMENT
[Build the argument step by step. Connect the laws to the facts. Explain why the law is on their side. Keep it logical and sequential.]

📋 SUPPORTING JUDGMENTS
[For each case from context: Case Name (Year) — what the court decided — why it directly supports this person's situation]

✅ WHAT YOU CAN DO RIGHT NOW
[Practical, specific steps. Which court to approach. What petition/writ to file. What documents to gather. Make it actionable.]

⚠️ IMPORTANT
This is legal information to help you understand your rights. For filing in court, always work with a qualified advocate who can verify citations and represent you properly.
"""

def get_llm_answer(query: str, contexts: list[dict]) -> str:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": build_prompt(query, contexts)}],
        max_tokens=800,
        temperature=0.3
    )
    return response.choices[0].message.content
