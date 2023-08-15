function generatePixels(){
    var totalPixels = xRes * yRes;

    for (var column  = 0; i < xRes; i++){
        pixelMatrix.push([])
        for (var row = 0; ii < yRes; ii++){
            pixelMatrix[0].push(new pixel(column,row));
        }
    }
    console.log(pixelMatrix)
}


class pixel {
    constructor(_x,_y){
        this.pos = new vector(_x,_y);
    }

    draw(){
        rect(this.pos.x,this.pos.y)
    }
}