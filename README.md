## Image Text Extraction
### Author : Rahul Bhoyar


#### Steps : 
**How to install tesseract on iOS Macbook?**
Tesseract OCR can be installed on a Macbook running iOS using the following steps:

Install Homebrew: Homebrew is a package manager for macOS that makes it easy to install and manage software. To install Homebrew, open Terminal and run the following command:

```

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

Install Tesseract: Once you have Homebrew installed, you can use it to install Tesseract by running the following command in Terminal:

```
brew install tesseract
```

This will download and install the latest version of Tesseract OCR on your Macbook.

Verify Installation: 
To verify that Tesseract is installed correctly, run the following command in Terminal:
```
tesseract -v
```
This should print the version of Tesseract that is installed on your system.

Now that Tesseract is installed, you can use it in combination with the Python pytesseract library to extract text from images.
