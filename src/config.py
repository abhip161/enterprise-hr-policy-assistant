"""
App-wide constants — models, prompts, and output-scan patterns.
"""

GROQ_MODELS = {

    # Qwen
    "qwen/qwen3.6-27b":
        "Qwen3.6 · 27B ★ Recommended for HR Assistant",

    "qwen/qwen3.8-27b":
        "Qwen3.8 · 27B — advanced general-purpose",

    # Meta Llama — Prompt Guard
    "meta-llama/llama-prompt-guard-2-22m":
        "Llama Prompt Guard 2 · 22M — fast",

    "meta-llama/llama-prompt-guard-2-86m":
        "Llama Prompt Guard 2 · 86M ★ stronger protection",

    # OpenAI
    "openai/gpt-oss-120b":
        "GPT-OSS · 120B ★ best for complex reasoning",

    "openai/gpt-oss-20b":
        "GPT-OSS · 20B — fast reasoning",
}

# Default models
GUARD_MODEL_DEFAULT = "meta-llama/llama-prompt-guard-2-86m"
CHAT_MODEL_DEFAULT = "qwen/qwen3.6-27b"


HR_SYSTEM_PROMPT = (
    "You are the HR Policy Assistant for Acme Corp. "
    "Answer the employee's question using ONLY the policy excerpts provided below. "
    "Be concise, cite the relevant policy section, and include specific numbers or rules where applicable. "
    "If the answer is not covered in the excerpts, say so clearly and direct the employee to hr@acmecorp.com.\n\n"
    "Policy Excerpts:\n{context}"
)


SENSITIVE_OUTPUT_PATTERNS = {
    "credential_leak":
        r"(?i)(password|passwd|secret|api[_\-]?key|token)\s*[:=]\s*['\"]?\w{6,}",

    "ssn_in_output":
        r"\b\d{3}-\d{2}-\d{4}\b",

    "hardcoded_salary":
        r"(?i)\b(earns?|is paid|salary of)\s+\$[\d,]+\b",
}