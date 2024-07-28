# ESX to Ox-Lib Locale Converter

This script processes a folder of ESX FiveM locale files (in `.lua` format) and converts them into JSON files suitable for use with Ox-Lib.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)

## Prerequisites

- Python 3.x installed on your machine.

## Installation

1. Clone this repository or download the script file directly.

2. Ensure you have the necessary permissions to execute the script.

## Usage

1. Place your ESX locale files in a directory named `locales` located in the same directory as the script.

2. Run the script using Python:

    ```bash
    python esx_ox_locale_converter.py
    ```

3. The script will create an `ox_output` directory within the `locales` directory and output the converted JSON files there.

