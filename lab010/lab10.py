import typer
import math
from sympy import *
from functools import lru_cache
import random
import string

app = typer.Typer()

def y(k, x):
    if x == 0:
        raise ValueError('x should not be 0')

    y_0 = 1
    b_0 = 1 / (2 * x)
    y_k = 0
    for i in range(1, k+1):
        b_k = b_0 * x**2
        y_k = b_k * y_0

        y_0 = y_k
        b_0 = b_k

    return y_k

def create_hero():
    max_hp = 100
    hp = max_hp
    is_dead = False

    def get_hp():
        return hp

    def change_hp(delta):
        nonlocal hp, is_dead
        
        if is_dead:
            return
        
        new_hp = hp + delta
        
        if new_hp > max_hp:
            hp = max_hp
        elif new_hp <= 0:
            hp = 0
            is_dead = True
        else:
            hp = new_hp

    def heal(amount):
        nonlocal hp, is_dead
        if is_dead:
            return
        change_hp(amount)

    def take_damage(amount):
        nonlocal hp, is_dead
        if is_dead:
            return
        change_hp(-amount)

    def resurrect():
        nonlocal hp, is_dead
        if not is_dead:
            return
        hp = 1
        is_dead = False

    return get_hp, heal, take_damage, resurrect

def merge(*iterables):
    generator = (iter(current) for current in iterables)
    iters = list(generator)
    while iters:
        for i in iters:
            try:
                yield i.__next__()
            except StopIteration:
                iters.remove(i)


@app.command()
def calculate_recursive(n: int):
    recursive_result = recursive_solution(n)
    typer.echo(f"Result using recursive solution: {recursive_result}")

@app.command()
def calculate_fibonacci(n: int):
    for i in range(1, n+1):
        typer.echo(f"{i} {fib(i)}")

@app.command()
def generate_password_command(length: int = 8):
    password = generate_password(length)
    typer.echo(f"Generated password: {password}")

if __name__ == "__main__":
    app()  