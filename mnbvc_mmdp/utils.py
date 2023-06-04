import json
import pathlib
from mmda.types import Document
from mmda.recipes import CoreRecipe

def parse_to_jsonl(pdfs_path: str, output_path: str) -> None:
    pdfs_dir = pathlib.Path(pdfs_path)
    recipe = CoreRecipe()
    with open(output_path, "w") as file:
        for pdf in pdfs_dir.iterdir():
            pdf_dir = pathlib.Path(pdf)
            print(pdf_dir)
            doc: Document = recipe.from_path(pdfpath=pdf_dir)
            doc_json = doc.to_json()
            json.dump(doc_json, file)
            file.write('\n')
