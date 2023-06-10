import "./styles.css";
import { BLOCK_SIZE, KEY, MOVES, LEVEL, POINTS } from './constants';
import { Board } from "./board";

const gameCanvas = document.getElementById('board');
const gameContext = gameCanvas.getContext('2d');
const playButton = document.getElementById('play-button');

const nextCanvas = document.getElementById('next');
const nextContext = nextCanvas.getContext('2d');

playButton.addEventListener('click', play);

const gameMetadata = {
  score: 0,
  level: 0,
  lines: 0,
  start: 0,
  elapsed: 0,
  speed: LEVEL[0]
};

const gameData = new Proxy(gameMetadata, {
  set: (target, key, value) => {
    if (target[key] === undefined) {
      return false;
    }

    if (isNaN(value)) {
      return false;
    }

    target[key] = value;
    updateGameData(key, value);
    return true;
  }
})

let board = new Board(gameContext, nextContext, gameData);
let requestId;
let running = false;

initNext();

function updateGameData(key, value) {
  const element = document.getElementById(key);
  if (element) {
    element.textContent = value;
  }
}

function initNext() {
  nextContext.canvas.width = 4 * BLOCK_SIZE
  nextContext.canvas.height = 4 * BLOCK_SIZE
  nextContext.scale(BLOCK_SIZE, BLOCK_SIZE)
}

function resetGame() {
  board.reset();
  gameData.score = 0;
  gameData.lines = 0;
  gameData.level = 0;
  gameData.start = 0;
  gameData.elapsed = 0;
  gameData.speed = LEVEL[0];
}

function play() {
  resetGame();
  animate();

  running = true;
}

function animate(now = 0) {
  gameData.elapsed = now - gameData.start;
  if (gameData.elapsed > gameData.speed) {
    gameData.start = now;

    if (!board.drop()) {
      gameOver();
      return;
    }
  }

  gameContext.clearRect(0, 0, gameContext.canvas.width, gameContext.canvas.height);
  board.draw();

  requestId = window.requestAnimationFrame(animate);
}

function gameOver() {
  window.cancelAnimationFrame(requestId);

  gameContext.fillStyle = 'black';
  gameContext.fillRect(1, 3, 8, 1.2);
  gameContext.font = '1px Arial';
  gameContext.fillStyle = 'red'
  gameContext.fillText('GAME OVER', 1.8, 4);
}

document.addEventListener('keydown', event => {
  if (!running) {
    return;
  }

  if (MOVES[event.keyCode]) {
    event.preventDefault();

    let movedPiece = MOVES[event.keyCode](board.piece)

    if (event.keyCode === KEY.SPACE) {

      // PART 4
      // TODO: Handle the space key
      //
      // Handle the space key by looping, and for each time you loop 
      // move the piece down 1 square until you can't move the piece down any further!
      // You can use the `board.valid(piece)` method to check if the
      // moved piece is in a valid position, and if it is, you'll want to continue the loop to move the piece down again.
      //
      // Hint: you'll want to use a while loop here

    } else if (board.valid(movedPiece)) {
      board.piece.move(movedPiece)

      if (event.keyCode === KEY.DOWN) {
        gameData.score += POINTS.SOFT_DROP;
      }
    }
  }
})
