from .gpt_img_node import (
    GPTImgAPIEdit,
    GPTImgAPIGenerate,
    GPTImgAPIGenerateAdvanced,
    GPTImgAPILLM,
    GPTImgOAuthEdit,
    GPTImgOAuthGenerate,
    GPTImgOAuthGenerateAdvanced,
    GPTImgOAuthLLM,
)


NODE_CLASS_MAPPINGS = {
    "GPTImgOAuthLLM": GPTImgOAuthLLM,
    "GPTImgOAuthGenerate": GPTImgOAuthGenerate,
    "GPTImgOAuthGenerateAdvanced": GPTImgOAuthGenerateAdvanced,
    "GPTImgOAuthEdit": GPTImgOAuthEdit,
    "GPTImgAPILLM": GPTImgAPILLM,
    "GPTImgAPIGenerate": GPTImgAPIGenerate,
    "GPTImgAPIGenerateAdvanced": GPTImgAPIGenerateAdvanced,
    "GPTImgAPIEdit": GPTImgAPIEdit,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "GPTImgOAuthLLM": "GPT img OAuth ChatGPT LLM",
    "GPTImgOAuthGenerate": "GPT img OAuth Generate",
    "GPTImgOAuthGenerateAdvanced": "GPT img OAuth Generate Advanced",
    "GPTImgOAuthEdit": "GPT img OAuth Edit",
    "GPTImgAPILLM": "GPT img API ChatGPT LLM",
    "GPTImgAPIGenerate": "GPT img API Generate",
    "GPTImgAPIGenerateAdvanced": "GPT img API Generate Advanced",
    "GPTImgAPIEdit": "GPT img API Edit",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
