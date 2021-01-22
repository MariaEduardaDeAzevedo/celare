# Celare v0.0.3

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

2.1 **For scripts**

2.1.1 Import the celare module inside your code
```
from celare import celare
from celare.read import read_tokens
```

2.1.2 Run your code in the terminal and enter the name of the variable and the token for it, as in the example below
```
python3 your_code.py TOKEN t0k3n SECRET_KEY s3cr3tk3y
```

2.2 **For notebooks**

2.2.1 Import the celare module inside your notebook
```
from celare.celare import celare_notebook
from celare.read import read_tokens
```

2.2.2 The celare_notebook function receives a dictionary containing the reference (key) and token (value). You can run the notebook cell only when necessary once as the code example below and then discard it.
```
celare_notebook({"TOKEN": "t0k3n", "SECRET_KEY": "s3cr3tk3y"})
```

3. A file called ".tokens.json" will be created in the root directory, where all tokens passed will be saved. If you are going to put your project on GitHub and need to hide this file, import the module that generates a gitignore template automatically or add the file's hiding information if it already exists.
```
from celare import gitignore
```

4. To update a saved token or add a new one, just repeat the step 2. if you only need to run the code, don't worry, you don't need to pass the token arguments every time you run, only when necessary.

6. To read the tokens file use the read_tokens() function, this will return a dictionary with all the tokens saved before.
```
tokens = read_tokens()
```

## How to contribute?

1. Clone this repository to make modifications 
Using HTTPS
```
git clone https://github.com/MariaEduardaDeAzevedo/celare.git
```
or using GitHub CLI
```
gh repo clone MariaEduardaDeAzevedo/celare
```
2. If you don't have modifications to do, just open an issue!

