import click
from sys import exit
from project import langSetup
import subprocess

# TODO:
# see that if click provides a way to only accept provided values for a argument(like argparse)
# else/also envolve supported languages in help
# see, if you can have globbing with filenames like for java, java8 or java11 both should be accepted and checked

@click.command()
@click.option('--language', '-l', prompt='Input Language', help='Enter the programming language to setup project for')
@click.option('--name', '-n', prompt='Input Project Name', help='Provide the name of project')
@click.option('--gitit', '-g', is_flag=True, help='Want git setup?')
def main(language, name, gitit):
    '''Project Setup Helper:

    Current Language Support:

    [C, C++, Java, Java-Servlet, Python, Web-Designing]

    You can provide '-g' or '--gitit' flag to initialize git inside the project of yours.

    You'll be provided option to select compiler for C/C++ projects.
    Default compiler for 'C' will be "cc" which is generally an aliased form of "gcc" in linux.
    For 'C++' will be 'g++'
    '''

    if language.lower() == 'c':
        print("project setup for C language, named: {}".format(name))
        langs = langSetup.LangC(name)
        langs.setup()
    elif language.lower() in ["cpp", "c++"]:
        print("project setup for C++ language, named: {}".format(name))
        langs = langSetup.LangCpp(name)
        langs.setup()
    elif language.lower() == "java":
        print("project setup for Java language, named: {}".format(name))
        langs = langSetup.LangJava(name)
        langs.setup()
    elif language.lower() == "python":
        print("project setup for Python language, named: {}".format(name))
        langs = langSetup.LangPython(name)
        langs.setup()
    elif language.lower() == "webd":
        print("project setup for Web Designing, named: {}".format(name))
        langs = langSetup.LangWebD(name)
        langs.setup()
    elif language.lower() in ["servlet", "java-servlet", "servlet-java"]:
        print("project setup for Java Servlet, named: {}".format(name))
        langs = langSetup.LangServlet(name)
        langs.setup()
    else:
        print("Language not supported or not correct language name")
        exit(2)
    extraSetup(name, gitit)


def extraSetup(dirname, isgit):
    """additional setup"""
    if isgit:
        subprocess.run(["git", "init"], cwd=dirname)
        subprocess.run(["git", "add", "*"], cwd=dirname)
        subprocess.run(["git", "commit", "-m", "'initial commit'"], cwd=dirname)


if __name__ == "__main__":
    print("Not a stand-alone script")
    exit(1)
