# Towel-PDF 📄🐍

This is a guide on how to compile the `towel-pdf.py` Python script into an executable on both Mac and Windows. 

## Prerequisites 📚

Before you start, make sure you have activated your Python virtual environment (`env`). You can do this by running the following command in your terminal or command prompt:

- On Mac/Linux:
    ```bash
    source env/bin/activate
    ```
- On Windows:
    ```cmd
    env\Scripts\activate
    ```

## Mac (using Platypus) 🍏

1. Download and install Platypus from its official website.

2. Open Platypus: Launch the Platypus application.

3. Create a new script: Click on the "+New" button at the bottom left of the Platypus window.

4. Set the script type: In the "Script Type" dropdown menu, select "Shell".

5. Set the interface type: In the "Interface" dropdown menu, select "None".

6. Add your scripts and files: Click on the "Bundled Files" tab, then click on the "+" button at the bottom. In the file dialog that opens, navigate to the env directory and the towel-pdf.py script, select them, and click "Open". These files will be bundled into the .app file.

7. Create the shell script: Click on the "Script" tab, then enter the following script in the text area:

    ```bash
    #!/bin/bash
    export PYTHONPATH=./env/bin/python3
    ./env/bin/python3 towel-pdf.py
    ```

8. Click the `Create App` button to create the executable.

## Windows (using Bat To Exe Converter) 💻

1. Create a new batch file named `run_towel_pdf.bat` with the following content:

    ```bat
    @echo off
    call env\Scripts\activate
    python towel-pdf.py
    pause
    ```

2. Download and install Bat To Exe Converter from its official website.

3. Open Bat To Exe Converter and click the `...` button next to the `Batch file` field. Navigate to your `run_towel_pdf.bat` file and open it.

4. Click the `Compile` button to create the executable.

## Merging Zips with Towel-ZipSplit 🗂️

You can use [Towel-ZipSplit](https://github.com/towelWet/Towel-ZipSplit) to merge the zips.

## Running the Executable 🏃‍♀️

After creating the executable, you can run it just like any other program on your computer. Just double-click the executable file to run it.

## Troubleshooting 🛠️

If you encounter any issues, make sure your Python virtual environment is activated and that all the required Python packages are installed. You can install the required packages using the following command:

```bash
pip install -r requirements.txt
