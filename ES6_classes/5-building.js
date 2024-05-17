export default class Building {
  constructor(sqft) {
    if (typeof sqft !== 'number') {
      throw TypeError('sqft must be a number');
    }
    this._sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }

  set sqft(newSqft) {
    if (typeof newSqft !== 'number') {
      throw TypeError('sqft must be a number');
    }
    this._sqft = newSqft;
  }

  evacuationWarningMessage() {
    return `Class extending Building must override evacuationWarningMessage`;
  }
}
