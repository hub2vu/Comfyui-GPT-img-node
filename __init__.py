from .gpt_img_node import (
    GPTImgAPIEdit,
    GPTImgAPIGenerate,
    GPTImgOAuthEdit,
    GPTImgOAuthGenerate,
)


NODE_CLASS_MAPPINGS = {
    "GPTImgOAuthGenerate": GPTImgOAuthGenerate,
    "GPTImgOAuthEdit": GPTImgOAuthEdit,
    "GPTImgAPIGenerate": GPTImgAPIGenerate,
    "GPTImgAPIEdit": GPTImgAPIEdit,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "GPTImgOAuthGenerate": "GPT img OAuth Generate",
    "GPTImgOAuthEdit": "GPT img OAuth Edit",
    "GPTImgAPIGenerate": "GPT img API Generate",
    "GPTImgAPIEdit": "GPT img API Edit",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
