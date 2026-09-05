import streamlit as st

st.set_page_config(
    page_title="Islamic HD Video Generator",
    page_icon="🕌",
    layout="wide"
)

st.title("🕌 Islamic HD Video Generator")

st.markdown(
    "### Create beautiful, meaningful Islamic videos with AI"
)

st.divider()

st.subheader("🎬 Video Settings")

topic = st.text_area(
    "Islamic Video Topic",
    placeholder="Example: Importance of Salah"
)

col1, col2 = st.columns(2)

with col1:
    language = st.selectbox(
        "Language",
        ["English", "Urdu", "Arabic", "Roman Urdu"]
    )

    duration = st.selectbox(
        "Video Duration",
        ["30 seconds", "60 seconds", "90 seconds",
         "2 minutes", "5 minutes"]
    )

    video_type = st.selectbox(
        "Video Type",
        [
            "Islamic Reminder",
            "Quran Reflection",
            "Hadith Reminder",
            "Islamic History",
            "Islamic Story",
            "Educational",
            "Inspirational",
            "Ramadan Reminder",
            "Dua & Dhikr"
        ]
    )

with col2:
    tone = st.selectbox(
        "Tone",
        [
            "Peaceful",
            "Inspirational",
            "Emotional",
            "Educational",
            "Serious",
            "Documentary"
        ]
    )

    resolution = st.selectbox(
        "Video Resolution",
        ["Full HD 1080p", "HD 720p"],
        index=0
    )

    aspect_ratio = st.selectbox(
        "Aspect Ratio",
        [
            "9:16 — Shorts / Reels / TikTok",
            "16:9 — YouTube",
            "1:1 — Social Media"
        ]
    )

voice = st.selectbox(
    "Voice",
    ["Male", "Female", "No Voice — Subtitles Only"]
)

st.divider()

if st.button("📝 Generate Script", use_container_width=True):

    if not topic.strip():
        st.warning("Please enter an Islamic topic.")
    else:
        st.success("Topic received successfully!")

        st.write("### Your Settings")

        st.write("**Topic:**", topic)
        st.write("**Language:**", language)
        st.write("**Duration:**", duration)
        st.write("**Video Type:**", video_type)
        st.write("**Tone:**", tone)
        st.write("**Resolution:**", resolution)
        st.write("**Aspect Ratio:**", aspect_ratio)
        st.write("**Voice:**", voice)
