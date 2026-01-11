# Changelog

## Jan 26 update

### [Unreleased ] — Planned updates
- New 2026 tab: loads data from 2025 summary tab.
    - Requires new method in sheets to read 2025 summary. 
    - Data could potentially be stored locally.

### [v1.1.0] — 11-01-26 — Implemented
- Bookings log now sorts chronologically (newest last)
    - New property, session_manager.sessions_chronologically, added. Returns session log chronologically.
    - session_manager.update_log_sheet() now updates sheets spreadsheet chronologically and from cell A2.
    - tables.print_log() now prints table chronologically

## [v1.0.0] — 11-01-26
- Current working version.