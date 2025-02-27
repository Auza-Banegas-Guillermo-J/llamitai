The following repository is a simple example of an RAG-based LLM that uses text files.

**DOCKER FILE NON-FUNCTIONAL, Work in progress**

The local version requires Ollama to be serving an embedding model and an LLM model, in this case, Nomic and DeepSeek, respectively.
A YAML file is attached to replicate the environment, in my case, a Conda environment.

The API version requires a .env file to be in the working directory to access OpenAI API services for both embedding and LLM services:

```OPENAI_API_KEY="My OpenAI API key"```

The repository has a CLI version that uses a predetermined question and a GUI version that uses Streamlit and receives user input prompts.

Finally, the algorithms expect there to be a ./docs/txt directory for RAG functionality. A ./chroma_db directory can be inserted or created if there is none.

![image showing Gui](./imgs/GUI_Example.png)

```plaintext
.
├── chroma_db
│   ├── chroma.sqlite3
│   └── f7addd67-f77e-40a3-a548-d9827348035a
│       ├── data_level0.bin
│       ├── header.bin
│       ├── length.bin
│       └── link_lists.bin
├── Dockerfile
├── docs
│   ├── pdfs
│   │   ├── DIY_Drone_1.pdf
│   │   └── DIY_Drone_2.pdf
│   └── txt
│       └── case_1.txt
├── my_LLM.py
└── streamlit.py
```
