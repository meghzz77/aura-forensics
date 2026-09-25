# 🛡️ AuraForensics: AI-Assisted Digital Evidence Reconstructor
**CalmStacks 24-Hour Hackathon | Track 01 Solution**

AuraForensics solves the critical limitation of legacy file-carving tools (`scalpel`, `foremost`) by using a dual-layer reconstruction pipeline: mathematical entropy pre-filtering paired with neural semantic boundary stitching.

## 🚀 Key Engineering Objectives Addressed

1. **Intelligent Fragment Reconstruction (Objective 01):** Reconnects dangling storage clusters and severed text/log boundaries using token sequence synthesis.
2. **Data Integrity & Corruption Assessment (Objective 02):** Computes Shannon Entropy ($H(X)$) and ASCII printable density to immediately identify valid data vs. ransomware-encrypted/destroyed sectors.
3. **Classification & Prioritization (Objective 03):** Automatically extracts and triages high-value investigative artifacts: IP addresses, transaction amounts, timestamps, and account numbers.
4. **Investigative Decision Support (Objective 04):** Synthesizes plain-English forensic advisories certifying chronological continuity and chain-of-custody admissibility.
5. **Offline Resilient Fallback:** Features a deterministic local reconstruction engine ensuring 100% demo availability even under network degradation.

## 🛠️ Architecture
- **Sensor Tier:** Python native Shannon Entropy calculator & ASCII density parser.
- **Neural Carving Tier:** Gemini 2.5 Flash semantic boundary reconciler via REST API.
- **Triage Tier:** Optimized regex pattern extractor for actionable incident triage.
- **Interface Tier:** Tailored dark-mode forensic dashboard built with zero heavy C/C++ compilation dependencies.

## 💻 Quickstart
```powershell
# 1. Install dependencies
pip install requests

# 2. Generate demo datasets
python generate_samples.py

# 3. Launch the dashboard
python app.py