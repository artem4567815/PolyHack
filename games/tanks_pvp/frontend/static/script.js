const sdk = new GeSdk()
const path = '/games/tanks_pvp/static/'

let canvas;

const fil = new Image();
const fil2 = new Image();
const tankIma = new Image();
const tankImaRight = new Image();
const tankImaDown = new Image();
const tankImaLeft = new Image();

const tankImaRedR = new Image();
const tankImaRedL = new Image();
const tankImaRedU = new Image();
const tankImaRedD = new Image();

const fil3 = new Image();

const bul = new Image();
const bulL = new Image();
const bulR = new Image();
const bulD = new Image();

const bulRedU = new Image();
const bulRedL = new Image();
const bulRedR = new Image();
const bulRedD = new Image();


function load_images() {

    return new Promise((resolve, reject) => {
        let loaded = 0;
        tankIma.src = path + "/images/tankBlue.png"
        tankImaRight.src = path + "/images/tankRight.png"
        tankImaDown.src = path + "/images/tankDown.png"
        tankImaLeft.src = path + "/images/tankLeft.png"

        tankImaRedR.src = path + "/images/tanksRedR.png"
        tankImaRedD.src = path + "/images/tanksRedD.png"
        tankImaRedL.src = path + "/images/tanksRedLeft.png"
        tankImaRedU.src = path + "/images/tanksRedU.png"

        fil.src = path + "/images/field.png";
        fil2.src = path + "/images/wall2.jpeg";
        fil3.src = path + "/images/brokenWall.jpeg";
        bul.src = path + "/images/bulBkue.png";
        bulL.src = path + "/images/bullL.png";
        bulR.src = path + "/images/bullR.png";
        bulD.src = path + "/images/bullD.png";

        bulRedU.src = path + "/images/bulRedU.png";
        bulRedL.src = path + "/images/bulRedL.png";
        bulRedR.src = path + "/images/bulRedR.png";
        bulRedD.src = path + "/images/bulRedD.png";

        const image_loaded = () => {
            loaded++;

            if (loaded === 19) {
                resolve();
            }
        }

        fil.onload = image_loaded
        fil2.onload = image_loaded
        tankIma.onload = image_loaded
        tankImaRight.onload = image_loaded
        tankImaDown.onload = image_loaded
        tankImaLeft.onload = image_loaded

        tankImaRedR.onload = image_loaded
        tankImaRedU.onload = image_loaded
        tankImaRedL.onload = image_loaded
        tankImaRedD.onload = image_loaded

        fil3.onload = image_loaded
        bul.onload = image_loaded
        bulL.onload = image_loaded
        bulD.onload = image_loaded
        bulR.onload = image_loaded

        bulRedU.onload = image_loaded
        bulRedD.onload = image_loaded
        bulRedL.onload = image_loaded
        bulRedR.onload = image_loaded
    })
}

function drawField(ctx, field, tx, ty, ttx, tty, bx, by, way, bbx, bby, bWay, tWay, ttWay) {
    const cellSize = 85.3;
    for (let i = 0; i < 15; i++) {
        for (let j = 0; j < 8; j++) {
            const x = -10 + cellSize * i
            const y = -50 + cellSize * j
            if (field[j][i] === 0) { ctx.drawImage(fil, x, y, cellSize, cellSize) }
            else if (field[j][i] === 1) { ctx.drawImage(fil2, x, y, cellSize, cellSize) }
            else if (field[j][i] === 3) { ctx.drawImage(fil3, x, y, cellSize, cellSize) }
            //else if(field[j][i] === 6){ctx.drawImage(fil4, -10 + cellSize * bby, -50 + cellSize * bbx, cellSize, cellSize)}
        }
    }
    if (tWay === "left") { ctx.drawImage(tankImaLeft, -10 + ty * cellSize, -50 + tx * cellSize, cellSize, cellSize); }
    else if (tWay === "down") { ctx.drawImage(tankImaDown, -10 + ty * cellSize, -50 + tx * cellSize, cellSize, cellSize); }
    else if (tWay === "up") { ctx.drawImage(tankIma, -10 + ty * cellSize, -50 + tx * cellSize, cellSize, cellSize); }
    else if (tWay === "right") { ctx.drawImage(tankImaRight, -10 + ty * cellSize, -50 + tx * cellSize, cellSize, cellSize); }

    if (bx != 0 && by != 0 && tWay == way) {
        if (way === "left") { ctx.drawImage(bulL, -10 + by * cellSize, -50 + bx * cellSize, cellSize, cellSize); }
        else if (way === "down") { ctx.drawImage(bulD, -10 + by * cellSize, -50 + bx * cellSize, cellSize, cellSize); }
        else if (way === "up") { ctx.drawImage(bul, -10 + by * cellSize, -50 + bx * cellSize, cellSize, cellSize); }
        else if (way === "right") { ctx.drawImage(bulR, -10 + by * cellSize, -50 + bx * cellSize, cellSize, cellSize); }
    }

    if (ttWay === "left") { ctx.drawImage(tankImaRedL, -10 + tty * cellSize, -50 + ttx * cellSize, cellSize, cellSize); }
    else if (ttWay === "down") { ctx.drawImage(tankImaRedD, -10 + tty * cellSize, -50 + ttx * cellSize, cellSize, cellSize); }
    else if (ttWay === "up") { ctx.drawImage(tankImaRedU, -10 + tty * cellSize, -50 + ttx * cellSize, cellSize, cellSize); }
    else if (ttWay === "right") {ctx.drawImage(tankImaRedR, -10 + tty * cellSize, -50 + ttx * cellSize, cellSize, cellSize);}

    if (bx != 0 && by != 0 && ttWay == bWay) {
        if (bWay === "left") { ctx.drawImage(bulRedL, -10 + bby * cellSize, -50 + bbx * cellSize, cellSize, cellSize); }
        else if (bWay === "down") { ctx.drawImage(bulRedD, -10 + bby * cellSize, -50 + bbx * cellSize, cellSize, cellSize); }
        else if (bWay === "up") { ctx.drawImage(bulRedU, -10 + bby * cellSize, -50 + bbx * cellSize, cellSize, cellSize); }
        else if (bWay === "right") { ctx.drawImage(bulRedR, -10 + bby * cellSize, -50 + bbx * cellSize, cellSize, cellSize); }
    }

}

function init() {
    canvas = document.getElementById("field");
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

}

function newFrame(frame) {
    const ctx = document.getElementById("field").getContext("2d");
    drawField(ctx, frame["field"], frame['x'], frame['y'], frame['x2'], frame['y2'],
        frame["bullet"]['bx'], frame["bullet"]['by'], frame["bullet"]["way"], frame["bullet2"]['bx'],
        frame["bullet2"]['by'], frame["bullet2"]["way"], frame['way1'], frame['way2'])

    console.log(frame)
}

init()
load_images().then(() => {
    sdk.subscribe_to_frame(newFrame)
})
