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

## 2025-12-18

### Added

- Documentation updates and improvements

### Changed

- Enhanced documentation structure

## 2025-12-17

### Added

- Test framework setup (pytest)
- Initial test cases for core functionality
- GitHub Actions workflow for CI (planned)

### Changed

- Applied Ruff formatting to all files
- Updated changelog with project history

## 2025-12-08

### Changed

- Code formatting improvements across codebase

## 2025-12-07

### Fixed

- Removed grey background artifact from dropped cards during drag and drop
- Fixed card rearranging logic
- Improved add dialog functionality

## 2025-12-06

### Added

- Button height consistency across code and settings page
- Modal dialog adjustments for pick cloud drives dialog

### Changed

- Updated app handler to bring dialog to top when leaving/returning to app (edge case when "stay on top" is activated)
- Removed redundant code

## 2025-12-03

### Added

- GitHub Pages landing page/docs page
- Auto-deploy GitHub Actions workflow for documentation
- Font installation handling for icons and text if not installed on system
- Bundled font loading from zip archive

### Changed

- Improved icons and button display
- Enhanced text placement
- Fixed font load and asset path resolution
- Applied Ruff formatting and fixed errors

## 2025-12-02

### Added

- Base program functionality
- Reads remotes from rclone
- Gets drive information
- macOS menu bar integration
- Initial UI implementation

### Fixed

- Memory leak in worker threads (RcloneWorker cleanup)

## 2025-12-02

### Added

- Initial project setup
- Project structure and configuration
