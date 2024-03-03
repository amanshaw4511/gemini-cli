## Gemini CLI: A Command Line Interface for Google's Generative AI Model

This project provides a Python-based command-line interface (CLI) for interacting with Google's Gemini Generative AI model. It allows users to:

* **Chat** with the model in a conversational way.
* **Generate** creative text formats based on provided prompts.

### Features

* **Interactive chat:** Engage in conversation with the model by asking questions or providing prompts.
* **Text generation:** Supply prompts and receive creatively generated text in response.
* **Rich formatting:** Utilize rich text formatting for visually appealing output.
* **Simple and user-friendly:** Easy to use with intuitive commands and clear prompts.

### Installation

1. **Prerequisites:**
    * Python 3.x ([https://www.python.org/downloads/](https://www.python.org/downloads/))
    * `rich` library: `pip install rich`
    * `google-generativeai` library: `pip install rich google-generativeai`
2. **Clone the repository:**

   ```bash
   git clone https://github.com/amanshaw4511/gemini-cli.git
   ```

3. **Set up environment variable:**

   Create an environment variable named `GEMINI_API_KEY` and assign your Google Generative AI API key to it. You can obtain your API key from the Google Cloud Console.

### Usage

1. **Navigate to the project directory:**

   ```bash
   cd gemini-cli
   ```

2. **Run the chat interface:**

   ```bash
   python app.py chat
   ```

   You can now interact with the model by entering prompts and receiving responses.

3. **Generate text:**

   ```bash
   python app.py tell "Write a poem about a robot cat."
   ```

   This will generate text based on the provided prompt and display it in a formatted manner.

### Contributing

We welcome contributions to this project! Please refer to the CONTRIBUTING.md file for guidelines on how to contribute.

### License

This project is licensed under the Apache License 2.0. See the LICENSE file for details.
