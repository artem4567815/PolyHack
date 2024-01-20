const sdk = new GeSdk()
const path = '/games/tanks_pvp/static/'

let canvas;

const fil = new Image();
const fil2 = new Image();
const tankIma = new Image();
const tankImaRight = new Image();
const tankImaDown = new Image();
const tankImaLeft = new Image();
const fil3 = new Image();
const fil4 = new Image();
const bul = new Image();


function load_images() {

    return new Promise((resolve, reject) => {
        let loaded = 0;
        tankIma.src = path + "/images/tankBlue.png"
        tankImaRight.src = path + "/images/tankRight.png"
        tankImaDown.src = path + "/images/tankDown.png"
        tankImaLeft.src = path + "/images/tankLeft.png"
        fil.src = path + "/images/field.png";
        fil2.src = path + "/images/wall2.jpeg";
        fil3.src = path + "/images/brokenWall.jpeg";
        fil4.src = path + "/images/field2.png";
        bul.src = path + "/images/bulBkue.png";

        const image_loaded = () => {
            loaded++;

            if (loaded === 9) {
                resolve();
            }
        }

        fil.onload = image_loaded
        fil2.onload = image_loaded
        tankIma.onload = image_loaded
        tankImaRight.onload = image_loaded
        tankImaDown.onload = image_loaded
        tankImaLeft.onload = image_loaded
        fil3.onload = image_loaded
        fil4.onload = image_loaded
        bul.onload = image_loaded
    })
}

function R(img, degrees, x, y, s){
    ctx.translate(x,y);
    ctx.rotate(-degrees + Math.PI/2.0);
    ctx.drawImage(img,x,y,s,s);
    ctx.rotate(degrees - Math.PI/2.0);
    ctx.translate(-x, -y);
}

function drawField(ctx, field, rotation, tx, ty, bbx, bby, bx, by) {
    const cellSize = 85.3;
    for (let i = 0; i < 15; i++) {
        for (let j = 0; j < 8; j++) {
            const x = -10 + cellSize * i
            const y = -50 + cellSize * j
            if (field[j][i] === 0){ctx.drawImage(fil, x, y, cellSize, cellSize)}
            else if (field[j][i] === 1){ctx.drawImage(fil2, x, y, cellSize, cellSize)}
            else if(field[j][i] === 3){ctx.drawImage(fil3, x, y, cellSize, cellSize)}
            else if(field[j][i] === 6){ctx.drawImage(fil4, -10 + cellSize * bby, -50 + cellSize * bbx, cellSize, cellSize)}
        }
    }
    ctx.drawImage(tankIma, -10 + ty * cellSize, -50 + tx * cellSize, cellSize, cellSize);
    if (bx != 0 && by!= 0){ctx.drawImage(bul, -10 + by * cellSize, -50 + bx * cellSize, cellSize, cellSize);}


}

function init() {
    canvas = document.getElementById("field");
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

}

function newFrame(frame) {
    const ctx = document.getElementById("field").getContext("2d");
    drawField(ctx, frame["field"], frame["rotate"], frame['x'], frame['y'], frame['baseX'], frame['baseY'], frame['bx'], frame['by'])

    console.log(frame)
}

init()
load_images().then(() => {
    sdk.subscribe_to_frame(newFrame)
})
