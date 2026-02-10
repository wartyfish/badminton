# Changelog

### Potential future features
- Score-based ranking system: 
    - score = w1*(Booking deficit) - w2*(Sessions since last booking)
    - Booking deficit = expected bookings - actual bookings
    - w1, w2 = weights to calibrate
- bext.get_key() for cleaner input handling

### [v1.2.0] — Rich CLI overhall — WIP
TODO
- Fix "Modify Session" logic
    - Get table to load chronologically
    - Load table in chunks again
- Rich tables for log sheet editing
- Update Due To Book logic to take bookings/session into account

Completed
- Log and stats tables now rendered using rich library. 
    - Both tables rendered side by side inside a Panel object. 01/02/26

### [v1.1.1] — 01-02-26 — Implemented
Completed
- tables.print_log() now allows user to enter:
    - the starting index to print from from most recent back (most recent session selected by default)                   
    - how many lines to print (10 by default) 
    - chronology (chronological by default)    
- refactored sessions.sessions_sorted property  
- clears log table and reloads 

Bug fixes
- fix broken print_log() logic DONE
- Implement working escape. DONE 12/01/26
- Fix bug that causes crash when players/bookers subtracted without players/booekrs also being added to session. DONE 29/01/26 
- Fix input bug in Add Session logic: pressing 1 to commit does nothing. DONE 29/01/26




### [v1.1.0] — 11-01-26 — Implemented
- Bookings log now sorts chronologically (newest last)
    - New property, session_manager.sessions_chronologically, added. Returns session log chronologically.
    - session_manager.update_log_sheet() now updates sheets spreadsheet chronologically and from cell A2.
    - tables.print_log() now prints table chronologically
- New 2026 tab: loads data from 2025 and 26 log sheets
    - Program only updates 2026 log and 2026 stats

## [v1.0.0] — 11-01-26
- 2025 final working version.