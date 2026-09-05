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

        try:

            with st.spinner("🕌 Creating your Islamic script..."):

                script = generate_script(
                    topic=topic,
                    language=language,
                    duration=duration,
                    video_type=video_type,
                    tone=tone
                )

            st.success("✅ Islamic script generated successfully!")

            st.subheader("📜 Generated Script")

            st.write(script)

            st.divider()

            st.subheader("🎬 Next Step")

            if st.button(
                "✅ Approve & Generate Video",
                use_container_width=True
            ):

                st.info(
                    "Video generation will be added in the next phase."
                )

        except Exception as e:

            st.error(
                "❌ Unable to generate the script."
            )

            st.info(
                "Please check your Groq API key and Streamlit Secrets."
            )
