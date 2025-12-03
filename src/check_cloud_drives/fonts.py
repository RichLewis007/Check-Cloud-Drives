"""Font loading utilities for bundled fonts."""

import zipfile
import tempfile
from pathlib import Path
from typing import Optional
from PySide6.QtGui import QFontDatabase


def load_font_from_zip(zip_path: Path, font_name_in_zip: str) -> bool:
    """
    Load a font file from a zip archive into Qt's font database.
    
    Args:
        zip_path: Path to the zip file containing fonts
        font_name_in_zip: Name of the font file inside the zip (e.g., "AtkynsonMonoNerdFontPropo-Regular.otf")
    
    Returns:
        True if font was loaded successfully, False otherwise
    """
    if not zip_path.exists():
        print(f"Font zip file not found: {zip_path}")
        return False
    
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # Check if font file exists in zip
            if font_name_in_zip not in zip_ref.namelist():
                print(f"Font file '{font_name_in_zip}' not found in zip: {zip_path}")
                return False
            
            # Extract font to temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix='.otf') as tmp_file:
                tmp_path = Path(tmp_file.name)
                tmp_file.write(zip_ref.read(font_name_in_zip))
                tmp_file.flush()
            
            # Load font into Qt's font database
            font_id = QFontDatabase.addApplicationFont(str(tmp_path))
            if font_id == -1:
                print(f"Failed to load font: {font_name_in_zip}")
                tmp_path.unlink()  # Clean up temp file
                return False
            
            # Verify font was loaded by checking font families
            font_families = QFontDatabase.applicationFontFamilies(font_id)
            if font_families:
                print(f"Successfully loaded font: {font_families[0]}")
                tmp_path.unlink()  # Clean up temp file after loading
                return True
            else:
                print(f"Font loaded but no families found: {font_name_in_zip}")
                tmp_path.unlink()
                return False
                
    except Exception as e:
        print(f"Error loading font from zip: {e}")
        import traceback
        traceback.print_exc()
        return False


def load_all_fonts_from_zip(zip_path: Path, font_pattern: str = "Propo") -> int:
    """
    Load all matching font files from a zip archive.
    
    Args:
        zip_path: Path to the zip file containing fonts
        font_pattern: Pattern to match font files (default: "Propo" for proportional fonts)
    
    Returns:
        Number of fonts successfully loaded
    """
    if not zip_path.exists():
        print(f"Font zip file not found: {zip_path}")
        return 0
    
    loaded_count = 0
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # Find all font files matching the pattern
            font_files = [f for f in zip_ref.namelist() if font_pattern in f and f.endswith('.otf')]
            
            for font_file in font_files:
                if load_font_from_zip(zip_path, font_file):
                    loaded_count += 1
                    
        print(f"Loaded {loaded_count} font(s) from {zip_path}")
        return loaded_count
                
    except Exception as e:
        print(f"Error loading fonts from zip: {e}")
        import traceback
        traceback.print_exc()
        return 0


def setup_bundled_fonts(project_root: Optional[Path] = None) -> bool:
    """
    Set up bundled fonts for the application.
    
    This function looks for the font zip file in the assets/fonts directory
    and loads the required fonts into Qt's font database.
    
    Args:
        project_root: Root directory of the project. If None, attempts to find it automatically.
    
    Returns:
        True if at least one font was loaded successfully, False otherwise
    """
    # Determine project root
    if project_root is None:
        # Try to find project root relative to this file
        current_file = Path(__file__)
        # Go up from src/check_cloud_drives/fonts.py to project root
        project_root = current_file.parent.parent.parent
    
    # Look for font zip file
    # In development: project_root/assets/fonts/
    # When installed: assets should be included via shared-data in pyproject.toml
    font_zip = project_root / "assets" / "fonts" / "AtkinsonHyperlegibleMono.zip"
    
    if not font_zip.exists():
        print(f"Font zip file not found at: {font_zip}")
        print("Application will use system fonts if available.")
        return False
    
    # Load the proportional font variant (used throughout the app)
    # The app uses "AtkynsonMono Nerd Font Propo" which corresponds to
    # "AtkynsonMonoNerdFontPropo-Regular.otf" in the zip
    success = load_font_from_zip(font_zip, "AtkynsonMonoNerdFontPropo-Regular.otf")
    
    # Optionally load other variants for better font rendering
    if success:
        # Load other Propo variants for different weights/styles
        load_font_from_zip(font_zip, "AtkynsonMonoNerdFontPropo-Bold.otf")
        load_font_from_zip(font_zip, "AtkynsonMonoNerdFontPropo-Italic.otf")
        load_font_from_zip(font_zip, "AtkynsonMonoNerdFontPropo-BoldItalic.otf")
        load_font_from_zip(font_zip, "AtkynsonMonoNerdFontPropo-Medium.otf")
    
    return success

