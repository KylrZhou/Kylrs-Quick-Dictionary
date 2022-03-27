## Kylrs-Quick-Dictionary
>Quick Awake Dictionary For Windows via Python

Hey folks, it's Kylr here. I recently realized that translating a single word by the translation websites or apps is so inconvenient. So I tried to code a program that is aiming to simplify this procedure.  

Here's some basic notices:  
1. The main function(translation) is based on provided API, I used CNKI translation for test. You can feel free to change the API for your convenience. 
2. The GUI is based on PyQt5 make sure that your terminal could use this package properly
3. The implementation of the frosted glass effect is quoted from the CSDN forum and the author is ***之一Yo*** <https://blog.csdn.net/zhiyiYo/article/details/106739263>. Make sure that you already had his/her permission if you wanna use this effect for commercial use.  

You can use command:  `pip install-r requirements.txt` to install dependence.

Notices For the One Who Want to Pack This with Pyinstaller:
1. You can use the following pyinstaller command in CMD to pack the code to exe file. `pyinstaller -w -i .\KZ_Dic.ico -D .\PyUI.py -p .\DataMiner.py`
2. The extra download of cacert.pem is needed due to the using of python requests package. You need to download the cacert.pem file at <https://curl.se/docs/caextract.html>. Then create a new folder and name it `certifi` at the `dist` folder which your exe exists. Copy the cacert.pem file into the `certifi` folder.
3. Copy folder `aero`, file `DicPic.png`, `FG.png` and `KZ_Dic.ico` into the `dist` folder after you run pyinstaller commands.
4. Enjoy!

Feel free to contact me via `KylrZhou@outlook.com` if you have any problem.
This project follows MIT license.

![image](https://github.com/KylrZhou/Kylrs-Quick-Dictionary/blob/main/Material/REFLECTIMPLEMENTARKHIVE.png)
