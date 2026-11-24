"""Funções auxiliares de texto e números."""
import math
import re
import unicodedata

import pandas as pd

from config import settings


def normalizar_texto(txt: str) -> str:
    if pd.isna(txt):
        return None

    txt = unicodedata.normalize("NFD", txt)
    txt = txt.encode("ascii", "ignore").decode("utf-8")
    txt = txt.upper()
    txt = re.sub(r"\s+", " ", txt).strip()

    return txt


# ---------------------------------------------------------------------------
# Números da IN MinC nº 5/2023
# ---------------------------------------------------------------------------

def arredonda_in5(x: float) -> int:
    """Arredondamento do §2º do art. 5º da IN 5: fração >= 0,5 arredonda para cima; < 0,5 para baixo.

    Não usar round()/np.round(), que arredondam 2,5 para 2 (arredondamento bancário).
    """
    return math.floor(x + 0.5 + settings.COTA_TOL)
