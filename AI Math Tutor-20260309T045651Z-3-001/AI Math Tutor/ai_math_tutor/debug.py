import os
from vision.ocr import OCREngine, llm_convert_to_latex
from utils.image_utils import preprocess_for_ocr
from solver.equation_solver import parse_latex_to_sympy
from PIL import Image

ocr = OCREngine()
img = Image.open('samples/eq_4.png')
pre = preprocess_for_ocr(img)
raw = ocr.extract_text(pre)
print("RAW:", repr(raw))
latex = llm_convert_to_latex(raw)
print("LATEX:", repr(latex))
try:
    s = parse_latex_to_sympy(latex)
    print("SYMPY:", repr(s))
except Exception as e:
    print("ERROR TYPE:", type(e))
    print("ERROR MSG:", str(e))
