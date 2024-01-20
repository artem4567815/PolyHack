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

function clearScreen(ctx) {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}

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
        fil3.src = path + "/images/brbl.png";
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

function drawField(ctx, field, player1, player2, bullet1, bullet2, winner) {
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
    if (!winner['player2']){
        if (player1['way'] === "left") { ctx.drawImage(tankImaLeft, -10 + player1['pos'][1] * cellSize, -50 +  player1['pos'][0] * cellSize, cellSize, cellSize); }
        else if (player1['way'] === "down") { ctx.drawImage(tankImaDown, -10 + player1['pos'][1] * cellSize, -50 +  player1['pos'][0] * cellSize, cellSize, cellSize); }
        else if (player1['way'] === "up") { ctx.drawImage(tankIma, -10 + player1['pos'][1] * cellSize, -50 +  player1['pos'][0] * cellSize, cellSize, cellSize); }
        else if (player1['way'] === "right") { ctx.drawImage(tankImaRight, -10 + player1['pos'][1] * cellSize, -50 +  player1['pos'][0] * cellSize, cellSize, cellSize); }

        if (bullet1['pos'][0] != 0 && bullet1['pos'][1] != 0){
            if (bullet1['way'] === "left") { ctx.drawImage(bulL, -10 +  bullet1['pos'][1] * cellSize, -50 +  bullet1['pos'][0] * cellSize, cellSize, cellSize); }
            else if (bullet1['way'] === "down") { ctx.drawImage(bulD, -10 +  bullet1['pos'][1] * cellSize, -50 +  bullet1['pos'][0] * cellSize, cellSize, cellSize); }
            else if (bullet1['way'] === "up") { ctx.drawImage(bul, -10 +  bullet1['pos'][1] * cellSize, -50 +  bullet1['pos'][0] * cellSize, cellSize, cellSize); }
            else if (bullet1['way'] === "right") { ctx.drawImage(bulR, -10 +  bullet1['pos'][1] * cellSize, -50 +  bullet1['pos'][0] * cellSize, cellSize, cellSize); }
        }
    }

    if (!winner['player1']){
        if (player2['way'] === "left") { ctx.drawImage(tankImaRedL, -10 + player2['pos'][1] * cellSize, -50 + player2['pos'][0] * cellSize, cellSize, cellSize); }
        if (player2['way'] === "down") { ctx.drawImage(tankImaRedD, -10 + player2['pos'][1] * cellSize, -50 + player2['pos'][0] * cellSize, cellSize, cellSize); }
        if (player2['way'] === "up") { ctx.drawImage(tankImaRedU, -10 + player2['pos'][1] * cellSize, -50 + player2['pos'][0] * cellSize, cellSize, cellSize); }
        if (player2['way'] === "right") { ctx.drawImage(tankImaRedR, -10 + player2['pos'][1] * cellSize, -50 + player2['pos'][0] * cellSize, cellSize, cellSize); }

        if (bullet2['pos'][0] != 0 && bullet2['pos'][1] != 0) {
            if (bullet2['way'] === "left") { ctx.drawImage(bulRedL, -10 + bullet2['pos'][1] * cellSize, -50 + bullet2['pos'][0] * cellSize, cellSize, cellSize); }
            if (bullet2['way'] === "down") { ctx.drawImage(bulRedD, -10 + bullet2['pos'][1] * cellSize, -50 + bullet2['pos'][0] * cellSize, cellSize, cellSize); }
            if (bullet2['way'] === "up") { ctx.drawImage(bulRedU, -10 + bullet2['pos'][1] * cellSize, -50 + bullet2['pos'][0] * cellSize, cellSize, cellSize); }
            if (bullet2['way'] === "right") { ctx.drawImage(bulRedR, -10 + bullet2['pos'][1] * cellSize, -50 + bullet2['pos'][0] * cellSize, cellSize, cellSize)};
        }
    }
    if (winner['player2'] || winner['player1']){
        ctx.font = "50px serif";
        ctx.fillStyle = "white";
        ctx.fillText(winner["winText"], 250, 300);
    }

}

function init() {
    canvas = document.getElementById("field");
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

}

function newFrame(frame) {
    const ctx = document.getElementById("field").getContext("2d");
    drawField(ctx, frame["field"], frame['player1'], frame['player2'], frame["bullet1"], frame["bullet2"],
    frame['winner'])
}

init()
load_images().then(() => {
    sdk.subscribe_to_frame(newFrame)
})
