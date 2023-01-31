import pytest
import os

def test_images():
    # Liste les images dans le répertoire test_data
    images = os.listdir("test_data")

    # Boucle sur chaque image et vérifie si elle existe
    for image in images:
        assert os.path.exists(os.path.join("test_data", image))
