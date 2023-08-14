// A vector... not much more to say.
// Also taken from one of my other projects.
// I did, however, remove some of the things I didn't need in here.
class vector{
    constructor(_x,_y){
      this.x = _x;
      this.y = _y;
    }
    
    // Returns the length of the vector.
    getLength(){
      return sqrt(sq(this.x)+sq(this.y));
    }
    
    // Returns an identical vector with its length modified.
    setLength(_length){
      return this.getUnit().scaleBy(_length);
    }
    
    // Returns the unit vector of this vector.
    getUnit(){
      return this.scaleBy(1/this.getLength())
    }
    
    // Returns this vector added with another vector.
    add(_v,c){
      if (c==1) console.log("Before\nX: " + this.x + "\nY: " + this.y + "\n_v.x: " + _v.x + "\n_v.y: " + _v.y + "\noutX: " + outX + "\noutY: " + outY);
      var outX = this.x + _v.x;
      var outY = this.y + _v.y;
      if (c==1) console.log("Before\nX: " + this.x + "\nY: " + this.y + "\n_v.x: " + _v.x + "\n_v.y: " + _v.y + "\noutX: " + outX + "\noutY: " + outY);
      return new vector(outX,outY);
    }
    
    // Returns this vector subtracted by another vector.
    sub(_v){
      var outX = this.x - _v.x;
      var outY = this.y - _v.y;
      return new vector(outX,outY);
    }
    
    // Returns this vector scaled by a modifier.
    scaleBy(_scale){
      var outX = this.x * _scale;
      var outY = this.y * _scale;
      return new vector(outX,outY);
    }
    
    // Returns this vector divided by a modifier.
    divideBy(_scale){
          var outX = this.x / _scale;
      var outY = this.y / _scale;
      return new vector(outX,outY);
    }
    
    // Returns a copy of this vector.
    // I have this, because I have run into some problems, where some classes accidentally got connected. This is much simpler.
    copy(){
      return new vector(this.x, this.y);
    }
  }