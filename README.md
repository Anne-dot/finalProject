# CNC Machining Centre Enhancement: Final Project

## Project Overview
This repository contains the development code for enhancing a CNC machining centre running Mach3 software. The project focuses on improving tool data management and safety through custom macros and interfaces.

## Core Components
- Tool data handling system with CSV backend
- Tool parameter validation and safety restrictions
- Web-based UI for tool management
- DXF to G-code conversion for horizontal drilling operations
- Enhanced safety mechanisms for tool operations

## Repository Structure
```
/src
  /macros        # Mach3 VBScript macros (.m1s files)
  /ui            # Browser-based tool management interface
  /preprocessing # G-code preprocessing utilities
  /dxf           # DXF file handling and conversion
  /utils         # Helper functions and common code
```

## Key Features
- Unified CSV structure for all tool types
- DRO-based tool data system for Mach3 integration
- Tool movement restrictions based on tool type
- Automatic safety validation for G-code
- DXF file parsing for horizontal drilling operations

## Technology Stack
- Mach3 VBScript for machine control
- Python for file processing and automation
- HTML/CSS/JavaScript for browser-based UI
- CSV for data storage and interchange

## Documentation
- All project documentation including technical specifications, user documentation, and system architecture is maintained in Jira.
- The GitHub repository contains only source code.
- The GitHub wiki contains a blog documenting the project's progress and process

## Status
Active development - implementing core tool management functionality with safety enhancements.

## Contact
Anne Ruusmann - ruusmann@gmail.com
