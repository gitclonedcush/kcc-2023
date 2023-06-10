import { PIECE_SHAPES, NUM_PIECES, PIECE_COLORS } from "./constants";

export class Piece {
  pieceId;
  x;
  y;
  ctx;
  color;
  shape;

  constructor(ctx) {
    this.ctx = ctx;

    this.pieceId = this.getRandomTetrisPieceId(NUM_PIECES - 1);
    this.shape = PIECE_SHAPES[this.pieceId];
    this.color = PIECE_COLORS[this.pieceId];

    this.x = 0;
    this.y = 0;
  }

  setStartingPosition() {
    this.x = this.typeId === 4 ? 4 : 3;
  }

  getRandomTetrisPieceId(numOfPieces) {
    // PART 3
    // TODO: Implement this method to return a random number between 1 and numOfPieces
    // Hint: Replace `1` with a number between 1 and numberOfPieces, which you can get with Math.random()
    return Math.floor(1)
  }

  move(p) {
    this.x = p.x;
    this.y = p.y;
    this.shape = p.shape;
  }

  rotate(p) {
    let clone = JSON.parse(JSON.stringify(p));

    for (let y = 0; y < clone.shape.length; ++y) {
      for (let x = 0; x < y; ++x) {
        [clone.shape[x][y], clone.shape[y][x]] = [clone.shape[y][x], clone.shape[x][y]];
      }
    }

    clone.shape.forEach(row => row.reverse());

    return clone;
  }

  draw() {
    this.ctx.fillStyle = this.color;
    this.shape.forEach((row, y) => {
      row.forEach((value, x) => {
        if (value > 0) {
          this.ctx.fillRect(this.x + x, this.y + y, 1, 1);
        }
      });
    });
  }
}