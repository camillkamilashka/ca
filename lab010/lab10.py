import typer
from mypackage import lab07, lab08, lab09

app = typer.Typer()

@app.command()
def run_lab07():
    """
    Run Lab 07
    """
    lab7.run()

@app.command()
def run_lab08():
    """
    Run Lab 08
    """
    lab08.run()

@app.command()
def run_lab09():
    """
    Run Lab 09
    """
    lab9.run()

if __name__ == "__main__":
    app()