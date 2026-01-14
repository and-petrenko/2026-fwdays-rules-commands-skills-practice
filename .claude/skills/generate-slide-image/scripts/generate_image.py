#!/usr/bin/env python3
"""
Генерація зображень за допомогою OpenAI DALL-E API.
Зберігає зображення в slidev/public/images/
"""

import os
import sys
import json
import argparse
import urllib.request
from pathlib import Path
from datetime import datetime


def load_env():
    """Завантажує змінні середовища з .env файлу."""
    # Шукаємо .env файл від кореня проєкту
    current = Path(__file__).resolve()
    for parent in [current] + list(current.parents):
        env_file = parent / ".env"
        if env_file.exists():
            with open(env_file, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        key, _, value = line.partition("=")
                        key = key.strip()
                        value = value.strip().strip('"').strip("'")
                        if key and value:
                            os.environ.setdefault(key, value)
            break


# Завантажуємо .env при імпорті
load_env()


def sanitize_filename(prompt: str, max_length: int = 40) -> str:
    """Створює безпечну назву файлу з промпту."""
    # Замінюємо небезпечні символи
    safe_chars = []
    for char in prompt[:max_length]:
        if char.isalnum() or char in '-_ ':
            safe_chars.append(char if char != ' ' else '_')
    return ''.join(safe_chars).strip('_') or 'image'


def generate_image(prompt: str, size: str = "1024x1024", quality: str = "standard") -> dict:
    """
    Генерує зображення через DALL-E API.

    Args:
        prompt: Текстовий опис зображення
        size: Розмір (1024x1024, 1792x1024, 1024x1792)
        quality: Якість (standard, hd)

    Returns:
        dict з результатом операції
    """
    # Перевірка API ключа
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return {
            "success": False,
            "error": "OPENAI_API_KEY не встановлено. Встанови змінну середовища."
        }

    # Імпорт OpenAI
    try:
        from openai import OpenAI
    except ImportError:
        return {
            "success": False,
            "error": "Пакет openai не встановлено. Виконай: pip install openai"
        }

    # Валідація розміру
    valid_sizes = ["1024x1024", "1792x1024", "1024x1792"]
    if size not in valid_sizes:
        return {
            "success": False,
            "error": f"Невірний розмір. Доступні: {', '.join(valid_sizes)}"
        }

    try:
        # Ініціалізація клієнта
        client = OpenAI(api_key=api_key)

        print(f"Генерація зображення: {prompt[:50]}...", file=sys.stderr)

        # Виклик DALL-E API
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size=size,
            quality=quality,
            n=1
        )

        # Отримання URL зображення
        image_url = response.data[0].url
        revised_prompt = response.data[0].revised_prompt

        # Створення директорії для зображень
        output_dir = Path("slidev/public/images")
        output_dir.mkdir(parents=True, exist_ok=True)

        # Генерація імені файлу
        safe_name = sanitize_filename(prompt)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{safe_name}_{timestamp}.png"
        output_path = output_dir / filename

        # Завантаження зображення
        print(f"Завантаження зображення...", file=sys.stderr)
        urllib.request.urlretrieve(image_url, output_path)

        # Відносний шлях для Slidev
        slidev_path = f"/images/{filename}"

        return {
            "success": True,
            "file_path": str(output_path),
            "slidev_path": slidev_path,
            "prompt": prompt,
            "revised_prompt": revised_prompt,
            "size": size,
            "quality": quality
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "prompt": prompt
        }


def main():
    parser = argparse.ArgumentParser(
        description="Генерація зображень через OpenAI DALL-E",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Приклади:
  python generate_image.py "Робот-асистент"
  python generate_image.py "Футуристичне місто" --size 1792x1024
  python generate_image.py "Портрет AI" --size 1024x1792 --quality hd
        """
    )

    parser.add_argument(
        "prompt",
        help="Текстовий опис зображення"
    )
    parser.add_argument(
        "--size",
        default="1024x1024",
        choices=["1024x1024", "1792x1024", "1024x1792"],
        help="Розмір зображення (за замовчуванням: 1024x1024)"
    )
    parser.add_argument(
        "--quality",
        default="standard",
        choices=["standard", "hd"],
        help="Якість зображення (за замовчуванням: standard)"
    )

    args = parser.parse_args()

    # Генерація зображення
    result = generate_image(args.prompt, args.size, args.quality)

    # Вивід результату
    print(json.dumps(result, ensure_ascii=False, indent=2))

    # Код виходу
    sys.exit(0 if result["success"] else 1)


if __name__ == "__main__":
    main()
