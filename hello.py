from flask import Flask
app = Flask(__name__)


snake_html = '''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <canvas id="gc" width="400" height="400"></canvas>
  </body>
  <script>
    window.onload = function () {
      canv = document.getElementById('gc');
      ctx = canv.getContext('2d');
      document.addEventListener('keydown', keyPush);
      setInterval(game, 1000 / 12);
    };
    xv = yv = 0;
    px = py = 10;
    ax = ay = 15;
    gs = tc = 20;
    trail = [];
    tail = 5;
    score = 0;
    function game() {
      px += xv;
      py += yv;
      if (px < 0) {
        px = tc - 1;
      }
      if (px > tc - 1) {
        px = 0;
      }
      if (py < 0) {
        py = tc - 1;
      }
      if (py > tc - 1) {
        py = 0;
      }
      //togloomiin talbai
      ctx.fillStyle = 'black';
      ctx.fillRect(0, 0, canv.width, canv.height);
      //mogiog zurj bn
      ctx.fillStyle = 'white';
      for (var i = 0; i < trail.length; i++) {
        ctx.fillRect(trail[i].x * gs, trail[i].y * gs, gs - 2, gs - 2);
        if (trail[i].x == px && trail[i].y == py) {
          tail = 5;
          score = 0;
        }
      }
      trail.push({ x: px, y: py });
      while (trail.length > tail) {
        trail.shift();
      }
      //ene alimiig mogoi ideh function
      if (ax == px && ay == py) {
        tail++;
        ax = Math.floor(Math.random() * tc);
        ay = Math.floor(Math.random() * tc);
        score++;
      }
      ctx.fillStyle = 'red';
      ctx.fillRect(ax * gs, ay * gs, gs - 2, gs - 2);
      console.log(score);
      //   score.text = 'SCORE: ';
      //   score.update();
      ctx.font = '30px Arial';
      ctx.fillText(score, 10, 50);
    }

    //togloomiig udirdah function
    function keyPush(evt) {
      switch (evt.keyCode) {
        case 37:
          xv = -1;
          yv = 0;
          break;
        case 38:
          xv = 0;
          yv = -1;
          break;
        case 39:
          xv = 1;
          yv = 0;
          break;
        case 40:
          xv = 0;
          yv = 1;
          break;
      }
    }
  </script>
</html>

'''


@app.route('/')
def hello_world():
    return 'hello'


@app.route('/bye')
def bye():
    return 'bye bye'


@app.route('/snake')
def snake():
    return snake_html


@app.route('/heeloo')
def hello_world1():
    return 'Hello, World!'


def sum1(n):
    num = 0
    for i in range(n+1):
        num += i
    print(num)


print("Sum1: ")
sum1(10)


def sum2(n):
    sum = 0
    i = 0
    while i <= n:
        sum = sum + i
        # print(sum)
        i += 1
    print(sum)


print("Sum2: ")
sum2(10)


def sum3(n):
    print(sum(range(n+1)))


print("Sum3: ")
sum3(10)


def sum4(n):
    if n == 1:
        return n
    return n + sum4(n+1)


print(sum4(10))
