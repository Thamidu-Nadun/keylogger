# Keylogger Project

This is a simple keylogger project in Python that logs keystrokes and writes them to a file.

## How it Works

The keylogger uses the `pynput` library to monitor and capture keystrokes. It listens to key presses and saves each key's information to a text file named `keylogs.txt`. The `keylogs.txt` file will be created in the same directory as the keylogger script.

## Getting Started

To use the keylogger, follow these steps:

1. Clone the repository.

2. Install the required dependencies.

3. Run the keylogger script.

4. The keylogger will start running, and it will log all the keystrokes you make.

## Automate The Programme

1. Convert .py to .exe
    ```shell
        pip install pyinstalller
        pyinstalller -F .\main.py
```
 -F = file
    <img src="https://github.com/Thamidu-Nadun/keylogger/blob/main/img/cmd.png">
    <img src="https://github.com/Thamidu-Nadun/keylogger/blob/main/img/file.png">
    <img src="https://github.com/Thamidu-Nadun/keylogger/blob/main/img/file2.png">
    <br>

2. Create a PowerShell script:
    Create a new text file and save it with a .ps1 extension (e.g., myscript.ps1).

```shell
Start-Process -FilePath "C:\path\to\your\file.exe" -WindowStyle Hidden
```
        Replace `"C:\path\to\your\file.exe"` with the actual path to your .exe file.
        <br>
    <img src="https://github.com/Thamidu-Nadun/keylogger/blob/main/img/file3.png"><br>
    **Test the file:**
        :Open terminal in your DIR and type=>
```shell
        .\yourScriptName.ps1
```
<br><br>

3. Move the .ps1 file to the Startup folder:
    Press Win + R to open the Run dialog box. Type **`shell:startup`** and hit Enter. This will open the Startup folder.
    <br>
    <img src="https://github.com/Thamidu-Nadun/keylogger/blob/main/img/run.png"><br>
    

4. Move the .ps1 file you created in step 2 into the Startup folder.<br><br>
5. Open setting and verify it.
    <br>`Setting > Apps > Startup`<br>
    <img src="https://github.com/Thamidu-Nadun/keylogger/blob/main/img/app.png"><br>
----------------------------------------------------------------
## Disclaimer

**Important**: This keylogger script is intended for educational and research purposes only. Misusing this script to monitor and record keystrokes without explicit permission from the users of the computer is illegal and unethical. The author does not condone any illegal use of this script.


## Acknowledgments

- [pynput](https://pypi.org/project/pynput/) - The Python library used to monitor and control input devices.

Feel free to modify and enhance this project according to your needs.

Happy coding!
<br>
<h3 align="center">Thamidu-Nadun<h3><br>