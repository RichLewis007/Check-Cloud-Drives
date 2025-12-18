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
- pytest-cov for code coverage reporting with HTML output
- Test fixtures and shared test utilities in `tests/conftest.py`
- Test documentation in `tests/README.md`
- pytest configuration in `pytest.ini`

### Changed

- Added pytest, pytest-qt, pytest-mock, and pytest-cov to dev dependencies

## 2025-12-18

### Added

- Documentation updates and improvements
- Code coverage reporting support with pytest-cov
- Enhanced test documentation with coverage examples

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

### Added

- Drag and drop card reordering functionality
  - Cards can be dragged and dropped to reorder drives
  - Drive order is automatically saved to configuration
  - Visual feedback during drag operations

### Fixed

- Removed grey background artifact from dropped cards during drag and drop
- Fixed card rearranging logic to properly maintain order
- Improved add dialog functionality for better user experience

## 2025-12-06

### Added

- Settings page with comprehensive configuration options:
  - Auto-refresh interval configuration (in seconds, 0 to disable)
  - Stay on top toggle
  - Run at startup option
  - Settings persist across application restarts
- Button height consistency across code and settings page
- Modal dialog adjustments for pick cloud drives dialog
- Window geometry persistence (position and size saved automatically)

### Changed

- Updated app handler to bring dialog to top when leaving/returning to app (edge case when "stay on top" is activated)
- Removed redundant code

## 2025-12-03

### Added

- GitHub Pages landing page/docs page with modern, responsive design
- Auto-deploy GitHub Actions workflow for documentation (`.github/workflows/pages.yml`)
- Font installation handling for icons and text if not installed on system
- Bundled font loading from zip archive (Atkinson Hyperlegible Mono Nerd Font)
- Custom SVG icon support for different drive types:
  - Icons automatically detected from `assets/icons/` directory
  - Support for `googledrive.svg`, `onedrive.svg`, `dropbox.svg`, etc.
  - Fallback to emoji icons if SVG files not found

### Changed

- Improved icons and button display with Nerd Font icons
- Enhanced text placement and UI layout
- Fixed font load and asset path resolution
- Applied Ruff formatting and fixed errors

## 2025-12-02

### Added

- Base program functionality with PySide6 GUI framework
- Rclone integration:
  - Reads remotes from rclone configuration
  - Gets drive information (total, used, free space)
  - Real-time status updates via `rclone about` command
- macOS menu bar integration:
  - System tray icon for easy access
  - Click to show/hide main window
  - Right-click context menu with "Stay on Top" toggle
- Initial UI implementation:
  - Modern dark theme with smooth animations
  - Drive cards displaying status information
  - Refresh All button for manual status updates
  - Add Drive button to add new drives to monitor
  - Settings button to access configuration
- Drive card features:
  - Click on drive name to enter edit mode
  - Edit display name and remote name inline
  - Real-time status display with timestamps
  - Visual indicators for drive status
- Configuration management:
  - TOML-based configuration file (`check-cloud-drives.toml`)
  - Automatic detection of available rclone remotes
  - Setup dialog for initial drive selection
  - Manual drive addition support
  - Drive order persistence
  - Window geometry persistence
- Auto-refresh functionality:
  - Configurable refresh interval (default: 300 seconds)
  - Automatic background updates
  - Can be disabled by setting interval to 0

### Fixed

- Memory leak in worker threads (RcloneWorker cleanup)

## 2025-12-02

### Added

- Initial project setup
- Project structure and configuration
