import gradio as gr
from transformers import pipeline
import matplotlib.pyplot as plt

# Load classifier
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

categories = [
    "politics", "technology", "sports",
    "entertainment", "business", "health",
    "education"
]

def chat_response(message):
    if not message.strip():
        return "❗ Please enter a news headline or text about current events!", None

    result = classifier(message, candidate_labels=categories)
    top_label = result['labels'][0]
    confidence = result['scores'][0]

    response = f"""
<div class='output-card'>
    <div class='output-header'>
        <h2>🔍 Analysis Results</h2>
    </div>
    <div class='output-content'>
        <div class='input-preview'>
            <p class='input-text'>"{message}"</p>
        </div>
        <div class='results'>
            <div class='main-category'>
                <span class='emoji'>🏷️</span>
                <span class='label'>Main Category:</span>
                <span class='value highlight'>{top_label} ({confidence:.0%} confidence)</span>
            </div>
            <div class='secondary-categories'>
                <span class='emoji'>📊</span>
                <span class='label'>Also Considered:</span>
                <span class='value'>{result['labels'][1]} ({result['scores'][1]:.0%})</span>
                <span class='value'>, {result['labels'][2]} ({result['scores'][2]:.0%})</span>
            </div>
        </div>
    </div>
</div>
"""
    return response, plot_confidence(result['labels'], result['scores'])

def plot_confidence(labels, scores):
    plt.figure(figsize=(7, 3))
    bars = plt.bar(labels, scores, color="#7a5af5")
    plt.xticks(rotation=45)
    plt.ylim(0, 1)
    plt.title("Category Confidence")
    for bar, score in zip(bars, scores):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.02, f"{score:.0%}", ha='center')
    return plt

# Define CSS as a string variable
css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Roboto:wght@400;500;700&display=swap');

body {
    font-family: 'Roboto', sans-serif !important;
    background: #f8f9fa !important;
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    min-height: 100vh !important;
    margin: 0 !important;
}

#main-container {
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    background: linear-gradient(to right, #f3e7e9, #e3eeff) !important;
    padding: 40px !important;
    border-radius: 36px !important;
    box-shadow: 0 10px 40px rgba(0,0,0,0.1) !important;
    max-width: 95vw !important;
    width: 780px !important;
    margin: 20px auto !important;
}

.glow {
    font-family: 'Dancing Script', cursive !important;
    font-size: 4rem !important;
    color: #6a1b9a !important;
    text-shadow: 0 0 10px rgba(122, 90, 245, 0.3) !important;
    margin: 0 0 20px 0 !important;
    text-align: center !important;
}

#main-card {
    background-color: #ffffff !important;
    border-radius: 20px !important;
    padding: 24px !important;
    box-shadow: 0 8px 20px rgba(0,0,0,0.08) !important;
    width: 100% !important;
}

.section-title {
    font-family: 'Dancing Script', cursive !important;
    font-size: 2.5rem !important;
    color: #4a148c !important;
    text-align: center !important;
    margin-bottom: 20px !important;
    display: block !important;
}

#input-text textarea {
    background: rgba(255,255,255,0.95) !important;
    border: 1px solid #ddd !important;
    border-radius: 12px !important;
    padding: 12px !important;
    font-size: 1.1rem !important;
    min-height: 100px !important;
    width: 100% !important;
}

#analyze-btn {
    background-color: #7a5af5 !important;
    color: white !important;
    border: none !important;
    padding: 14px 22px !important;
    font-size: 1.5rem !important;
    font-weight: bold !important;
    border-radius: 36px !important;
    cursor: pointer !important;
    font-family: 'Dancing Script', cursive !important;
    transition: all 0.3s ease !important;
    margin: 12px 0 !important;
    width: 100% !important;
}

.output-card {
    background: #ffffff !important;
    border-radius: 16px !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08) !important;
    padding: 20px !important;
    margin-top: 20px !important;
}

.output-header h2 {
    color: #4a148c !important;
    font-size: 1.5rem !important;
    margin: 0 0 15px 0 !important;
    text-align: center !important;
    font-weight: 700 !important;
}

.input-preview {
    background: #f9f9ff !important;
    border-radius: 12px !important;
    padding: 15px !important;
    margin-bottom: 20px !important;
    border-left: 4px solid #7a5af5 !important;
}

.input-text {
    font-style: italic !important;
    color: #555 !important;
    margin: 0 !important;
    font-size: 1.1rem !important;
    line-height: 1.5 !important;
}

.results {
    display: flex !important;
    flex-direction: column !important;
    gap: 15px !important;
}

.main-category, .secondary-categories {
    display: flex !important;
    align-items: center !important;
    gap: 10px !important;
    font-size: 1.1rem !important;
}

.emoji {
    font-size: 1.3rem !important;
}

.label {
    font-weight: 500 !important;
    color: #444 !important;
}

.value {
    font-weight: 400 !important;
    color: #333 !important;
}

.highlight {
    color: #7a5af5 !important;
    font-weight: 700 !important;
}
</style>
"""

with gr.Blocks() as demo:
    # Add the CSS to the page
    gr.HTML(css)
    
    with gr.Column(elem_id="main-container"):
        gr.HTML('<h1 class="glow">TagTheNews</h1>')

        with gr.Group(elem_id="main-card"):
            gr.HTML("<div class='section-title'>Analyze Your Headline</div>")
            user_input = gr.Textbox(
                placeholder="Type or paste a news headline here...",
                lines=2,
                label="",
                elem_id="input-text"
            )
            with gr.Row():
                analyze_button = gr.Button("🔍 Analyze", elem_id="analyze-btn")
            analysis_output = gr.HTML(elem_id="output-box")
            chart_output = gr.Plot()

            analyze_button.click(fn=chat_response, inputs=user_input, outputs=[analysis_output, chart_output])

demo.launch()
