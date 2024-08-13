import streamlit as st


def set_footer():
    footer = """
    </style>
        <div class="footer">
            <p>Built with <a href="https://streamlit.io/">Streamlit</a> 💻</p>
            <p>Made with ❤️ by Jordi Onrubia Palacios</p>
        </div>
    """

    st.markdown(footer, unsafe_allow_html=True)
