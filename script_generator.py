from groq import Groq
import streamlit as st


def generate_script(
    topic,
    language,
    duration,
    video_type,
    tone
):

    if "api_keys" not in st.secrets:
        raise RuntimeError(
            "Groq API key is not configured in Streamlit Secrets."
        )

    if "GROQ_API_KEY" not in st.secrets["api_keys"]:
        raise RuntimeError(
            "GROQ_API_KEY is missing from Streamlit Secrets."
        )

    client = Groq(
        api_key=st.secrets["api_keys"]["GROQ_API_KEY"]
    )

    prompt = f"""
You are an Islamic educational content writer.

Create a respectful and accurate Islamic video script.

Topic:
{topic}

Language:
{language}

Duration:
{duration}

Video type:
{video_type}

Tone:
{tone}

IMPORTANT RULES:

1. Never invent Quran verses.
2. Never invent Hadith.
3. Never invent religious references.
4. Do not attribute fabricated statements to Prophet Muhammad ﷺ.
5. Do not fabricate statements from Islamic scholars.
6. Clearly identify Quran and Hadith references.
7. If a quotation cannot be reliably verified,
   do not present it as authentic.
8. Do not depict Allah.
9. Do not create realistic depictions of prophets.
10. Keep the content respectful and educational.

Return the following:

TITLE:
HOOK:
INTRODUCTION:
MAIN CONTENT:
QURAN/HADITH REFERENCES:
CONCLUSION:
CALL TO ACTION:

Keep the narration appropriate for the requested duration.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": (
                    "You create careful, respectful and "
                    "educational Islamic content."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
        max_completion_tokens=1500
    )

    return response.choices[0].message.content
