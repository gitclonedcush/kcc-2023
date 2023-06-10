import { ROWS, COLS, BLOCK_SIZE, MOVES, PIECE_COLORS, KEY, POINTS, LINES_PER_LEVEL, LEVEL } from './constants';
import { Piece } from './piece';

export class Board {
  grid;
  piece;
  next;
  ctx;
  ctxNext;
  gameMetaData;

  constructor(ctx, ctxNext, gameMetaData) {
    this.ctx = ctx;
    this.ctxNext = ctxNext;
    this.gameMetaData = gameMetaData;

    this.init();
  }

  init() {
    this.ctx.canvas.width = COLS * BLOCK_SIZE;
    this.ctx.canvas.height = ROWS * BLOCK_SIZE;
    this.ctx.scale(BLOCK_SIZE, BLOCK_SIZE);
  }

  reset() {
    this.grid = this.getEmptyBoard();
    this.piece = new Piece(this.ctx);
    this.piece.setStartingPosition();
    this.getNextPiece();
  }

  getEmptyBoard() {
    return Array.from(
      { length: ROWS }, () => Array(COLS).fill(0)
    )
  }

  valid(p) {
    return p.shape.every((row, dy) => {
      return row.every((value, dx) => {
        const x = p.x + dx;
        const y = p.y + dy;

        return (
          value === 0 ||
          (this.notOccupied(x, y) && this.insideWalls(x) && this.aboveFloor(y))
        )
      })
    })
  }

  drop() {
    const p = MOVES[KEY.DOWN](this.piece)
    if (this.valid(p)) {
      this.piece.move(p);
    } else {
      this.freeze();
      this.clearLines();

      if (this.piece.y === 0) {
        return false;
      }

      // get next piece
      this.piece = this.next;
      this.piece.ctx = this.ctx;
      this.piece.setStartingPosition();
      this.getNextPiece();
    }

    return true;
  }

  freeze() {
    this.piece.shape.forEach((row, y) => {
      row.forEach((value, x) => {
        if (value > 0) {
          this.grid[y + this.piece.y][x + this.piece.x] = value;
        }
      })
    })
  }

  clearLines() {
    let lines = 0;

    this.grid.forEach((row, y) => {
      if (row.every(value => value > 0)) {
        lines++;
        this.grid.splice(y, 1);
        this.grid.unshift(Array(COLS).fill(0));
      }
    })

    // calculate scores
    if (lines > 0) {
      this.gameMetaData.score += this.getLinesClearedPoints(lines);
      this.gameMetaData.lines += lines;

      if (this.gameMetaData.lines >= LINES_PER_LEVEL) {
        this.gameMetaData.level++;
        this.gameMetaData.lines -= LINES_PER_LEVEL;
        this.gameMetaData.speed = LEVEL[this.gameMetaData.level];
      }
    }
  }

  getLinesClearedPoints(lines) {
    const points =
      lines === 1
        ? POINTS.SINGLE
        : lines === 2
          ? POINTS.DOUBLE
          : lines === 3
            ? POINTS.TRIPLE
            : lines === 4
              ? POINTS.TETRIS
              : 0;

    return (this.gameMetaData.level + 1) * points;
  }

  getNextPiece() {
    this.next = new Piece(this.ctxNext);
    this.ctxNext.clearRect(0, 0, this.ctxNext.canvas.width, this.ctxNext.canvas.height);
    this.next.draw();
  }

  draw() {
    this.piece.draw();
    this.drawBoard();
  }

  drawBoard() {
    this.grid.forEach((row, y) => {
      row.forEach((value, x) => {
        if (value > 0) {
          this.ctx.fillStyle = PIECE_COLORS[value];
          this.ctx.fillRect(x, y, 1, 1);
        }
      })
    })
  }

  notOccupied(x, y) {
    return this.grid[y] && this.grid[y][x] === 0;
  }

  insideWalls(x) {
    return x >= 0 && x < COLS;
  }

  aboveFloor(y) {
    return y < ROWS;
  }
}