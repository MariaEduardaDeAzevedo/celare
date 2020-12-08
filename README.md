# Celare 

A package to write and hide tokens, passwords, secret keys, without having to put them in the code!

## How to use?

1. Install the package using pip
```
pip3 install celare
```
or
```
pip3 install celare
```

2. Import the celare module inside yor code
```
from celare import celare
from celare.read import read_tokens
```

3. Run your code in the terminal and enter the name of the variable and the token for it, as in the example below
```
python3 your_code.py TOKEN t0k3n SECRET_KEY s3cr3tk3y
```

4. A file called ".tokens.json" will be created in the root directory, where all tokens passed will be saved. If you are going to put your project on GitHub and need to hide this file, import the module that generates a gitignore template automatically or add the file's hiding information if it already exists
```
from celare import gitignore
```

5. To update a saved token or add a new one, just repeat the step 3. if you only need to run the code, don't worry, you don't need to pass the token arguments every time you run, only when necessary

## How to contribute?

1. Clone this repository to make modifications 
Using HTTPS
```
git clone https://github.com/MariaEduardaDeAzevedo/celare.git
```
or usign GitHub CLI
```
gh repo clone MariaEduardaDeAzevedo/celare
```
2. If you don't have modifications to do, just open an issue!

