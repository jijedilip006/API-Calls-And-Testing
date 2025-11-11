This is small project that I created to discover Gemini API calls and the different features using it. 
The project may develop into a chat window where users can upload files to the window and ask questions in relation to the documents uploaded which will use the API to respond with




### Getting the API key

Head into https://aistudio.google.com/api-keys in any web browser to aquire your Gemini API key and ensure that it is the 2.5 flash model since this code uses that specific model to run

#### **Note: This project is not a deployed project and all commands below are to be run within an IDE that supports python (for example: VS Code)**

# Setting the API key as an environment variable

Use the name GEMINI_API_KEY (matches the code in this repo). Keep this key secret and never commit it to source control.

## macOS (zsh / bash)

- Temporarily (current terminal session only):
  - zsh or bash:
    ```
    export GEMINI_API_KEY="your_api_key_here"
    ```
- Persistently (every new terminal):
  - Add the line above to your shell startup file:
    - zsh (default on modern macOS): `~/.zshrc`
    - bash: `~/.bash_profile` or `~/.bashrc`
  - Example:
    ```
    echo 'export GEMINI_API_KEY="your_api_key_here"' >> ~/.zshrc
    source ~/.zshrc
    ```
- Verify:
  ```
  echo $GEMINI_API_KEY
  ```

## Windows

### Command Prompt (cmd.exe)
- Temporarily (current cmd window only):
  ```
  set GEMINI_API_KEY=your_api_key_here
  ```
- Persistently (for current user):
  ```
  setx GEMINI_API_KEY "your_api_key_here"
  ```
  After setx, open a new Command Prompt to see the value.
- Verify (cmd):
  ```
  echo %GEMINI_API_KEY%
  ```

### PowerShell
- Temporarily (current PowerShell session only):
  ```
  $env:GEMINI_API_KEY = "your_api_key_here"
  ```
- Persistently (current user):
  ```
  [Environment]::SetEnvironmentVariable("GEMINI_API_KEY","your_api_key_here","User")
  ```
  After that, open a new PowerShell window.
- Verify (PowerShell):
  ```
  echo $env:GEMINI_API_KEY
  ```

## GUI (Windows)
- Settings → System → About → Advanced system settings → Environment Variables → New (or Edit) under User variables.
- Restart affected apps/terminals to pick up changes.

## Security note
- Treat this key like a password. Do not paste it into public places or commit it to repositories. Use secrets managers for production systems.

**To run the app head into the App folder and run main.py**