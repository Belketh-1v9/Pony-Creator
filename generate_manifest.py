from pathlib import Path
import json

ASSETS_DIR = Path("assets")
OUTPUT_FILE = ASSETS_DIR / "manifest.json"

SVG_CATEGORIES = [
    "body",
    "body-merpony",
    "head",
    "ears",
    "eye",
    "iris",
    "glimmer",
    "mane",
    "tail",
    "tail-merpony",
    "horn",
    "wings",
    "accessories",
    "cutiemark",
    "gem",
    "background",
]

IMAGE_CATEGORIES = {
    "crystal": [".png", ".jpg", ".jpeg", ".webp", ".svg"]
}

def list_files(folder: Path, extensions: list[str]) -> list[str]:
    if not folder.exists():
        return []

    return sorted(
        file.name
        for file in folder.iterdir()
        if file.is_file()
        and file.suffix.lower() in extensions
        and not file.name.startswith(".")
    )

def main():
    if not ASSETS_DIR.exists():
        raise FileNotFoundError("Nie znaleziono folderu assets")

    manifest = {}

    for category in SVG_CATEGORIES:
        manifest[category] = list_files(
            ASSETS_DIR / category,
            [".svg"]
        )

    for category, extensions in IMAGE_CATEGORIES.items():
        manifest[category] = list_files(
            ASSETS_DIR / category,
            extensions
        )

    OUTPUT_FILE.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )

    print(f"Gotowe: {OUTPUT_FILE}")
    print(f"Liczba kategorii: {len(manifest)}")
    print(f"Liczba assetów: {sum(len(v) for v in manifest.values())}")

if __name__ == "__main__":
    main()