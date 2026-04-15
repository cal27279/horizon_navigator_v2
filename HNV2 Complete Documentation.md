```markdown
# Horizon Navigator V2: Enterprise Technical Manual
**Document Version:** 2.1.0
**Lead Architect:** Carlos Arriaga Luna, PMP
**Architecture Pattern:** Hybrid Local/Cloud ("Nano Banana" Protocol)

---

## 1. Executive Summary & Product Vision

**Horizon Navigator V2** represents a paradigm shift in Enterprise Project Management Office (PMO) operations. Traditional risk management relies on static tracking spreadsheets and reactive mitigation strategies. Horizon Navigator V2 functions as an **Autonomous AI Governance Agent** and a **Self-Healing Risk Register**.

By ingesting unstructured project artifacts (e.g., meeting transcripts, stakeholder dialogue, technical requirements), the system utilizes state-of-the-art Large Language Models (LLMs) and advanced Retrieval-Augmented Generation (RAG) to dynamically identify hidden risks, categorize them according to international Project Management Professional (PMP) standards, and generate deterministic, context-aware mitigation strategies.

### 1.1 Core Business Value
* **Proactive Intelligence:** Transforms PMO from a historical logging function into a predictive risk center.
* **Semantic Risk Mapping:** Replaces manual categorization with automated mapping to standard Risk Breakdown Structure (RBS) pillars (e.g., *Technical Architecture*, *Legal Compliance*, *Resource Allocation*).
* **Cost-Optimized Compute:** Leverages a hybrid local-orchestration model to minimize sustained cloud infrastructure costs while maximizing burst-inference capabilities.

---

## 2. System Architecture ("Nano Banana" Framework)

To achieve enterprise-grade performance without incurring unnecessary continuous cloud computing costs, Horizon Navigator V2 utilizes a proprietary hybrid architecture known internally as the **"Nano Banana" Framework**. This design keeps primary orchestration localized while offloading heavy cognitive tasks to managed GenAI services.

### 2.1 Core Intelligence Layer (AWS Bedrock)
The cognitive engine of the system relies on **Amazon Bedrock**, utilizing a multi-model approach:
* **Reasoning Engine:** Anthropic **Claude 3 (Haiku/Sonnet)**. Selected for its superior contextual window, nuanced sentiment analysis, and ability to follow strict deterministic formatting for governance outputs.
* **Embedding Engine:** AWS **Titan Text Embeddings**. Converts raw project text into high-density (1024-dimension) mathematical vectors for semantic mapping.

### 2.2 Memory & Retrieval Layer (Pinecone Serverless)
Standard LLMs lack persistent memory of specific enterprise projects. Horizon Navigator solves this via a robust vector database:
* **Infrastructure:** **Pinecone Serverless**. Ensures high-availability and rapid sub-second semantic retrieval without the cost of a dedicated, always-on instance.
* **Knowledge Base:** Stores both historical project precedents and embedded PMBOK® guidelines, allowing the LLM to ground its advice in proven methodologies.

### 2.3 User Interface & Orchestration Layer
* **Frontend Dashboard:** Built with **Streamlit**, featuring a custom "Black Edition" CSS override. The UI acts as the PMO Command Center, offering stateful session management, real-time infrastructure telemetry, and chat-based query interfaces.
* **Local Compute:** Python-based orchestration that manages the RAG pipeline, coordinates API calls, and handles local data sanitization prior to cloud transmission.

---

## 3. Data Flow & Execution Pipeline

The lifecycle of a risk query within Horizon Navigator V2 follows a strict, secure pipeline:

1. **Ingestion & Sanitization:** Unstructured input (prompt or transcript) is received via the Streamlit UI. Local orchestration scrubs the input of basic malformed data.
2. **Vectorization:** The sanitized text string is transmitted via secure API to AWS Bedrock, where Titan Text models convert the query into a high-dimensional vector.
3. **Semantic Retrieval:** The vector is pushed to the Pinecone Serverless index. Pinecone performs a cosine similarity search, returning the top `k` (e.g., 25) most relevant historical context nodes and PM guidelines.
4. **Contextual Assembly:** The local orchestrator combines the original user prompt with the retrieved Pinecone context into a master prompt.
5. **Inference Execution:** The master prompt is routed to Claude 3 via AWS Bedrock. The model analyzes the data against the provided context and generates a structured mitigation strategy.
6. **Stateful Rendering:** The output is pushed to the Streamlit UI, where it is appended to the session state, ensuring the system maintains conversational continuity for follow-up drill-downs.

---

## 4. Zero-Trust Security & Governance Protocols

As an enterprise governance tool, Horizon Navigator V2 enforces strict data security and infrastructure protection measures.

### 4.1 Credential & Infrastructure Isolation
* **No Hardcoded Secrets:** AWS Access Keys, Secret Keys, Bedrock Profile IDs, and Pinecone API keys are strictly forbidden within the source code.
* **Environment Variables:** All secrets are dynamically injected at runtime via a local `.env` file, which is enforced by `.gitignore` policies to prevent accidental repository commits.

### 4.2 Data Sovereignty & Model Training
* **Managed GenAI Protections:** By routing inference exclusively through Amazon Bedrock, Horizon Navigator ensures that proprietary enterprise risk data and intellectual property are **never** utilized by AWS or Anthropic for underlying foundational model training.
* **IAM Scoping:** Cloud execution relies on strictly scoped IAM roles, utilizing Inference Profile IDs rather than raw ARNs to prevent unauthorized access or lateral movement within the AWS environment.

---

## 5. Deployment & Configuration Guide

### 5.1 Environment Prerequisites
* **Runtime:** Python 3.9+
* **Cloud Services:** Active AWS Account (Bedrock / Claude 3 access enabled in target region) and Pinecone Account (Serverless Index created).

### 5.2 Local Environment Setup
Execute the following commands to initialize the local orchestrator:

```bash
# 1. Clone the repository
git clone [https://github.com/your-org/horizon-navigator-v2.git](https://github.com/your-org/horizon-navigator-v2.git)
cd horizon-navigator-v2

# 2. Initialize a virtual environment (Recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# 3. Install required dependencies
pip install -r requirements.txt
```

### 5.3 Infrastructure Configuration
Create an environment file (`.env`) in the root directory. Copy the schema below and populate it with your specific infrastructure credentials:

```env
# AWS Authentication & Bedrock Configuration
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
AWS_DEFAULT_REGION=us-east-1
MODEL_ID=your_claude_inference_profile_id
KNOWLEDGE_BASE_ID=your_aws_knowledge_base_id

# Pinecone Vector DB Configuration
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_INDEX_NAME=horizon-navigator-v2
```

---

## 6. Operational Manual

Horizon Navigator V2 supports two execution modes depending on the user's operational requirements.

### 6.1 Headless Execution (CLI Mode)
Designed for rapid debugging, infrastructure testing, and headless pipeline integrations. This mode bypasses the Streamlit frontend.

```bash
python horizon_rag.py
```
*System will initialize a secure terminal loop. Input queries directly. Terminate via `exit` or `quit`.*

### 6.2 Command Center Execution (Streamlit UI)
Designed for standard PMO operations, providing the full graphical interface, historical session state, and simulated telemetry.

```bash
streamlit run app.py
```
* **Access:** The application will bind to `localhost:8501` by default.
* **Features:** Monitor active connections to AWS Secrets Manager and Pinecone in the left sidebar while engaging the risk agent in the primary chat console.

---

## 7. Future Architecture Roadmap (V3 Outlook)
* **Automated Data Pipelines:** Integration with AWS S3 for automated batch processing of meeting transcripts (VTT/TXT) via AWS Lambda triggers.
* **Enterprise Exporting:** Automated PDF/CSV compilation of generated Risk Breakdown Structures for integration into legacy tools (Jira, Asana).
* **SSO Integration:** Implementation of SAML/OAuth2 for secure corporate team access.

---
*Document officially approved for enterprise demonstration. For architectural support, contact the Lead Architect.*
```
