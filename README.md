# Language Translation System  
**Module E – AI Applications | Individual Open Project**

---

## 📌 Overview
This project implements and evaluates an AI-based **Language Translation System** using modern **Neural Machine Translation (NMT)** models.  
The system focuses on translating text between **English and Hindi**, addressing real-world language accessibility challenges in multilingual environments.

📍 **Primary Evaluation Artifact:**  
➡️ `Language_Translation_System.ipynb` (Jupyter Notebook)

---

## 🎯 Project Track
- **AI Domain:** Natural Language Processing (NLP)  
- **Project Type:** AI Application – Individual Open Project (Module E)

---

## 🧠 Problem Statement
Language barriers restrict access to digital content, services, and information.  
The objective of this project is to design, compare, and evaluate multiple pretrained translation models to understand their performance, limitations, and suitability for real-world applications.

---

## 📂 Repository Structure

├── Language_Translation_System.ipynb # PRIMARY evaluation artifact

├── models/ # Model-specific inference scripts

├── preprocessing/ # Data preprocessing notebook

├── src/ # Inference utilities and run instructions

├── evaluation_.csv # Quantitative evaluation results

├── evaluated_result.txt # Sample translation outputs

├── requirements.txt # Core dependencies

├── requirements_freeze.txt # Full environment snapshot

└── README.md


---

## 📊 Dataset Information
- **Source:** Public parallel corpora (e.g., IIT Bombay English–Hindi dataset and other Indic language resources)
- **Note:**  
  Datasets are **not included** in this repository due to size and licensing constraints.
- The project emphasizes **inference, evaluation, and comparative analysis** using pretrained models.

---

## 🤖 Models Used
The following pretrained translation models are explored and compared:
- **MarianMT** (English ↔ Hindi)
- **mBART** (Multilingual Translation)
- **M2M-100** (Many-to-Many Translation)
- **IndicTrans** (Indic language focused)

Model architecture, design choices, and comparison rationale are explained in detail in the notebook.

---

## 🧪 Evaluation
- Quantitative evaluation results are provided in CSV files
- Sample translation outputs are included for qualitative analysis
- Comparative performance and limitations are discussed in the notebook

---

## ⚖️ Ethical Considerations & Responsible AI
- Translation models may inherit biases from training data
- Cultural nuances and regional dialects may not always be preserved
- Outputs should not be used for sensitive or critical applications without human verification
- Responsible and transparent use of AI systems is emphasized

---

## ▶️ How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt

2. Open and run:
    ```bash
   Language_Translation_System.ipynb

3. Execute cells top-to-bottom using sample inputs provided in the notebook.


## 🏁 Conclusion

This project demonstrates how modern NLP models can be leveraged for practical translation tasks while highlighting their strengths, limitations, and ethical considerations.
Future improvements include fine-tuning, expanded language support, and real-time deployment.

  

