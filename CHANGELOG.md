# Changelog

### Potential future features

- Implement score-based ranking system: 
    - score = w1*(Booking deficit) - w2*(Sessions since last booking)
    - Booking deficit = expected bookings - actual bookings
    - w1, w2 = weights to calibrate

### [v1.1.1] - 12-01-26 — Almost implemented, needs bugfix
- tables.print_log() now allows user to enter:
    - the starting index to print from from most recent back (most recent session selected by default)                      (DONE)
    - how many lines to print (10 by default) (DONE)
    - chronology (chronological by default)   (DONE) 
    - clears log table and reloads            (NOT DONE)
### [v1.1.0] — 11-01-26 — Implemented
- Bookings log now sorts chronologically (newest last)
    - New property, session_manager.sessions_chronologically, added. Returns session log chronologically.
    - session_manager.update_log_sheet() now updates sheets spreadsheet chronologically and from cell A2.
    - tables.print_log() now prints table chronologically
- New 2026 tab: loads data from 2025 and 26 log sheets
    - Program only updates 2026 log and 2026 stats

## [v1.0.0] — 11-01-26
- 2025 final working version.