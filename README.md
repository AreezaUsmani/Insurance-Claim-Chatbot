# Insurance-Claim-Chatbot
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Insurance Claims Chatbot - README</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background: #f4f8fb;
            line-height: 1.6;
        }

        header {
            background: linear-gradient(to right, #2c3e50, #4ca1af);
            color: white;
            padding: 20px;
            text-align: center;
        }

        section {
            padding: 20px 40px;
            margin: 20px;
            background: white;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        }

        h2 {
            color: #2c3e50;
            border-left: 5px solid #4ca1af;
            padding-left: 10px;
        }

        ul {
            margin-left: 20px;
        }

        code {
            background: #eee;
            padding: 5px;
            border-radius: 5px;
        }

        footer {
            text-align: center;
            padding: 15px;
            background: #2c3e50;
            color: white;
        }

        .highlight {
            color: #4ca1af;
            font-weight: bold;
        }
    </style>
</head>
<body>

<header>
    <h1> Insurance Claims Chatbot</h1>
    <p>AI-Powered Claims Assistance using Ollama & RAG</p>
</header>

<section>
    <h2> Project Overview</h2>
    <p>
        The <span class="highlight">Insurance Claims Chatbot</span> is an AI-powered web application 
        designed to assist users in understanding insurance claim procedures, coverage details, 
        and required documentation through natural language interaction.
    </p>
    <p>
        The system uses <b>Retrieval-Augmented Generation (RAG)</b> architecture and runs locally 
        using <b>Ollama (Llama 3.2)</b> to ensure privacy and security.
    </p>
</section>

<section>
    <h2> Problem Statement</h2>
    <p>
        Insurance claim procedures are often complex and confusing. Customers struggle with:
    </p>
    <ul>
        <li>Understanding claim eligibility</li>
        <li>Required documentation</li>
        <li>Policy coverage details</li>
        <li>Claim submission steps</li>
    </ul>
    <p>
        This chatbot simplifies the process by providing instant, policy-based answers.
    </p>
</section>

<section>
    <h2> Key Features</h2>
    <ul>
        <li>PDF Policy Document Processing</li>
        <li>Text Chunking</li>
        <li>Embedding Generation using Ollama</li>
        <li>Vector Storage using ChromaDB</li>
        <li>Semantic Search Retrieval</li>
        <li>Natural Language Question Answering</li>
        <li>Offline & Secure Execution</li>
        <li>Web Interface using Flask</li>
    </ul>
</section>

<section>
    <h2> System Architecture</h2>
    <ol>
        <li>Load Insurance Policy PDF</li>
        <li>Split text into chunks</li>
        <li>Generate embeddings using Ollama</li>
        <li>Store embeddings in ChromaDB</li>
        <li>Accept user query</li>
        <li>Retrieve relevant policy sections</li>
        <li>Generate response using LLM</li>
    </ol>
</section>

<section>
    <h2> Technologies Used</h2>
    <ul>
        <li>Python</li>
        <li>Flask</li>
        <li>LangChain</li>
        <li>Ollama (Llama 3.2)</li>
        <li>ChromaDB</li>
        <li>HTML & CSS</li>
        <li>Vector Embeddings</li>
        <li>RAG Architecture</li>
    </ul>
</section>

<section>
    <h2> Installation & Setup</h2>
    <p><b>Step 1:</b> Install dependencies</p>
    <code>pip install flask langchain chromadb ollama</code>

    <p><b>Step 2:</b> Pull Llama model</p>
    <code>ollama pull llama3.2</code>

    <p><b>Step 3:</b> Run application</p>
    <code>python app.py</code>

    <p>Open in browser:</p>
    <code>http://127.0.0.1:5000</code>
</section>

<section>
    <h2> Example Queries</h2>
    <ul>
        <li>What documents are required to file a claim?</li>
        <li>Is accidental damage covered?</li>
        <li>What is the claim settlement process?</li>
        <li>What is the waiting period?</li>
    </ul>
</section>

<section>
    <h2>Security & Privacy</h2>
    <ul>
        <li>Runs locally using Ollama</li>
        <li>No external API calls</li>
        <li>No cloud dependency</li>
        <li>All data remains on local machine</li>
    </ul>
</section>

<section>
    <h2> Future Enhancements</h2>
    <ul>
        <li>Claim submission automation</li>
        <li>Claim status tracking</li>
        <li>Multi-policy support</li>
        <li>User authentication</li>
        <li>Cloud deployment</li>
    </ul>
</section>

<footer>
    <p> Developed by Areeza Usmani | Insurance Claims Chatbot Project</p>
</footer>

</body>
</html>
