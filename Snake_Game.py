import streamlit as st
from game_component import snake_game_component

st.set_page_config(
    page_title="Snake Pro",
    layout="wide"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');

    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Outfit', sans-serif;
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        color: white;
    }

    .main-header {
        font-size: 3.5rem;
        font-weight: 800;
        background: -webkit-linear-gradient(#00f2fe, #4facfe);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0.5rem;
        letter-spacing: -1px;
    }

    .sub-header {
        text-align: center;
        color: #a0a0c0;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }

    .stat-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 1.5rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        text-align: center;
        transition: transform 0.3s ease;
    }

    .stat-card:hover {
        transform: translateY(-5px);
        border-color: rgba(79, 172, 254, 0.5);
    }

    .stat-value {
        font-size: 2rem;
        font-weight: 700;
        color: #00f2fe;
    }

    .stat-label {
        color: #a0a0c0;
        text-transform: uppercase;
        font-size: 0.8rem;
        letter-spacing: 1px;
    }

    .control-hint {
        background: rgba(0, 0, 0, 0.3);
        padding: 5px 10px;
        border-radius: 5px;
        border: 1px solid #4facfe;
        font-family: monospace;
        color: #00f2fe;
    }

    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

def main():
    st.markdown('<h1 class="main-header">SNAKE PRO</h1>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        st.write("### Instructions")
        st.write("Use the Arrow Keys to navigate the snake.")
        st.write("Eat the Red Dots to grow and increase your score.")
        st.write("Avoid crashing into your own tail")

    with col2:
        snake_game_component()
        
    with col3:
        st.write("### Tips")
        st.info("The snake wraps around walls, you can use this for your advantage.")
        st.warning("Speed increases as you eat more food.")

    st.write("---")

if __name__ == "__main__":
    main()
