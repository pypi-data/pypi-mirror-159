from pathlib import Path
from typing import Dict

from PIL import Image  # type: ignore
from fpdf import FPDF, HTMLMixin  # type: ignore


class PDF(FPDF, HTMLMixin):
    author: str = ''
    creator: str = ''
    producer: str = ''
    subject: str = ''
    compress: bool = False

    def add_item(self, x: int, y: int, text: str, font: str, size: int, color: Dict[str, int], url: str = '') -> None:
        self.set_text_color(**color if color else {'r': 51, 'g': 51, 'b': 51})
        self.set_font(font, size=size)
        self.text(x, y, text)
        if url:
            link = self.add_link()
            self.set_link(link)
            self.link(x, y - 3, 50, 5, url)

    def add_image(self, x: int, y: int, w: int, h: int, path: str) -> None:
        img = Image.open(path)
        self.image(img, x=x, y=y, w=w, h=h)

    def install_font(self, content: dict, path: Path) -> None:
        for item in content['items']['fonts']:
            name = [item][0].get('name')
            font_path = Path(path) / [item][0].get('path')
            ttf = [item][0].get('ttf') or True
            self.add_font(family=name, fname=font_path, uni=ttf)

    def add_line(self, x1: int, y1: int, x2: int, y2: int, w: float, color: Dict[str, int]) -> None:
        self.set_line_width(w)
        self.set_draw_color(**color)
        self.line(x1=x1, y1=y1, x2=x2, y2=y2)

    def load_from_json(self, content: dict) -> None:
        self.author = self.creator = self.producer = content['metadata'].get('author') or ''
        self.subject = content['metadata'].get('subject') or ''
        self.set_title(content['metadata'].get('title') or '')
        self.set_keywords(keywords=content['metadata'].get('keywords') or '')
        self.set_lang(lang=content['metadata'].get('language') or '')
        self.set_margin(0)
        self.compress = False
        self.set_display_mode('fullpage', 'single')

    def load_layouts(self, content: dict, path: Path) -> None:
        for item in content['items']['layout']:
            layout_type = [item][0].get('type')

            if layout_type == 'image':
                x = [item][0].get('x')
                y = [item][0].get('y')
                w = [item][0].get('w')
                h = [item][0].get('h')
                image_path = path / [item][0].get('path')
                self.add_image(x, y, w, h, image_path)

            elif layout_type == 'line':
                x1 = [item][0].get('x1')
                y1 = [item][0].get('y1')
                x2 = [item][0].get('x2')
                y2 = [item][0].get('y2')
                w = [item][0].get('w')
                color = [item][0].get('color')
                self.add_line(x1, y1, x2, y2, w, color)

    def load_items(self, content: dict) -> None:
        keys = ['left', 'right', 'footer']
        for key in keys:
            for item in content['items'][key]:
                x = [item][0].get('x')
                y = [item][0].get('y')
                text = [item][0].get('text')
                font = [item][0].get('font')
                size = [item][0].get('size')
                color = [item][0].get('color')
                url = [item][0].get('url')
                self.add_item(x, y, text, font, size, color, url)
