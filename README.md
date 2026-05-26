# Password Security Analyzer

## Overview
A simple Python tool that reads passwords from a CSV file and evaluates their strength based on common security rules.

## Features
- Reads CSV files
- Calculates password strength score
- Classifies passwords (Weak / Medium / Strong)
- Provides basic improvement suggestions

## Input Format
CSV file with columns:

name, url, username, password, note

## How It Works
The tool checks:
- Password length
- Uppercase letters
- Lowercase letters
- Numbers
- Special characters

****
Then assigns a score and returns a classification.

## Run

Then enter the CSV file path.

## Future Improvements
- Export results to file
- Detect common passwords
- Improve classification rules
- Add reporting system
