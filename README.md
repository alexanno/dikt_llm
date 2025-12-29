# Dikt LLM - AI-Generated Norwegian Poetry with Mathematical Visualizations

![License](https://img.shields.io/badge/license-MIT-blue.svg)

## Overview

**Dikt LLM** is a creative Python project that combines artificial intelligence, poetry, and mathematics. The project uses Azure OpenAI's language models to generate random Norwegian poems (dikts) and automatically creates mathematical visualizations that represent each poem artistically using matplotlib.

Each generated poem comes with:
- Original Norwegian poetry text
- Custom Python code that mathematically interprets the poem
- Beautiful visualization plots (using sine waves, cosine functions, exponentials, etc.)
- HTML output files that combine text, code, and visualizations

## Features

- 🎨 **AI-Powered Poetry Generation**: Uses Azure OpenAI (GPT-4o-mini) to create unique Norwegian poems
- 📊 **Mathematical Interpretations**: Automatically generates Python code that represents poems through mathematical functions
- 📈 **Visual Representations**: Creates matplotlib plots using trigonometric functions, exponentials, and other mathematical concepts
- 💾 **HTML Output**: Saves each poem with its visualization and code in a beautifully formatted HTML file
- 🔄 **Batch Generation**: Can generate multiple poems in a single run
- 🌐 **Bilingual Comments**: Code includes Norwegian comments for an immersive experience

## Prerequisites

- Python 3.8 or higher
- Azure OpenAI API access with valid credentials
- Required Python packages:
  - `openai` - Azure OpenAI Python SDK
  - `numpy` - Numerical computing
  - `matplotlib` - Plotting and visualization
  - `python-dotenv` - Environment variable management

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/alexanno/dikt_llm.git
   cd dikt_llm
   ```

2. **Install dependencies**:
   ```bash
   pip install openai numpy matplotlib python-dotenv
   ```

3. **Configure Azure OpenAI credentials**:
   
   Create a `.env` file in the project root with your Azure OpenAI credentials:
   ```
   AZURE_OPENAI_ENDPOINT=your_azure_endpoint_here
   AZURE_OPENAI_API_KEY=your_api_key_here
   OPENAI_API_VERSION=2024-02-15-preview
   ```

4. **Create output directory** (if it doesn't exist):
   ```bash
   mkdir -p dikt
   ```

## Usage

### Running the Jupyter Notebook

Open and run the `dikt_llm.ipynb` notebook:

```bash
jupyter notebook dikt_llm.ipynb
```

The notebook will:
1. Connect to Azure OpenAI using your credentials
2. Generate random Norwegian poems with mathematical themes
3. Parse the AI response to extract poem text and Python code
4. Execute the generated code to create visualizations
5. Save outputs as timestamped HTML files in the `dikt/` directory

### Key Functions

- **`run_azure_openai_prompt(prompt, model)`**: Sends prompts to Azure OpenAI and returns AI-generated content
- **`parse_response(response)`**: Parses AI response to extract TEXT and CODE sections
- **`execute_python_and_save(text, code)`**: Executes generated Python code, saves visualizations, and creates HTML files
- **`generate_dikt()`**: Orchestrates the complete poem generation workflow

### Customization

You can modify the prompt in the `run_azure_openai_prompt()` function to change the style or theme of generated poems:

```python
prompt = '''
Lag et dikt om noe helt tilfeldig du finner på. Bruk diktet til å lage pythonkode som laget en matematisk representasjon av diktet og plotter. Svar strukturert på dette formatet:

TEXT: <text>

CODE: <code>
'''
```

## Output Format

Generated HTML files are saved in the `dikt/` directory with timestamp naming (e.g., `2025-03-20-19-45-27.html`). Each HTML file contains:

1. **Poem Text**: The AI-generated Norwegian poem
2. **Visualization**: An embedded PNG image showing the mathematical representation
3. **Source Code**: The Python code used to generate the visualization

### Example Output Structure

```html
<html>
    <body>
    <h2>Dagens dikt</h2>
    <pre>[Poem text in Norwegian]</pre>
    <img src='./[timestamp].png' alt="Generated visualization">
    <h2>Kode</h2>
    <pre><code>[Python code]</code></pre>
    </body>
</html>
```

### Sample Poem Themes

The AI generates poems about various topics, often with mathematical or natural themes:
- Mathematical forests with sine and cosine trees
- Dance of light and shadow
- Cloud dances represented by wave functions
- Abstract mathematical concepts expressed poetically

## Example

Here's what a typical generated poem might look like:

**Poem (Norwegian)**:
```
I en skog av tall, der kurver bor,  
En granskog av plott som aldri forgår.  
Med røtter av sinus og stammer av cos,  
De svever i luft, helt uten trods.
```

**Generated Visualization Code**:
```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 1000)
y1 = np.sin(x)  # Røtter av sinus
y2 = np.cos(x)  # Stammer av cos
y3 = np.sin(x) + np.cos(x)  # Kvister og blader

plt.figure(figsize=(10, 6))
plt.plot(x, y1, label="Sin(x)", color='green')
plt.plot(x, y2, label="Cos(x)", color='blue')
plt.plot(x, y3, label="Sin(x) + Cos(x)", color='orange')
plt.title("En Tilfeldig Matematisk Skog")
plt.legend()
plt.grid(True)
plt.show()
```

## Project Structure

```
dikt_llm/
├── dikt_llm.ipynb          # Main Jupyter notebook
├── dikt/                   # Output directory for generated HTML and PNG files
│   ├── 2025-03-20-*.html   # Generated poems and visualizations
│   └── 2025-03-20-*.png    # Visualization images
├── .env                    # Azure OpenAI credentials (not tracked)
├── .gitignore             # Git ignore rules
├── LICENSE                # MIT License
└── README.md              # This file
```

## Technologies Used

- **Azure OpenAI**: GPT-4o-mini model for poem and code generation
- **Python**: Core programming language
- **NumPy**: Mathematical operations and array handling
- **Matplotlib**: Plotting and visualization library
- **Jupyter Notebook**: Interactive development environment

## Notes

- The project generates Norwegian-language poems by default
- Each run creates unique, random poems with their own mathematical interpretations
- Visualization styles vary based on the poem's theme and the AI's creative interpretation
- The default configuration generates 20 poems per execution (configurable in the notebook)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Alexander Salveson Nossum

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page or submit a pull request.

## Acknowledgments

- Azure OpenAI for providing the language model capabilities
- The Norwegian poetry tradition for inspiration
- The mathematical visualization community for inspiring creative data representation
