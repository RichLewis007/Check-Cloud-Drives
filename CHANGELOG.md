# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Comprehensive unit test suite with 64 tests covering:
  - ConfigManager (config loading/saving, persistence, TOML handling)
  - DriveConfig and DriveStatus models (validation, serialization)
  - RcloneWorker integration (command execution, output parsing)
  - DriveCard UI component (edit mode, status updates, display)
- pytest testing framework with pytest-qt for Qt widget testing
- Test fixtures and shared test utilities in `tests/conftest.py`
- Test documentation in `tests/README.md`
- pytest configuration in `pytest.ini`

### Changed

- Added pytest, pytest-qt, and pytest-mock to dev dependencies

## [0.1.0] - 2024-01-XX

### Added

- Initial release
- PySide6 GUI application for monitoring cloud drives
- Menu bar integration for macOS
- Support for multiple cloud drive types (Google Drive, OneDrive, Dropbox, etc.)
- Real-time status updates with auto-refresh
- Customizable display names for drives
- Stay on top window option
- Configuration management via TOML files
- Custom SVG icon support
- Bundled font loading (Atkinson Hyperlegible Mono)
- Drag and drop reordering of drive cards
- Edit mode for drive card titles
- Remove drive functionality

[Unreleased]: https://github.com/yourusername/check-cloud-drives/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/yourusername/check-cloud-drives/releases/tag/v0.1.0
