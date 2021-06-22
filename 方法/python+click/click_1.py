import  click

@click.command()
@click.option("-name", default='world', help="姓名", type=str)
@click.option("-age", default='12', help="年龄", type=str)
def say_hello(name,age):
    print(f"hi world,{name}. i m {age}")


if __name__ == '__main__':
    say_hello()